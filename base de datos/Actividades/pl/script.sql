CREATE TABLE cliente(
    id_cliente, 
    Nombre VARCHAR(50),
    apellido VARCHAR(50),
    email VARCHAR(100),
    telefono VARCHAR(15)
);

ALTER TABLE cliente
    RENAME COLUMN id_cliente TO id;


CREATE TABLE cuenta_bancaria(
    id_cuenta_bancaria,
    numero_cuenta VARCHAR(20),
    tipo_cuenta VARCHAR(20),
    saldo
);

ALTER TABLE cuenta_bancaria
    RENAME COLUMN id_cuenta_bancaria TO 

CREATE TABLE producto_financiero(
    id_producto_financiero SERIAL,
    nombre_producto VARCHAR(50),
    rentabilidad_anual NUMERIC (3, 2),

)

ALTER TABLE cuenta_bancaria
    ADD CONSTRAINT fk_cliente 
    FOREIGN KEY (id_cliente)
    REFERENCES cliente(id);

--tabla de inveriones ??
CREATE TABLE inversion (
	id SERIAL PRIMARY KEY,
	id_cliente INT,
	id_producto INT,
	fecha_inversion DATE DEFAULT CURRENT_DATE 
	cantidad_invertida NUMERIC(15,2) CHECK()
	
);