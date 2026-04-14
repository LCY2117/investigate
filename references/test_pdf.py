import pdfplumber

print('Opening PDF...')
with pdfplumber.open(r'D:\WARE_HOUSE\desktop_file\市调大赛\references\Economic-Index_v4_2026.01.14_g.pdf') as pdf:
    print(f'Pages: {len(pdf.pages)}')
    text = pdf.pages[0].extract_text()
    print(f'First page text length: {len(text or "")}')
    print('First 200 chars:', text[:200] if text else 'No text')