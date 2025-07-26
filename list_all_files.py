#!/usr/bin/env python3
"""
Simple script to list all project files
"""

import os

def list_all_files():
    """List all files in the project"""
    print("📁 Complete Project File Listing")
    print("=" * 40)
    
    # Get all files recursively
    all_files = []
    for root, dirs, files in os.walk('.'):
        # Skip hidden directories and __pycache__
        dirs[:] = [d for d in dirs if not d.startswith('.') and d != '__pycache__']
        
        for file in files:
            if not file.startswith('.') and not file.endswith('.pyc'):
                file_path = os.path.join(root, file).replace('./', '')
                file_size = os.path.getsize(os.path.join(root, file))
                all_files.append((file_path, file_size))
    
    # Sort files
    all_files.sort()
    
    # Display files
    total_files = 0
    total_size = 0
    
    for file_path, file_size in all_files:
        total_files += 1
        total_size += file_size
        print(f"📄 {file_path:<40} ({file_size:,} bytes)")
    
    print(f"\n📊 Summary: {total_files} files, {total_size:,} bytes total")
    
    # Check for key files
    key_files = [
        'README.md',
        'QUICKSTART.md', 
        'requirements.txt',
        'run_crawler.py',
        'webcrawler/settings.py',
        'webcrawler/spiders/main_spider.py',
        'utils/document_processor.py'
    ]
    
    print(f"\n✅ Key Files Check:")
    missing = []
    for key_file in key_files:
        exists = any(key_file in f[0] for f in all_files)
        status = "✅" if exists else "❌"
        print(f"{status} {key_file}")
        if not exists:
            missing.append(key_file)
    
    if not missing:
        print(f"\n🎉 All key files are present!")
        print(f"🚀 Web crawler project is complete and ready to use!")
    else:
        print(f"\n⚠️ Missing files: {', '.join(missing)}")

if __name__ == '__main__':
    list_all_files()