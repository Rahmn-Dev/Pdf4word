from pdf2docx import Converter
import os
import uuid
def convert_pdf_to_word(pdf_file_path, document_pk):
    unique_id = uuid.uuid4()

    docx_filename = f"{unique_id}{document_pk}.docx"
    
    directory = 'words'
    if not os.path.exists(directory):
        os.makedirs(directory)
    docx_file_path = os.path.join(directory, docx_filename)
    cv = Converter(pdf_file_path)
    cv.convert(docx_file_path, start=0, end=None)
    cv.close()
    
    return docx_file_path