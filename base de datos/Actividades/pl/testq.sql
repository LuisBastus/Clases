CREATE TABLE cliente (
    id SERIAL PRIMARY KEY,
);

CREATE TABLE orden (
    id SERIAL PRIMARY KEY
    id_cliente INT 

    CONSTRAINT fk_cliente
        FOREIGN KEY (id_cliente)
            REFERENCES cliente(id)

);