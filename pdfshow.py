#!/usr/bin/env python3

from PyPDF2 import PdfFileReader
import os

pdfpath = "./pdf/"

for filename in os.listdir(pdfpath):
	pdf = PdfFileReader(pdfpath + filename)
	
	print(filename)
	
	for i in range(0, pdf.getNumPages()):
		pdfPage = pdf.getPage(i)
		print(pdfPage.extractText())
