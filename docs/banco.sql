DROP DATABASE discord_bot;
CREATE DATABASE discord_bot;
USE discord_bot;

CREATE TABLE jogos(
	id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(50) NOT NULL UNIQUE
);

CREATE TABLE users(
	id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(50) NOT NULL UNIQUE,
    id_discord VARCHAR(20) NOT NULL,
    vitorias INT DEFAULT 0,
    derrotas INT DEFAULT 0
);

CREATE TABLE mdx(
	id INT PRIMARY KEY AUTO_INCREMENT,
    mdx INT NOT NULL,
    placar1 INT DEFAULT 0,
    placar2 INT DEFAULT 0,
    id_jogo INT NOT NULL,
    id_user1 INT NOT NULL,
    id_user2 INT NOT NULL,
    FOREIGN KEY (id_jogo) REFERENCES jogos(id),
    FOREIGN KEY (id_user1) REFERENCES users(id),
    FOREIGN KEY (id_user2) REFERENCES users(id)
);

CREATE TABLE partidas(
	id INT PRIMARY KEY AUTO_INCREMENT,
    placar1 INT NOT NULL,
    placar2 INT NOT NULL,
    id_mdx INT NOT NULL,
    FOREIGN KEY (id_mdx) REFERENCES mdx(id)
);

DELIMITER //

CREATE TRIGGER altera_placar_mdx AFTER INSERT ON partidas
FOR EACH ROW
BEGIN
    IF NEW.placar1 > NEW.placar2 THEN
        UPDATE mdx 
        SET placar1 = placar1 + 1 
        WHERE id = NEW.id_mdx;
    ELSE
        UPDATE mdx 
        SET placar2 = placar2 + 1 
        WHERE id = NEW.id_mdx;
    END IF;
END; //

DELIMITER ;

DELIMITER //

CREATE TRIGGER verifica_vitoria AFTER UPDATE ON mdx
FOR EACH ROW
BEGIN
    IF NEW.mdx/2 < NEW.placar1 THEN
		UPDATE users
        SET vitorias = vitorias + 1
        WHERE id = NEW.id_user1;
        UPDATE users
        SET derrotas = derrotas + 1
        WHERE id = NEW.id_user2;
	END IF;
	IF NEW.mdx/2 < NEW.placar2 THEN
		UPDATE users
        SET vitorias = vitorias + 1
        WHERE id = NEW.id_user2;
        UPDATE users
        SET derrotas = derrotas + 1
        WHERE id = NEW.id_user1;
	END IF;
END; //

DELIMITER ;
