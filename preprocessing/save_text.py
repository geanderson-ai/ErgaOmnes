import requests
from bs4 import BeautifulSoup


def save_webpage_text(url, filename):
    try:

        # Desativa a verificação do certificado SSL
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.123 Safari/537.36'}
        response = requests.get(url, headers=headers)
        # response.raise_for_status()  # Verifica se a solicitação foi bem-sucedida

        # Analisa o HTML da página
        soup = BeautifulSoup(response.content, 'html5lib')

        # Obtém o texto da página
        page_text = soup.get_text()

        # Salva o texto em um arquivo .txt com o nome fornecido
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(page_text)

        print(f"Texto da página salvo em {filename}")
    except requests.exceptions.RequestException as e:
        print(f"Erro ao acessar a página: {e}")
    except Exception as e:
        print(f"Erro ao processar a página: {e}")


# Exemplo de uso:
url = "https://www.planalto.gov.br/ccivil_03/leis/l5172compilado.htm"
filename = "codigo_tributario_nacional.txt"

save_webpage_text(url, filename)
