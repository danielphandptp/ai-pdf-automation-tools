from heapq import merge
import sys
import os
import PyPDF2
from jinja2 import TemplateError
from numpy import source


def pdf_watermarker(watermark_path, source_dir, destination_dir):
    watermark_pdf = open(watermark_path, 'rb')
    watermark = PyPDF2.PdfFileReader(watermark_pdf)
    for filename in os.listdir(source_dir):
        # retrieve the current pdf file, and
        # prepare it for watermarking
        template_pdf = open(f'{source_dir}{filename}', 'rb')
        template = PyPDF2.PdfFileReader(template_pdf)

        # watermark all the pages of the current pdf and
        # parse the pages into a output buffer
        output = PyPDF2.PdfFileWriter()
        for i in range(template.getNumPages()):
            page = template.getPage(i)
            page.mergePage(watermark.getPage(0))
            output.addPage(page)
            with open(f'{destination_dir}{filename}', 'wb') as file:
                output.write(file)
        template_pdf.close()
    watermark_pdf.close()


if __name__ == '__main__':
    watermark_path = sys.argv[1]
    source_dir = sys.argv[2]
    destination_dir = sys.argv[3]
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)
    pdf_watermarker(watermark_path, source_dir, destination_dir)
