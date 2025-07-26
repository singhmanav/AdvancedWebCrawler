import json
import os
import hashlib
from datetime import datetime
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem
from utils.document_processor import DocumentProcessor


class ValidationPipeline:
    """Pipeline to validate items"""

    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        
        # Check if required fields are present
        if not adapter.get('url'):
            raise DropItem(f"Missing url in {item}")
        
        return item


class DeduplicationPipeline:
    """Pipeline to filter out duplicate items"""

    def __init__(self):
        self.urls_seen = set()

    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        url = adapter['url']
        
        # Create a hash of the URL for deduplication
        url_hash = hashlib.md5(url.encode()).hexdigest()
        
        if url_hash in self.urls_seen:
            raise DropItem(f"Duplicate item found: {url}")
        else:
            self.urls_seen.add(url_hash)
            return item


class DocumentProcessingPipeline:
    """Pipeline to process documents (PDF, DOC, etc.)"""

    def __init__(self):
        self.processor = DocumentProcessor()

    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        
        # Only process document items
        if adapter.get('file_type'):
            try:
                # Process the document based on its type
                processed_content = self.processor.process_document(
                    item['content'], 
                    item['file_type']
                )
                adapter['text_content'] = processed_content
                spider.logger.info(f"Processed document: {adapter['url']}")
            except Exception as e:
                spider.logger.error(f"Error processing document {adapter['url']}: {str(e)}")
        
        return item


class JsonWriterPipeline:
    """Pipeline to write items to JSON files"""

    def __init__(self):
        self.ensure_directories()

    def ensure_directories(self):
        """Create necessary directories"""
        directories = ['data', 'data/pages', 'data/documents', 'data/links', 'data/logs']
        for directory in directories:
            os.makedirs(directory, exist_ok=True)

    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        timestamp = datetime.now().isoformat()
        adapter['timestamp'] = timestamp
        
        # Determine file path based on item type
        if 'file_type' in adapter:
            # Document item
            filename = f"data/documents/{timestamp.replace(':', '-')}-document.json"
        elif 'target_url' in adapter:
            # Link item
            filename = f"data/links/{timestamp.replace(':', '-')}-link.json"
        else:
            # Web page item
            filename = f"data/pages/{timestamp.replace(':', '-')}-page.json"

        # Write item to JSON file
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(dict(adapter), f, ensure_ascii=False, indent=2)
            spider.logger.info(f"Saved item to {filename}")
        except Exception as e:
            spider.logger.error(f"Error saving item to {filename}: {str(e)}")

        return item


class DatabasePipeline:
    """Pipeline to save items to database (optional)"""

    def __init__(self):
        # Initialize database connection here if needed
        pass

    def process_item(self, item, spider):
        # Implement database saving logic here
        return item