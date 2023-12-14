use empresarial_oliveiras; 

CREATE TABLE IF NOT EXISTS locadoras (
codigo INT PRIMARY KEY,
Nome_locadora VARCHAR(40),
endereco VARCHAR(75));


CREATE TABLE IF NOT EXISTS Carros (
CarroID INT NOT NULL,
Marca VARCHAR(50) NOT NULL,
Modelo VARCHAR(50) NOT NULL,
Ano YEAR NOT NULL,
Locadora VARCHAR(250) REFERENCES locadora(nome_locadora),
Disponibilidade ENUM('disponivel', 'indisponivel') NOT NULL);
    
CREATE TABLE IF NOT EXISTS cliente (
codigo INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
nome VARCHAR(50) NOT NULL,
CPF VARCHAR (14),
endereco VARCHAR(30),
telefone CHAR(15),
email VARCHAR(30),
senha VARCHAR(8));


-- Inserir dados na tabela locadoras
INSERT INTO Carros (CarroID, Marca, Modelo, Ano, Locadora, Disponibilidade) VALUES
	(1, 'Ford', 'Focus', 2020, 'Locadora SP', 'disponivel'),
    (2, 'Chevrolet', 'Cruze', 2019, 'Locadora RJ', 'disponivel'),
    (3, 'Toyota', 'Corolla', 2021, 'Locadora MG', 'indisponivel'),
    (4, 'Honda', 'Civic', 2022, 'Locadora RS', 'disponivel'),
    (5, 'Fiat', 'Palio', 2018, 'Locadora BA', 'indisponivel'),
    (6, 'Volkswagen', 'Golf', 2020, 'Locadora PR', 'disponivel'),
    (7, 'Hyundai', 'HB20', 2019, 'Locadora SC', 'indisponivel'),
    (8, 'Nissan', 'Versa', 2021, 'Locadora PE', 'disponivel'),
    (9, 'Renault', 'Duster', 2022, 'Locadora GO', 'indisponivel'),
    (10, 'Mercedes-Benz', 'C180', 2023, 'Locadora DF', 'disponivel');



/* insert de cliente */

INSERT INTO cliente (nome, CPF, endereco, telefone, email, senha) VALUES ('Rosangela Silva', '256.284.268-76',  'Av. Recife, 303', '(81)99989-1312', 'rosinha@gmail.com', '123');
INSERT INTO cliente (nome, CPF, endereco, telefone, email, senha) VALUES ('Dolores Santos', '216.566.216-26', 'Rua da Palma, 504', '(81)98738-3546', 'dores@gmail.com', '123');
INSERT INTO cliente (nome, CPF, endereco, telefone, email, senha) VALUES ('Fabricio Xavier', '892.546.897-58', 'Rua do Hospício, 122', '(81)98754-2367', 'bricio@gmail.com', '123');
INSERT INTO cliente (nome, CPF, endereco, telefone, email, senha) VALUES ('Vanuza Lima', '001.395.669-54', 'Av. Padre Lemos, 333', '(81)97054-7543',  'vava@gmail.com', '123');
INSERT INTO cliente (nome, CPF, endereco, telefone, email, senha) VALUES ('José Maria', '181.190.192-99',  'Rua da Concórdia, 55', '(81)98900-4300',  'zemari@gmail.com', '123');