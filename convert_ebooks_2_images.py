import os
from pdf2image import convert_from_path
from PyPDF2 import PdfFileReader

pdf_dir = "./dataset/ebooks"

os.system("mkdir -p ./dataset/ebooks")
os.system("mkdir -p ./dataset/images")

for pdf_file in os.listdir(pdf_dir):
    if pdf_file.endswith(".pdf"):
        print(pdf_file)
        pages = convert_from_path(os.path.join(pdf_dir, pdf_file), 300)
        for page in pages:
            output = os.path.join('./dataset', 'images', str(page)+".jpg")
            page.save(output, 'JPEG')
        #print(pages)


