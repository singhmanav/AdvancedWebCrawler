#!/usr/bin/env python3
"""
Deployment script for Advanced Web Crawler
Automates the process of committing and pushing changes to GitHub
"""

import subprocess
import sys
import os
from datetime import datetime


def run_command(command, description, check=True):
    """Run a shell command with description"""
    print(f"🔧 {description}...")
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        if check and result.returncode != 0:
            print(f"❌ Failed: {result.stderr}")
            return False
        else:
            if result.stdout.strip():
                print(f"   {result.stdout.strip()}")
            print(f"✅ {description} completed")
            return True
    except Exception as e:
        print(f"❌ Error: {e}")
        return False


def check_git_status():
    """Check if there are changes to commit"""
    result = subprocess.run("git status --porcelain", shell=True, capture_output=True, text=True)
    return result.stdout.strip() != ""


def get_commit_message():
    """Get commit message from user"""
    print("\n📝 Commit Message Options:")
    print("1. Auto-generate commit message")
    print("2. Enter custom commit message")
    print("3. Cancel deployment")
    
    choice = input("\nSelect option (1-3): ").strip()
    
    if choice == "1":
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
        return f"Update project files - {timestamp}"
    elif choice == "2":
        message = input("Enter commit message: ").strip()
        if not message:
            print("❌ Empty commit message. Cancelling deployment.")
            return None
        return message
    else:
        print("⏹️  Deployment cancelled.")
        return None


def deploy_to_github():
    """Deploy changes to GitHub"""
    print("🚀 Advanced Web Crawler - GitHub Deployment")
    print("=" * 50)
    
    # Check if we're in a git repository
    if not os.path.exists('.git'):
        print("❌ Not a git repository. Please run 'git init' first.")
        return False
    
    # Check for changes
    if not check_git_status():
        print("✅ No changes to commit. Repository is up to date.")
        return True
    
    # Show status
    print("\n📊 Current Git Status:")
    run_command("git status --short", "Git status", check=False)
    
    # Confirm deployment
    print(f"\n🔍 Repository: https://github.com/singhmanav/AdvancedWebCrawler.git")
    response = input("Continue with deployment? (y/N): ").lower().strip()
    if response != 'y':
        print("⏹️  Deployment cancelled.")
        return False
    
    # Get commit message
    commit_message = get_commit_message()
    if not commit_message:
        return False
    
    # Deployment steps
    steps = [
        ("git add .", "Stage all changes"),
        (f'git commit -m "{commit_message}"', "Commit changes"),
        ("git push origin main", "Push to GitHub"),
    ]
    
    print(f"\n🚀 Starting deployment...")
    
    for command, description in steps:
        if not run_command(command, description):
            print(f"\n❌ Deployment failed at: {description}")
            return False
    
    print(f"\n🎉 Deployment successful!")
    print(f"📍 Repository: https://github.com/singhmanav/AdvancedWebCrawler")
    print(f"💬 Commit: {commit_message}")
    
    return True


def show_repository_info():
    """Show repository information"""
    print("\n📋 Repository Information:")
    print("-" * 30)
    print("🔗 GitHub URL: https://github.com/singhmanav/AdvancedWebCrawler")
    print("📊 Clone command: git clone https://github.com/singhmanav/AdvancedWebCrawler.git")
    print("🌐 Issues: https://github.com/singhmanav/AdvancedWebCrawler/issues")
    print("📚 Documentation: https://github.com/singhmanav/AdvancedWebCrawler#readme")


def main():
    """Main deployment function"""
    try:
        success = deploy_to_github()
        
        if success:
            show_repository_info()
            print(f"\n✨ Next steps:")
            print(f"   - Visit the repository to see your changes")
            print(f"   - Check GitHub Actions for CI/CD status")
            print(f"   - Share your project with others!")
        
        return 0 if success else 1
        
    except KeyboardInterrupt:
        print(f"\n⏹️  Deployment interrupted by user.")
        return 1
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        return 1


if __name__ == '__main__':
    sys.exit(main())