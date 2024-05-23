# Paper Title Extractor

Short Python code that extracts the title from the PDF of a scientific paper and renames to it.
This code relies on the idea that the title usually is at most three lines on either first or the second page.
Only useful for file naming convention freaks like me or if there is no related meta-data within the PDF file.

## Prerequisite

This code requires `argparse`, `pypdf`, `re`, and `nltk`.
```bash
pip install argparse pypdf re nltk
```

## Usage

```bash
python3 main.py -p /path/to/pdf
```

## Arguments

- `-p` or `--path`
  - ***Required argument***.
  - The path to the PDF.
  - The user must specify the PDF path for title extranction and file name conversion.

## TODO

- [ ] Take in multiple paths
- [ ] Try to show the title from metadata if it exists
- [x] Create and print candidates of the title to choose from
