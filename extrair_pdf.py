import pdfplumber
import pandas as pd
import zipfile
import io

#Função para abrir um pdf e extrair as tabelas, retornando um unico DataFrame
def extrair_tabela(pdf_path):
    dataframes = []

    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            #Extrai a tabela da página
            table = page.extract_table()
            if table:
                df_page = pd.DataFrame(table[1:], columns=table[0])
                dataframes.append(df_page)
    
    #Concatena todos os DataFrames em um único
    if dataframes:
        df = pd.concat(dataframes, ignore_index=True)
        return df
    else:
        return pd.DataFrame()
    
#Substitui as colunas OD e AMB pelos nomes completos
def substituir_abreviacoes(df):
    colunas_renome = {
        "OD": "Seg. Odontológica",
        "AMB": "Seg. Ambulatorial"
    }

    df.rename(columns=colunas_renome, inplace=True)

    #Substitui os valores "OD" e "AMB" nas células das colunas
    if "Seg. Odontológica" in df.columns:
        df["Seg. Odontológica"] = df["Seg. Odontológica"].apply(
            lambda x: "Seg. Odontológica" if isinstance(x, str) and x.strip() == "OD" else x
        )
    if "Seg. Ambulatorial" in df.columns:
        df["Seg. Ambulatorial"] = df["Seg. Ambulatorial"].apply(
            lambda x: "Seg. Ambulatorial" if isinstance(x, str) and x.strip() == "AMB" else x
        )
    return df

#Salva o DataFrame em formato CSV em memória para então compacta-lo em ZIP
def salvar_csv_pdf(df, nome_zip, nome_csv_interno="saida.csv"):
    csv_buffer = io.StringIO()
    df.to_csv(csv_buffer, index=False, encoding='utf-8-sig')

    with zipfile.ZipFile(nome_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
        zipf.writestr(nome_csv_interno, csv_buffer.getvalue())

def main():
    #1. Caminho para o PDF do Anexo 1
    caminho_pdf = "anexo1.pdf"
    
    #2. Extrair dados da tabela
    df = extrair_tabela(caminho_pdf)

    if df.empty:
        print("Nenhuma tabela encontrada no PDF fornecido.")
        return

    #3. Substituir abreviações com base no rodapé
    df = substituir_abreviacoes(df)

    #4. Salvar o CSV criado em ZIP
    nome_zip = "Teste_Matheus.zip"
    salvar_csv_pdf(df, nome_zip)
    
    print(f"Arquivo ZIP gerado: {nome_zip}")

if __name__ == "__main__":
    main()