CREATE TABLE users(
    id SERIAL,
    nombre VARCHAR(20)
    edad INT,
    DNI VARCHAR(20) UNIQUE
    email VARCHAR(50) NOT NULL  

    CONSTRAINT pk_users
    PRIMARY KEY (id, DNI)


);

CREATE TABLE trasactions(
    id SERIAL PRIMARY KEY,
    users_id INT, 
    cantidad FLOAT,
    CONSTRAINT fk_users
        FOREIGN KEY(users_id)
            REFERENCES users(id)
                ON DELETE CASCADE 
                ON UPDATE SET NULL 
);



