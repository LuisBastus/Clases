CREATE TABLE cliente (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(50),
    apellido VARCHAR(50),
    email VARCHAR(100) UNIQUE,
    telefono VARCHAR(15)
);

ALTER TABLE 
    ALTER COLUMN telefono TYPE VARCHAR(25);

INSERT INTO cliente (nombre, apellido, email, telefono)
    VALUES ('luis','bastus','luis@gmail.com','+902 23423454355')

INSERT INTO cliente (nombre, apellido, email, telefono)
    VALUES ('fernando','rivera','fernando@gmail.com','+34 9098979');

INSERT INTO cliente (nombre, apellido, email, telefono)
    VALUES ('ambrosio','salcedo','ambrobebe1@gmail.com','+92 2434355');

INSERT INTO cliente (nombre, apellido, email, telefono)
    VALUES ('lionel','ronaldo','neymar@gmail.com','+90 23322555')

-- Tabla Cuenta Bancaria
CREATE TABLE cuenta_bancaria (
    id SERIAL PRIMARY KEY,
    numero_cuenta VARCHAR(20) UNIQUE,
    tipo_cuenta VARCHAR(20) CHECK (tipo_cuenta IN ('Ahorros', 'Corriente')),
    saldo NUMERIC(15, 2) CHECK (saldo >= 0),
    id_cliente INT REFERENCES cliente(id) 
);

INSERT INTO cuenta_bancaria (numero_cuenta, tipo_cuenta, saldo)
    VALUES ('1234 5678 9012 3456', 'Ahorros','1246,98')

ALTER TABLE cuenta_bancaria
    DROP CONSTRAINT tipo_cuenta;

ALTER TABLE cuenta_bancaria
    ADD CONSTRAINT check_tipo_cuenta CHECK(tipo_cuenta IN ('Ahorros', 'Corriente','Remunerada'));

ALTER TABLE cuenta_bancaria
    DROP CONSTRAINT cuenta_bancaria_tipo_cuenta_check;

ALTER TABLE cuenta_bancaria
    ADD CONSTRAINT check_tipo_cuenta CHECK(tipo_cuenta IN ('Ahorros', 'Corriente','Remunerada'));

INSERT INTO cuenta_bancaria (numero_cuenta, tipo_cuenta, saldo)
    VALUES ('1234 1235 9012 3456', 'Remunerada','12764.98')



    -- Tabla Producto Financiero
CREATE TABLE producto_financiero (
    id SERIAL PRIMARY KEY,
    nombre_producto VARCHAR(50),
    tipo_producto VARCHAR(20) CHECK (tipo_producto IN ('Acción', 'Fondo', 'Bono')),
    rentabilidad_anual NUMERIC(5, 2)
);

-- Tabla Inversiones (Intermedia)
CREATE TABLE inversion (
    id SERIAL PRIMARY KEY,
    id_cliente INT REFERENCES cliente(id) ON DELETE CASCADE,
    id_producto INT REFERENCES producto_financiero(id) ON DELETE CASCADE,
    fecha_inversion DATE DEFAULT CURRENT_DATE,
    monto_invertido NUMERIC(15, 2) CHECK (monto_invertido > 0)
);

-- Tabla Transacción
CREATE TABLE transaccion (
    id SERIAL PRIMARY KEY,
    id_cuenta INT REFERENCES cuenta_bancaria(id) ON DELETE CASCADE,
    fecha_transaccion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    tipo_transaccion VARCHAR(20) CHECK (tipo_transaccion IN ('Depósito', 'Retiro')),
    monto NUMERIC(15, 2) CHECK (monto > 0)
);