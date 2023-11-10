import requests
from bs4 import BeautifulSoup


def get_urls():
    url = "http://normas.receita.fazenda.gov.br/sijut2consulta/consulta.action?facetsExistentes=&orgaosSelecionados=&tiposAtosSelecionados=42&lblTipo"

    # Make a request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        html_content = response.content

        # Parse the HTML content with BeautifulSoup
        soup = BeautifulSoup(html_content, 'html.parser')

        # Find all <a> tags with href attribute containing 'link.action?idAto='
        links = soup.find_all('a', href=lambda href: href and 'link.action?idAto=' in href)

        # Extract the URLs from the href attributes
        urls = [link['href'] for link in links]

        unique_list = list(set(urls))

        return print(len(unique_list))
    else:
        print(f"Failed to retrieve content. Status code: {response.status_code}")
        return []

if __name__ == "__main__":
    get_urls()