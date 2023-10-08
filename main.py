import sys
from pypdf import PdfMerger, PdfReader
import os

file_directory = 'C:\\Users\\jacob\\Desktop\\test\\'
file_names = os.listdir(file_directory)
pdf1 = ''


def merge_pdfs():
    merger = PdfMerger()
    for file in file_names:
        merger.append(f'{file_directory}{file}')
        # if file.endswith('.pdf'):
    merger.write(f'{file_directory}merged-pdf.pdf')
    merger.close()


if __name__ == '__main__':
    merge_pdfs()
