-- Tabela para Operadoras Ativas
DROP TABLE IF EXISTS operadoras_ativas;
CREATE TABLE operadoras_ativas (
    id_operadora SERIAL PRIMARY KEY,
    registro_ans VARCHAR(50),
    cnpj VARCHAR(20),
    razao_social VARCHAR(255),
    nome_fantasia VARCHAR(255),
    modalidade VARCHAR(255),
    logradouro VARCHAR(255),
    numero VARCHAR(255),
    complemento VARCHAR(255),
    bairro VARCHAR(255),
    cidade VARCHAR(255),
    uf VARCHAR(2),
    cep VARCHAR(20),
    ddd VARCHAR(10),
    telefone VARCHAR(20),
    fax VARCHAR(20),
    endereco_eletronico VARCHAR(255),
    representante VARCHAR(255),
    cargo_representante VARCHAR(255),
    regiao_de_comercializacao VARCHAR(10),
    data_registro_ans DATE
);

-- Tabela para Demonstrações Contábeis
DROP TABLE IF EXISTS demonstracoes_contabeis;
CREATE TABLE demonstracoes_contabeis (
    id SERIAL PRIMARY KEY,
    data DATE,
    reg_ans VARCHAR(50),
    cd_conta_contabil VARCHAR(50),
    descricao VARCHAR(255),
    vl_saldo_inicial NUMERIC(18,2),
    vl_saldo_final NUMERIC(18,2)
)