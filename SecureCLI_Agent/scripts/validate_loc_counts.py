#!/usr/bin/env python3
"""
Validate LOC counts across 50 repositories to ensure ≥50K LOC constraint.
Usage: python validate_loc_counts.py --repos-dir /path/to/repos --output loc_report.json
"""

import argparse
import json
import subprocess
import sys
from pathlib import Path
from collections import defaultdict

def run_cloc(repo_path):
    """Run cloc on a repository and return results."""
    try:
        result = subprocess.run(
            ['cloc', '--json', str(repo_path)],
            capture_output=True,
            text=True,
            timeout=300
        )
        if result.returncode == 0:
            return json.loads(result.stdout)
        return None
    except (subprocess.TimeoutExpired, json.JSONDecodeError, FileNotFoundError):
        return None

def run_tokei(repo_path):
    """Run tokei on a repository and return results."""
    try:
        result = subprocess.run(
            ['tokei', '--output', 'json', str(repo_path)],
            capture_output=True,
            text=True,
            timeout=300
        )
        if result.returncode == 0:
            return json.loads(result.stdout)
        return None
    except (subprocess.TimeoutExpired, json.JSONDecodeError, FileNotFoundError):
        return None

def categorize_language(lang):
    """Categorize language into target ecosystems."""
    lang_lower = lang.lower()
    if 'typescript' in lang_lower or 'javascript' in lang_lower or 'node' in lang_lower:
        return 'Node.js/TypeScript'
    elif 'python' in lang_lower:
        return 'Python'
    elif 'go' in lang_lower:
        return 'Go'
    elif 'java' in lang_lower:
        return 'Java'
    elif 'terraform' in lang_lower or 'hcl' in lang_lower or 'iac' in lang_lower:
        return 'Terraform/IaC'
    return 'Other'

def validate_loc_counts(repos_dir, output_file, tool='cloc'):
    """Validate LOC counts across repositories."""
    repos_path = Path(repos_dir)
    if not repos_path.exists():
        print(f"Error: Directory {repos_dir} does not exist", file=sys.stderr)
        return False
    
    repos = [d for d in repos_path.iterdir() if d.is_dir()]
    if len(repos) == 0:
        print(f"Error: No repositories found in {repos_dir}", file=sys.stderr)
        return False
    
    print(f"Processing {len(repos)} repositories using {tool}...")
    
    total_loc = 0
    language_totals = defaultdict(int)
    repo_results = []
    
    for repo in repos:
        print(f"  Processing {repo.name}...", end=' ', flush=True)
        
        if tool == 'cloc':
            result = run_cloc(repo)
            if result and 'SUM' in result:
                repo_loc = result['SUM'].get('code', 0)
                total_loc += repo_loc
                
                # Extract language breakdown
                lang_breakdown = {}
                for lang, data in result.items():
                    if lang != 'header' and lang != 'SUM' and isinstance(data, dict):
                        loc = data.get('code', 0)
                        if loc > 0:
                            category = categorize_language(lang)
                            language_totals[category] += loc
                            lang_breakdown[lang] = loc
                
                repo_results.append({
                    'repo': repo.name,
                    'total_loc': repo_loc,
                    'languages': lang_breakdown
                })
                print(f"✓ {repo_loc} LOC")
            else:
                print("✗ Failed")
                repo_results.append({
                    'repo': repo.name,
                    'total_loc': 0,
                    'languages': {},
                    'error': 'cloc failed or not installed'
                })
        else:  # tokei
            result = run_tokei(repo)
            if result:
                repo_loc = result.get('total', {}).get('code', 0)
                total_loc += repo_loc
                
                lang_breakdown = {}
                for lang, data in result.items():
                    if lang != 'total' and isinstance(data, dict):
                        loc = data.get('code', 0)
                        if loc > 0:
                            category = categorize_language(lang)
                            language_totals[category] += loc
                            lang_breakdown[lang] = loc
                
                repo_results.append({
                    'repo': repo.name,
                    'total_loc': repo_loc,
                    'languages': lang_breakdown
                })
                print(f"✓ {repo_loc} LOC")
            else:
                print("✗ Failed")
                repo_results.append({
                    'repo': repo.name,
                    'total_loc': 0,
                    'languages': {},
                    'error': 'tokei failed or not installed'
                })
    
    # Validation targets
    targets = {
        'Node.js/TypeScript': 15000,
        'Python': 12000,
        'Go': 10000,
        'Java': 8000,
        'Terraform/IaC': 5000
    }
    
    # Generate report
    report = {
        'summary': {
            'total_repos': len(repos),
            'total_loc': total_loc,
            'target_loc': 50000,
            'meets_target': total_loc >= 50000
        },
        'language_breakdown': {
            lang: {
                'actual': language_totals[lang],
                'target': targets.get(lang, 0),
                'meets_target': language_totals[lang] >= targets.get(lang, 0)
            }
            for lang in targets.keys()
        },
        'repositories': repo_results
    }
    
    # Save report
    with open(output_file, 'w') as f:
        json.dump(report, f, indent=2)
    
    # Print summary
    print("\n" + "="*60)
    print("LOC COUNT VALIDATION SUMMARY")
    print("="*60)
    print(f"Total Repositories: {len(repos)}")
    print(f"Total LOC: {total_loc:,}")
    print(f"Target LOC: 50,000")
    print(f"Status: {'✓ PASS' if total_loc >= 50000 else '✗ FAIL'}")
    print("\nLanguage Breakdown:")
    for lang, target in targets.items():
        actual = language_totals[lang]
        status = "✓" if actual >= target else "✗"
        print(f"  {status} {lang}: {actual:,} / {target:,} LOC")
    
    return total_loc >= 50000

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Validate LOC counts across repositories')
    parser.add_argument('--repos-dir', required=True, help='Directory containing repositories')
    parser.add_argument('--output', required=True, help='Output JSON report file')
    parser.add_argument('--tool', choices=['cloc', 'tokei'], default='cloc', help='LOC counting tool')
    
    args = parser.parse_args()
    success = validate_loc_counts(args.repos_dir, args.output, args.tool)
    sys.exit(0 if success else 1)

