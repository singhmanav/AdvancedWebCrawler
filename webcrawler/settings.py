# Scrapy settings for webcrawler project

BOT_NAME = 'webcrawler'

SPIDER_MODULES = ['webcrawler.spiders']
NEWSPIDER_MODULE = 'webcrawler.spiders'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure delays for requests
DOWNLOAD_DELAY = 1
RANDOMIZE_DOWNLOAD_DELAY = 0.5

# The download delay setting will honor only one of:
CONCURRENT_REQUESTS_PER_DOMAIN = 8
CONCURRENT_REQUESTS_PER_IP = 8

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

# Enable or disable spider middlewares
SPIDER_MIDDLEWARES = {
    'webcrawler.middlewares.WebcrawlerSpiderMiddleware': 543,
}

# Enable or disable downloader middlewares
DOWNLOADER_MIDDLEWARES = {
    'webcrawler.middlewares.WebcrawlerDownloaderMiddleware': 543,
    'webcrawler.middlewares.UserAgentMiddleware': 400,
}

# Enable or disable extensions
EXTENSIONS = {
    'scrapy.extensions.telnet.TelnetConsole': None,
}

# Configure item pipelines
ITEM_PIPELINES = {
    'webcrawler.pipelines.ValidationPipeline': 100,
    'webcrawler.pipelines.DeduplicationPipeline': 200,
    'webcrawler.pipelines.DocumentProcessingPipeline': 300,
    'webcrawler.pipelines.JsonWriterPipeline': 800,
}

# Enable autothrottling
AUTOTHROTTLE_ENABLED = True
AUTOTHROTTLE_START_DELAY = 1
AUTOTHROTTLE_MAX_DELAY = 10
AUTOTHROTTLE_TARGET_CONCURRENCY = 2.0
AUTOTHROTTLE_DEBUG = False

# HTTP cache settings
HTTPCACHE_ENABLED = True
HTTPCACHE_EXPIRATION_SECS = 3600
HTTPCACHE_DIR = 'httpcache'
HTTPCACHE_IGNORE_HTTP_CODES = [503, 504, 505, 500, 403, 404, 408, 429]

# File storage settings
FILES_STORE = 'data/files'
MEDIA_ALLOW_REDIRECTS = True

# Custom settings
DEPTH_LIMIT = 5
DOWNLOAD_TIMEOUT = 30
RETRY_TIMES = 3
RETRY_HTTP_CODES = [500, 502, 503, 504, 408, 429]

# Logging
LOG_LEVEL = 'INFO'
LOG_FILE = 'data/logs/webcrawler.log'

# Custom file extensions to crawl
CRAWL_FILE_EXTENSIONS = [
    'pdf', 'doc', 'docx', 'xls', 'xlsx', 'ppt', 'pptx',
    'txt', 'rtf', 'odt', 'ods', 'odp'
]

# Maximum file size to download (in bytes)
MAX_FILE_SIZE = 50 * 1024 * 1024  # 50 MB