import fitz # Used to read the pdf. Has the name PyMuPDF in requirements.txt

def convert_pdf_to_image(pdf):
    doc = fitz.open(pdf)
    for page in doc:
        page.get_pixmap(matrix=fitz.Matrix(2.5,2.5)).save("maze_page-%i.png" % page.number)


