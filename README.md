# PLZ to Bundesland Converter

This Python script converts German postal codes (PLZ, Postleitzahl) to their corresponding Bundesland (federal state). It can process individual PLZ inputs or bulk process PLZ data from Excel files.

## Features

- Convert a single PLZ to Bundesland
- Bulk convert PLZ from an Excel file
- Command-line interface for easy use
- Exportable results to Excel

## Requirements

- Python 3.6+
- pandas
- openpyxl

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/plz-to-bundesland.git
   cd plz-to-bundesland
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

   Note: The `requirements.txt` file specifies minimum versions of the required packages. Running this command will install these versions or newer ones, ensuring you have the latest compatible versions.

## Usage

### Command-line Interface

1. To convert a single PLZ:
   ```
   python plz_to_bundesland.py -p 10115
   ```

2. To process an Excel file:
   ```
   python plz_to_bundesland.py -f input.xlsx -o output.xlsx
   ```

### As a Python Module

You can also use the `get_bundesland` function in your own Python scripts:

```python
from plz_to_bundesland import get_bundesland

bundesland = get_bundesland("10115")
print(bundesland)  # Output: Berlin
```

## Input Excel File Format

The input Excel file should have the following format:

- The file must be in `.xlsx` format.
- It must contain a column named 'PLZ' (case-sensitive).
- The 'PLZ' column should contain the postal codes to be converted.
- Each PLZ should be in a separate row.
- The PLZ can be formatted as either text or numbers.
- Additional columns may be present in the file; they will be preserved in the output.

Example input Excel file structure:

| PLZ   | City     | Other Data |
|-------|----------|------------|
| 10115 | Berlin   | ...        |
| 80331 | München  | ...        |
| 70173 | Stuttgart| ...        |

Note: Only the 'PLZ' column is required. Any additional columns will be included in the output file unchanged.

## Output

When processing an Excel file, the script will create a new Excel file with the following columns:
- All original columns from the input file
- A new 'Bundesland' column containing the corresponding federal state for each PLZ

Example output Excel file structure:

| PLZ   | City     | Other Data | Bundesland        |
|-------|----------|------------|-------------------|
| 10115 | Berlin   | ...        | Berlin            |
| 80331 | München  | ...        | Bayern            |
| 70173 | Stuttgart| ...        | Baden-Württemberg |

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
