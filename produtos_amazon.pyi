import requests
from bs4 import BeautifulSoup

headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
  'Accept-Language': 'pt-BR,pt;q=0.9'
}

def detalhes_do_produto(product_url: str) -> dict:
  # Cria um dicionário vazio de detalhes dos produtos
  product_details = {}

  # Pega o conteúdo da página do produto e cria uma soup (para separar o conteúdo dos atributos do produto)
  page = requests.get(product_url, headers=headers)
  soup = BeautifulSoup(page.content, features="lxml")
  try:
    # Tira os dados do produto
    title = soup.find(
      'span', attrs={'id': 'productTitle'}).get_text().strip()
    extracted_price = soup.find(
      'span', attrs={'class': 'a-price'}).get_text().strip()
    price = 'R$' + extracted_price.split('R$')[1]
    
    # Adiciona ao dicionário de detalhes do produto
    product_details['título'] = title
    product_details['preço'] = price
    
    # Devolve o dicionário pronto
    return product_details
  except Exception as e:
    print('Detalhes do produto não puderam ser extraídos')
    print(f'Falha com exceção: {e}')
  
product_url = input('Enter product url: ')
product_details = detalhes_do_produto(product_url)

print(product_details)
