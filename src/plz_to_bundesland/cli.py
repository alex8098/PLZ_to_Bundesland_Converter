import argparse
import sys
from .converter import get_bundesland, process_excel

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