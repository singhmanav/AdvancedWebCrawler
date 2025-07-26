import scrapy


class WebPageItem(scrapy.Item):
    """Item for storing web page data"""
    url = scrapy.Field()
    title = scrapy.Field()
    content = scrapy.Field()
    text_content = scrapy.Field()
    links = scrapy.Field()
    images = scrapy.Field()
    meta_description = scrapy.Field()
    meta_keywords = scrapy.Field()
    headers = scrapy.Field()
    timestamp = scrapy.Field()
    response_status = scrapy.Field()
    content_type = scrapy.Field()
    file_size = scrapy.Field()


class DocumentItem(scrapy.Item):
    """Item for storing document data (PDF, DOC, etc.)"""
    url = scrapy.Field()
    filename = scrapy.Field()
    file_type = scrapy.Field()
    content = scrapy.Field()
    text_content = scrapy.Field()
    metadata = scrapy.Field()
    file_size = scrapy.Field()
    timestamp = scrapy.Field()
    page_count = scrapy.Field()
    
    
class LinkItem(scrapy.Item):
    """Item for storing discovered links"""
    source_url = scrapy.Field()
    target_url = scrapy.Field()
    link_text = scrapy.Field()
    link_type = scrapy.Field()
    timestamp = scrapy.Field()