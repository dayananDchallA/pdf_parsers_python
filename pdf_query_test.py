import pdfquery

def extract_text_from_pdf(pdf_file):
    pdf = pdfquery.PDFQuery(pdf_file)
    pdf.load()  # Load the PDF
    
    # Use XPath queries to extract data
    # Here, we extract all the text
    pdf.tree.write("output.xml", pretty_print=True)  # Optional: Save the XML tree for inspection
    
    text_elements = pdf.tree.xpath('//LTTextLineHorizontal')
    extracted_text = "\n".join([el.text for el in text_elements if el.text])
    
    return extracted_text

if __name__ == "__main__":
    pdf_file_path = "data/sample.pdf"
    pdf_text = extract_text_from_pdf(pdf_file_path)
