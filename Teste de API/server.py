from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd

app = Flask(__name__)
CORS(app)

#Carrega o CSV das operadoras.
df_operadoras = pd.read_csv("Relatorio_cadop.csv", delimiter=";", encoding="utf-8")
df_operadoras.columns = df_operadoras.columns.str.strip().str.lower()

@app.route('/buscar', methods=['GET'])
def search_operadoras():
    #Obtém o parâmetro 'q' da query string
    query = request.args.get('q', '').strip().lower()

    if not query:
        return jsonify([])
    
    #Busca nas colunas razao_social e nome_fantasia
    mask = (
        df_operadoras['razao_social'].str.strip().str.lower().str.contains(query, na=False) |
        df_operadoras['nome_fantasia'].str.strip().str.lower().str.contains(query, na=False)
    )

    #Seleciona os 10 primeiros resultados relevantes
    results = df_operadoras[mask].head(10).fillna('').astype(str).to_dict(orient='records')
    return jsonify(results)

if __name__ == '__main__':
    print("Colunas do DataFrame:", df_operadoras.columns)
    print(df_operadoras.head())
    app.run(debug=True)