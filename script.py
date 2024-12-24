import sys

import PyPDF2
from PyPDF2.errors import PdfReadError


def merge_pdfs(pdf_list, output_path):
    merger = PyPDF2.PdfMerger()
    for pdf in pdf_list:
        try:
            merger.append(pdf)
        except FileNotFoundError:
            print(f"Error: The file {pdf} was not found.")
        except PdfReadError:
            print(f"Error: The file {pdf} is not a valid PDF.")
            return
    try:
        merger.write(output_path)
    except Exception as e:
        print(f"Error: Could not write to output file {output_path}. {e}")
    finally:
        merger.close()


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: python script.py <pdf1> <pdf2> ... <output>")
    else:
        pdf_list = sys.argv[1:-1]
        output_path = sys.argv[-1]
        merge_pdfs(pdf_list, output_path)
