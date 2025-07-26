#!/usr/bin/env python3
"""
Display project information and structure
"""

import os
import json
from datetime import datetime


def show_project_info():
    """Display comprehensive project information"""
    
    print("🕷️  Web Crawler Project Information")
    print("=" * 60)
    
    project_info = {
        "name": "Advanced Web Crawler with Scrapy",
        "description": "Comprehensive web crawler with document processing capabilities",
        "version": "1.0.0",
        "created": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "features": [
            "Web page crawling and content extraction",
            "Document processing (PDF, Word, Excel, PowerPoint)",
            "Recursive link following with depth control",
            "Configurable crawling policies",
            "Data deduplication and validation",
            "JSON output with organized structure", 
            "Comprehensive logging and monitoring",
            "Respectful crawling with robots.txt support"
        ],
        "supported_formats": [
            "HTML/Web pages",
            "PDF documents",
            "Microsoft Word (.doc, .docx)",
            "Microsoft Excel (.xls, .xlsx)", 
            "Microsoft PowerPoint (.ppt, .pptx)",
            "Plain text files (.txt)",
            "Rich Text Format (.rtf)",
            "OpenDocument formats (.odt, .ods, .odp)"
        ]
    }
    
    # Display basic info
    print(f"📋 Name: {project_info['name']}")
    print(f"📝 Description: {project_info['description']}")
    print(f"🏷️  Version: {project_info['version']}")
    print(f"📅 Created: {project_info['created']}")
    
    # Display features
    print(f"\n✨ Features:")
    for feature in project_info['features']:
        print(f"   • {feature}")
    
    # Display supported formats
    print(f"\n📄 Supported Document Formats:")
    for format_type in project_info['supported_formats']:
        print(f"   • {format_type}")
    
    print(f"\n📁 Project Structure:")
    show_project_structure()
    
    print(f"\n🚀 Quick Start Commands:")
    show_quick_commands()
    
    print(f"\n📚 Documentation Files:")
    docs = [
        "README.md - Complete documentation",
        "QUICKSTART.md - Quick start guide", 
        "requirements.txt - Python dependencies",
        "config/custom_settings.py - Configuration profiles"
    ]
    for doc in docs:
        print(f"   • {doc}")


def show_project_structure():
    """Display project directory structure"""
    
    structure = {
        "webcrawler/": "Main crawler package",
        "├── __init__.py": "Package initialization",
        "├── settings.py": "Scrapy configuration settings",
        "├── items.py": "Data structure definitions",
        "├── pipelines.py": "Data processing pipelines",
        "├── middlewares.py": "Request/response middlewares",
        "└── spiders/": "Spider implementations",
        "    ├── __init__.py": "Spiders package init",
        "    └── main_spider.py": "Main crawling spider",
        "utils/": "Utility modules",
        "├── __init__.py": "Utils package init",
        "└── document_processor.py": "Document processing utilities",
        "config/": "Configuration files",
        "└── custom_settings.py": "Custom setting profiles",
        "examples/": "Example scripts",
        "└── run_examples.py": "Interactive examples",
        "tests/": "Test files",
        "└── test_document_processor.py": "Document processor tests",
        "data/": "Output directory",
        "├── pages/": "Web page data",
        "├── documents/": "Document data", 
        "├── links/": "Link data",
        "├── logs/": "Log files",
        "└── files/": "Downloaded files"
    }
    
    for path, description in structure.items():
        if path.startswith("├──") or path.startswith("└──") or path.startswith("    "):
            print(f"   {path:<25} {description}")
        else:
            print(f"   {path:<25} {description}")


def show_quick_commands():
    """Display quick start commands"""
    
    commands = [
        ("Test setup", "python3 test_setup.py"),
        ("Run demo", "python3 demo_crawler.py"),
        ("Basic crawl", "python3 run_crawler.py --start-urls 'https://httpbin.org'"),
        ("Document crawl", "python3 run_crawler.py --start-urls 'https://python.org' --max-depth 3"),
        ("Custom crawl", "python3 run_crawler.py --start-urls 'site1.com,site2.com' --delay 2"),
        ("Run examples", "python3 examples/run_examples.py"),
        ("Run tests", "python3 tests/test_document_processor.py")
    ]
    
    for description, command in commands:
        print(f"   • {description:<15} {command}")


def save_project_info():
    """Save project information to JSON file"""
    
    project_data = {
        "name": "Advanced Web Crawler with Scrapy",
        "version": "1.0.0",
        "description": "Comprehensive web crawler with document processing capabilities",
        "created": datetime.now().isoformat(),
        "main_files": [
            "run_crawler.py",
            "demo_crawler.py", 
            "test_setup.py",
            "scrapy.cfg"
        ],
        "directories": [
            "webcrawler/",
            "utils/",
            "config/",
            "examples/",
            "tests/",
            "data/"
        ],
        "dependencies": [
            "scrapy", "requests", "PyPDF2", "pdfplumber", 
            "python-docx", "openpyxl", "beautifulsoup4", 
            "lxml", "selenium", "fake-useragent", "python-pptx"
        ]
    }
    
    with open('project_info.json', 'w') as f:
        json.dump(project_data, f, indent=2)
    
    print(f"\n💾 Project information saved to: project_info.json")


def main():
    """Main function"""
    show_project_info()
    save_project_info()
    
    print(f"\n🎉 Web crawler project setup complete!")
    print(f"   Next steps:")
    print(f"   1. Install dependencies: pip3 install -r requirements.txt")
    print(f"   2. Test setup: python3 test_setup.py")
    print(f"   3. Run demo: python3 demo_crawler.py")
    print(f"   4. Read documentation: README.md and QUICKSTART.md")


if __name__ == '__main__':
    main()