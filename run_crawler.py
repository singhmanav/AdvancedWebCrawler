#!/usr/bin/env python3
"""
Web Crawler Runner Script

This script provides a convenient way to run the web crawler with various options.
"""

import argparse
import sys
import os
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from webcrawler.spiders.main_spider import MainSpider


def main():
    """Main function to run the crawler"""
    parser = argparse.ArgumentParser(description='Run the web crawler')
    
    # Add command line arguments
    parser.add_argument(
        '--start-urls', 
        type=str, 
        required=True,
        help='Comma-separated list of URLs to start crawling from'
    )
    
    parser.add_argument(
        '--allowed-domains', 
        type=str, 
        help='Comma-separated list of allowed domains (optional)'
    )
    
    parser.add_argument(
        '--max-depth', 
        type=int, 
        default=3,
        help='Maximum crawling depth (default: 3)'
    )
    
    parser.add_argument(
        '--delay', 
        type=float, 
        default=1.0,
        help='Download delay in seconds (default: 1.0)'
    )
    
    parser.add_argument(
        '--concurrent-requests', 
        type=int, 
        default=8,
        help='Number of concurrent requests (default: 8)'
    )
    
    parser.add_argument(
        '--obey-robots', 
        action='store_true',
        default=True,
        help='Obey robots.txt (default: True)'
    )
    
    parser.add_argument(
        '--log-level', 
        type=str, 
        default='INFO',
        choices=['DEBUG', 'INFO', 'WARNING', 'ERROR'],
        help='Log level (default: INFO)'
    )
    
    parser.add_argument(
        '--output-dir', 
        type=str, 
        default='data',
        help='Output directory for crawled data (default: data)'
    )
    
    args = parser.parse_args()
    
    # Validate start URLs
    if not args.start_urls:
        print("Error: --start-urls is required")
        sys.exit(1)
    
    # Create output directory if it doesn't exist
    os.makedirs(args.output_dir, exist_ok=True)
    os.makedirs(f"{args.output_dir}/logs", exist_ok=True)
    
    # Get project settings
    settings = get_project_settings()
    
    # Override settings with command line arguments
    settings.set('DOWNLOAD_DELAY', args.delay)
    settings.set('CONCURRENT_REQUESTS_PER_DOMAIN', args.concurrent_requests)
    settings.set('ROBOTSTXT_OBEY', args.obey_robots)
    settings.set('LOG_LEVEL', args.log_level)
    settings.set('LOG_FILE', f'{args.output_dir}/logs/webcrawler.log')
    
    # Create and configure crawler process
    process = CrawlerProcess(settings)
    
    # Add spider to the process
    process.crawl(
        MainSpider,
        start_urls=args.start_urls,
        allowed_domains=args.allowed_domains,
        max_depth=args.max_depth
    )
    
    print(f"Starting web crawler...")
    print(f"Start URLs: {args.start_urls}")
    print(f"Max depth: {args.max_depth}")
    print(f"Output directory: {args.output_dir}")
    print(f"Log level: {args.log_level}")
    
    # Start crawling
    process.start()


if __name__ == '__main__':
    main()