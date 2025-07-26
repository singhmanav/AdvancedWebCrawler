"""
Custom settings for different crawling scenarios
"""

# Settings for respectful crawling
RESPECTFUL_CRAWLING = {
    'DOWNLOAD_DELAY': 3,
    'RANDOMIZE_DOWNLOAD_DELAY': 0.5,
    'CONCURRENT_REQUESTS_PER_DOMAIN': 2,
    'CONCURRENT_REQUESTS_PER_IP': 2,
    'ROBOTSTXT_OBEY': True,
    'AUTOTHROTTLE_ENABLED': True,
    'AUTOTHROTTLE_START_DELAY': 2,
    'AUTOTHROTTLE_MAX_DELAY': 15,
    'AUTOTHROTTLE_TARGET_CONCURRENCY': 1.0,
}

# Settings for aggressive crawling (use with caution)
AGGRESSIVE_CRAWLING = {
    'DOWNLOAD_DELAY': 0.5,
    'RANDOMIZE_DOWNLOAD_DELAY': 0.1,
    'CONCURRENT_REQUESTS_PER_DOMAIN': 16,
    'CONCURRENT_REQUESTS_PER_IP': 16,
    'ROBOTSTXT_OBEY': False,
    'AUTOTHROTTLE_ENABLED': False,
}

# Settings for document-focused crawling
DOCUMENT_CRAWLING = {
    'DOWNLOAD_DELAY': 2,
    'CONCURRENT_REQUESTS_PER_DOMAIN': 4,
    'DEPTH_LIMIT': 10,
    'MAX_FILE_SIZE': 100 * 1024 * 1024,  # 100 MB
    'CRAWL_FILE_EXTENSIONS': [
        'pdf', 'doc', 'docx', 'xls', 'xlsx', 'ppt', 'pptx',
        'txt', 'rtf', 'odt', 'ods', 'odp', 'csv'
    ]
}

# Settings for news/blog crawling
NEWS_CRAWLING = {
    'DOWNLOAD_DELAY': 1,
    'CONCURRENT_REQUESTS_PER_DOMAIN': 6,
    'DEPTH_LIMIT': 3,
    'ROBOTSTXT_OBEY': True,
    'HTTPCACHE_ENABLED': False,  # Always get fresh content
}

# Settings for academic/research crawling
ACADEMIC_CRAWLING = {
    'DOWNLOAD_DELAY': 4,
    'CONCURRENT_REQUESTS_PER_DOMAIN': 2,
    'DEPTH_LIMIT': 8,
    'MAX_FILE_SIZE': 200 * 1024 * 1024,  # 200 MB
    'ROBOTSTXT_OBEY': True,
    'CRAWL_FILE_EXTENSIONS': [
        'pdf', 'doc', 'docx', 'tex', 'bib', 'txt',
        'xls', 'xlsx', 'csv', 'json', 'xml'
    ]
}