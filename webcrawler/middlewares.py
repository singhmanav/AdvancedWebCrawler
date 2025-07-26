import random
import logging
from scrapy import signals
from scrapy.http import HtmlResponse
from fake_useragent import UserAgent
from itemadapter import is_item, ItemAdapter


class WebcrawlerSpiderMiddleware:
    """Spider middleware for custom processing"""

    @classmethod
    def from_crawler(cls, crawler):
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        return None

    def process_spider_output(self, response, result, spider):
        return result

    def process_spider_exception(self, response, exception, spider):
        pass

    def process_start_requests(self, start_requests, spider):
        return start_requests

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class WebcrawlerDownloaderMiddleware:
    """Downloader middleware for custom request/response processing"""

    @classmethod
    def from_crawler(cls, crawler):
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        return None

    def process_response(self, request, response, spider):
        return response

    def process_exception(self, request, exception, spider):
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class UserAgentMiddleware:
    """Middleware to rotate user agents"""

    def __init__(self):
        self.ua = UserAgent()
        self.user_agents = [
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:89.0) Gecko/20100101 Firefox/89.0',
        ]

    def process_request(self, request, spider):
        try:
            ua = self.ua.random
        except:
            ua = random.choice(self.user_agents)
        
        request.headers['User-Agent'] = ua
        return None


class FileSizeMiddleware:
    """Middleware to check file size before downloading"""

    def __init__(self):
        self.max_size = 50 * 1024 * 1024  # 50 MB

    def process_request(self, request, spider):
        # For file downloads, we'll check size in the response
        return None

    def process_response(self, request, response, spider):
        content_length = response.headers.get('Content-Length')
        if content_length:
            size = int(content_length)
            if size > self.max_size:
                spider.logger.warning(f"File too large ({size} bytes): {request.url}")
                return HtmlResponse(url=request.url, status=413)
        return response