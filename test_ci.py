#!/usr/bin/env python3
"""
Lightweight CI test script
Tests basic functionality without external dependencies
"""

import sys
import os
import unittest
from pathlib import Path


class CITestSuite(unittest.TestCase):
    """Basic test suite for CI"""
    
    def test_imports(self):
        """Test that all modules can be imported"""
        try:
            import scrapy
            import requests
            import PyPDF2
            import pdfplumber
            import docx
            import openpyxl
            from bs4 import BeautifulSoup
            from fake_useragent import UserAgent
            print("✅ All main dependencies imported successfully")
        except ImportError as e:
            self.fail(f"Import failed: {e}")
    
    def test_project_structure(self):
        """Test that project structure is correct"""
        required_files = [
            'webcrawler/__init__.py',
            'webcrawler/settings.py',
            'webcrawler/items.py',
            'webcrawler/pipelines.py',
            'webcrawler/middlewares.py',
            'webcrawler/spiders/__init__.py',
            'webcrawler/spiders/main_spider.py',
            'utils/__init__.py',
            'utils/document_processor.py',
            'requirements.txt',
            'scrapy.cfg',
        ]
        
        for file_path in required_files:
            self.assertTrue(
                os.path.exists(file_path), 
                f"Required file missing: {file_path}"
            )
        print("✅ Project structure verified")
    
    def test_scrapy_spider_import(self):
        """Test that Scrapy spider can be imported"""
        try:
            from webcrawler.spiders.main_spider import MainSpider
            spider = MainSpider()
            self.assertEqual(spider.name, 'main_spider')
            print("✅ Main spider imported and instantiated successfully")
        except Exception as e:
            self.fail(f"Spider import failed: {e}")
    
    def test_document_processor(self):
        """Test document processor functionality"""
        try:
            from utils.document_processor import DocumentProcessor
            processor = DocumentProcessor()
            
            # Test text processing
            test_content = b"Hello, world!"
            result = processor.process_document(test_content, 'txt')
            self.assertEqual(result, "Hello, world!")
            print("✅ Document processor basic functionality verified")
        except Exception as e:
            self.fail(f"Document processor test failed: {e}")
    
    def test_scrapy_items(self):
        """Test Scrapy items"""
        try:
            from webcrawler.items import WebPageItem, DocumentItem, LinkItem
            
            # Test WebPageItem
            item = WebPageItem()
            item['url'] = 'https://example.com'
            item['title'] = 'Test Title'
            self.assertEqual(item['url'], 'https://example.com')
            
            print("✅ Scrapy items verified")
        except Exception as e:
            self.fail(f"Items test failed: {e}")
    
    def test_settings_import(self):
        """Test Scrapy settings can be imported"""
        try:
            from scrapy.utils.project import get_project_settings
            settings = get_project_settings()
            self.assertIsNotNone(settings)
            print("✅ Scrapy settings imported successfully")
        except Exception as e:
            self.fail(f"Settings import failed: {e}")


def run_ci_tests():
    """Run CI test suite"""
    print("🧪 Running CI Test Suite")
    print("=" * 40)
    
    # Create test suite
    suite = unittest.TestLoader().loadTestsFromTestCase(CITestSuite)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Print summary
    print("\n" + "=" * 40)
    if result.wasSuccessful():
        print("🎉 All CI tests passed!")
        return True
    else:
        print(f"❌ {len(result.failures)} test(s) failed")
        print(f"❌ {len(result.errors)} test(s) had errors")
        return False


if __name__ == '__main__':
    success = run_ci_tests()
    sys.exit(0 if success else 1)