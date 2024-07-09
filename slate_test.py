import slate
with open('data/sample.pdf', 'rb') as f:
    document = slate.PDF(f)
    text = " ".join(document)
print(text)