#!/usr/bin/env python3
"""
Demo script showing how to use the web crawler programmatically
"""

import os
import sys
import json
from datetime import datetime
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

# Add the current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from webcrawler.spiders.main_spider import MainSpider


def run_demo_crawl():
    """Run a demonstration crawl"""
    
    print("🕷️  Web Crawler Demo")
    print("=" * 50)
    print("This demo will crawl a test website and show you the results.")
    print()
    
    # Create output directory
    output_dir = f"demo_output_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    os.makedirs(output_dir, exist_ok=True)
    os.makedirs(f"{output_dir}/logs", exist_ok=True)
    
    # Configure settings
    settings = get_project_settings()
    settings.set('LOG_LEVEL', 'INFO')
    settings.set('LOG_FILE', f'{output_dir}/logs/demo.log')
    settings.set('DOWNLOAD_DELAY', 1)
    settings.set('CONCURRENT_REQUESTS_PER_DOMAIN', 2)
    settings.set('DEPTH_LIMIT', 2)
    
    # Update pipelines to use demo output directory
    settings.set('ITEM_PIPELINES', {
        'webcrawler.pipelines.ValidationPipeline': 100,
        'webcrawler.pipelines.DeduplicationPipeline': 200,
        'webcrawler.pipelines.DocumentProcessingPipeline': 300,
        'webcrawler.pipelines.JsonWriterPipeline': 800,
    })
    
    # Demo URLs (safe test sites)
    demo_urls = [
        'https://httpbin.org',  # HTTP testing service
        'https://quotes.toscrape.com',  # Quotes scraping practice site
    ]
    
    print(f"Demo URLs: {', '.join(demo_urls)}")
    print(f"Output directory: {output_dir}")
    print(f"Max depth: 2")
    print()
    
    # Create and run crawler
    process = CrawlerProcess(settings)
    
    process.crawl(
        MainSpider,
        start_urls=demo_urls,
        max_depth=2
    )
    
    print("Starting crawl...")
    try:
        process.start()
        print(f"\n✅ Demo crawl completed!")
        print(f"📁 Check results in: {output_dir}/")
        
        # Show summary of results
        show_results_summary(output_dir)
        
    except Exception as e:
        print(f"\n❌ Demo crawl failed: {e}")


def show_results_summary(output_dir):
    """Show a summary of crawled results"""
    
    print("\n📊 Crawl Results Summary:")
    print("-" * 30)
    
    # Count files in each category
    categories = ['pages', 'documents', 'links']
    
    for category in categories:
        category_dir = f"{output_dir}/{category}"
        if os.path.exists(category_dir):
            file_count = len([f for f in os.listdir(category_dir) if f.endswith('.json')])
            print(f"{category.capitalize()}: {file_count} items")
            
            # Show sample data for pages
            if category == 'pages' and file_count > 0:
                sample_file = os.listdir(category_dir)[0]
                try:
                    with open(f"{category_dir}/{sample_file}", 'r') as f:
                        sample_data = json.load(f)
                        print(f"  Sample page: {sample_data.get('title', 'No title')} ({sample_data.get('url', '')})")
                except:
                    pass
        else:
            print(f"{category.capitalize()}: 0 items")
    
    # Show log summary
    log_file = f"{output_dir}/logs/demo.log"
    if os.path.exists(log_file):
        with open(log_file, 'r') as f:
            log_lines = f.readlines()
            print(f"Log entries: {len(log_lines)}")
    
    print(f"\n📝 Full logs available at: {log_file}")


def main():
    """Main function"""
    try:
        run_demo_crawl()
    except KeyboardInterrupt:
        print("\n⏹️  Demo interrupted by user")
    except Exception as e:
        print(f"\n❌ Demo failed: {e}")
        print("Please check that all dependencies are installed:")
        print("pip3 install -r requirements.txt")


if __name__ == '__main__':
    main()