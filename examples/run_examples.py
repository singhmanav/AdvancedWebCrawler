#!/usr/bin/env python3
"""
Example usage of the web crawler
"""

import os
import sys
import subprocess


def run_example_crawl():
    """Run example crawls with different configurations"""
    
    print("Web Crawler Examples")
    print("=" * 50)
    
    examples = [
        {
            "name": "Basic Website Crawl",
            "description": "Crawl a website with default settings",
            "command": [
                "python", "run_crawler.py",
                "--start-urls", "https://httpbin.org",
                "--max-depth", "2",
                "--delay", "1"
            ]
        },
        {
            "name": "Deep Crawl with Documents",
            "description": "Deep crawl including document processing",
            "command": [
                "python", "run_crawler.py",
                "--start-urls", "https://www.python.org",
                "--max-depth", "3",
                "--delay", "2",
                "--concurrent-requests", "4",
                "--log-level", "INFO"
            ]
        },
        {
            "name": "Multi-site Crawl",
            "description": "Crawl multiple websites",
            "command": [
                "python", "run_crawler.py",
                "--start-urls", "https://httpbin.org,https://quotes.toscrape.com",
                "--max-depth", "2",
                "--delay", "1.5"
            ]
        }
    ]
    
    for i, example in enumerate(examples, 1):
        print(f"\n{i}. {example['name']}")
        print(f"   Description: {example['description']}")
        print(f"   Command: {' '.join(example['command'])}")
        
        response = input(f"\nRun this example? (y/n): ").lower().strip()
        if response == 'y':
            print(f"\nRunning: {example['name']}")
            print("-" * 40)
            try:
                subprocess.run(example['command'], check=True)
                print(f"\n✅ {example['name']} completed successfully!")
            except subprocess.CalledProcessError as e:
                print(f"\n❌ {example['name']} failed: {e}")
            except KeyboardInterrupt:
                print(f"\n⏹️  {example['name']} interrupted by user")
        else:
            print("Skipped.")


if __name__ == "__main__":
    run_example_crawl()