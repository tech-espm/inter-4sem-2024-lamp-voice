# Projeto Interdisciplinar IV - Sistemas de Informação ESPM

<p align="center">
    <a href="https://www.espm.br/cursos-de-graduacao/sistemas-de-informacao/"><img src="https://raw.githubusercontent.com/tech-espm/misc-template/main/logo.png" alt="Sistemas de Informação ESPM" style="width: 375px;"/></a>
</p>

# Projeto de Monitoramento de Iluminação e Consumo de Energia

### 2024-02

## Integrantes
- [Alex Macedo](https://github.com/Alexxmfs)
- [Débora Duarte](https://github.com/duartedebis)
- [Henrique Sardella](https://github.com/henrique-sdc)
- [Thiago Alonso](https://github.com/ThiagoAlonso05)

## Descrição do Projeto
  
Este projeto integra um sensor de luminosidade com Arduino, um servidor web Python com Flask e um banco de dados MySQL para monitorar e controlar a iluminação, além de registrar e visualizar o consumo de energia.

## Funcionamento

O sistema opera da seguinte forma:

1. **Sensor de Luminosidade (Arduino):** Um sensor de luminosidade conectado ao Arduino mede a intensidade da luz ambiente.
2. **Controle da Lâmpada (Arduino):** Com base na leitura do sensor, o Arduino aciona ou desliga uma lâmpada conectada à porta digital D1.  Se a luminosidade estiver abaixo de um limite predefinido (250), a lâmpada acende; caso contrário, apaga. O consumo da lâmpada (8 unidades quando acesa) é registrado.
3. **Envio de Dados (Arduino):** O Arduino envia os dados de consumo e luminosidade para o servidor web via requisições HTTP POST no formato JSON.
4. **Servidor Web (Python/Flask):** O servidor recebe os dados do Arduino e os armazena no banco de dados MySQL.  Ele também disponibiliza uma interface web para visualização dos dados em forma de gráficos e tabelas.
5. **Visualização de Dados (Web):** A interface web, construída com HTML, CSS, JavaScript e Chart.js, exibe gráficos de consumo diário, mensal, por dispositivo e por hora.

## Características Principais

* **Automação da Iluminação:**  Liga e desliga a lâmpada automaticamente de acordo com a luminosidade ambiente, promovendo a eficiência energética.
* **Monitoramento do Consumo:**  Registra o consumo de energia da lâmpada, permitindo análises temporais e por dispositivo.
* **Visualização Interativa:**  Apresenta os dados de consumo em gráficos interativos e de fácil compreensão.
* **Interface Web Responsiva:**  Adapta-se a diferentes tamanhos de tela, garantindo uma boa experiência de usuário em dispositivos móveis e desktops.

## Tecnologias Utilizadas

* **Hardware:** Arduino (ESP8266), Sensor de Luminosidade, Lâmpada.
* **Software:**
    * **Microcontrolador:** Arduino IDE, Linguagem C++.
    * **Servidor:** Python, Flask, SQLAlchemy, MySQL Connector.
    * **Frontend:** HTML, CSS, JavaScript, Chart.js, Bootstrap, jQuery, SweetAlert2.

 ## Demonstração do Projeto

Veja como o projeto funciona:

Assista ao vídeo completo da demonstração: [Vídeo de Demonstração](https://youtu.be/7fhjjQ3WA9E)


## Instalação e Execução

**Pré-requisitos:**

* Python 3
* MySQL 8.x (ou 5.x - veja o script SQL)
* Arduino IDE


**Passos:**

1. **Clone o Repositório:**
   ```bash
   git clone https://github.com/Alexxmfs/inter-4sem-2024-lamp-voice.git
   ```

2. **Configure o Banco de Dados:**
   * Crie o banco de dados `arduinodb` executando o script `script.sql`.
   * Adapte os dados de conexão no arquivo `config.py`:
     ```python
     host = '0.0.0.0'  # ou seu IP local
     port = 3000  # porta do seu servidor
     conn_str = 'mysql+mysqlconnector://<usuario>:<senha>@<host>[:<porta>]/arduinodb'
     ```

3. **Crie e Ative o Ambiente Virtual (venv):**
   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # Windows
   source .venv/bin/activate  # Linux/macOS
   ```

4. **Instale as Dependências:**
   ```bash
   pip install -r requirements.txt
   ```

5. **Execute o Servidor Flask:**
   ```bash
   python app.py
   ```

6. **Carregue o Código do Arduino:**
   * Abra o arquivo `Arduino.ino` na Arduino IDE.
   * Configure as credenciais de sua rede Wi-Fi no código do Arduino.
   * Carregue o código para o seu dispositivo ESP8266.

7. **Acesse a Interface Web:**
   Abra um navegador e acesse `http://localhost:3000`.



## Estrutura do Projeto

* `Arduino.ino`: Código do Arduino para leitura do sensor, controle da lâmpada e envio de dados.
* `app.py`: Aplicação Flask que gerencia as rotas, interage com o banco de dados e renderiza as páginas web.
* `banco.py`:  Módulo com funções para interação com o banco de dados.
* `config.py`: Arquivo de configuração do projeto (banco de dados, servidor).
* `requirements.txt`:  Lista de dependências Python.
* `script.sql`: Script para criação do banco de dados e tabelas.
* `templates/`:  Diretório com os arquivos HTML das páginas web.
* `static/`:  Diretório com arquivos estáticos (CSS, JavaScript, imagens).

# Licença

Este projeto é licenciado sob a [MIT License](https://github.com/tech-espm/inter-4sem-2024-lamp-voice/blob/master/LICENSE).

<p align="right">
    <a href="https://www.espm.br/cursos-de-graduacao/sistemas-de-informacao/"><img src="https://raw.githubusercontent.com/tech-espm/misc-template/main/logo-si-512.png" alt="Sistemas de Informação ESPM" style="width: 375px;"/></a>
</p>
