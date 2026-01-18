#!/usr/bin/env python3
"""
Calculate gap matrix for RQ × Cluster heatmap.
Usage: python calculate_gap_matrix.py --input 02-included-papers.csv --output gap_matrix.csv
"""

import pandas as pd
import numpy as np
import argparse
import sys

def calculate_gap_matrix(csv_file, output_file):
    """Calculate RQ × Cluster gap matrix from included papers CSV."""
    
    try:
        # Read included papers CSV
        df = pd.read_csv(csv_file)
        
        # RQs and Clusters
        rqs = ['RQ1', 'RQ2', 'RQ3', 'RQ4', 'RQ5']
        clusters = ['C1', 'C2', 'C3', 'C4', 'C5']
        
        # Initialize matrix
        gap_matrix = pd.DataFrame(index=rqs, columns=clusters, data=0)
        
        # Parse RQ Mapping column (assumes format like "RQ1, RQ2" or "RQ1;RQ2")
        for idx, row in df.iterrows():
            rq_mapping = str(row.get('RQ Mapping', ''))
            cluster = str(row.get('Cluster', ''))
            
            if pd.notna(rq_mapping) and pd.notna(cluster):
                # Parse RQs (handle comma or semicolon separated)
                paper_rqs = [rq.strip() for rq in rq_mapping.replace(';', ',').split(',')]
                
                # Increment matrix cells
                for rq in paper_rqs:
                    if rq in rqs and cluster in clusters:
                        gap_matrix.loc[rq, cluster] += 1
        
        # Save to CSV
        gap_matrix.to_csv(output_file)
        print(f"✓ Gap matrix calculated and saved to: {output_file}")
        print("\nMatrix preview:")
        print(gap_matrix)
        
        return gap_matrix
        
    except Exception as e:
        print(f"✗ Error calculating gap matrix: {e}", file=sys.stderr)
        return None

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Calculate RQ × Cluster gap matrix')
    parser.add_argument('--input', required=True, help='Input CSV file with included papers')
    parser.add_argument('--output', required=True, help='Output CSV file for gap matrix')
    
    args = parser.parse_args()
    matrix = calculate_gap_matrix(args.input, args.output)
    sys.exit(0 if matrix is not None else 1)

