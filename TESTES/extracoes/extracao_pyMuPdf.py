import fitz

def extract_text_pymupdf(pdf_path, txt_path):
    doc = fitz.open(pdf_path)
    with open(txt_path, "w", encoding="utf-8") as txt_file:
        for page in doc:
            txt_file.write(page.get_text("text") + "\n")

# Exemplo de uso
extract_text_pymupdf("C:\Projetos\Pessoal\Microsoft\TESTES\TESTES\P&R IRPF 2024 - v1.0 - 2024.05.03.pdf", "PyMuPdf.txt")