import os
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import re
import time

def get_urls(url):

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

        return unique_list
    else:
        print(f"Failed to retrieve content. Status code: {response.status_code}")
        return []

def save_text(base_url, links):
    # Create a folder to store the files
    output_folder = 'output_files2'
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Iterate through each link
    for link in links:
        time.sleep(1)
        # Extract the right part of the string after '=' symbol in the URL
        file_name = re.search(r'(?<=\=)\d+', link).group()

        # Combine the base URL with the current link
        full_url = base_url + link

        # Make a request to the URL
        response = requests.get(full_url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            html_content = response.content

            # Parse the HTML content with BeautifulSoup
            soup = BeautifulSoup(html_content, 'html.parser')

            # Extract the text from the HTML content
            text = soup.get_text()

            # Add a timestamp to the file name
            timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
            file_name_with_timestamp = f"{file_name}_{timestamp}.txt"

            # Create the full path for the output file
            file_path = os.path.join(output_folder, file_name_with_timestamp)

            # Save the text to the output file
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(text)

            print(f"File saved: {file_path}")
        else:
            print(f"Failed to retrieve content for {full_url}. Status code: {response.status_code}")




if __name__ == "__main__":
    base_url = "http://normas.receita.fazenda.gov.br/sijut2consulta/consulta.action?facetsExistentes=&orgaosSelecionados=&tiposAtosSelecionados=42&lblTiposAtosSelecionados=&ordemColuna=&ordemDirecao=&tipoConsulta=formulario&tipoAtoFacet=&siglaOrgaoFacet=&anoAtoFacet=&termoBusca=&numero_ato=&tipoData=2&dt_inicio=&dt_fim=&ano_ato=&p=1&optOrdem=Publicacao_DESC&p="
    for i in range(19, 56):
        webpage = base_url + str(i)
        links = get_urls(webpage)
        save_text(webpage, links)
        print(f"Page {i} done!")