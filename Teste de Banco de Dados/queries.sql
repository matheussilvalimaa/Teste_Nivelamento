-- 10 Operadoras com maiores despesas - Último Trimestre
WITH ultimo_trimestre AS (
  SELECT date_trunc('quarter', max(data)) AS comeco_trimestre
  FROM demonstracoes_contabeis
)
SELECT 
    oa.razao_social,
    SUM(dc.vl_saldo_inicial - dc.vl_saldo_final) AS total_despesas
FROM demonstracoes_contabeis dc
JOIN operadoras_ativas oa ON dc.reg_ans = oa.registro_ans
JOIN ultimo_trimestre ut
  ON dc.data >= ut.comeco_trimestre
     AND dc.data < (ut.comeco_trimestre + INTERVAL '3 MONTH')
WHERE dc.descricao ILIKE '%SAÚDE MEDICO HOSPITALAR%'
GROUP BY oa.razao_social
ORDER BY total_despesas DESC
LIMIT 10;

--10 Operadoras com maiores despesas - Último Ano

WITH ultimo_ano AS (
  SELECT date_trunc('year', max(data)) AS comeco_ano
  FROM demonstracoes_contabeis
)
SELECT 
    oa.razao_social,
    SUM(dc.vl_saldo_inicial - dc.vl_saldo_final) AS total_despesas
FROM demonstracoes_contabeis dc
JOIN operadoras_ativas oa ON dc.reg_ans = oa.registro_ans
JOIN ultimo_ano ua
  ON dc.data >= ua.comeco_ano
     AND dc.data < (ua.comeco_ano + INTERVAL '1 year')
WHERE dc.descricao ILIKE '%SAÚDE MEDICO HOSPITALAR%'
GROUP BY oa.razao_social
ORDER BY total_despesas DESC
LIMIT 10;
