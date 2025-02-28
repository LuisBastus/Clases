-- Ejercicio 1: Uso de Variables y RAISE NOTICE
-- Declarar una variable, asignarle un valor y mostrarlo en la salida.

-- Ejercicio:
-- Declara una variable customer_name para almacenar el nombre de un cliente con customer_id = 5 y muestra su nombre en un mensaje.

    -- Asignar el nombre del cliente con ID 5
    
    -- Mostrar el nombre del cliente
DO $$
DECLARE 
   customer_name 
BEGIN 
   SELECT first_name INTO customer_name
   FROM customer
   WHERE customer_id = 5;
   RAISE NOTICE 'El nombre del cliente es %', customer_name;
END $$; 

-- Ejercicio 2: Uso de %TYPE para Copiar Tipos de Datos
-- Usar %TYPE para definir variables basadas en columnas de una tabla.

-- Ejercicio:
-- Declara una variable film_title con el mismo tipo de dato que la columna title de la tabla film. 
-- Luego, almacena en esta variable el título de la película con film_id = 50 y muéstralo.

    -- Obtener el título de la película con ID 50
    
    -- Mostrar el título de la película


-- Ejercicio 3: Uso del Ámbito de Variables en Bloques
-- Comprender el ámbito de las variables dentro de bloques anidados.

-- Ejercicio:
-- Declara dos variables counter, una en el bloque externo y otra en un sub-bloque. Modifica ambas y muestra sus valores en cada nivel.


    -- Modificar el contador en el bloque externo


    -- Sub-bloque

        -- Modificar el contador en el sub-bloque


    -- Volver a mostrar el valor del counter en el bloque externo

-- Ejercicios sobre SELECT INTO y Múltiples Variables
-- Usar SELECT INTO para almacenar datos en variables.

-- Ejercicio 1: Contar películas disponibles
-- Declara una variable film_count y almacena en ella la cantidad total de películas en la tabla film


   -- Obtener la cantidad total de películas

   -- Mostrar el total


-- Ejercicio 2: Obtener datos de un cliente específico
-- Declara dos variables v_first_name y v_last_name para almacenar el nombre y apellido del cliente con customer_id = 5.

   -- Obtener nombre y apellido del cliente con ID 5


   -- Mostrar el nombre completo


-- Ejercicio 3: Obtener el total de pagos de un cliente
-- Declara una variable total_payment y almacena en ella la suma total de pagos realizados por el cliente con customer_id = 3.


   -- Obtener el total de pagos del cliente con ID 3

   -- Mostrar el total pagado


-- Ejercicios sobre ROW TYPE y RECORD TYPE
-- Usar variables compuestas (%ROWTYPE y RECORD) para almacenar filas completas.

-- Ejercicio 4: Obtener datos de un actor con ROW TYPE
-- Declara una variable selected_actor basada en %ROWTYPE para almacenar toda la fila del actor con actor_id = 20.

   -- Obtener la información completa del actor con ID 20

   -- Mostrar su nombre completo


-- Ejercicio 5: Obtener datos de una película con RECORD TYPE
-- Declara una variable rec de tipo RECORD y almacena en ella los datos de la película con film_id = 50


   -- Obtener la película con ID 50

   -- Mostrar información


-- Ejercicio 6: Obtener los datos de un alquiler con ROW TYPE
-- Declara una variable selected_rental basada en %ROWTYPE para almacenar toda la fila del alquiler con rental_id = 100.


   -- Obtener toda la información del alquiler con ID 100

   -- Mostrar la fecha de alquiler y el ID del cliente


-- EJERCICIO IF

    -- Contar cuántas veces aparece el email en la tabla usuarios

    -- Lanzar excepción si el email existe



    -- Verificar si la edad es menor a 18