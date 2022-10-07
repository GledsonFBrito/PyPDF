# Compactando / Descompactando arquivos
from zipfile import ZipFile
import os

# Para caminhos com barra invertida (\), utilize r (normalmente no windows)
caminho = r'C:\Users\Gledson\Documents\python_test'

# ESCREVE:
with ZipFile('arquivo.zip', 'w') as zip:  # cria um arquivo zip
    for arquivo in os.listdir(caminho):  # arquivos da pasta (não contando com subpastas)
        caminho_completo = os.path.join(caminho, arquivo)  # se você quiser incluir as demais pastas, 
        zip.write(caminho_completo, arquivo)               # use os.walk()
        

# LISTA ARQUIVOS:
with ZipFile('arquivo.zip', 'r') as zip:
    for arquivo in zip.namelist():
        print(arquivo)

# EXTRAI:
with ZipFile('arquivo.zip', 'r') as zip:
    zip.extractall('descompactado') 
