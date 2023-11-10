import requests
from bs4 import BeautifulSoup
import pandas as pd

# Create an URL object
url = "http://normas.receita.fazenda.gov.br/sijut2consulta/consulta.action?facetsExistentes=&orgaosSelecionados=&tiposAtosSelecionados=42&lblTiposAtosSelecionados=&ordemColuna=&ordemDirecao=&tipoConsulta=formulario&tipoAtoFacet=&siglaOrgaoFacet=&anoAtoFacet=&termoBusca=&numero_ato=&tipoData=2&dt_inicio=&dt_fim=&ano_ato=&p=1&optOrdem=Publicacao_DESC&p=1"

# Create object page
page = requests.get(url)

# parser-lxml = Change html to Python friendly format
# Obtain page's information
soup = BeautifulSoup(page.text, 'lxml')

# Obtain information from tag <table>
table1 = soup.find('table', id='tabelaAtos')

# Obtain every title of columns with tag <th>
headers = [i.text.strip() for i in table1.find_all('th')]

# Create a list to store the rows
rows = []

# Obtain every row of data with tag <tr>
for row in table1.find_all('tr')[1:]:  # Skip the header row
    row_data = [cell.text.strip() for cell in row.find_all('td')]
    rows.append(row_data)

# Create a pandas DataFrame
df = pd.DataFrame(rows, columns=headers)

# Display the DataFrame
print(df)
