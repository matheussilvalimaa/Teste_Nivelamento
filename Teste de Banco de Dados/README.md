# Teste de Banco de Dados 

Teste de banco de dados desenvolvido em PostgreSQL, que inclui a criação de tabelas, importação de dados a partir de arquivos CSV e execução de queries analíticas.

## Estrutura do Teste

O projeto está dividido em três arquivos SQL:

1. **create_tables.sql**  
   Contém os comandos DDL para criação do schema e das tabelas necessárias.

2. **import_data.sql**  
   Possui os comandos de importação dos dados dos arquivos CSV para as tabelas utilizando o comando `COPY`.  
   - Arquivos CSV utilizados:
     - `operadoras_ativas.csv`
     - 8 arquivos de demonstrações contábeis (por exemplo: `1T2023c.csv`, `2T2023c.csv`, ..., `4T2024c.csv`)

3. **queries.sql**  
   Contém as queries analíticas que respondem às perguntas do teste, como por exemplo:
   - Quais as 10 operadoras com maiores despesas em “EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR” no último trimestre.
   - Quais as 10 operadoras com maiores despesas nessa mesma categoria no último ano.

4. **converter.py**
   Arquivo script criado em Python para converter as vírgulas utilizadas nos arquivos csv das demonstrações contábeis de cada trimestre em pontos, para ter a possibilidade da leitura dos mesmos no Postgre. Não é necessário roda-lo, mantive-o apenas para demonstrar o que tive que fazer para garantir a qualidade e funcionalidade do teste proposto.

## Pré-requisitos

- PostgreSQL (versão 10 ou superior)
- Acesso aos arquivos CSV

## Instruções para Execução

1. **Criação do Banco e Tabelas**

   - Abra o terminal e conecte-se ao seu banco de dados PostgreSQL usando o `psql`
   - Execute o script `create_db.sql` para criar o banco de dados "ans_dados"
   - Depois, execute o script `create_tables.sql` para criar as tabelas necessárias:
     ```bash
     psql -U seu_usuario -d ans_dados -f create_tables.sql
     ```

2. **Importação dos Dados**

   - Execute o script `import_data.sql` para importar os dados:
     ```bash
     psql -U seu_usuario -d ans_dados -f import_data.sql
     ```

3. **Execução das Queries Analíticas**

   - Por fim, execute o script `queries.sql` para rodar as consultas que geram os resultados solicitados:
     ```bash
     psql -U seu_usuario -d ans_dados -f queries.sql
     ```

## Considerações

- **Caminhos dos Arquivos CSV:**  
  Certifique-se de que os arquivos CSV estejam disponíveis no caminho especificado nos comandos `\copy` dentro do arquivo `import_data.sql`. Caso necessário, ajuste os caminhos para que fiquem corretos de acordo com o seu ambiente.

- **Execução dos Scripts:**  
  A ordem de execução é importante: primeiro a criação do banco, depois a criação das tabelas, depois a importação dos dados e, por fim, as consultas.

