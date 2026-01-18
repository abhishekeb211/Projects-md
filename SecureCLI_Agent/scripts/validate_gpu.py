#!/usr/bin/env python3
"""
Validate GPU availability and CodeLlama 13B inference speed.
Usage: python validate_gpu.py --output gpu_validation.json
"""

import argparse
import json
import subprocess
import sys
import time

def check_nvidia_gpu():
    """Check for NVIDIA GPU using nvidia-smi."""
    try:
        result = subprocess.run(
            ['nvidia-smi', '--query-gpu=name,memory.total,driver_version', '--format=csv,noheader'],
            capture_output=True,
            text=True,
            timeout=10
        )
        if result.returncode == 0:
            gpus = []
            for line in result.stdout.strip().split('\n'):
                if line:
                    parts = [p.strip() for p in line.split(',')]
                    if len(parts) >= 2:
                        name = parts[0]
                        memory = parts[1] if len(parts) > 1 else 'Unknown'
                        driver = parts[2] if len(parts) > 2 else 'Unknown'
                        # Extract memory value (e.g., "8192 MiB" -> 8192)
                        memory_mb = 0
                        if 'MiB' in memory:
                            try:
                                memory_mb = int(memory.replace(' MiB', ''))
                            except ValueError:
                                pass
                        
                        gpus.append({
                            'name': name,
                            'memory_mb': memory_mb,
                            'memory_gb': memory_mb / 1024,
                            'driver_version': driver,
                            'meets_requirement': memory_mb >= 8192  # 8GB requirement
                        })
            return gpus
        return None
    except (subprocess.TimeoutExpired, FileNotFoundError):
        return None

def check_gpu_hardware():
    """Check GPU hardware using lspci."""
    try:
        result = subprocess.run(
            ['lspci'],
            capture_output=True,
            text=True,
            timeout=10
        )
        if result.returncode == 0:
            gpu_lines = [line for line in result.stdout.split('\n') if 'VGA' in line or '3D' in line]
            return gpu_lines if gpu_lines else None
        return None
    except (subprocess.TimeoutExpired, FileNotFoundError):
        return None

def test_ollama_inference():
    """Test Ollama CodeLlama 13B inference speed."""
    try:
        # Check if Ollama is installed
        result = subprocess.run(
            ['ollama', '--version'],
            capture_output=True,
            text=True,
            timeout=10
        )
        if result.returncode != 0:
            return {'ollama_installed': False, 'error': 'Ollama not found'}
        
        # Check if codellama:13b model is available
        result = subprocess.run(
            ['ollama', 'list'],
            capture_output=True,
            text=True,
            timeout=10
        )
        if 'codellama:13b' not in result.stdout:
            return {
                'ollama_installed': True,
                'model_available': False,
                'error': 'codellama:13b model not found. Run: ollama pull codellama:13b'
            }
        
        # Test inference with a simple prompt
        test_prompt = "Analyze this security finding: SQL injection vulnerability in user input validation."
        
        start_time = time.time()
        result = subprocess.run(
            ['ollama', 'run', 'codellama:13b', test_prompt],
            capture_output=True,
            text=True,
            timeout=30  # 30 second timeout
        )
        inference_time = time.time() - start_time
        
        if result.returncode == 0:
            return {
                'ollama_installed': True,
                'model_available': True,
                'inference_time_seconds': inference_time,
                'meets_target': inference_time < 5.0,  # <5s target
                'output_length': len(result.stdout)
            }
        else:
            return {
                'ollama_installed': True,
                'model_available': True,
                'error': f'Inference failed: {result.stderr[:200]}'
            }
    except subprocess.TimeoutExpired:
        return {
            'ollama_installed': True,
            'model_available': True,
            'error': 'Inference timeout (>30s)',
            'meets_target': False
        }
    except FileNotFoundError:
        return {'ollama_installed': False, 'error': 'Ollama not found in PATH'}

def validate_gpu(output_file):
    """Validate GPU availability and CodeLlama inference."""
    results = {
        'gpu_available': False,
        'gpu_details': None,
        'ollama_test': None,
        'overall_status': 'FAIL'
    }
    
    print("GPU Validation for CodeLlama 13B")
    print("="*60)
    
    # Check NVIDIA GPU
    print("\n1. Checking NVIDIA GPU...")
    nvidia_gpus = check_nvidia_gpu()
    if nvidia_gpus:
        results['gpu_available'] = True
        results['gpu_details'] = nvidia_gpus
        print(f"  ✓ Found {len(nvidia_gpus)} GPU(s):")
        for i, gpu in enumerate(nvidia_gpus, 1):
            status = "✓" if gpu['meets_requirement'] else "✗"
            print(f"    {status} GPU {i}: {gpu['name']}")
            print(f"      Memory: {gpu['memory_gb']:.1f} GB ({'Meets 8GB requirement' if gpu['meets_requirement'] else 'Below 8GB requirement'})")
            print(f"      Driver: {gpu['driver_version']}")
    else:
        # Check generic GPU hardware
        print("  Checking generic GPU hardware...")
        gpu_hardware = check_gpu_hardware()
        if gpu_hardware:
            print(f"  ⚠ Found GPU hardware (details unavailable):")
            for line in gpu_hardware:
                print(f"    {line}")
            results['gpu_available'] = True
            results['gpu_details'] = {'hardware_detected': True, 'details': gpu_hardware}
        else:
            print("  ✗ No GPU detected")
            results['gpu_available'] = False
    
    # Test Ollama inference
    print("\n2. Testing Ollama CodeLlama 13B inference...")
    ollama_test = test_ollama_inference()
    results['ollama_test'] = ollama_test
    
    if not ollama_test.get('ollama_installed'):
        print(f"  ✗ Ollama not installed")
    elif not ollama_test.get('model_available'):
        print(f"  ✗ Model not available: {ollama_test.get('error')}")
    elif 'inference_time_seconds' in ollama_test:
        inference_time = ollama_test['inference_time_seconds']
        meets_target = ollama_test.get('meets_target', False)
        status = "✓" if meets_target else "✗"
        print(f"  {status} Inference time: {inference_time:.2f}s (target: <5s)")
        if meets_target:
            print(f"  ✓ Meets performance requirement")
        else:
            print(f"  ✗ Does not meet performance requirement (consider CodeLlama 7B or batch processing)")
    else:
        print(f"  ✗ Inference test failed: {ollama_test.get('error')}")
    
    # Overall status
    gpu_ok = results['gpu_available'] and any(
        gpu.get('meets_requirement', False) 
        for gpu in (results['gpu_details'] if isinstance(results['gpu_details'], list) else [])
    )
    inference_ok = ollama_test.get('meets_target', False) if ollama_test else False
    
    if gpu_ok and inference_ok:
        results['overall_status'] = 'PASS'
        print("\n" + "="*60)
        print("✓ GPU VALIDATION PASSED")
        print("="*60)
    elif gpu_ok:
        results['overall_status'] = 'WARNING'
        print("\n" + "="*60)
        print("⚠ GPU AVAILABLE BUT INFERENCE TOO SLOW")
        print("  Consider: CodeLlama 7B, batch processing, or CPU fallback")
        print("="*60)
    else:
        results['overall_status'] = 'FAIL'
        print("\n" + "="*60)
        print("✗ GPU VALIDATION FAILED")
        print("  Mitigation: Use CodeLlama 7B, batch processing, or GPT-4 API fallback")
        print("="*60)
    
    # Save results
    with open(output_file, 'w') as f:
        json.dump(results, f, indent=2)
    
    return results['overall_status'] == 'PASS'

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Validate GPU availability and CodeLlama inference')
    parser.add_argument('--output', required=True, help='Output JSON report file')
    
    args = parser.parse_args()
    success = validate_gpu(args.output)
    sys.exit(0 if success else 1)

