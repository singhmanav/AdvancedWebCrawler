# 🕷️ Advanced Web Crawler with Scrapy

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![Scrapy](https://img.shields.io/badge/Scrapy-2.11+-green.svg)](https://scrapy.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![GitHub](https://img.shields.io/badge/GitHub-singhmanav/AdvancedWebCrawler-blue.svg)](https://github.com/singhmanav/AdvancedWebCrawler)

A comprehensive, production-ready web crawler built with Scrapy that can crawl websites, extract data from various document types (PDFs, Word docs, Excel files, etc.), and traverse links recursively with intelligent rate limiting and content processing.

## Features

- **Web Page Crawling**: Extract content, metadata, links, and images from web pages
- **Document Processing**: Handle PDFs, Word documents, Excel files, PowerPoint presentations, and more
- **Link Traversal**: Recursively follow internal links with configurable depth limits
- **Content Extraction**: Clean text extraction from various document formats
- **Deduplication**: Automatic filtering of duplicate URLs and content
- **Configurable Settings**: Customizable delays, concurrent requests, and crawling limits
- **Data Storage**: Save crawled data in JSON format with organized directory structure
- **Logging**: Comprehensive logging for monitoring and debugging

## Installation

1. Clone this repository or copy the project files
2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Project Structure

```
webcrawler/
├── scrapy.cfg                 # Scrapy configuration
├── requirements.txt           # Python dependencies
├── run_crawler.py            # Main runner script
├── README.md                 # This file
├── webcrawler/               # Main package
│   ├── __init__.py
│   ├── settings.py           # Scrapy settings
│   ├── pipelines.py          # Data processing pipelines
│   ├── middlewares.py        # Custom middlewares
│   ├── items.py              # Data structure definitions
│   └── spiders/              # Spider implementations
│       ├── __init__.py
│       └── main_spider.py    # Main crawling spider
├── utils/                    # Utility modules
│   ├── __init__.py
│   └── document_processor.py # Document processing utilities
└── data/                     # Output directory
    ├── pages/                # Web page data
    ├── documents/            # Document data
    ├── links/                # Link data
    └── logs/                 # Log files
```

## Usage

### Basic Usage

Run the crawler with a single URL:

```bash
python run_crawler.py --start-urls "https://example.com"
```

### Advanced Usage

```bash
python run_crawler.py \
    --start-urls "https://example.com,https://another-site.com" \
    --allowed-domains "example.com,another-site.com" \
    --max-depth 5 \
    --delay 2.0 \
    --concurrent-requests 4 \
    --log-level DEBUG \
    --output-dir my_crawl_data
```

### Command Line Options

- `--start-urls`: Comma-separated list of URLs to start crawling (required)
- `--allowed-domains`: Comma-separated list of allowed domains (optional)
- `--max-depth`: Maximum crawling depth (default: 3)
- `--delay`: Download delay in seconds (default: 1.0)
- `--concurrent-requests`: Number of concurrent requests (default: 8)
- `--obey-robots`: Obey robots.txt rules (default: True)
- `--log-level`: Logging level (DEBUG, INFO, WARNING, ERROR)
- `--output-dir`: Output directory for crawled data (default: data)

### Using Scrapy Directly

You can also run the spider directly using Scrapy commands:

```bash
# Basic crawl
scrapy crawl main_spider -a start_urls="https://example.com"

# With custom settings
scrapy crawl main_spider \
    -a start_urls="https://example.com" \
    -a max_depth=5 \
    -s DOWNLOAD_DELAY=2 \
    -s LOG_LEVEL=DEBUG
```

## Supported Document Types

The crawler can process the following document types:

- **PDF**: `.pdf` files
- **Microsoft Word**: `.doc`, `.docx` files
- **Microsoft Excel**: `.xls`, `.xlsx` files
- **Microsoft PowerPoint**: `.ppt`, `.pptx` files (basic support)
- **Text Files**: `.txt` files
- **Rich Text Format**: `.rtf` files
- **OpenDocument**: `.odt`, `.ods`, `.odp` files
- **HTML**: `.html`, `.htm` files

## Output Data

The crawler generates three types of output files:

### 1. Web Page Data (`data/pages/`)
```json
{
  "url": "https://example.com/page",
  "title": "Page Title",
  "content": "Full HTML content",
  "text_content": "Clean text content",
  "meta_description": "Page description",
  "meta_keywords": "page, keywords",
  "links": [...],
  "images": [...],
  "headers": {...},
  "timestamp": "2024-01-01T12:00:00",
  "response_status": 200,
  "content_type": "text/html",
  "file_size": 12345
}
```

### 2. Document Data (`data/documents/`)
```json
{
  "url": "https://example.com/document.pdf",
  "filename": "document.pdf",
  "file_type": "pdf",
  "content": "base64_encoded_content",
  "text_content": "Extracted text content",
  "metadata": {...},
  "file_size": 54321,
  "timestamp": "2024-01-01T12:00:00"
}
```

### 3. Link Data (`data/links/`)
```json
{
  "source_url": "https://example.com/page1",
  "target_url": "https://example.com/page2",
  "link_text": "Link text",
  "link_type": "internal",
  "timestamp": "2024-01-01T12:00:00"
}
```

## Configuration

### Settings (`webcrawler/settings.py`)

Key settings you can modify:

- `DOWNLOAD_DELAY`: Delay between requests (default: 1 second)
- `CONCURRENT_REQUESTS_PER_DOMAIN`: Concurrent requests per domain (default: 8)
- `DEPTH_LIMIT`: Maximum crawling depth (default: 5)
- `ROBOTSTXT_OBEY`: Respect robots.txt (default: True)
- `MAX_FILE_SIZE`: Maximum file size to download (default: 50MB)
- `CRAWL_FILE_EXTENSIONS`: File extensions to process as documents

### Custom Processing

You can extend the crawler by:

1. **Adding new document processors** in `utils/document_processor.py`
2. **Creating custom pipelines** in `webcrawler/pipelines.py`
3. **Adding middlewares** in `webcrawler/middlewares.py`
4. **Modifying spider behavior** in `webcrawler/spiders/main_spider.py`

## Monitoring and Logging

- Logs are saved to `data/logs/webcrawler.log`
- Use different log levels for varying detail:
  - `DEBUG`: Detailed debugging information
  - `INFO`: General information about crawling progress
  - `WARNING`: Warning messages
  - `ERROR`: Error messages only

## Performance Tips

1. **Adjust delay settings** based on target website's capacity
2. **Use appropriate concurrent request limits** to avoid overwhelming servers
3. **Set reasonable depth limits** to prevent infinite crawling
4. **Monitor memory usage** for large-scale crawls
5. **Use allowed_domains** to focus crawling scope

## Ethical Considerations

- Always respect `robots.txt` files
- Use reasonable delays to avoid overloading servers
- Be mindful of website terms of service
- Consider reaching out to website owners for large-scale crawling
- Respect copyright and data privacy laws

## Troubleshooting

### Common Issues

1. **Import errors**: Ensure all dependencies are installed
2. **Permission errors**: Check file/directory permissions
3. **Memory issues**: Reduce concurrent requests or depth limit
4. **Robots.txt blocking**: Disable with `--no-obey-robots` if appropriate

### Debug Mode

Run with debug logging to see detailed information:

```bash
python run_crawler.py --start-urls "https://example.com" --log-level DEBUG
```

## Contributing

Feel free to contribute by:

1. Adding support for more document types
2. Improving text extraction algorithms
3. Adding new output formats
4. Enhancing error handling
5. Adding tests

## License

This project is open source. Please ensure compliance with applicable laws and website terms of service when using this crawler.