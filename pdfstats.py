#!/usr/bin/env python3

from PyPDF2 import PdfFileReader
import re, os

def word_count(str):
    counts = dict()
    words = str.split()
    
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts

def contains_number(string):
    return any(char.isdigit() for char in string)


pdfpath = "./pdf/"
replace2space = ".,()/:;!?"

for filename in os.listdir(pdfpath):
	pdf = PdfFileReader(pdfpath + filename)
	allhits = 0
	t = ""
	print(filename)
	
	for i in range(0, pdf.getNumPages()):
		pdfPage = pdf.getPage(i)
		pdfText = pdfPage.extractText().lower()
		
		for j in range(0, len(pdfText)):
			if pdfText[j:j+1] == "-" and pdfText[j+1:j+2] != " ":
				pdfText = pdfText[0:j] + pdfText[j+1:]
		
		for char in replace2space:
			pdfText = pdfText.replace(char, " ")
		
		hits = re.findall("utlandet", pdfText)
		allhits = allhits + len(hits)
		t = t + pdfText
	
		
	print(allhits)
	wordarray = word_count(t)

	for word in wordarray:
		if not contains_number(word):
			print(str(word), ":", wordarray[str(word)])

