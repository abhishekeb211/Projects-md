#!/usr/bin/env python3
"""
Generate literature card template from paper metadata.
Usage: python generate_card_template.py --paper-id C1_001 --output C1_orchestration/C1_001_Smith2020_SARIFAdoption.md
"""

import argparse
import sys

def generate_card_template(paper_id, output_path):
    """Generate a literature card template with placeholders."""
    
    template = f"""### {paper_id} AuthorYear_TitleKeyword

**Citation:**
```bibtex
@article{{AuthorYear,
  title={{[Title - to be filled]}},
  author={{[Authors - to be filled]}},
  journal={{[Journal/Venue - to be filled]}},
  year={{[Year - to be filled]}},
  volume={{[Volume - if applicable]}},
  number={{[Number - if applicable]}},
  pages={{[Pages - if applicable]}},
  doi={{[DOI - if available]}}
}}
```

**Core Method:**
[2-sentence summary of the paper's primary method/approach - to be filled]

**Evaluation:**
- **Setup:** [Experimental setup, tool used, sample size - to be filled]
- **Metrics:** [Evaluation metrics reported - to be filled]
- **Sample Size:** [Number of participants, repositories, findings, etc. - to be filled]

**Strengths:**
- [Bullet 1: Key strength relevant to AegisCLI - to be filled]
- [Bullet 2: Methodological strength - to be filled]
- [Bullet 3: Practical applicability - to be filled]

**Limitations:**
- [Gap 1: Directly relevant to AegisCLI research gap - to be filled]
- [Gap 2: Methodological or practical limitation - to be filled]

**Relevance:**
- **RQ Mapping:** RQ[X], RQ[Y] (which RQs this paper informs - to be filled)
- **Relevance Score:** [1-5, where 5 = highly relevant, 1 = marginally relevant - to be filled]
- **Justification:** [Brief explanation of relevance - to be filled]

**Follow-Chain:**
- **Cites:** [3 key papers this work cites - important foundational works - to be filled]
- **Cited By:** [2 recent follow-up papers (from forward snowballing) - to be filled]

**Artifact Link:**
- **GitHub:** [URL if available - to be filled]
- **Zenodo:** [DOI if available - to be filled]
- **Other:** [Additional links - to be filled]

**Quality Score:** [X/12] (Relevance: [X/3], Rigor: [X/3], Reproducibility: [X/3], Citations: [X/3] - to be filled)
"""
    
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(template)
        print(f"✓ Template generated: {output_path}")
        return True
    except Exception as e:
        print(f"✗ Error generating template: {e}", file=sys.stderr)
        return False

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate literature card template')
    parser.add_argument('--paper-id', required=True, help='Paper ID (e.g., C1_001)')
    parser.add_argument('--output', required=True, help='Output file path')
    
    args = parser.parse_args()
    success = generate_card_template(args.paper_id, args.output)
    sys.exit(0 if success else 1)

