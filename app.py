from flask import Flask, render_template, json, request, Response
import config
from banco import listarDispositivos, listarLeituras, listarConsolidadoPorDiaPorMes, criarDispositivo, criarLeitura  # Importando as funções necessárias

app = Flask(__name__)

@app.get('/')
def index():
    return render_template('index/index.html')

@app.get('/home')
def home():
    return render_template('index/home.html')

@app.get('/sobre')
def sobre():
    return render_template('index/sobre.html', titulo='Sobre Nós')

@app.get('/listar-dispositivos')
def listar_dispositivos():
    dispositivos = listarDispositivos()

    lista = [{'id_dispositivo': dispositivo['id_dispositivo'], 'nome': dispositivo['nome']} for dispositivo in dispositivos]

    return json.jsonify(lista)

@app.get('/listar-leituras')
def listar_leituras():
    leituras = listarLeituras()

    return json.jsonify(leituras)

@app.get('/listar-consolidado-dia-mes')
def listar_consolidado_dia_mes():
    mes = int(request.args.get('mes'))
    leituras = listarConsolidadoPorDiaPorMes(mes)

    return json.jsonify(leituras)

@app.post('/criar-dispositivo')
def criar_dispositivo():
    dados = request.json
    nome = dados['nome']
    criarDispositivo(nome)
    return Response(status=204)

@app.post('/criar-leitura')
def criar_leitura():
    dados = request.json
    id_dispositivo = dados['id_dispositivo']
    consumo = dados['consumo']
    luminosidade = dados['luminosidade']
    criarLeitura(id_dispositivo, consumo, luminosidade)
    return Response(status=204)

if __name__ == '__main__':
    app.run(host=config.host, port=config.port, debug=True)
