CREATE TABLE Setor (
  id_setor INT,
  nome VARCHAR (10),
  CONSTRAINT pk_setor PRIMARY KEY (id_setor) 
 );
 CREATE TABLE Produto (
    id_produto INT,
  	nome VARCHAR (40),
    preco FLOAT,
    qtd INT,
    id_setor INT,
    CONSTRAINT pk_produto PRIMARY KEY (id_produto),
    CONSTRAINT fk_produto FOREIGN KEY (id_setor) REFERENCES Setor (id_setor)
);

CREATE TABLE Funcionario(
	id_funcionario INT,
  	nome VARCHAR (50),
  	funcao VARCHAR (20),
  	salario FLOAT,
  	CONSTRAINT pk_funcionario PRIMARY KEY (id_funcionario)
);
	
#QUERY SQL
INSERT INTO Funcionario (id_funcionario, nome ,funcao, salario)
VALUES
(1, 'João' ,'Caixa',1.104),
(2, 'Maria', 'Repositora', 1.520),
(3,'Marcos','Gerente' , 1.320),
(4, 'Julia' , 'Empacotadora' , 1.340);
SELECT funcao FROM Funcionario;
SELECT nome , ROUND(salario * 1.10,3) AS salario_aumentado FROM Funcionario;

SELECT nome , funcao FROM Funcionario
WHERE (nome LIKE 'A__') OR (LOWER(nome) LIKE '%a');

SELECT nome , funcao FROM Funcionario
WHERE nome IN ('João', 'Marcos');



INSERT INTO Produto (id_produto, nome, preco, qtd)
VALUES
(1, 'Arroz', 9.39, 45),
(2, 'Feijão', 4.58, 45),
(3, 'Macarrão', 2.99, 35), 
(4, 'Farinha', 6.49, 56),
(5, 'Ovo', 0.50, 100),
(6, 'Oleo', 4.59, 78);

SELECT COUNT(*) AS total_linhas 
FROM Produto;
SELECT MIN(preco) AS menor_preco
FROM Produto;
SELECT MAX(Preco) AS maior_preco
FROM Produto;

SELECT MIN(preco) AS menor_preco, MAX(preco) AS maior_preco
FROM Produto;

SELECT AVG(preco) as media_valor FROM Produto;

SELECT SUM(qtd) as valor_total FROM Produto;
SELECT SUM(qtd*preco) as valor_total FROM Produto;
SELECT nome , ROUND(preco * 2,2) AS preco_aumentando FROM Produto;