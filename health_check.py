#!/usr/bin/env python3
"""
Health check script for CI/CD
Quick verification that the environment is properly set up
"""

import sys
import importlib
import traceback


def check_module(module_name, description=""):
    """Check if a module can be imported"""
    try:
        importlib.import_module(module_name)
        print(f"✅ {module_name} - {description}")
        return True
    except ImportError as e:
        print(f"❌ {module_name} - {description} - Error: {e}")
        return False
    except Exception as e:
        print(f"⚠️  {module_name} - {description} - Unexpected error: {e}")
        return False


def main():
    """Main health check function"""
    print("🏥 Advanced Web Crawler - Health Check")
    print("=" * 50)
    
    modules_to_check = [
        ("scrapy", "Web scraping framework"),
        ("requests", "HTTP library"),
        ("PyPDF2", "PDF processing library"),
        ("pdfplumber", "PDF text extraction"),
        ("docx", "Word document processing"),
        ("openpyxl", "Excel file processing"),
        ("bs4", "BeautifulSoup HTML parsing"),
        ("fake_useragent", "User agent rotation"),
        ("lxml", "XML/HTML parser"),
        ("urllib3", "HTTP client"),
        ("chardet", "Character encoding detection"),
    ]
    
    optional_modules = [
        ("pptx", "PowerPoint processing"),
        ("selenium", "Web browser automation"),
        ("pytest", "Testing framework"),
        ("magic", "File type detection"),
    ]
    
    print("\n📋 Core Dependencies:")
    print("-" * 30)
    core_success = 0
    for module, desc in modules_to_check:
        if check_module(module, desc):
            core_success += 1
    
    print(f"\n📋 Optional Dependencies:")
    print("-" * 30)
    optional_success = 0
    for module, desc in optional_modules:
        if check_module(module, desc):
            optional_success += 1
    
    print("\n📊 Health Check Summary:")
    print("-" * 30)
    print(f"Core modules: {core_success}/{len(modules_to_check)} working")
    print(f"Optional modules: {optional_success}/{len(optional_modules)} working")
    
    # Test project-specific imports
    print(f"\n🕷️ Project-Specific Imports:")
    print("-" * 30)
    
    project_modules = [
        ("webcrawler.items", "Scrapy items"),
        ("webcrawler.settings", "Scrapy settings"),
        ("webcrawler.spiders.main_spider", "Main spider"),
        ("utils.document_processor", "Document processor"),
    ]
    
    project_success = 0
    for module, desc in project_modules:
        if check_module(module, desc):
            project_success += 1
    
    print(f"Project modules: {project_success}/{len(project_modules)} working")
    
    # Overall health assessment
    core_health = (core_success / len(modules_to_check)) * 100
    project_health = (project_success / len(project_modules)) * 100
    
    print(f"\n🎯 Overall Health:")
    print("-" * 30)
    print(f"Core dependencies: {core_health:.1f}%")
    print(f"Project modules: {project_health:.1f}%")
    
    if core_health >= 80 and project_health >= 75:
        print(f"\n✅ Health Check: PASSED")
        print(f"Environment is ready for web crawling!")
        return True
    else:
        print(f"\n❌ Health Check: FAILED")
        print(f"Environment needs attention before use.")
        return False


if __name__ == '__main__':
    success = main()
    sys.exit(0 if success else 1)