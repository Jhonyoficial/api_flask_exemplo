USE PycoderBr;

CREATE TABLE carros(
    id integer NOT NULL auto_increment,
    marca varchar(100),
    modelo varchar(100),
    ano integer,
    PRIMARY KEY (id)
);

INSERT INTO carros (marca, modelo, ano) VALUES ('Fiat','MArea', 1999);
INSERT INTO carros (marca, modelo, ano) VALUES ('Fiat','Uno', 1992);

