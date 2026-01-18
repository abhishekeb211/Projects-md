#!/usr/bin/env python3
"""
Generate gap heatmap visualization from gap matrix CSV.
Usage: python generate_heatmap.py --input gap_matrix.csv --output 02-gap-heatmap.png
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import argparse
import sys
import numpy as np

def generate_heatmap(csv_file, output_file):
    """Generate RQ × Cluster gap heatmap."""
    
    try:
        # Read gap matrix
        gap_matrix = pd.read_csv(csv_file, index_col=0)
        
        # Create custom colormap: Red (0-1), Yellow (2-4), Green (5+)
        from matplotlib.colors import LinearSegmentedColormap
        colors = ['#d32f2f', '#ffa726', '#66bb6a']  # Red, Yellow, Green
        n_bins = 3
        cmap = LinearSegmentedColormap.from_list('gap_heatmap', colors, N=n_bins)
        
        # Create figure
        plt.figure(figsize=(10, 8))
        
        # Generate heatmap
        ax = sns.heatmap(
            gap_matrix,
            annot=True,
            fmt='d',
            cmap=cmap,
            vmin=0,
            vmax=10,
            cbar_kws={'label': 'Number of Papers'},
            linewidths=0.5,
            linecolor='gray'
        )
        
        # Customize colorbar based on thresholds
        # This is a simplified version; for exact thresholds, you'd need custom normalization
        # For now, using discrete color thresholds via vmin/vmax
        
        plt.title('SLR Gap Heatmap: RQ Coverage by Cluster', fontsize=14, fontweight='bold', pad=20)
        plt.xlabel('Literature Clusters', fontsize=12, fontweight='bold')
        plt.ylabel('Research Questions', fontsize=12, fontweight='bold')
        
        # Add cluster labels
        cluster_labels = ['C1: Orchestration', 'C2: AI Triage', 'C3: PaC', 'C4: Adoption', 'C5: Privacy']
        ax.set_xticklabels(cluster_labels, rotation=45, ha='right')
        
        plt.tight_layout()
        plt.savefig(output_file, dpi=300, bbox_inches='tight')
        print(f"✓ Heatmap generated: {output_file}")
        plt.close()
        
        return True
        
    except Exception as e:
        print(f"✗ Error generating heatmap: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate gap heatmap visualization')
    parser.add_argument('--input', required=True, help='Input CSV file with gap matrix')
    parser.add_argument('--output', required=True, help='Output PNG file path')
    
    args = parser.parse_args()
    success = generate_heatmap(args.input, args.output)
    sys.exit(0 if success else 1)

