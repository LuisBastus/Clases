
-- 1. Listar los títulos, calificación y duración de películas con duración mayor a 100 min y clasificación 'PG-13', ordenadas por duración descendente.
SELECT
	title,
	rating,
	length
FROM
	film
WHERE
	length > 100
	AND
	rating = 'PG-13'
ORDER BY
	length DESC
;

-- 2. Obtener los nombres de clientes que contienen la letra 'z' en su apellido y viven en ciudades acabadas en a
SELECT
	CONCAT(c.first_name, ' ', c.last_name) AS full_name,
	ci.city
FROM customer c

INNER JOIN address a USING (address_id)

INNER JOIN city ci USING (city_id)

GROUP BY
	c.first_name, c.last_name, ci.city

HAVING
	c.last_name ILIKE '%z%'
	AND ci.city ILIKE '%a'
;

-- 3. Mostrar las 5 películas más largas con clasificación 'R' o 'NC-17', excluyendo aquellas con una duración menor a 120 minutos.
SELECT
	title,
	rating,
	length
FROM
	film
WHERE
	rating IN ('NC-17','R') AND length >= 120
ORDER BY
	length DESC
FETCH FIRST 5 ROW ONLY;

-- 4. Utiliza operadores de comparación Lista el cliente que se llame Kelly de nombre pero no Knott de apellido
SELECT
	CONCAT(first_name, ' ', last_name) AS full_name
FROM
	customer
WHERE
	first_name ILIKE '%Kelly%' AND last_name NOT LIKE '%Knott%'
-- 5. (Utiliza operadores lógicos)  Nombre que empiece con la letra A y el apellido con que no empieze con la letra B 
SELECT
	CONCAT(first_name, ' ', last_name) AS full_name
FROM
	customer
WHERE
	first_name ILIKE 'A%' AND last_name NOT LIKE 'B%'

-- 6. Lista alquileres realizados entre el 2005-05-25/2005-05-26 o devueltas entre esas mismas fechas gestionado por el staff 1
SELECT
	r.rental_id, CONCAT(s.first_name, ' ', s.last_name) AS full_name,
	r.rental_date,
	r.return_date
FROM
	staff s INNER JOIN rental r USING (staff_id)
WHERE
	s.staff_id = 1
	AND (r.rental_date BETWEEN '2005-05-25' AND '2005-05-26')
	OR (r.return_date BETWEEN '2005-05-25' AND '2005-05-26')
ORDER BY
	r.rental_date
;

-- 7. Lista Alquileres entre 2007-02-15/2007-02-20 y con un valor más alto que 10


-- 8. Lista Cantidad de total de pagos, mínimo, máximo, promedio, total facturado
SELECT
	COUNT(payment_id),
	MIN(amount),
	MAX(amount),
	SUM(amount),
	AVG(amount)
	
FROM
	payment
;

-- 9. Lista Cantidad de total de pagos, mínimo, máximo, promedio, total facturado por mes
SELECT
	TO_CHAR(payment_date, 'dd/mm/yyyy') AS mes,
	COUNT(payment_id),
	MIN(amount),
	MAX(amount),
	SUM(amount),
	AVG(amount)
FROM
	payment
GROUP BY
	mes
ORDER BY
	mes
;

-- 10. Obtener los nombres de los clientes y las películas que han alquilado
SELECT
	CONCAT(c.first_name, ' ', c.last_name) AS full_name,
	f.title
FROM
	customer c

INNER JOIN rental r USING (customer_id) INNER JOIN inventory i USING (inventory_id)
INNER JOIN film f USING (film_id)
;
-- 11. Obtener los empleados con el total de pagos que han procesado y su monto acumulado.
SELECT
	CONCAT(s.first_name, ' ', s.last_name) AS full_name, COUNT(p.payment_id) AS total_pagos, SUM(p.amount) AS monto_acumulado
FROM
	staff s
INNER JOIN payment p 
USING (staff_id)
GROUP BY
	s.first_name, s.last_name
ORDER BY
	monto_acumulado DESC
;
-- 12. Clientes que han gastado más de $100

SELECT
	CONCAT(c.first_name, ' ', c.last_name) AS full_name, SUM(p.amount) AS total_pagos
FROM
	customer c
INNER JOIN payment p 
USING (customer_id)
GROUP BY
	c.first_name, c.last_name
HAVING
	SUM(p.amount) > 100
ORDER BY
	total_pagos
;
-- 13. Lista el Número de películas por actor DE AQUELLOS ACTORES CON MAS DE 20 PELIS
SELECT
	CONCAT(a.first_name, ' ', a.last_name) AS full_name, COUNT(f.film_id) AS total_pelis
FROM
	actor a INNER JOIN film_actor f 

USING (actor_id)

GROUP BY
	a.first_name, a.last_name  HAVING COUNT(f.film_id) > 20
ORDER BY
	total_pelis DESC
;
-- 14. Lista Clientes con más de 30 alquileres
SELECT
	CONCAT(c.first_name, ' ', c.last_name) AS full_name, COUNT(r.rental_id) AS total_alquileres
FROM
	customer c INNER JOIN rental r 

USING (customer_id)

GROUP BY 
	c.first_name, c.last_name HAVING COUNT(r.rental_id) > 30
ORDER BY
	total_alquileres DESC
;

-- 15. Listar las películas más alquiladas y la cantidad de veces que fueron alquiladas
SELECT
	f.title,
	COUNT(r.rental_id) AS total_alquiladas
FROM
	film f
    
INNER JOIN inventory i USING (film_id)

INNER JOIN rental r USING (inventory_id)

GROUP BY
	f.title
ORDER BY
	total_alquiladas DESC
;

-- SUBQUERIES
-- 16. Clientes que han gastado por encima de la media
SELECT
	CONCAT(c.first_name, ' ', c.last_name) AS full_name, SUM(p.amount) AS total_pagos
FROM
	customer c
INNER JOIN payment p 

USING (customer_id)

GROUP BY
	c.first_name, c.last_name
HAVING
	SUM(p.amount) > (SELECT AVG(amount) FROM payment)
ORDER BY
	total_pagos DESC
;

-- 17. Las ciudades que pertenezcan a ESPAÑA

SELECT
	c.city
FROM
	city c
INNER JOIN country co 
USING (country_id)
WHERE 
	co.country = 'Spain'
;

-- 18. Los pagos hechos por la persona en la tienda 1
SELECT
	COUNT(p.payment_id) AS total_pagos, CONCAT(c.first_name, ' ', c.last_name) AS full_name
FROM
	payment p
INNER JOIN customer c 
USING (customer_id)

INNER JOIN staff s 
USING (staff_id)

GROUP BY 
	 s.store_id, c.first_name, c.last_name
HAVING
	s.store_id = 1
ORDER BY
	total_pagos DESC
;

-- 19. Obtener las películas que tienen un precio de alquiler superior al promedio)

SELECT 
	film_id, 
	title, 
	rental_rate

FROM 
	film

WHERE 
	rental_rate > (SELECT AVG(rental_rate) FROM film)
;

-- 20. Obtener las películas cuyo precio de alquiler es mayor que el de al menos una película de la categoría 'Action'
SELECT film.title, film.rental_rate

FROM film

WHERE film.rental_rate > any (
    SELECT rental_rate 
    FROM film
    JOIN film_category ON film.film_id = film_category.film_id
    WHERE category.name = 'Action');

