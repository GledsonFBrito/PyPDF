import PyPDF2
import os

# JUNTAS PDFs
caminho_dos_pdfs = 'pdf'  # nome da pasta com pdfs

novo_pdf = PyPDF2.PdfFileMerger()

for root, dirs, files in os.walk(caminho_dos_pdfs):  # percorre pastas
    for file in files:
        caminho_completo_arquivo = os.path.join(root, file)

        arquivo_pdf = open(caminho_completo_arquivo, 'rb')
        novo_pdf.append(arquivo_pdf)

with open(f'{caminho_dos_pdfs}/novo_arquivo.pdf', 'wb') as meu_novo_pdf:
    novo_pdf.write(meu_novo_pdf)