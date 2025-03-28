#Import da biblioteca requests para requisições com a página e zipfile para compactar os arquivos em formato ZIP
import requests
import zipfile

#Variaveis para obter as URLs dos anexos
URL_ANEXO1 = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos/Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf"
URL_ANEXO2 = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos/Anexo_I_Rol_2021RN_465.2021_RN627L.2024.xlsx"

#Função para baixar o arquivo da URL
def download_pdf(url, nome_arquivo):
    response = requests.get(url);
    with open(nome_arquivo, 'wb') as f:
        f.write(response.content)

#Baixar os arquivos PDFs
download_pdf(URL_ANEXO1, "anexo1.pdf")
download_pdf(URL_ANEXO2, "anexo2.pdf")

#Compactar os PDFs em um único arquivo ZIP
with zipfile.ZipFile("anexos.zip", 'w') as zipf:
    zipf.write("anexo1.pdf")
    zipf.write("anexo2.pdf")