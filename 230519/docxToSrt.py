#docxToSrt.py
import os
from docx import Document
doc = Document("202009list.docx")
# doc.save("test.docx")
# for i, paragraph in enumerate(doc.paragraphs):
#     print(str(i+1) + ": " + paragraph.text)