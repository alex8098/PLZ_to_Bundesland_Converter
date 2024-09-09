#!/usr/bin/env python3
"""
PLZ to Bundesland Converter

This script converts German postal codes (PLZ) to their corresponding Bundesland (federal state).
It can process individual PLZ inputs or bulk process PLZ data from Excel files.

Usage:
    python plz_to_bundesland.py [OPTIONS]

Options:
    -p, --plz PLZ           Single PLZ to convert
    -f, --file FILE         Input Excel file path
    -o, --output FILE       Output Excel file path (default: output.xlsx)
    -h, --help              Show this help message and exit

Example:
    python plz_to_bundesland.py -p 10115
    python plz_to_bundesland.py -f input.xlsx -o output.xlsx
"""

import argparse
import sys
from typing import Dict, Tuple, Optional

import pandas as pd

from plz_data import PLZ_RANGES

def get_bundesland(plz: str) -> str:
    """
    Determine the Bundesland based on the given PLZ.

    Args:
        plz (str): The postal code (PLZ) to look up.

    Returns:
        str: The corresponding Bundesland or 'Unknown' if not found.
    """
    plz = plz.zfill(5)  # Ensure 5-digit format
    for (start, end), bundesland in PLZ_RANGES.items():
        if start <= plz <= end:
            return bundesland
    return 'Unknown'

def process_excel(input_file: str, output_file: str) -> None:
    """
    Process an Excel file containing PLZ data and output results to a new Excel file.

    Args:
        input_file (str): Path to the input Excel file.
        output_file (str): Path to the output Excel file.

    Raises:
        ValueError: If the input file doesn't contain a 'PLZ' column.
    """
    try:
        df = pd.read_excel(input_file)
        if 'PLZ' not in df.columns:
            raise ValueError("The Excel file must contain a 'PLZ' column.")

        df['PLZ'] = df['PLZ'].astype(str).str.zfill(5)
        df['Bundesland'] = df['PLZ'].apply(get_bundesland)
        df.to_excel(output_file, index=False)
        print(f"Conversion completed. Results saved to {output_file}")
    except Exception as e:
        print(f"An error occurred while processing the Excel file: {e}")
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description="Convert German PLZ to Bundesland")
    parser.add_argument("-p", "--plz", help="Single PLZ to convert")
    parser.add_argument("-f", "--file", help="Input Excel file path")
    parser.add_argument("-o", "--output", default="output.xlsx", help="Output Excel file path")

    args = parser.parse_args()

    if args.plz:
        bundesland = get_bundesland(args.plz)
        print(f"PLZ {args.plz} belongs to {bundesland}")
    elif args.file:
        process_excel(args.file, args.output)
    else:
        parser.print_help()
        sys.exit(1)

if __name__ == "__main__":
    main()
