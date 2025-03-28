# Testes de Nivelamento

Este repositório contem uma série de testes que visam demonstrar conhecimentos e habilidades em:

1. Web Scraping
2. Transformação de Dados
3. Banco de Dados
4. API

Os dois primeiros testes estão em arquivos .py na raiz do projeto, enquanto os outros dois estão em suas respectivas pastas.

# Estrutura do Repositório

```bash
├── Teste de API/
│   ├── server.py                  # Servidor Flask
│   ├── index.html                 # Interface Vue.js (página de busca)
│   ├── Relatorio_cadop.csv        # Arquivo CSV das operadoras
│   ├── API_Operadoras.postman.json # Coleção criada no Postman
├── Teste de Banco de Dados/
│   ├── converter.py               # Script Python para converter dados do CSV em formato SQL
│   ├── criar_db.sql               # Script SQL para criar o Banco de Dados
│   ├── criar_tabela.sql           # Script SQL para criar as tabelas
│   ├── importar_csv.sql           # Script SQL para importar os dados
│   ├── README.md                  # Instruções específicas para o Teste de Banco de Dados
│   └── ...
├── extrair_pdf.py                 # Script Python para extrair dados do Anexo I (Teste 2)
├── baixar_anexos.py               # Script para baixar anexos (Teste 1)
└── README.md                      # (Este arquivo)
```

---

## Teste 1: Web Scraping

**Objetivo:**  
Acessar o site da ANS e fazer download dos Anexos I e II em formato PDF, depois compactá-los em um único arquivo ZIP/RAR.

**Script**  
- `baixar_anexos.py`.

---

## Teste 2: Transformação de Dados

**Objetivo:**  
Extrair os dados da tabela "Rol de Procedimentos e Eventos em Saúde" do PDF do Anexo I, salvar os dados em um arquivo CSV e compactá-lo em um arquivo denominado `Teste_{seu_nome}.zip`. Além disso, substituir as abreviações "OD" e "AMB" pelas descrições completas conforme especificado.

**Script Relevante:**  
- `extrair_pdf.py`.

**Importante:**  
Para executar o Teste 2, é necessário primeiro baixar os anexos (através do script realizado no Teste 1).

---

## Teste 3: Banco de Dados

**Objetivo:**  
Criar e estruturar tabelas em um banco de dados (MySQL 8 ou Postgres >10), importar os dados dos arquivos CSV e responder queries analíticas.

**Observação:**  
Dentro da pasta **Teste de Banco de Dados** há um arquivo `README.md` com instruções detalhadas sobre a execução dos scripts e a importação dos dados.

---

## Teste 4: API

**Objetivo:**  
Desenvolver uma API que realiza uma busca textual na lista de cadastros de operadoras (obtidos no Teste 3.2). A API é implementada em Python utilizando Flask e possui uma rota `/buscar` que retorna os registros mais relevantes conforme o termo de busca informado. Além disso, foi criada uma interface web usando Vue.js para consumir a API e uma coleção no Postman para demonstrar os resultados.

**Scripts Relevantes:**  
- `Teste de API/server.py` – Implementa o servidor Flask com a rota `/buscar`.
- `Teste de API/index.html` – Interface web em Vue.js para realizar as buscas e exibir os resultados.

**Importante:**  
Para executar e testar a API, deve inicializar o arquivo server.py para conseguir fazer requisições.

---

## Pré-Requisitos

- **Python 3.8+** (recomendado usar ambiente virtual)

- **Bibliotecas Python**:
  - `requests`
  - `pdfplumber`
  - `pandas`
  - `Flask`
  - `Flask-Cors`
  - `io` e `zipfile` (já inclusas na biblioteca padrão Python)

- **Postman** (para testar a API)

---
