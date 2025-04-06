# Markdown to PDF Converter

A Python script that converts Markdown files to PDF with black and white formatting, properly preserving code blocks, headings, and other Markdown elements. The output is optimized for 10-inch e-readers.

## Features

- Converts Markdown to PDF with black and white color scheme
- Preserves code blocks with proper formatting and syntax highlighting
- Handles bold and italic text properly
- Formats blockquotes, headings, and paragraphs
- Simple command-line interface
- Optimized page size and formatting for 10-inch e-readers

## Requirements

- Python 3.6+
- Required packages:
  - markdown-it-py
  - reportlab
  - pygments

## Installation

1. Clone this repository or download the script
2. Create and activate a virtual environment (recommended):

```bash
python -m venv .venv
.venv\Scripts\activate  # On Windows
source .venv/bin/activate  # On Unix/Linux
```

3. Install the required packages:

```bash
pip install markdown-it-py reportlab pygments
```

Or using UV:

```bash
uv pip install markdown-it-py reportlab pygments
```

## Usage

### Basic Usage

```bash
python markdown_to_pdf.py path/to/your/markdown_file.md
```

This will create a PDF file with the same name as the input file but with a `.pdf` extension, formatted for a 10-inch e-reader.

### Specifying Output File

```bash
python markdown_to_pdf.py path/to/your/markdown_file.md -o path/to/output_file.pdf
```

### Help

```bash
python markdown_to_pdf.py -h
```

## Examples

Convert the example Supabase article to PDF:

```bash
python markdown_to_pdf.py supabase/medium_article.md
```

## How It Works

The script uses the following process to convert Markdown to PDF:

1. Parses the Markdown file using the `markdown-it-py` library
2. Converts it to HTML with syntax highlighting for code blocks using Pygments
3. Processes the HTML to create a structured document optimized for e-readers
4. Renders the document to PDF using the `reportlab` library with a page size appropriate for 10-inch e-readers

## E-reader Optimization

The PDF is optimized for 10-inch e-readers with:
- Appropriate page dimensions (6 × 8 inches)
- Adjusted margins (0.5 inch)
- Font sizes optimized for readability
- Well-formatted code blocks with borders and background colors
- Balanced spacing between elements

## License

MIT