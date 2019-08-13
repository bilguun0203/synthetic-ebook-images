import os
import time
from pdf2image import convert_from_path
#from PyPDF2 import PdfFileReader

pdf_dir = "./dataset/ebooks"

os.system("mkdir -p ./dataset/ebooks")
os.system("mkdir -p ./dataset/images")

for pdf_file in os.listdir(pdf_dir):
    if pdf_file.endswith(".pdf"):
        print(pdf_file)
        try:
            pages = convert_from_path(os.path.join(pdf_dir, pdf_file), 300, output_folder='./dataset/images', output_file=str(pdf_file)+str(time.time()), fmt='jpg', thread_count=4)
        except KeyboardInterrupt:
            print('Interrupting...')
            break
        except Exception as e:
            print('Error:', str(e))
            pass
        #print(pages)


