#include <ESP8266WiFi.h>

// A biblioteca HttpClient padrão do Arduino é essa aqui:
// https://www.arduino.cc/reference/en/libraries/httpclient/
// Mas, como estamos utilizando o ESP8266, vamos utilizar a biblioteca própria dele:
// https://github.com/esp8266/Arduino/blob/master/libraries/ESP8266HTTPClient/src/ESP8266HTTPClient.h
#include <ESP8266HTTPClient.h>

// https://github.com/esp8266/Arduino/blob/master/libraries/ESP8266WiFi/src/WiFiClient.h
#include <WiFiClient.h>

// Wi-Fi
extern const char* ssid;
extern const char* password;

bool conectarWiFi() {
  Serial.println("Tentando estabelecer uma conexao com a rede Wi-Fi...");
  
  const unsigned long tempoInicial = millis();
  
  WiFi.begin(ssid, password);
  
  do {
    
    if (WiFi.status() == WL_CONNECTED) {
      Serial.println("Conexao Wi-Fi estabelecida com sucesso!");
      
      IPAddress ip = WiFi.localIP();
      Serial.print("IP local: ");
      Serial.printf("%d.%d.%d.%d\n", ip[0], ip[1], ip[2], ip[3]);
      
      return true;
    }
    
    delay(1000);
    
  } while ((millis() - tempoInicial) < 30000L);
  
  Serial.println("Impossivel estabelecer uma conexao com a rede Wi-Fi!");
  
  return false;
}

bool verificarWiFi() {
  if (WiFi.status() == WL_CONNECTED)
    return true;
  
  Serial.println("Conexao Wi-Fi perdida.");
  
  WiFi.disconnect(true);
  
  delay(5000);
  
  return conectarWiFi();
}

void setup() {
  pinMode(D1, OUTPUT);
  digitalWrite(D1, 0);
  
  Serial.begin(115200);
  
  // Para evitar perder as primeiras mensagens do console
  Serial.println();
  Serial.flush();
  delay(1000);
  Serial.println();
  Serial.flush();
  delay(1000);
  
  Serial.println("Iniciando...");
  
  WiFi.mode(WIFI_STA);
  conectarWiFi();
}

void loop() {
  if (!verificarWiFi())
    return;
  
  WiFiClient wiFiClient;
  
  HTTPClient httpClient;
  
  // begin() não realiza nenhum tipo de comunicação via rede, apenas
  // prepara o objeto para ser utilizado depois. Existe uma forma mais
  // prática, mas consome mais memória:
  httpClient.begin(wiFiClient, "10.10.137.36", 3000, "/criar-leitura", false);
  
  // Configura o tempo máximo de espera.
  httpClient.setTimeout(30000);
  
  // Configura o cabeçalho HTTP Connection: close,
  // para pedir para o servidor encerrar a conexão TCP ao final.
  // Por padrão HTTPClient envia o cabeçalho Connection: keep-alive,
  // e tenta reaproveitar a conexão TCP.
  httpClient.setReuse(false);
  
  // Vamos precisar enviar ao menos um cabeçalho, com o tipo do dado
  // que estamos enviando para o servidor. Estou definindo application/octet-stream
  // apenas para que o retorno do servidor fique diferente do outro exemplo :)
  // Poderíamos enviar qualquer outro tipo, como application/json, text/plain,
  // application/x-www-form-urlencoded etc.
  httpClient.addHeader("Content-Type", "application/json");
  
  Serial.println("Enviando requisicao POST HTTP...");
  // Aqui pode ser enviado tanto um array de bytes como uma String:
  //https://github.com/esp8266/Arduino/blob/master/libraries/ESP8266HTTPClient/src/ESP8266HTTPClient.h#L192
  // Importante!!! Aqui nenhum tipo de conversão é realizada pela classe HTTPClient!
  // Ou seja, precisamos saber direitinho o formato/codificação dos dados
  // que estão sendo enviados para o servidor!
  String json = "{\"id_dispositivo\":1,\"consumo\":";
  int luminosidade = analogRead(A0);
  int consumo = 0;
  if (luminosidade < 250) {
    digitalWrite(D1, 0);
  } else {
    consumo = 8;
    digitalWrite(D1, 1);
  }
  json += consumo;
  json += ",\"luminosidade\":";
  json += 100.0f * (float)(1023 - luminosidade) / 1023.0f;
  json += "}";
  unsigned char dados[100];
  json.toCharArray((char*)dados, 100);
  int statusCode = httpClient.POST(dados, json.length());
  
  // Valores negativos não são códigos HTTP válidos, e indicam
  // um erro de comunicação, ou do hardware.
  if (statusCode > 0) {
    Serial.print("Status code: ");
    Serial.println(statusCode);
    
    // O cabeçalho Content-Length não precisa ser pedido
    // explicitamente, porque ele é sempre tratado.
    Serial.print("Content-Length: ");
    Serial.println(httpClient.getSize());
    
    // Todas as contantes disponíveis:
    // https://github.com/esp8266/Arduino/blob/master/libraries/ESP8266HTTPClient/src/ESP8266HTTPClient.h#L64
    if (statusCode == HTTP_CODE_OK) {
      // Podemos pedir para o httpClient ler todo o conteúdo
      // na memória, para depois ser trabalhado, ou podemos
      // simplesmente pedir para o conteúdo ser redirecionado
      // para outro stream, como a porta serial.
      //String body = httpClient.getString();
      //Serial.println(body);
      httpClient.writeToStream(&Serial);
    }
  } else {
    Serial.print("Ocorreu um erro de comunicacao: ");
    Serial.println(httpClient.errorToString(statusCode));
  }
  
  httpClient.end();
  
  Serial.println();
  Serial.println();
  Serial.println("Aguardando para repetir o processo...");
  Serial.println();
  Serial.println();
  
  delay(5000);
}
