#!/usr/bin/env python3
"""
CmdRx Installation Verification Script

This script verifies that CmdRx is properly installed and can be imported.
"""

import sys
import importlib
from pathlib import Path

def test_imports():
    """Test that all CmdRx modules can be imported."""
    modules_to_test = [
        'cmdrx',
        'cmdrx.cli',
        'cmdrx.core',
        'cmdrx.config',
        'cmdrx.llm',
        'cmdrx.output',
        'cmdrx.exceptions'
    ]
    
    failed_imports = []
    
    for module_name in modules_to_test:
        try:
            importlib.import_module(module_name)
            print(f"✓ {module_name}")
        except ImportError as e:
            print(f"✗ {module_name}: {e}")
            failed_imports.append(module_name)
    
    return failed_imports

def test_dependencies():
    """Test that all required dependencies are available."""
    dependencies = [
        'click',
        'rich',
        'requests',
        'keyring',
        'openai',
        'cryptography',
        'pydantic',
        'textual'
    ]
    
    failed_deps = []
    
    for dep in dependencies:
        try:
            importlib.import_module(dep)
            print(f"✓ {dep}")
        except ImportError as e:
            print(f"✗ {dep}: {e}")
            failed_deps.append(dep)
    
    return failed_deps

def test_cli_access():
    """Test that the CLI command is accessible."""
    try:
        from cmdrx.cli import main
        print("✓ CLI main function accessible")
        return True
    except ImportError as e:
        print(f"✗ CLI main function: {e}")
        return False

def main():
    """Main verification function."""
    print("CmdRx Installation Verification")
    print("=" * 40)
    
    print("\n1. Testing CmdRx module imports...")
    failed_imports = test_imports()
    
    print("\n2. Testing dependencies...")
    failed_deps = test_dependencies()
    
    print("\n3. Testing CLI access...")
    cli_ok = test_cli_access()
    
    print("\n4. Summary")
    print("-" * 20)
    
    if not failed_imports and not failed_deps and cli_ok:
        print("🎉 All tests passed! CmdRx appears to be properly installed.")
        print("\nNext steps:")
        print("1. Run 'cmdrx --config' to set up your LLM provider")
        print("2. Try 'cmdrx --help' to see usage options")
        print("3. Test with 'cmdrx echo Hello World'")
        return 0
    else:
        print("❌ Some tests failed:")
        if failed_imports:
            print(f"   - Failed imports: {', '.join(failed_imports)}")
        if failed_deps:
            print(f"   - Missing dependencies: {', '.join(failed_deps)}")
        if not cli_ok:
            print("   - CLI not accessible")
        
        print("\nTroubleshooting:")
        print("1. Ensure you installed CmdRx properly: pip install cmdrx")
        print("2. Check that all dependencies are installed")
        print("3. Try reinstalling: pip install --force-reinstall cmdrx")
        return 1

if __name__ == "__main__":
    sys.exit(main())