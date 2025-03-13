-- Ejercicio 1: Bloque anónimo y variables básicas
DO $$
DECLARE
    total_actores INT;
BEGIN
    SELECT COUNT(*) INTO total_actores FROM actor;
    RAISE NOTICE 'Total de actores: %', total_actores;
END $$;

-- Ejercicio 2: Uso de SELECT INTO, ROW TYPE y RECORD TYPE
DO $$
DECLARE
    actor_nombre VARCHAR;
    actor_info actor%ROWTYPE;
    film_info RECORD;
BEGIN
    SELECT first_name || ' ' || last_name INTO actor_nombre FROM actor WHERE actor_id = 5;
    SELECT * INTO actor_info FROM actor WHERE actor_id = 5;
    SELECT title, description INTO film_info FROM film WHERE film_id = 10;
    RAISE NOTICE 'Actor: %', actor_nombre;
    RAISE NOTICE 'Película: %, Descripción: %', film_info.title, film_info.description;
END $$;

-- Ejercicio 3: Uso de constantes
DO $$
DECLARE
    CONSTANT MAX_RENTAL_DAYS INT := 5;
    total_peliculas INT;
BEGIN
    SELECT COUNT(*) INTO total_peliculas FROM film WHERE rental_duration > MAX_RENTAL_DAYS;
    RAISE NOTICE 'Películas con rental_duration mayor a %: %', MAX_RENTAL_DAYS, total_peliculas;
END $$;

-- Ejercicio 4: Uso de IF en una condición
DO $$
DECLARE
    cantidad_copias INT;
BEGIN
    SELECT COUNT(*) INTO cantidad_copias FROM inventory WHERE film_id = 10;
    IF cantidad_copias > 5 THEN
        RAISE NOTICE 'Suficientes copias disponibles';
    ELSIF cantidad_copias BETWEEN 1 AND 5 THEN
        RAISE NOTICE 'Stock limitado';
    ELSE
        RAISE NOTICE 'No disponible';
    END IF;
END $$;

-- Ejercicio 5: Uso de CASE en una condición
DO $$
DECLARE
    cantidad_copias INT;
    mensaje TEXT;
BEGIN
    SELECT COUNT(*) INTO cantidad_copias FROM inventory WHERE film_id = 10;
    mensaje := CASE 
        WHEN cantidad_copias > 5 THEN 'Suficientes copias disponibles'
        WHEN cantidad_copias BETWEEN 1 AND 5 THEN 'Stock limitado'
        ELSE 'No disponible'
    END;
    RAISE NOTICE '%', mensaje;
END $$;

-- Ejercicio 6: Uso de LOOP para contar del 1 al 5
DO $$
DECLARE
    i INT := 1;
BEGIN
    LOOP
        RAISE NOTICE 'Contador: %', i;
        EXIT WHEN i = 5;
        i := i + 1;
    END LOOP;
END $$;

-- Ejercicio 7: Uso de FOR LOOP para recorrer registros
DO $$
DECLARE
    actor_nombre RECORD;
BEGIN
    FOR actor_nombre IN SELECT first_name, last_name FROM actor LIMIT 10 LOOP
        RAISE NOTICE 'Actor: % %', actor_nombre.first_name, actor_nombre.last_name;
    END LOOP;
END $$;

-- Ejercicio 8: Creación de una función simple
CREATE OR REPLACE FUNCTION get_rental_count(actor_id INT) RETURNS INT AS $$
DECLARE
    rental_count INT;
BEGIN
    SELECT COUNT(*) INTO rental_count 
    FROM rental r
    JOIN inventory i ON r.inventory_id = i.inventory_id
    JOIN film_actor fa ON i.film_id = fa.film_id
    WHERE fa.actor_id = actor_id;
    RETURN rental_count;
END;
$$ LANGUAGE plpgsql;

-- Ejercicio 9: Función sobrecargada
CREATE OR REPLACE FUNCTION get_rental_count(actor_id INT, start_date DATE, end_date DATE) RETURNS INT AS $$
DECLARE
    rental_count INT;
BEGIN
    SELECT COUNT(*) INTO rental_count 
    FROM rental r
    JOIN inventory i ON r.inventory_id = i.inventory_id
    JOIN film_actor fa ON i.film_id = fa.film_id
    WHERE fa.actor_id = actor_id AND r.rental_date BETWEEN start_date AND end_date;
    RETURN rental_count;
END;
$$ LANGUAGE plpgsql;

-- Ejercicio 10: Función que retorna una tabla
CREATE OR REPLACE FUNCTION get_film_info() RETURNS TABLE(film_id INT, title TEXT, rental_rate NUMERIC, rental_duration INT) AS $$
BEGIN
    RETURN QUERY SELECT film_id, title, rental_rate, rental_duration FROM film;
END;
$$ LANGUAGE plpgsql;
