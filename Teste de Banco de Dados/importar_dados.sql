\copy operadoras_ativas(registro_ans, cnpj, razao_social, nome_fantasia, modalidade, logradouro, numero, complemento, bairro, cidade, uf, cep, ddd, telefone, fax, endereco_eletronico, representante, cargo_representante, regiao_de_comercializacao, data_registro_ans) FROM './operadoras_ativas/Relatorio_cadop.csv' DELIMITER ';' CSV HEADER QUOTE '"' ENCODING 'UTF8';

\copy demonstracoes_contabeis(data, reg_ans, cd_conta_contabil, descricao, vl_saldo_inicial, vl_saldo_final) FROM './demonstracoes_contabeis/1T2023c.csv' DELIMITER ';' CSV HEADER QUOTE '"' ENCODING 'UTF8';

\copy demonstracoes_contabeis(data, reg_ans, cd_conta_contabil, descricao, vl_saldo_inicial, vl_saldo_final) FROM './demonstracoes_contabeis/2T2023c.csv' DELIMITER ';' CSV HEADER QUOTE '"' ENCODING 'UTF8';

\copy demonstracoes_contabeis(data, reg_ans, cd_conta_contabil, descricao, vl_saldo_inicial, vl_saldo_final) FROM './demonstracoes_contabeis/3T2023c.csv' DELIMITER ';' CSV HEADER QUOTE '"' ENCODING 'UTF8';

\copy demonstracoes_contabeis(data, reg_ans, cd_conta_contabil, descricao, vl_saldo_inicial, vl_saldo_final) FROM './demonstracoes_contabeis/4T2023c.csv' DELIMITER ';' CSV HEADER QUOTE '"' ENCODING 'UTF8';

\copy demonstracoes_contabeis(data, reg_ans, cd_conta_contabil, descricao, vl_saldo_inicial, vl_saldo_final) FROM './demonstracoes_contabeis/1T2024c.csv' DELIMITER ';' CSV HEADER QUOTE '"' ENCODING 'UTF8';

\copy demonstracoes_contabeis(data, reg_ans, cd_conta_contabil, descricao, vl_saldo_inicial, vl_saldo_final) FROM './demonstracoes_contabeis/2T2024c.csv' DELIMITER ';' CSV HEADER QUOTE '"' ENCODING 'UTF8';

\copy demonstracoes_contabeis(data, reg_ans, cd_conta_contabil, descricao, vl_saldo_inicial, vl_saldo_final) FROM './demonstracoes_contabeis/3T2024c.csv' DELIMITER ';' CSV HEADER QUOTE '"' ENCODING 'UTF8';

\copy demonstracoes_contabeis(data, reg_ans, cd_conta_contabil, descricao, vl_saldo_inicial, vl_saldo_final) FROM './demonstracoes_contabeis/4T2024c.csv' DELIMITER ';' CSV HEADER QUOTE '"' ENCODING 'UTF8';
