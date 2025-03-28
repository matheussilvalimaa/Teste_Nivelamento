import csv

#Lê o arquivo CSV e converte as vírgulas em pontos nas colunas especificadas
def converter_virgula_para_ponto(input_csv, output_csv, colunas_numericas):
    with open(input_csv, 'r', encoding='utf-8-sig', newline='') as infile, \
    open(output_csv, 'w', encoding='utf-8-sig', newline='') as outfile:
        
        leitor = csv.DictReader(infile, delimiter=';')
        #Cria o DictWriter com as mesmas colunas do leitor
        escritor = csv.DictWriter(outfile, fieldnames=leitor.fieldnames, delimiter=';', quoting=csv.QUOTE_MINIMAL)

        #Escreve o cabeçalho
        escritor.writeheader()

        for linha in leitor:
            #Cada coluna que for numérica, substitui a vírgula pelo ponto
            for col in colunas_numericas:
                if linha[col]:
                    linha[col] = linha[col].replace(',','.')
            escritor.writerow(linha)

if __name__ == "__main__":
    #Colunas numéricas dos arquivos CSVs
    colunas_numericas = ["VL_SALDO_INICIAL", "VL_SALDO_FINAL"]

    input_csv = "demonstracoes_contabeis/4T2024.csv"
    output_csv = "demonstracoes_contabeis/4T2024c.csv"

    converter_virgula_para_ponto(input_csv, output_csv, colunas_numericas)
    print(f"Arquivo de saída: {output_csv}")