from flask import Flask, jsonify, render_template
from flask_cors import CORS

from modulos.conversoes import converter

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/converter/<valor>/<unidade_origem>/<unidade_destino>')
def getConversao(valor, unidade_origem, unidade_destino):
    try:
        conversao = converter(float(valor), unidade_origem, unidade_destino)
        if conversao is not None:
            return jsonify(
                {
                    'codigo': 200, 
                    'conversao': conversao, 
                    "unidade_origem": unidade_origem, 
                    "unidade_destino": unidade_destino
                }
            )
        else:
            raise Exception(f'Nao foi possivel converter! Impossivel converter {unidade_origem} para {unidade_destino}')
        
    except Exception as ex:
        return jsonify({'codigo': 400, "message": str(ex)})



app.run(host='0.0.0.0', port=81)
