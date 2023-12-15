CREATE TABLE IF NOT EXISTS locadoras (
codigo INT PRIMARY KEY,
Nome_locadora VARCHAR(40),
endereco VARCHAR(75));


CREATE TABLE IF NOT EXISTS Carros (
CarroID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
Marca VARCHAR(50) NOT NULL,
Modelo VARCHAR(50) NOT NULL,
Locadora VARCHAR(250) REFERENCES locadora(nome_locadora)
);
    

CREATE TABLE IF NOT EXISTS Cliente (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    login VARCHAR(50) NOT NULL,
    senha VARCHAR(50) NOT NULL
);


-- Inserir dados na tabela locadoras
INSERT INTO Carros (Marca, Modelo, Locadora) VALUES
	('Ford', 'Focus', 'Locadora SP'),
    ('Chevrolet', 'Cruze', 'Locadora RJ'),
    ('Toyota', 'Corolla', 'Locadora MG'),
    ('Honda', 'Civic', 'Locadora RS'),
    ( 'Fiat', 'Palio', 'Locadora BA'),
    ( 'Volkswagen', 'Golf', 'Locadora PR'),
    ( 'Hyundai', 'HB20', 'Locadora SC'),
    ( 'Nissan', 'Versa', 'Locadora PE'),
    ( 'Renault', 'Duster', 'Locadora GO'),
    ('Mercedes-Benz', 'C180',  'Locadora DF');



/* insert de cliente */

INSERT INTO cliente (login, senha) VALUES ('rosinha@gmail.com', '123');
INSERT INTO cliente (login, senha) VALUES ('dores@gmail.com', '123');
INSERT INTO cliente (login, senha) VALUES ('bricio@gmail.com', '123');
INSERT INTO cliente (login, senha) VALUES ('vava@gmail.com', '123');
INSERT INTO cliente (login, senha) VALUES ('zemari@gmail.com', '123');