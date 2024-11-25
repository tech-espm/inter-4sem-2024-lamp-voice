-- Esse script vale para o MySQL 8.x. Se seu MySQL for 5.x, precisa executar essa linha comentada:
-- CREATE DATABASE IF NOT EXISTS arduinodb;
CREATE DATABASE IF NOT EXISTS arduinodb DEFAULT CHARACTER SET utf8mb4 DEFAULT COLLATE utf8mb4_0900_ai_ci;

USE arduinodb;

CREATE TABLE dispositivo (
  id_dispositivo INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
  nome VARCHAR(50) NOT NULL
);

INSERT INTO dispositivo (nome) VALUES ('Sala de Estar'), ('Quarto 1'), ('Quarto 2'), ('Cozinha');

CREATE TABLE leitura (
  id_leitura BIGINT NOT NULL PRIMARY KEY AUTO_INCREMENT,
  id_dispositivo INT NOT NULL,
  consumo FLOAT NOT NULL,
  luminosidade FLOAT NOT NULL,
  data DATETIME NOT NULL,
  FOREIGN KEY (id_dispositivo) REFERENCES dispositivo(id_dispositivo)
);
