# src/plz_to_bundesland/converter.py

from .plz_data import PLZ_RANGES

def get_bundesland(plz: str) -> str:
    plz = plz.zfill(5)
    for (start, end), bundesland in PLZ_RANGES.items():
        if start <= plz <= end:
            return bundesland
    return 'Unknown'

def process_excel(input_file: str, output_file: str) -> None:
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