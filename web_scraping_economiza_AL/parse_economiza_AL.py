from bs4 import BeautifulSoup
import pandas as pd

def scrap_economiza_AL(html_doc):
    soup = BeautifulSoup(html_doc, 'html.parser')

    nome_produtos = soup.find_all('h6', {'class': 'cartao_titulo_texto mdl-card__title-text'})
    
    preco_produtos = soup.find_all('span', {'class': 'valor_ultima_venda'})
    
    endereco_produtos = soup.find_all('div', {'class': 'cartao_contribuinte_bloco_esquerdo'})

    data = {'Nome': [],
            'Preço': [],
            'Estabelecimento': [],
            'Rua_numero': [],
            'Bairro': [],
            'CEP': [],
            'Cidade': []}
    for i in range(len(nome_produtos)):
        # Nome dos produtos nos estabelecimentos
        nome_produto = nome_produtos[i].text.strip()
        data['Nome'].append(nome_produto)

        # Preço do produto
        preco_produto = preco_produtos[i].text.strip()
        preco_produto = preco_produto[3:].replace(',', '.')
        preco_produto = float(preco_produto)
        data['Preço'].append(preco_produto)

        # Separando as informações do endereço
        endereco_produto = [item.strip() for item in endereco_produtos[i].text.strip().split('\n')]

        # Nome do estabelecimento
        nome_estabelecimento = endereco_produto[0]
        data['Estabelecimento'].append(nome_estabelecimento)

        # Rua e número 
        rua_numero = endereco_produto[1]
        data['Rua_numero'].append(rua_numero)

        # Cidade, bairro e CEP
        cidade, bairro, cep = ' '.join(endereco_produto[2:]).split(', ')
        bairro = bairro.upper()
        cep = int(''.join(char for char in cep if char.isnumeric()))
        data['Cidade'].append(cidade)
        data['Bairro'].append(bairro)
        data['CEP'].append(cep)
        
    df = pd.DataFrame(data=data)
    
    return df