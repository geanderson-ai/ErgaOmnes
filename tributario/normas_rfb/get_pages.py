

base_url = "http://normas.receita.fazenda.gov.br/sijut2consulta/consulta.action?facetsExistentes=&orgaosSelecionados=&tiposAtosSelecionados=42&lblTiposAtosSelecionados=&ordemColuna=&ordemDirecao=&tipoConsulta=formulario&tipoAtoFacet=&siglaOrgaoFacet=&anoAtoFacet=&termoBusca=&numero_ato=&tipoData=2&dt_inicio=&dt_fim=&ano_ato=&p=1&optOrdem=Publicacao_DESC&p="

for i in range(2, 57):
    webpage = base_url + str(i)
    print(webpage)