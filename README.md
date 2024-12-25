# PDF Merger Python script

This repository contains a Python script (`script.py`) that merges multiple PDF files into a single PDF file.

## Requirements

- Python 3.x
- `PyPDF2` library

You can install the required library using pip:

```sh
pip install PyPDF2
```

## Usage

To use the script, navigate to the directory containing `script.py` and run the following command:

```sh
python script.py output.pdf input1.pdf input2.pdf ...
```

- `output.pdf`: The name of the resulting merged PDF file.
- `input1.pdf`, `input2.pdf`, ...: The PDF files you want to merge.

## Example

```sh
python script.py merged.pdf document1.pdf document2.pdf document3.pdf
```

This command will merge `document1.pdf`, `document2.pdf`, and `document3.pdf` into a single file named `merged.pdf`.
