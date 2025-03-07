import PyPDF2

def extract_text_pypdf2(pdf_path, txt_path):
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        with open(txt_path, "w", encoding="utf-8") as txt_file:
            for page in reader.pages:
                txt_file.write(page.extract_text() + "\n")

# Exemplo de uso
extract_text_pypdf2("C:\Projetos\Pessoal\Microsoft\TESTES\TESTES\P&R IRPF 2024 - v1.0 - 2024.05.03.pdf", "PyPDF2.txt")
