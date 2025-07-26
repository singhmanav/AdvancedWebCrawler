#!/usr/bin/env python3
"""
Project verification script - checks all files and components
"""

import os
import sys
from pathlib import Path


def check_file_exists(file_path, description=""):
    """Check if a file exists and return status"""
    exists = os.path.exists(file_path)
    status = "✅" if exists else "❌"
    size = ""
    if exists and os.path.isfile(file_path):
        size = f" ({os.path.getsize(file_path)} bytes)"
    print(f"{status} {file_path}{size} {description}")
    return exists


def check_directory_exists(dir_path, description=""):
    """Check if a directory exists"""
    exists = os.path.exists(dir_path) and os.path.isdir(dir_path)
    status = "✅" if exists else "❌"
    print(f"{status} {dir_path}/ {description}")
    return exists


def verify_project_structure():
    """Verify complete project structure"""
    print("🔍 Web Crawler Project Verification")
    print("=" * 50)
    
    # Core files
    print("\n📋 Core Project Files:")
    core_files = [
        ("README.md", "- Main documentation"),
        ("QUICKSTART.md", "- Quick start guide"),
        ("requirements.txt", "- Python dependencies"),
        ("scrapy.cfg", "- Scrapy configuration"),
        ("run_crawler.py", "- Main execution script"),
        ("demo_crawler.py", "- Demo script"),
        ("test_setup.py", "- Setup verification"),
        ("project_info.py", "- Project information"),
        ("project_info.json", "- Project metadata"),
    ]
    
    missing_core = []
    for file_path, desc in core_files:
        if not check_file_exists(file_path, desc):
            missing_core.append(file_path)
    
    # Main package files
    print("\n📦 Main Package (webcrawler/):")
    package_files = [
        ("webcrawler/__init__.py", "- Package init"),
        ("webcrawler/settings.py", "- Scrapy settings"),
        ("webcrawler/items.py", "- Data structures"),
        ("webcrawler/pipelines.py", "- Data processing"),
        ("webcrawler/middlewares.py", "- Request/response handling"),
        ("webcrawler/spiders/__init__.py", "- Spiders package init"),
        ("webcrawler/spiders/main_spider.py", "- Main spider implementation"),
    ]
    
    missing_package = []
    for file_path, desc in package_files:
        if not check_file_exists(file_path, desc):
            missing_package.append(file_path)
    
    # Utility files
    print("\n🔧 Utility Files:")
    util_files = [
        ("utils/__init__.py", "- Utils package init"),
        ("utils/document_processor.py", "- Document processing"),
    ]
    
    missing_utils = []
    for file_path, desc in util_files:
        if not check_file_exists(file_path, desc):
            missing_utils.append(file_path)
    
    # Configuration files
    print("\n⚙️ Configuration Files:")
    config_files = [
        ("config/custom_settings.py", "- Custom configurations"),
    ]
    
    missing_config = []
    for file_path, desc in config_files:
        if not check_file_exists(file_path, desc):
            missing_config.append(file_path)
    
    # Example and test files
    print("\n🧪 Examples and Tests:")
    test_files = [
        ("examples/run_examples.py", "- Interactive examples"),
        ("tests/test_document_processor.py", "- Unit tests"),
    ]
    
    missing_tests = []
    for file_path, desc in test_files:
        if not check_file_exists(file_path, desc):
            missing_tests.append(file_path)
    
    # Directories
    print("\n📁 Output Directories:")
    directories = [
        ("data", "- Main output directory"),
        ("data/pages", "- Web page data"),
        ("data/documents", "- Document data"),
        ("data/links", "- Link data"),
        ("data/logs", "- Log files"),
        ("data/files", "- Downloaded files"),
    ]
    
    missing_dirs = []
    for dir_path, desc in directories:
        if not check_directory_exists(dir_path, desc):
            missing_dirs.append(dir_path)
            # Create missing directories
            try:
                os.makedirs(dir_path, exist_ok=True)
                print(f"  ↳ Created directory: {dir_path}")
            except Exception as e:
                print(f"  ↳ Failed to create: {dir_path} - {e}")
    
    # Summary
    print("\n📊 Verification Summary:")
    print("-" * 30)
    
    all_missing = missing_core + missing_package + missing_utils + missing_config + missing_tests
    
    if not all_missing and not missing_dirs:
        print("🎉 All files and directories are present!")
        print("✅ Project structure is complete and ready to use")
        return True
    else:
        if all_missing:
            print(f"❌ Missing files ({len(all_missing)}):")
            for missing in all_missing:
                print(f"   - {missing}")
        
        if missing_dirs:
            print(f"❌ Missing directories ({len(missing_dirs)}):")
            for missing in missing_dirs:
                print(f"   - {missing}")
        
        return False


def check_file_contents():
    """Check if key files have proper content"""
    print("\n🔍 Content Verification:")
    print("-" * 30)
    
    # Check README.md
    try:
        with open('README.md', 'r') as f:
            readme_content = f.read()
            if len(readme_content) > 1000 and "Web Crawler with Scrapy" in readme_content:
                print("✅ README.md - Complete documentation present")
            else:
                print("❌ README.md - Content appears incomplete")
    except Exception as e:
        print(f"❌ README.md - Error reading: {e}")
    
    # Check requirements.txt
    try:
        with open('requirements.txt', 'r') as f:
            requirements = f.read().strip().split('\n')
            essential_packages = ['scrapy', 'requests', 'PyPDF2', 'pdfplumber', 'python-docx']
            missing_packages = []
            
            for package in essential_packages:
                if not any(package in req for req in requirements):
                    missing_packages.append(package)
            
            if not missing_packages:
                print(f"✅ requirements.txt - All {len(requirements)} dependencies listed")
            else:
                print(f"❌ requirements.txt - Missing: {', '.join(missing_packages)}")
                
    except Exception as e:
        print(f"❌ requirements.txt - Error reading: {e}")
    
    # Check main spider
    try:
        with open('webcrawler/spiders/main_spider.py', 'r') as f:
            spider_content = f.read()
            if "class MainSpider" in spider_content and "parse" in spider_content:
                print("✅ main_spider.py - Spider implementation complete")
            else:
                print("❌ main_spider.py - Spider implementation incomplete")
    except Exception as e:
        print(f"❌ main_spider.py - Error reading: {e}")


def show_usage_examples():
    """Show usage examples"""
    print("\n🚀 Ready to Use! Try these commands:")
    print("-" * 40)
    
    examples = [
        "# Test the setup",
        "python3 test_setup.py",
        "",
        "# Run a demo crawl", 
        "python3 demo_crawler.py",
        "",
        "# Basic website crawl",
        "python3 run_crawler.py --start-urls 'https://httpbin.org' --max-depth 2",
        "",
        "# Advanced crawl with documents",
        "python3 run_crawler.py --start-urls 'https://python.org' --max-depth 3 --delay 2",
        "",
        "# Interactive examples",
        "python3 examples/run_examples.py"
    ]
    
    for example in examples:
        print(example)


def main():
    """Main verification function"""
    project_complete = verify_project_structure()
    check_file_contents()
    
    if project_complete:
        show_usage_examples()
        print("\n🎯 Your web crawler is ready to use!")
    else:
        print("\n⚠️ Please fix missing files before using the crawler")
        return 1
    
    return 0


if __name__ == '__main__':
    sys.exit(main())