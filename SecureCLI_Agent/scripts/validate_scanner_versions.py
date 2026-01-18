#!/usr/bin/env python3
"""
Validate scanner versions meet requirements and test SARIF output compatibility.
Usage: python validate_scanner_versions.py --output scanner_validation.json
"""

import argparse
import json
import subprocess
import sys
import re
from pathlib import Path

# Required versions
REQUIRED_VERSIONS = {
    'semgrep': '1.45.0',
    'trivy': '0.48.0',
    'checkov': '3.0.0',
    'gitleaks': '8.18.0'
}

def get_version(command, version_flag='--version'):
    """Get version of a command-line tool."""
    try:
        result = subprocess.run(
            [command, version_flag],
            capture_output=True,
            text=True,
            timeout=10
        )
        if result.returncode == 0:
            output = result.stdout.strip()
            # Extract version number (e.g., "1.45.0" from "semgrep 1.45.0")
            version_match = re.search(r'(\d+\.\d+\.\d+)', output)
            if version_match:
                return version_match.group(1)
            return output
        return None
    except (subprocess.TimeoutExpired, FileNotFoundError):
        return None

def compare_versions(actual, required):
    """Compare version strings (simple numeric comparison)."""
    try:
        actual_parts = [int(x) for x in actual.split('.')]
        required_parts = [int(x) for x in required.split('.')]
        
        for a, r in zip(actual_parts, required_parts):
            if a > r:
                return True
            elif a < r:
                return False
        return True  # Equal versions
    except ValueError:
        return False

def test_sarif_output(scanner, test_repo=None):
    """Test if scanner can produce SARIF output."""
    test_commands = {
        'semgrep': ['semgrep', '--sarif', '--output', '/tmp/test.sarif', '.'],
        'trivy': ['trivy', 'fs', '--format', 'sarif', '--output', '/tmp/test.sarif', '.'],
        'checkov': ['checkov', '-f', '.', '--framework', 'all', '--output', 'sarif', '--output-file-path', '/tmp/test.sarif'],
        'gitleaks': ['gitleaks', 'detect', '--format', 'sarif', '--output', '/tmp/test.sarif', '--source', '.']
    }
    
    if scanner not in test_commands:
        return {'supported': False, 'error': 'Unknown scanner'}
    
    try:
        # Create a temporary test directory if none provided
        test_dir = Path(test_repo) if test_repo else Path('/tmp/sarif_test')
        if not test_dir.exists() and not test_repo:
            test_dir.mkdir(exist_ok=True)
        
        cmd = test_commands[scanner]
        # Replace '.' with test_dir if provided
        if test_repo:
            cmd = [c if c != '.' else str(test_dir) for c in cmd]
        
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=60,
            cwd=str(test_dir) if test_dir.exists() else None
        )
        
        # Check if SARIF file was created
        sarif_file = Path('/tmp/test.sarif')
        if sarif_file.exists():
            # Basic validation: check if it's valid JSON
            try:
                with open(sarif_file, 'r') as f:
                    sarif_data = json.load(f)
                    if 'version' in sarif_data and 'runs' in sarif_data:
                        sarif_file.unlink()  # Clean up
                        return {'supported': True, 'sarif_version': sarif_data.get('version')}
            except json.JSONDecodeError:
                pass
            finally:
                if sarif_file.exists():
                    sarif_file.unlink()
        
        return {'supported': False, 'error': f'Command failed: {result.stderr[:100]}'}
    except Exception as e:
        return {'supported': False, 'error': str(e)}

def validate_scanners(output_file):
    """Validate all scanner versions and SARIF support."""
    results = {}
    
    print("Validating Scanner Versions...")
    print("="*60)
    
    for scanner, required_version in REQUIRED_VERSIONS.items():
        print(f"\n{scanner}:")
        print(f"  Required version: {required_version}+")
        
        actual_version = get_version(scanner)
        if actual_version is None:
            results[scanner] = {
                'installed': False,
                'required_version': required_version,
                'error': 'Scanner not found or not in PATH'
            }
            print(f"  Status: ✗ NOT INSTALLED")
            continue
        
        print(f"  Actual version: {actual_version}")
        
        meets_requirement = compare_versions(actual_version, required_version)
        print(f"  Meets requirement: {'✓' if meets_requirement else '✗'}")
        
        # Test SARIF output
        print(f"  Testing SARIF output...", end=' ', flush=True)
        sarif_test = test_sarif_output(scanner)
        print(f"{'✓' if sarif_test.get('supported') else '✗'}")
        
        results[scanner] = {
            'installed': True,
            'actual_version': actual_version,
            'required_version': required_version,
            'meets_requirement': meets_requirement,
            'sarif_support': sarif_test
        }
    
    # Save results
    with open(output_file, 'w') as f:
        json.dump(results, f, indent=2)
    
    # Print summary
    print("\n" + "="*60)
    print("VALIDATION SUMMARY")
    print("="*60)
    
    all_valid = True
    for scanner, result in results.items():
        if not result.get('installed'):
            print(f"✗ {scanner}: NOT INSTALLED")
            all_valid = False
        elif not result.get('meets_requirement'):
            print(f"✗ {scanner}: Version {result['actual_version']} < {result['required_version']}")
            all_valid = False
        elif not result.get('sarif_support', {}).get('supported'):
            print(f"✗ {scanner}: SARIF output not supported")
            all_valid = False
        else:
            print(f"✓ {scanner}: Version {result['actual_version']}, SARIF supported")
    
    print(f"\nOverall Status: {'✓ ALL VALID' if all_valid else '✗ VALIDATION FAILED'}")
    
    return all_valid

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Validate scanner versions and SARIF support')
    parser.add_argument('--output', required=True, help='Output JSON report file')
    
    args = parser.parse_args()
    success = validate_scanners(args.output)
    sys.exit(0 if success else 1)

