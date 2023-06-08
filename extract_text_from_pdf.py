# !pip install -q fitz
# !pip install -q PyMuPDF

import fitz
doc = fitz.open('MA-Part-I-Litearry-Theory-and-Criticism-New.pdf')

text = ""
text_file = open("MA-Part-I-Litearry-Theory-and-Criticism-New.txt", "w")
for page in doc:
    text+= page.get_text()

text_file.write(text)

#close file
text_file.close()

