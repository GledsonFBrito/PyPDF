from bs4 import BeautifulSoup
import requests
import pandas as pd

# url = input('paste the URL from page of Mercado Livre: ')
url = input('Cole aqui a URL da página de produtos do mercado Livre: ')
resposta = requests.get(url)
html_puro = resposta.text
html_limpo = BeautifulSoup(html_puro, 'html.parser')


# nome do produto:
html_nome = html_limpo.find_all('h2', {"class" : "ui-search-item__title ui-search-item__group__element shops__items-group-details shops__item-title"})
# for produto in html_nome:
#     str_produto = produto.contents[0].text
#     print(str_produto)


print('##')

# preço do produto:
html_preco = html_limpo.find_all('span',{'class': 'price-tag-fraction'})
# for preco in html_preco:
#     str_preco = preco.contents[0].text
#     print(str_preco)

lista_de_produtos_e_precos = []
for produto, preco in zip(html_nome, html_preco):
    str_produto = produto.contents[0].text
    str_preco = preco.contents[0].text
    lista_de_produtos_e_precos.append((produto.text, preco.text))

df_produtos = pd.DataFrame(lista_de_produtos_e_precos, columns=['Produto', 'Preço'])
print(df_produtos)
print()
print(df_produtos.describe())

