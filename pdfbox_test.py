import pdfbox
def extract_text_from_pdf(file_path):
    p = pdfbox.PDFBox()
    text = p.extract_text(file_path)
    return text
text = extract_text_from_pdf('data/sample.pdf')
print(text)