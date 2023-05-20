from pdf2docx import Converter

pdf_file = r"C:\Users\yinzijue\Desktop\documents\mOI.pdf"
docx_file = r"C:\Users\yinzijue\Desktop\documents\mOI.docx"
cv = Converter(pdf_file)
cv.convert(docx_file,start=0,end=None)
cv.close()