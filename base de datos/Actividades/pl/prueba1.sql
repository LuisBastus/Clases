CREATE TABLE libro(
    id_libro SERIAL PRIMARY KEY,
    titulo VARCHAR(255),
    isbn NUMERIC(10),
    genero VARCHAR(50),
    num_copias NUMERIC,
    disponible BOOLEAN NOT NULL
);

ALTER TABLE libro   
    ADD CONSTRAINT isbn_unique UNIQUE (isbn)

ALTER TABLE libro
ALTER COLUMN isbn VARCHAR(13);

ALTER TABLE libro 
    ALTER COLUMN disponible 
    SET DEFAULT TRUE;

ALTER TABLE libro
 ADD COLUMN id_autor

ALTER TABLE libro 
    ADD CONSTRAINT fk_autor
    FOREIGN KEY (id_autor)
    REFERENCES autor(id_autor)
    ON UPDATE CASCADE;





CREATE TABLE autor(
    id_autor SERIAL PRIMARY KEY, 
    nom_autor VARCHAR(100)

);


ALTER TABLE libro
    ADD CONSTRAINT libro_check CHECK (genero IN('terror', 'fantasia','thriller','policiaca')) KEY, 

CREATE TABLE persona(
    id_persona SERIAL PRIMARY KEY, 
    nom_persona VARCHAR(100),
    dni VARCHAR(9) UNIQUE,
    correo VARCHAR(50),
    fecha_inscrpicion DATE,
    activo BOOLEAN NOT NULL
    
);

ALTER TABLE persona
    ADD CONSTRAINT  correo_dni_unique UNIQUE(correo, dni)

ALTER TABLE persona
    ADD PRIMARY KEY (id_persona, nom_persona, dni);

ALTER TABLE persona 
    ADD CONSTRAINT fecha_inscrpicion_check CHECK (fecha_inscrpicion < CURRENT_DATE)

ALTER TABLE persona 
    ALTER COLUMN activo
    SET DEFAULT FALSE;

ALTER TABLE persona 
    RENAME TO usuario 

CREATE TABLE prestamo(
    id_prestamo SERIAL PRIMARY KEY, 
    fecha_prestamo TIMESTAMPTZ,
    fecha_devolucion TIMESTAMPTZ
); 

ALTER TABLE prestamo
    ADD CONSTRAINT fecha_prestamo_check CHECK(fecha_prestamo < CURRENT_DATE)

ALTER TABLE prestamo
ADD COLUMN id_usuario
ADD CONSTRAINT fk_libro
FOREIGN KEY (id_libro) REFERENCES libro(id_libro);

ALTER TABLE prestamo
ADD CONSTRAINT fk_libro
FOREIGN KEY (id_usuario) REFERENCES persona(id_usuario);