import scrapy
import re
import mimetypes
from urllib.parse import urljoin, urlparse
from scrapy.http import Request
from webcrawler.items import WebPageItem, DocumentItem, LinkItem


class MainSpider(scrapy.Spider):
    """Main spider for crawling websites and documents"""
    
    name = 'main_spider'
    
    # File extensions to process as documents
    document_extensions = [
        'pdf', 'doc', 'docx', 'xls', 'xlsx', 'ppt', 'pptx',
        'txt', 'rtf', 'odt', 'ods', 'odp'
    ]
    
    def __init__(self, start_urls=None, allowed_domains=None, max_depth=5, *args, **kwargs):
        super(MainSpider, self).__init__(*args, **kwargs)
        
        if start_urls:
            self.start_urls = start_urls.split(',') if isinstance(start_urls, str) else start_urls
        else:
            self.start_urls = ['https://example.com']
            
        if allowed_domains:
            self.allowed_domains = allowed_domains.split(',') if isinstance(allowed_domains, str) else allowed_domains
        else:
            self.allowed_domains = []
            
        self.max_depth = int(max_depth)
        self.crawled_urls = set()

    def start_requests(self):
        """Generate initial requests"""
        for url in self.start_urls:
            yield Request(
                url=url,
                callback=self.parse,
                meta={'depth': 0}
            )

    def parse(self, response):
        """Parse web pages and extract data"""
        current_depth = response.meta.get('depth', 0)
        
        # Check if we've exceeded max depth
        if current_depth >= self.max_depth:
            self.logger.info(f"Max depth reached for {response.url}")
            return
            
        # Add to crawled URLs
        self.crawled_urls.add(response.url)
        
        # Determine content type
        content_type = response.headers.get('Content-Type', b'').decode('utf-8').lower()
        
        # Check if this is a document
        if self.is_document_url(response.url) or self.is_document_content_type(content_type):
            yield from self.parse_document(response)
        else:
            yield from self.parse_webpage(response, current_depth)

    def parse_webpage(self, response, current_depth):
        """Parse HTML web pages"""
        try:
            # Extract page data
            item = WebPageItem()
            item['url'] = response.url
            item['title'] = self.extract_title(response)
            item['content'] = response.text
            item['text_content'] = self.extract_text_content(response)
            item['meta_description'] = self.extract_meta_description(response)
            item['meta_keywords'] = self.extract_meta_keywords(response)
            item['headers'] = self.extract_headers(response)
            item['response_status'] = response.status
            item['content_type'] = response.headers.get('Content-Type', b'').decode('utf-8')
            item['file_size'] = len(response.body)
            
            # Extract links and images
            links = self.extract_links(response)
            images = self.extract_images(response)
            
            item['links'] = links
            item['images'] = images
            
            yield item
            
            # Follow links for further crawling
            yield from self.follow_links(response, links, current_depth)
            
        except Exception as e:
            self.logger.error(f"Error parsing webpage {response.url}: {str(e)}")

    def parse_document(self, response):
        """Parse document files"""
        try:
            item = DocumentItem()
            item['url'] = response.url
            item['filename'] = self.extract_filename(response.url)
            item['file_type'] = self.get_file_extension(response.url)
            item['content'] = response.body
            item['file_size'] = len(response.body)
            item['metadata'] = self.extract_document_metadata(response)
            
            yield item
            
        except Exception as e:
            self.logger.error(f"Error parsing document {response.url}: {str(e)}")

    def follow_links(self, response, links, current_depth):
        """Follow discovered links"""
        for link_data in links:
            url = link_data['url']
            
            # Skip if already crawled
            if url in self.crawled_urls:
                continue
                
            # Create link item
            link_item = LinkItem()
            link_item['source_url'] = response.url
            link_item['target_url'] = url
            link_item['link_text'] = link_data.get('text', '')
            link_item['link_type'] = link_data.get('type', 'internal')
            
            yield link_item
            
            # Follow the link if it's internal and within depth limit
            if link_data.get('type') == 'internal' and current_depth < self.max_depth:
                yield Request(
                    url=url,
                    callback=self.parse,
                    meta={'depth': current_depth + 1},
                    dont_filter=False
                )

    def extract_title(self, response):
        """Extract page title"""
        title = response.css('title::text').get()
        return title.strip() if title else ''

    def extract_text_content(self, response):
        """Extract clean text content from page"""
        # Remove script and style elements
        text = response.css('body *:not(script):not(style)::text').getall()
        # Clean and join text
        cleaned_text = ' '.join([t.strip() for t in text if t.strip()])
        return cleaned_text

    def extract_meta_description(self, response):
        """Extract meta description"""
        return response.css('meta[name="description"]::attr(content)').get() or ''

    def extract_meta_keywords(self, response):
        """Extract meta keywords"""
        return response.css('meta[name="keywords"]::attr(content)').get() or ''

    def extract_headers(self, response):
        """Extract page headers (h1-h6)"""
        headers = {}
        for i in range(1, 7):
            headers[f'h{i}'] = response.css(f'h{i}::text').getall()
        return headers

    def extract_links(self, response):
        """Extract all links from the page"""
        links = []
        
        # Extract anchor tags
        for link in response.css('a[href]'):
            href = link.css('::attr(href)').get()
            text = link.css('::text').get() or ''
            
            if href:
                absolute_url = urljoin(response.url, href)
                link_type = self.classify_link(absolute_url, response.url)
                
                links.append({
                    'url': absolute_url,
                    'text': text.strip(),
                    'type': link_type
                })
        
        # Extract links from other elements (iframe, embed, etc.)
        for src_link in response.css('[src]'):
            src = src_link.css('::attr(src)').get()
            if src:
                absolute_url = urljoin(response.url, src)
                links.append({
                    'url': absolute_url,
                    'text': '',
                    'type': 'resource'
                })
        
        return links

    def extract_images(self, response):
        """Extract all images from the page"""
        images = []
        
        for img in response.css('img'):
            src = img.css('::attr(src)').get()
            alt = img.css('::attr(alt)').get() or ''
            
            if src:
                absolute_url = urljoin(response.url, src)
                images.append({
                    'url': absolute_url,
                    'alt': alt
                })
        
        return images

    def classify_link(self, url, base_url):
        """Classify link as internal, external, or document"""
        base_domain = urlparse(base_url).netloc
        link_domain = urlparse(url).netloc
        
        if self.is_document_url(url):
            return 'document'
        elif base_domain == link_domain:
            return 'internal'
        else:
            return 'external'

    def is_document_url(self, url):
        """Check if URL points to a document"""
        file_extension = self.get_file_extension(url)
        return file_extension in self.document_extensions

    def is_document_content_type(self, content_type):
        """Check if content type indicates a document"""
        document_types = [
            'application/pdf',
            'application/msword',
            'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
            'application/vnd.ms-excel',
            'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
            'application/vnd.ms-powerpoint',
            'application/vnd.openxmlformats-officedocument.presentationml.presentation',
            'text/plain',
            'application/rtf'
        ]
        
        for doc_type in document_types:
            if doc_type in content_type:
                return True
        return False

    def get_file_extension(self, url):
        """Get file extension from URL"""
        parsed_url = urlparse(url)
        path = parsed_url.path.lower()
        
        # Extract extension
        if '.' in path:
            return path.split('.')[-1]
        return ''

    def extract_filename(self, url):
        """Extract filename from URL"""
        parsed_url = urlparse(url)
        path = parsed_url.path
        
        if '/' in path:
            return path.split('/')[-1]
        return 'unknown'

    def extract_document_metadata(self, response):
        """Extract metadata from document response"""
        metadata = {}
        
        # Extract headers that might contain metadata
        for header_name, header_value in response.headers.items():
            if header_name.decode().lower() in ['last-modified', 'content-length', 'content-type']:
                metadata[header_name.decode().lower()] = header_value.decode()
        
        return metadata