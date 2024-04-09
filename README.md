# Paper Title Extractor

Short Python code that extracts the title from the PDF of a scientific paper and renames to it.
This code relies on the idea that usually the title does not exceed two lines and the first author's name does not exist in the word dictionary corpus.
Therefore, this code retrieves first two sentences from the PDF and checks if the first word in the second sentence is a name or not.

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

- [ ] Create and print candidates of the title to choose from
  - [ ] Try to show all two lines
  - [ ] Try to show just one line
  - [ ] Try to show the title from metadata if it exists