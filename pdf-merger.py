from heapq import merge
import sys
import os
import PyPDF2


def pdf_merge(master_pdf_name='merged.pdf', pdf_list=[]):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        merger.append(pdf)
    merger.write(master_pdf_name)


if __name__ == '__main__':
    pdf_merge(sys.argv[1], sys.argv[2:])
