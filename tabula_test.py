import tabula

def extract_table_from_pdf(file_path):
    df = tabula.read_pdf(file_path, pages='all')
    return df
df = extract_table_from_pdf('data/sample.pdf')
print(df)