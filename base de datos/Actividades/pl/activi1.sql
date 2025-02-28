CREATE TABLE cliente (
    id_cliente SERIAL,
    nombre VARCHAR(50),
    correo VARCHAR(100),
    telefono VARCHAR(15)
);

ALTER TABLE cliente
    ADD COLUMN NIF VARCHAR(9);

ALTER TABLE cliente 
    ADD CONSTRAINT nif_unique UNIQUE(NIF)

ALTER TABLE cliente
    ADD PRIMARY KEY (id_cliente)

      

CREATE TABLE vehiculo(
    id_vehiculo SERIAL,
    marca VARCHAR(50),
    modelo VARCHAR(50),
    Año INT 
);

ALTER TABLE vehiculo
    ADD COLUMN estado VARCHAR(20);

ALTER TABLE vehiculo 
    ADD CONSTRAINT estado_check CHECK (estado IN('Disponible', 'reservado', 'mantenimiento'))

ALTER TABLE vehiculo
    ADD PRIMARY KEY (id_vehiculo);

ALTER TABLE vehiculo 
    ADD CONSTRAINT año_check CHECK (año>2000)

CREATE TABLE reserva(
    id_reserva SERIAL,
    fecha_inicio DATE,
    precio_total NUMERIC(9,2)
);

ALTER TABLE reserva
    ADD CONSTRAINT precio_check CHECK (precio_total>0)

--He añadido la columna fecha_fin con un alter porque se me olvido añadirlo desde el principio 
ALTER TABLE reserva 
	ADD COLUMN fecha_fin DATE 

ALTER TABLE reserva
    ADD COLUMN estado_reservado VARCHAR(50);

ALTER TABLE reserva 
    ADD CONSTRAINT reserva_check CHECK (estado_reservado IN('Activa', 'Cancelada', 'Finalizada'))


ALTER TABLE Reserva
ALTER COLUMN estado_reservado 
    SET DEFAULT 'Activa';

ALTER TABLE reserva
    ADD PRIMARY KEY (id_reserva)

ALTER TABLE reserva
ADD COLUMN id_cliente INT;

ALTER TABLE reserva
ADD CONSTRAINT fk_cliente
FOREIGN KEY (id_cliente)
REFERENCES cliente(id_cliente)
ON DELETE CASCADE;

ALTER TABLE reserva
    ADD COLUMN id_vehiculo INT;

ALTER TABLE rerseva 
    ADD CONSTRAINT fk_vehiculo
    FOREIGN KEY (id_vehiculo)
    REFERENCES vehiculo(id_vehiculo)

CREATE TABLE transaccion (
    id_transaccion SERIAL,
    fecha_transaccion DATE DEFAULT CURRENT_DATE,
    suma NUMERIC(15, 2),
    tipo_transaccion VARCHAR(20)
);

ALTER TABLE transaccion
    ADD PRIMARY KEY (id_transaccion);

ALTER TABLE transaccion 
    ADD CONSTRAINT suma_check CHECK (suma>0);

ALTER TABLE transaccion
    ADD CONSTRAINT tipo_transaccion_check CHECK(tipo_transaccion IN('pago','devolucion'))