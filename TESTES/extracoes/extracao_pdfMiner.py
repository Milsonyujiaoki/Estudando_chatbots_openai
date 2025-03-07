from pdfminer.high_level import extract_text

def extract_text_pdfminer(pdf_path, txt_path):
    text = extract_text(pdf_path)
    with open(txt_path, "w", encoding="utf-8") as txt_file:
        txt_file.write(text)

# Exemplo de uso
extract_text_pdfminer("C:\Projetos\Pessoal\Microsoft\TESTES\TESTES\P&R IRPF 2024 - v1.0 - 2024.05.03.pdf", "pdfMiner.txt")