import pdfplumber

def extract_text_pdfplumber(pdf_path, txt_path):
    with pdfplumber.open(pdf_path) as pdf:
        with open(txt_path, "w", encoding="utf-8") as txt_file:
            for page in pdf.pages:
                txt_file.write(page.extract_text() + "\n")

# Exemplo de uso
extract_text_pdfplumber("TESTES/P&R IRPF 2024 - v1.0 - 2024.05.03.pdf", "pdfPlumber.txt")