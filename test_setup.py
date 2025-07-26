#!/usr/bin/env python3
"""
Test script to verify the web crawler setup
"""

import sys
import importlib
import os


def test_imports():
    """Test if all required modules can be imported"""
    print("Testing imports...")
    
    required_modules = [
        'scrapy',
        'requests',
        'PyPDF2',
        'pdfplumber', 
        'docx',
        'openpyxl',
        'bs4',
        'fake_useragent'
    ]
    
    failed_imports = []
    
    for module in required_modules:
        try:
            importlib.import_module(module)
            print(f"✅ {module}")
        except ImportError as e:
            print(f"❌ {module}: {e}")
            failed_imports.append(module)
    
    if failed_imports:
        print(f"\n⚠️  Failed to import: {', '.join(failed_imports)}")
        print("Please install missing dependencies with: pip install -r requirements.txt")
        return False
    else:
        print("\n✅ All required modules imported successfully!")
        return True


def test_project_structure():
    """Test if project structure is correct"""
    print("\nTesting project structure...")
    
    required_files = [
        'scrapy.cfg',
        'requirements.txt',
        'run_crawler.py',
        'webcrawler/__init__.py',
        'webcrawler/settings.py',
        'webcrawler/items.py',
        'webcrawler/pipelines.py',
        'webcrawler/middlewares.py',
        'webcrawler/spiders/__init__.py',
        'webcrawler/spiders/main_spider.py',
        'utils/__init__.py',
        'utils/document_processor.py'
    ]
    
    missing_files = []
    
    for file_path in required_files:
        if os.path.exists(file_path):
            print(f"✅ {file_path}")
        else:
            print(f"❌ {file_path}")
            missing_files.append(file_path)
    
    if missing_files:
        print(f"\n⚠️  Missing files: {', '.join(missing_files)}")
        return False
    else:
        print("\n✅ All required files present!")
        return True


def test_scrapy_project():
    """Test if Scrapy project is correctly configured"""
    print("\nTesting Scrapy project configuration...")
    
    try:
        from scrapy.utils.project import get_project_settings
        settings = get_project_settings()
        
        if settings.get('BOT_NAME') == 'webcrawler':
            print("✅ Scrapy project configured correctly")
            return True
        else:
            print("❌ Scrapy project configuration issue")
            return False
    except Exception as e:
        print(f"❌ Scrapy configuration error: {e}")
        return False


def test_document_processor():
    """Test document processor functionality"""
    print("\nTesting document processor...")
    
    try:
        from utils.document_processor import DocumentProcessor
        processor = DocumentProcessor()
        
        # Test text processing
        test_content = b"Hello, world!"
        result = processor.process_document(test_content, 'txt')
        
        if result == "Hello, world!":
            print("✅ Document processor working correctly")
            return True
        else:
            print("❌ Document processor test failed")
            return False
    except Exception as e:
        print(f"❌ Document processor error: {e}")
        return False


def main():
    """Run all tests"""
    print("🕷️  Web Crawler Setup Test")
    print("=" * 50)
    
    tests = [
        test_imports,
        test_project_structure,
        test_scrapy_project,
        test_document_processor
    ]
    
    results = []
    for test in tests:
        results.append(test())
    
    print("\n" + "=" * 50)
    print("📊 Test Results:")
    
    if all(results):
        print("🎉 All tests passed! Your web crawler is ready to use.")
        print("\nNext steps:")
        print("1. Run a test crawl: python run_crawler.py --start-urls 'https://httpbin.org'")
        print("2. Check the examples: python examples/run_examples.py")
        print("3. Read the README.md for detailed usage instructions")
    else:
        print("⚠️  Some tests failed. Please fix the issues before using the crawler.")
        return 1
    
    return 0


if __name__ == '__main__':
    sys.exit(main())