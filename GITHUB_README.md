# 🕷️ Advanced Web Crawler with Scrapy

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![Scrapy](https://img.shields.io/badge/Scrapy-2.11+-green.svg)](https://scrapy.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![GitHub Stars](https://img.shields.io/github/stars/singhmanav/AdvancedWebCrawler.svg)](https://github.com/singhmanav/AdvancedWebCrawler/stargazers)
[![GitHub Issues](https://img.shields.io/github/issues/singhmanav/AdvancedWebCrawler.svg)](https://github.com/singhmanav/AdvancedWebCrawler/issues)

A comprehensive, production-ready web crawler built with Scrapy that can crawl websites, extract data from various document types (PDFs, Word docs, Excel files, etc.), and traverse links recursively with intelligent rate limiting and content processing.

## 🚀 Features

- **🌐 Web Page Crawling** - Extract content, metadata, links, and images from web pages
- **📄 Document Processing** - Handle PDFs, Word documents, Excel files, PowerPoint presentations, and more
- **🔗 Smart Link Traversal** - Recursively follow internal links with configurable depth limits
- **🧹 Content Extraction** - Clean text extraction from various document formats
- **🔄 Deduplication** - Automatic filtering of duplicate URLs and content
- **⚙️ Highly Configurable** - Customizable delays, concurrent requests, and crawling policies
- **💾 Structured Output** - Save crawled data in organized JSON format
- **📊 Comprehensive Logging** - Monitor crawling progress with detailed logs
- **🤖 Respectful Crawling** - Built-in robots.txt support and rate limiting
- **🔄 User Agent Rotation** - Anti-blocking measures with fake user agents

## 📋 Supported Document Types

| Type | Extensions | Processing |
|------|------------|------------|
| PDF | `.pdf` | Full text extraction with metadata |
| Microsoft Word | `.doc`, `.docx` | Text and table extraction |
| Microsoft Excel | `.xls`, `.xlsx` | Cell data extraction from all sheets |
| Microsoft PowerPoint | `.ppt`, `.pptx` | Slide text extraction |
| Text Files | `.txt` | Multi-encoding support |
| Rich Text | `.rtf` | RTF command parsing |
| HTML | `.html`, `.htm` | Clean text extraction |
| OpenDocument | `.odt`, `.ods`, `.odp` | Full document parsing |

## 🛠️ Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/singhmanav/AdvancedWebCrawler.git
cd AdvancedWebCrawler

# Install dependencies
pip3 install -r requirements.txt

# Test setup
python3 test_setup.py
```

### Basic Usage

```bash
# Simple crawl
python3 run_crawler.py --start-urls "https://example.com" --max-depth 2

# Advanced crawl with document processing
python3 run_crawler.py \
    --start-urls "https://python.org" \
    --max-depth 3 \
    --delay 2 \
    --log-level INFO

# Multiple sites
python3 run_crawler.py \
    --start-urls "https://site1.com,https://site2.com" \
    --allowed-domains "site1.com,site2.com" \
    --max-depth 2
```

### Run Demo

```bash
# Safe demo with test sites
python3 demo_crawler.py

# Interactive examples
python3 examples/run_examples.py
```

## 📊 Output Examples

### Web Page Data
```json
{
  "url": "https://example.com/page",
  "title": "Example Page",
  "text_content": "Clean extracted text...",
  "links": [{"url": "...", "text": "..."}],
  "images": [{"url": "...", "alt": "..."}],
  "timestamp": "2024-01-01T12:00:00",
  "response_status": 200
}
```

### Document Data
```json
{
  "url": "https://example.com/document.pdf",
  "filename": "document.pdf",
  "file_type": "pdf",
  "text_content": "Extracted PDF text...",
  "metadata": {"author": "...", "title": "..."},
  "file_size": 54321
}
```

## ⚙️ Configuration

### Command Line Options

| Option | Description | Default |
|--------|-------------|---------|
| `--start-urls` | URLs to start crawling (required) | - |
| `--allowed-domains` | Restrict crawling to these domains | All |
| `--max-depth` | Maximum crawling depth | 3 |
| `--delay` | Download delay in seconds | 1.0 |
| `--concurrent-requests` | Concurrent requests per domain | 8 |
| `--log-level` | Logging level | INFO |
| `--output-dir` | Output directory | data |

### Custom Settings

```python
# Use predefined configurations
from config.custom_settings import RESPECTFUL_CRAWLING, AGGRESSIVE_CRAWLING

# Or modify webcrawler/settings.py for custom behavior
```

## 📁 Project Structure

```
AdvancedWebCrawler/
├── README.md                    # Main documentation
├── QUICKSTART.md               # Quick start guide
├── requirements.txt            # Dependencies
├── run_crawler.py              # Main execution script
├── demo_crawler.py             # Safe demo script
├── webcrawler/                 # Main Scrapy package
│   ├── spiders/               # Spider implementations
│   ├── pipelines.py           # Data processing
│   ├── middlewares.py         # Request/response handling
│   ├── items.py               # Data structures
│   └── settings.py            # Configuration
├── utils/                      # Utility modules
│   └── document_processor.py  # Document processing
├── config/                     # Configuration profiles
├── examples/                   # Usage examples
├── tests/                      # Test suite
└── data/                       # Output directory
```

## 🧪 Testing

```bash
# Run setup verification
python3 test_setup.py

# Run unit tests
python3 -m pytest tests/

# Run document processor tests
python3 tests/test_document_processor.py
```

## 🔧 Extending the Crawler

### Add New Document Processors

```python
# In utils/document_processor.py
def process_new_format(self, content: bytes) -> str:
    # Your processing logic here
    return extracted_text
```

### Custom Pipelines

```python
# In webcrawler/pipelines.py
class CustomPipeline:
    def process_item(self, item, spider):
        # Your custom processing
        return item
```

### Custom Middlewares

```python
# In webcrawler/middlewares.py
class CustomMiddleware:
    def process_request(self, request, spider):
        # Your custom logic
        return None
```

## 📈 Performance Tips

1. **Adjust delays** based on target website capacity
2. **Use domain restrictions** to focus crawling scope
3. **Monitor memory usage** for large-scale crawls
4. **Set reasonable depth limits** to prevent infinite crawling
5. **Use concurrent request limits** appropriately

## 🐳 Docker Support

```bash
# Build and run with Docker
docker-compose up

# Run specific commands
docker-compose run --rm webcrawler python demo_crawler.py
docker-compose run --rm webcrawler python run_crawler.py --start-urls "https://httpbin.org"
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

### Development Setup

```bash
git clone https://github.com/singhmanav/AdvancedWebCrawler.git
cd AdvancedWebCrawler
pip3 install -r requirements.txt
python3 test_setup.py
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ⚠️ Ethical Usage

- Always respect `robots.txt` files
- Use reasonable delays to avoid overloading servers
- Be mindful of website terms of service
- Consider reaching out to website owners for large-scale crawling
- Respect copyright and data privacy laws

## 🐛 Troubleshooting

### Common Issues

1. **Import errors**: Run `pip3 install -r requirements.txt`
2. **Permission errors**: Check file/directory permissions
3. **Memory issues**: Reduce concurrent requests or depth limit
4. **Robots.txt blocking**: Use `--no-obey-robots` if appropriate

### Getting Help

- Check the [QUICKSTART.md](QUICKSTART.md) guide
- Run the demo: `python3 demo_crawler.py`
- Enable debug logging: `--log-level DEBUG`
- Open an issue on GitHub

## 📞 Support

If you found this project helpful, please give it a ⭐ on GitHub!

For questions or support, please open an issue or contact the maintainers.

## 🔗 Links

- [GitHub Repository](https://github.com/singhmanav/AdvancedWebCrawler)
- [Issue Tracker](https://github.com/singhmanav/AdvancedWebCrawler/issues)
- [Scrapy Documentation](https://docs.scrapy.org/)

---

**Built with ❤️ using Python and Scrapy**