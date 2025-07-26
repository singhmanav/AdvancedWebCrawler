#!/usr/bin/env python3
"""
Show project structure in a tree format
"""

import os

def show_tree(directory='.', prefix='', max_depth=3, current_depth=0):
    """Display directory tree structure"""
    if current_depth >= max_depth:
        return
    
    items = []
    try:
        items = sorted(os.listdir(directory))
        items = [item for item in items if not item.startswith('.') and item != '__pycache__']
    except PermissionError:
        return
    
    for i, item in enumerate(items):
        item_path = os.path.join(directory, item)
        is_last = i == len(items) - 1
        
        current_prefix = '└── ' if is_last else '├── '
        print(f"{prefix}{current_prefix}{item}")
        
        if os.path.isdir(item_path):
            extension = '    ' if is_last else '│   '
            show_tree(item_path, prefix + extension, max_depth, current_depth + 1)

def main():
    print("🌳 Web Crawler Project Structure")
    print("=" * 40)
    print("playbook/")
    show_tree('.', '', max_depth=4)
    
    print(f"\n📋 File Summary:")
    
    # Count files by extension
    file_counts = {}
    total_files = 0
    
    for root, dirs, files in os.walk('.'):
        dirs[:] = [d for d in dirs if not d.startswith('.') and d != '__pycache__']
        for file in files:
            if not file.startswith('.') and not file.endswith('.pyc'):
                total_files += 1
                ext = os.path.splitext(file)[1] or 'no extension'
                file_counts[ext] = file_counts.get(ext, 0) + 1
    
    for ext, count in sorted(file_counts.items()):
        print(f"  {ext}: {count} files")
    
    print(f"\nTotal: {total_files} files")
    
    # Show key files status
    key_files = [
        'README.md', 'QUICKSTART.md', 'requirements.txt', 'scrapy.cfg',
        'run_crawler.py', 'demo_crawler.py', 'test_setup.py',
        'webcrawler/settings.py', 'webcrawler/items.py', 'webcrawler/pipelines.py',
        'webcrawler/spiders/main_spider.py', 'utils/document_processor.py'
    ]
    
    print(f"\n✅ Essential Files Status:")
    all_present = True
    for file_path in key_files:
        exists = os.path.exists(file_path)
        status = "✅" if exists else "❌"
        print(f"  {status} {file_path}")
        if not exists:
            all_present = False
    
    if all_present:
        print(f"\n🎉 All essential files are present!")
        print(f"🚀 Your web crawler is ready to use!")
    else:
        print(f"\n⚠️ Some essential files are missing!")

if __name__ == '__main__':
    main()