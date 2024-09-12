from bisect import bisect_right
from .plz_data import PLZ_RANGES
import pandas as pd

def get_bundesland(plz: str) -> str:
    plz = plz.zfill(5)
    index = bisect_right(PLZ_RANGES, (plz,)) - 1
    if index >= 0 and PLZ_RANGES[index][0] <= plz <= PLZ_RANGES[index][1]:
        return PLZ_RANGES[index][2]
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
