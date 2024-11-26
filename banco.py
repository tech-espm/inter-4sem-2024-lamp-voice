# Vamos utilizar o pacote SQLAlchemy para acesso a banco de dados:
# https://docs.sqlalchemy.org
#
# Para isso, ele precisa ser instalado via pip (de preferência com o VS Code fechado):
# python -m pip install SQLAlchemy
#
# Além disso, o SQLAlchemy precisa de um driver de conexão ao banco. Isso depende do servidor
# (MySQL, Postgres, SQL Server, Oracle...) e do driver real. Vamos utilizar o driver MySQL-Connector,
# que também precisa ser instalado (de preferência com o VS Code fechado):
# python -m pip install mysql-connector-python
from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session
import config

# Tabelas utilizadas nos exemplos:
# 
# CREATE TABLE dispositivo (
#   id_dispositivo int NOT NULL PRIMARY KEY AUTO_INCREMENT,
#   nome varchar(50) NOT NULL
# );
#
# CREATE TABLE leitura (
#   id_leitura BIGINT NOT NULL PRIMARY KEY AUTO_INCREMENT,
#   id_dispositivo INT,
#   consumo FLOAT,
#   `data` DATETIME,
#   FOREIGN KEY (id_dispositivo) REFERENCES dispositivo(id_dispositivo)
# );

# Como criar uma comunicação com o banco de dados:
# https://docs.sqlalchemy.org/en/14/core/engines.html
#
# Detalhes específicos ao MySQL:
# https://docs.sqlalchemy.org/en/14/dialects/mysql.html#module-sqlalchemy.dialects.mysql.mysqlconnector
#
# mysql+mysqlconnector://<user>:<password>@<host>[:<port>]/<dbname>
engine = create_engine(config.conn_str)

# A função text(), utilizada ao longo desse código, serve para encapsular um comando
# SQL qualquer, de modo que o SQLAlchemy possa entender!

def listarDispositivos():
    with Session(engine) as sessao:
        dispositivos = sessao.execute(text("SELECT id_dispositivo, nome FROM dispositivo ORDER BY nome")).fetchall()
        lista_dispositivos = [{'id_dispositivo': dispositivo.id_dispositivo, 'nome': dispositivo.nome} for dispositivo in dispositivos]
        return lista_dispositivos  

def listarLeituras():
    with Session(engine) as sessao:
        leituras = sessao.execute(text("""
            SELECT l.id_leitura, l.id_dispositivo, l.consumo, l.data, d.nome 
            FROM leitura l 
            JOIN dispositivo d ON l.id_dispositivo = d.id_dispositivo 
            ORDER BY l.data
        """)).fetchall()
        lista_leituras = [{'id_leitura': leitura.id_leitura, 'nome_dispositivo': leitura.nome, 'consumo': leitura.consumo, 'data': leitura.data} for leitura in leituras]
        return lista_leituras  

def listarConsolidadoPorDispositivoPorDiaPorMes(mes, id_dispositivo):
    with Session(engine) as sessao:
        parametros = {
            'mes': mes,
            'id_dispositivo': id_dispositivo
        }
        leituras = sessao.execute(text("""
            SELECT AVG(consumo) AS consumo, DATE_FORMAT(data, '%d/%m/%Y') AS dia
            FROM leitura
            WHERE EXTRACT(MONTH FROM data) = :mes
              AND id_dispositivo = :id_dispositivo
            GROUP BY DATE_FORMAT(data, '%d/%m/%Y')
            ORDER BY dia;
        """), parametros).fetchall()
        
        lista_leituras = [{'consumo': leitura.consumo, 'dia': leitura.dia} for leitura in leituras]
        return lista_leituras
    
def listarConsolidadoPorDiaPorMes(mes):
    with Session(engine) as sessao:
        parametros = {
            'mes': mes
		}
        leituras = sessao.execute(text("""
            SELECT AVG(consumo) consumo, DATE_FORMAT(data, '%d/%m/%Y') dia
			FROM leitura
			WHERE EXTRACT(MONTH FROM data) = :mes
			GROUP BY DATE_FORMAT(data, '%d/%m/%Y')
			ORDER BY dia;
        """), parametros).fetchall()
        lista_leituras = [{'consumo': leitura.consumo, 'dia': leitura.dia} for leitura in leituras]
        return lista_leituras  
    
def listarConsolidadoPorHoraPorDia(data):
    with Session(engine) as sessao:
        parametros = {
            'data': data
        }
        leituras = sessao.execute(text("""
            SELECT AVG(consumo) AS consumo, DATE_FORMAT(data, '%H') AS hora
            FROM leitura
            WHERE DATE(data) = :data
            GROUP BY DATE_FORMAT(data, '%H')
            ORDER BY hora;
        """), parametros).fetchall()
        
        lista_leituras = [{'consumo': leitura.consumo, 'hora': leitura.hora} for leitura in leituras]
        return lista_leituras

def obterDispositivo(id_dispositivo):
    with Session(engine) as sessao:
        parametros = {'id_dispositivo': id_dispositivo}
        dispositivo = sessao.execute(text("SELECT id_dispositivo, nome FROM dispositivo WHERE id_dispositivo = :id_dispositivo"), parametros).first()

        if dispositivo is None:
            print('Dispositivo não encontrado!')
        else:
            print(f'\nid_dispositivo: {dispositivo.id_dispositivo} / nome: {dispositivo.nome}')

def criarDispositivo(nome):
    with Session(engine) as sessao, sessao.begin():
        dispositivo = {'nome': nome}
        sessao.execute(text("INSERT INTO dispositivo (nome) VALUES (:nome)"), dispositivo)

def criarLeitura(id_dispositivo, consumo, luminosidade):
    with Session(engine) as sessao, sessao.begin():
        leitura = {
            'id_dispositivo': id_dispositivo,
            'consumo': consumo,
            'luminosidade': luminosidade
        }
        sessao.execute(text("INSERT INTO leitura (id_dispositivo, consumo, luminosidade, data) VALUES (:id_dispositivo, :consumo, :luminosidade, now())"), leitura)

# O uso desse tipo de instrução é muito comum em Python!
# Quando executamos um arquivo direto pela linha de comando, como
# python exemplo_sql.py
# o Python fará com que a variável global __name__ valha '__main__', indicando
# que a execução do programa se deu a partir daquele arquivo, e não de outro.
# Quando o arquivo é importado, __name__ valerá o nome do arquivo sem a extensão
# .py, como 'exemplo_sql'
if __name__ == '__main__':
    # Exemplo de listagem de dispositivos
    dispositivos = listarDispositivos()
    for dispositivo in dispositivos:
        print(f'id_dispositivo: {dispositivo["id_dispositivo"]} / nome: {dispositivo["nome"]}')
    
    # Exemplo de listagem de leituras de consumo
    leituras = listarLeituras()
    for leitura in leituras:
        print(f'id_leitura: {leitura["id_leitura"]} / dispositivo: {leitura["nome_dispositivo"]} / consumo: {leitura["consumo"]} / data: {leitura["data"]}')
