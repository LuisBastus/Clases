

CREATE TABLE fabricante(
    id_ SERIAL PRIMARY KEY,
    nombre VARCHAR(20),
    web VARCHAR(50),
    telefono NUMERIC(9)
);

CREATE TABLE producto(
    id_producto serial PRIMARY KEY, 
    nombre VARCHAR(20) NOT NULL,
    descripcion TEXT(50) NOT NULL,
    categoria VARCHAR(20) NOT NULL,
    precio NUMERIC (10, 2),  
);



