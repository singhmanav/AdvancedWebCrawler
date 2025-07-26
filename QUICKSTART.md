# Quick Start Guide

## 1. Installation

First, ensure you have Python 3.7+ installed, then install dependencies:

```bash
pip3 install scrapy requests PyPDF2 pdfplumber python-docx openpyxl beautifulsoup4 lxml selenium fake-useragent
```

Or use the requirements file:

```bash
pip3 install -r requirements.txt
```

## 2. Test Your Setup

Run the setup test to verify everything is working:

```bash
python3 test_setup.py
```

## 3. Basic Usage Examples

### Example 1: Crawl a Simple Website

```bash
python3 run_crawler.py --start-urls "https://httpbin.org" --max-depth 2
```

### Example 2: Crawl with Document Processing

```bash
python3 run_crawler.py \
    --start-urls "https://www.python.org" \
    --max-depth 3 \
    --delay 2 \
    --log-level INFO
```

### Example 3: Multiple Sites with Custom Settings

```bash
python3 run_crawler.py \
    --start-urls "https://httpbin.org,https://quotes.toscrape.com" \
    --allowed-domains "httpbin.org,quotes.toscrape.com" \
    --max-depth 2 \
    --delay 1.5 \
    --concurrent-requests 4
```

## 4. Check Results

After crawling, check the `data/` directory for results:

- `data/pages/` - Web page content
- `data/documents/` - Document files and extracted text
- `data/links/` - Discovered links
- `data/logs/` - Crawling logs

## 5. Advanced Usage

### Using Scrapy Directly

```bash
scrapy crawl main_spider -a start_urls="https://example.com" -a max_depth=3
```

### Custom Settings

Edit `webcrawler/settings.py` or use configuration profiles in `config/custom_settings.py`

## 6. Common Issues

1. **Permission denied**: Use `chmod +x run_crawler.py`
2. **Import errors**: Install missing dependencies
3. **Slow crawling**: Adjust `--delay` and `--concurrent-requests`
4. **Blocked by robots.txt**: Use `--no-obey-robots` (use responsibly)

## 7. Output Examples

### Web Page Data
```json
{
  "url": "https://example.com",
  "title": "Example Page", 
  "text_content": "Extracted clean text...",
  "links": [{"url": "...", "text": "..."}],
  "timestamp": "2024-01-01T12:00:00"
}
```

### Document Data
```json
{
  "url": "https://example.com/doc.pdf",
  "filename": "doc.pdf",
  "file_type": "pdf", 
  "text_content": "Extracted PDF text...",
  "file_size": 12345
}
```

## 8. Next Steps

- Read the full README.md for detailed documentation
- Explore example configurations in `config/custom_settings.py`
- Run interactive examples with `python3 examples/run_examples.py`
- Customize spiders in `webcrawler/spiders/` for specific needs