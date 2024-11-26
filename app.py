from flask import Flask, render_template, jsonify, request, Response
import config
from banco import listarDispositivos, listarLeituras, listarConsolidadoPorDiaPorMes, criarDispositivo, criarLeitura, listarConsolidadoPorDispositivoPorDiaPorMes, listarConsolidadoPorHoraPorDia 

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

@app.get('/consolidadoPorHora')
def consolidadoPorHora():
    return render_template('index/consolidadoPorHora.html', titulo='Consolidado Por Hora')

@app.get('/consolidadoDispositivo')
def consolidadoDispositivo():
    return render_template('index/consolidadoDispositivo.html', titulo='Consolidado Dispositivo') 

@app.get('/listar-dispositivos')
def listar_dispositivos():
    dispositivos = listarDispositivos()
    lista = [{'id_dispositivo': dispositivo['id_dispositivo'], 'nome': dispositivo['nome']} for dispositivo in dispositivos]
    return jsonify(lista)

@app.get('/listar-leituras')
def listar_leituras():
    leituras = listarLeituras()
    return jsonify(leituras)

@app.get('/listar-consolidado-dia-mes')
def listar_consolidado_dia_mes():
    mes = request.args.get('mes')
    if mes is None:
        return jsonify({"error": "Parâmetro 'mes' é obrigatório"}), 400
    
    try:
        mes = int(mes)
    except ValueError:
        return jsonify({"error": "Parâmetro 'mes' deve ser um número inteiro"}), 400

    leituras = listarConsolidadoPorDiaPorMes(mes)
    return render_template('index/consolidadoDiarioMensal.html', leituras=leituras)

@app.get('/listar-consolidado-por-hora-dia')
def listar_consolidado_por_hora_dia():
    data = request.args.get('data')
    
    if not data:
        return jsonify({"error": "Parâmetro 'data' é obrigatório"}), 400
    
    leituras = listarConsolidadoPorHoraPorDia(data)
    
    # Retornar os dados como JSON
    return jsonify(leituras)

@app.get('/listar-consolidado-por-dispositivo-dia-mes')
def listar_consolidado_por_dispositivo_dia_mes():
    mes = request.args.get('mes')
    id_dispositivo = request.args.get('id_dispositivo')

    # Verifique se os parâmetros foram fornecidos
    if mes is None or id_dispositivo is None:
        return jsonify({"error": "Parâmetros 'mes' e 'id_dispositivo' são obrigatórios"}), 400

    try:
        # Converta os parâmetros para int
        mes = int(mes)
        id_dispositivo = int(id_dispositivo)
    except ValueError:
        return jsonify({"error": "Parâmetros 'mes' e 'id_dispositivo' devem ser números inteiros"}), 400

    leituras = listarConsolidadoPorDispositivoPorDiaPorMes(mes, id_dispositivo)
    return jsonify(leituras)

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
