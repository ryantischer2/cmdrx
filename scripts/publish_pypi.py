#!/usr/bin/env python3
"""
PyPI publishing script for CmdRx.

This script handles the complete PyPI publishing workflow:
1. Clean build artifacts
2. Build package
3. Test package locally
4. Upload to PyPI test server
5. Upload to production PyPI
"""

import os
import sys
import subprocess
import shutil
from pathlib import Path

def run_command(cmd, description, check=True):
    """Run a command and handle output."""
    print(f"\n🔄 {description}")
    print(f"   Command: {cmd}")
    
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    
    if result.returncode != 0 and check:
        print(f"❌ Error: {description} failed")
        print(f"   stdout: {result.stdout}")
        print(f"   stderr: {result.stderr}")
        sys.exit(1)
    
    if result.stdout:
        print(f"   Output: {result.stdout.strip()}")
    
    return result

def clean_build():
    """Clean all build artifacts."""
    artifacts = ['dist/', 'build/', 'src/*.egg-info', '*.egg-info']
    
    for pattern in artifacts:
        for path in Path('.').glob(pattern):
            if path.exists():
                if path.is_dir():
                    shutil.rmtree(path)
                    print(f"   Removed directory: {path}")
                else:
                    path.unlink()
                    print(f"   Removed file: {path}")

def build_package():
    """Build the package."""
    run_command("python3 -m build", "Building package")

def test_package_locally():
    """Test the built package locally."""
    print("\n🧪 Testing package locally...")
    
    # Create a temporary virtual environment for testing
    test_env = Path("test_env")
    if test_env.exists():
        shutil.rmtree(test_env)
    
    run_command("python3 -m venv test_env", "Creating test environment")
    
    # Install the built wheel
    wheel_file = list(Path("dist").glob("*.whl"))[0]
    run_command(f"test_env/bin/pip install {wheel_file}", f"Installing {wheel_file}")
    
    # Test the installation
    result = run_command("test_env/bin/cmdrx --version", "Testing cmdrx --version", check=False)
    if "CmdRx version" not in result.stdout:
        print("❌ Package test failed: cmdrx --version didn't work")
        sys.exit(1)
    
    print("✅ Package test passed")
    
    # Clean up test environment
    shutil.rmtree(test_env)

def check_package():
    """Check package metadata and quality."""
    run_command("python3 -m twine check dist/*", "Checking package metadata")

def upload_to_test_pypi():
    """Upload to TestPyPI."""
    print("\n📤 Uploading to TestPyPI...")
    print("   Note: You'll need TestPyPI credentials")
    print("   Create an account at: https://test.pypi.org/")
    
    result = run_command(
        "python3 -m twine upload --repository testpypi dist/*", 
        "Uploading to TestPyPI",
        check=False
    )
    
    if result.returncode == 0:
        print("✅ Successfully uploaded to TestPyPI")
        print("   Test installation with:")
        print("   pip install --index-url https://test.pypi.org/simple/ cmdrx")
    else:
        print("⚠️  TestPyPI upload failed - this might be expected if version already exists")

def upload_to_pypi():
    """Upload to production PyPI."""
    print("\n📤 Uploading to Production PyPI...")
    print("   WARNING: This is the PRODUCTION PyPI!")
    
    confirm = input("   Are you sure you want to upload to production PyPI? (yes/no): ")
    if confirm.lower() != 'yes':
        print("   Upload cancelled")
        return
    
    print("   Note: You'll need PyPI credentials")
    print("   Create an account at: https://pypi.org/")
    
    result = run_command(
        "python3 -m twine upload dist/*", 
        "Uploading to PyPI",
        check=False
    )
    
    if result.returncode == 0:
        print("🎉 Successfully uploaded to PyPI!")
        print("   Users can now install with: pip install cmdrx")
    else:
        print("❌ PyPI upload failed")

def main():
    """Main publishing workflow."""
    print("🚀 CmdRx PyPI Publishing Workflow")
    print("=" * 50)
    
    # Check if we're in the right directory
    if not Path("pyproject.toml").exists():
        print("❌ Error: pyproject.toml not found. Run this script from the project root.")
        sys.exit(1)
    
    # Step 1: Clean
    print("\n🧹 Cleaning build artifacts...")
    clean_build()
    
    # Step 2: Build
    print("\n🔨 Building package...")
    build_package()
    
    # Step 3: Check package quality
    print("\n📋 Checking package quality...")
    check_package()
    
    # Step 4: Test locally
    print("\n🧪 Testing package locally...")
    test_package_locally()
    
    # Step 5: Upload to TestPyPI
    print("\n📤 Publishing workflow...")
    choice = input("Upload to TestPyPI first? (recommended) (y/n): ")
    if choice.lower() in ['y', 'yes']:
        upload_to_test_pypi()
    
    # Step 6: Upload to production PyPI
    choice = input("Upload to production PyPI? (y/n): ")
    if choice.lower() in ['y', 'yes']:
        upload_to_pypi()
    
    print("\n✅ Publishing workflow complete!")
    print("\nNext steps:")
    print("1. Test installation: pip install cmdrx")
    print("2. Create GitHub release")
    print("3. Update documentation")

if __name__ == "__main__":
    main()