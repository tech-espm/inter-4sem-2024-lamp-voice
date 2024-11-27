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

USE arduinodb;

INSERT INTO leitura (id_dispositivo, consumo, luminosidade, data) VALUES
(1, 12.34, 50.2, '2022-01-15 14:30:00'),
(2, 9.80, 35.1, '2022-01-16 09:20:00'),
(3, 15.78, 60.0, '2022-02-01 12:00:00'),
(4, 22.45, 70.4, '2022-02-05 18:45:00'),
(1, 13.56, 40.7, '2022-03-10 11:15:00'),
(2, 8.92, 30.9, '2022-03-11 08:10:00'),
(3, 17.65, 65.5, '2022-04-20 19:30:00'),
(4, 19.80, 75.8, '2022-04-25 20:50:00'),
(1, 11.25, 45.3, '2022-05-12 06:45:00'),
(2, 10.35, 38.6, '2022-05-13 07:20:00'),
(3, 14.90, 55.4, '2022-06-15 13:10:00'),
(4, 20.40, 78.1, '2022-06-18 21:05:00'),
(1, 12.00, 50.0, '2022-07-21 15:35:00'),
(2, 9.10, 33.2, '2022-07-22 10:25:00'),
(3, 18.75, 67.8, '2022-08-30 16:45:00'),
(4, 21.90, 82.3, '2022-09-02 22:10:00'),
(1, 13.45, 48.1, '2022-10-05 17:15:00'),
(2, 11.70, 42.9, '2022-10-06 09:40:00'),
(3, 16.35, 62.7, '2022-11-11 14:50:00'),
(4, 23.10, 85.2, '2022-11-15 23:00:00'),
(1, 12.80, 49.5, '2023-01-10 18:15:00'),
(2, 10.00, 36.7, '2023-01-12 08:30:00'),
(3, 15.20, 58.3, '2023-02-14 13:25:00'),
(4, 22.75, 80.4, '2023-02-18 21:40:00'),
(1, 11.90, 46.6, '2023-03-21 06:50:00'),
(2, 9.40, 34.8, '2023-03-23 07:55:00'),
(3, 18.00, 63.5, '2023-04-29 19:20:00'),
(4, 24.20, 87.0, '2023-05-03 22:55:00'),
(1, 14.25, 51.7, '2023-06-09 15:05:00'),
(2, 10.60, 40.1, '2023-06-12 10:15:00'),
(3, 17.50, 60.2, '2023-07-16 13:45:00'),
(4, 21.30, 79.6, '2023-07-19 21:25:00'),
(1, 13.10, 48.8, '2023-08-23 15:50:00'),
(2, 9.70, 36.9, '2023-08-25 10:35:00'),
(3, 16.10, 58.0, '2023-09-29 17:00:00'),
(4, 22.55, 81.7, '2023-10-02 23:15:00'),
(1, 12.45, 46.5, '2023-11-07 18:40:00'),
(2, 8.80, 32.4, '2023-11-09 08:20:00'),
(3, 19.20, 70.3, '2023-12-12 16:30:00'),
(4, 23.75, 84.5, '2023-12-15 23:45:00'),
(1, 13.70, 52.8, '2024-01-05 14:15:00'),
(2, 9.95, 39.3, '2024-01-07 09:10:00'),
(3, 18.25, 66.1, '2024-02-09 18:00:00'),
(4, 24.50, 88.9, '2024-02-12 20:20:00'),
(1, 14.00, 47.9, '2024-03-17 15:10:00'),
(2, 10.10, 35.2, '2024-03-19 09:30:00'),
(3, 17.90, 65.0, '2024-04-23 19:40:00'),
(4, 25.00, 90.0, '2024-05-01 23:10:00'),
(1, 12.75, 44.7, '2024-06-04 13:25:00'),
(2, 9.85, 38.8, '2024-06-06 10:45:00'),
(3, 15.75, 55.6, '2024-07-09 15:35:00'),
(4, 20.80, 77.5, '2024-07-11 21:55:00'),
(1, 13.20, 46.3, '2024-08-14 14:45:00'),
(2, 10.50, 41.7, '2024-08-16 10:05:00'),
(3, 16.60, 59.5, '2024-09-18 16:25:00'),
(4, 23.30, 83.4, '2024-09-22 22:35:00'),
(1, 14.12, 52.3, '2024-11-27 08:15:00'),
(2, 9.34, 40.7, '2024-11-27 09:20:00'),
(3, 16.75, 65.2, '2024-11-27 10:30:00'),
(4, 23.45, 82.1, '2024-11-27 11:45:00'),
(1, 13.98, 48.9, '2024-11-27 12:00:00'),
(2, 10.50, 42.0, '2024-11-27 13:15:00'),
(3, 17.34, 68.3, '2024-11-27 14:25:00'),
(4, 22.89, 80.5, '2024-11-27 15:40:00'),
(1, 14.23, 50.2, '2024-11-27 16:50:00'),
(2, 11.10, 43.8, '2024-11-27 17:55:00'),
(3, 18.75, 72.4, '2024-11-27 18:15:00'),
(4, 24.10, 85.6, '2024-11-27 19:30:00'),
(1, 12.67, 46.5, '2024-11-27 20:10:00'),
(2, 9.85, 39.1, '2024-11-27 21:45:00'),
(3, 15.43, 61.7, '2024-11-27 22:30:00'),
(4, 20.75, 75.3, '2024-11-27 23:00:00'),
(1, 14.89, 54.0, '2024-11-27 07:30:00'),
(2, 10.35, 41.2, '2024-11-27 08:45:00'),
(3, 16.65, 64.1, '2024-11-27 09:50:00'),
(4, 23.75, 83.5, '2024-11-27 10:10:00'),
(1, 12.75, 48.2, '2024-11-26 06:45:00'),
(2, 9.50, 36.4, '2024-11-26 07:20:00'),
(3, 14.90, 58.5, '2024-11-26 08:30:00'),
(4, 21.30, 74.9, '2024-11-26 09:40:00'),
(1, 13.25, 50.1, '2024-11-26 10:50:00'),
(2, 10.45, 41.6, '2024-11-26 11:35:00'),
(3, 17.10, 62.8, '2024-11-26 12:45:00'),
(4, 23.50, 81.3, '2024-11-26 13:55:00'),
(1, 14.12, 51.3, '2024-11-26 14:10:00'),
(2, 11.75, 45.0, '2024-11-26 15:20:00'),
(3, 16.00, 60.5, '2024-11-26 16:40:00'),
(4, 22.25, 78.7, '2024-11-26 17:55:00'),
(1, 12.55, 46.7, '2024-11-26 18:30:00'),
(2, 9.90, 39.3, '2024-11-26 19:10:00'),
(3, 15.70, 61.5, '2024-11-26 20:50:00'),
(4, 21.80, 76.2, '2024-11-26 21:45:00'),
(1, 14.00, 53.0, '2024-11-26 22:25:00'),
(2, 10.75, 42.7, '2024-11-26 23:10:00'),
(3, 16.85, 65.3, '2024-11-26 23:50:00'),
(4, 23.20, 82.9, '2024-11-26 05:30:00'),
(1, 13.40, 49.5, '2024-11-26 06:15:00'),
(2, 9.95, 38.9, '2024-11-26 07:05:00'),
(3, 17.50, 69.1, '2024-11-26 08:20:00'),
(4, 24.10, 85.4, '2024-11-26 09:35:00'),
(1, 12.80, 48.0, '2024-11-26 10:50:00'),
(1, 13.50, 51.7, '2024-11-01 08:15:00'),
(2, 9.80, 38.6, '2024-11-01 09:30:00'),
(3, 15.60, 62.5, '2024-11-01 10:45:00'),
(4, 22.30, 78.1, '2024-11-03 11:50:00'),
(1, 14.20, 53.3, '2024-11-03 12:10:00'),
(2, 10.50, 40.4, '2024-11-05 07:25:00'),
(3, 17.40, 66.7, '2024-11-05 08:15:00'),
(4, 24.50, 84.2, '2024-11-07 09:40:00'),
(1, 12.85, 48.6, '2024-11-07 10:30:00'),
(2, 11.20, 43.8, '2024-11-10 14:25:00'),
(3, 18.10, 70.4, '2024-11-10 15:40:00'),
(4, 25.60, 89.1, '2024-11-12 16:50:00'),
(1, 13.10, 50.5, '2024-11-12 17:30:00'),
(2, 9.90, 37.9, '2024-11-15 06:20:00'),
(3, 14.85, 61.8, '2024-11-15 07:10:00'),
(4, 21.70, 76.3, '2024-11-18 08:30:00'),
(1, 14.35, 54.2, '2024-11-18 09:20:00'),
(2, 10.75, 42.6, '2024-11-20 12:40:00'),
(3, 16.40, 65.1, '2024-11-20 13:30:00'),
(4, 23.90, 83.7, '2024-11-22 14:50:00'),
(1, 12.95, 49.0, '2024-11-22 15:40:00'),
(2, 11.05, 41.3, '2024-11-24 10:20:00'),
(3, 18.75, 73.0, '2024-11-24 11:35:00'),
(4, 24.70, 85.5, '2024-11-25 08:30:00'),
(1, 13.45, 51.1, '2024-11-25 09:15:00'),
(2, 9.60, 36.5, '2024-11-25 10:40:00'),
(3, 17.20, 66.0, '2024-11-25 11:25:00'),
(4, 23.10, 82.6, '2024-11-30 15:50:00'),
(1, 14.00, 53.5, '2024-11-30 16:30:00'),
(2, 10.35, 39.2, '2024-11-30 17:15:00');
