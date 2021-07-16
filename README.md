# README HABI TECHNICAL TEST
***
##Tecnologias a utilizar

- FASTAPI
- SWAGGER
- SQL ALCHEMY (ORM)
- MYSQL
- PYDANTIC
- Inyeccion de dependencias
- PYTEST
- PYCHARM

##Desarrollo

Se piensa realizar una arquitectura basada en capas para distribuir la logica
y no mezclarla, se piensa utilizar la siguiente estructura de capas:

- Controller: Tendrá toda la lógica para exponer el api en forma de REST y pueda
ser consumida por el usuario u otras aplicaciones
- Service: Aquí se manejará toda la lógica de negocio y se conectará con el controller
para que este pueda enviar la información requerida al cliente
- Repository: Aquí se hará toda la lógica de conexiones a base de datos, para obtener 
información y pasársela al service y desde el service se procese esa información 
- Model: Aquí se maneja toda la parte de modelos, sirve para que el orm obtenga la información
por medio de la base de datos, pero sin utilizar sql nativo dentro del código, también tiene los
  modelos que se utilizaran para pedir los parámetros cuando el usuario consulte el api y la respuesta
  que esta envía al usuario
    - Library: Aquí se colocan las librerías requeridas como conexiones a base de datos u alguna otra
    - Enum: Se utiliza para almacenar información de los status de las propiedades
    
### Inyección de dependencias
Se plantea el uso de inyección de dependencias, esto para evitar el acoplamiento del código que puede
provocar que en un futuro sea difícil de modificar y mantener

### Realización de la solución
Se planea consultar la base de datos para revisar la información con la que se cuenta de primera mano,
después se realizara un diagrama para ver la estructura de la base de datos y sus relaciones, una vez
comprendido esa parte, se planea investigar respecto a sqlalchemy y como funciona el ORM, una vez realizado se harán 
algunas pruebas para ver como formar los queries exponiendo un servicio de prueba (que ese codigo no 
estará en la versión final del api) y los filtros a aplicar, por último se procederá a realizar cada funcionalidad
de cada capa, también se contempla una respuesta estándar como respuesta del api.

Para la parte de los likes, se planea ver cómo debe funcionar y proponer una estructura en un diagrama para
solventar esa funcionalidad.

##Explicación de la funcionalidad de la consulta de propiedades
Se expone un microservicio por medio de REST con los siguientes campos:
- status_id: Si no se coloca ningún status, por default será 0 y se mostraran todas las propiedades, si se colocan los status
  3 (Preventa), 4 (En Venta), 5 (Vendido) se mostrarán únicamente las propiedades con esos status, si se coloca cualquier otro
  status la consulta no arroja resultados de propiedades
- city: Si no se coloca ninguna ciudad la consulta arroja resultados de todas las ciudades, si se coloca una ciudad específica,
  se regresaran los resultados específicos con esa ciudad
- year: Si no se coloca ningún año se regresaran resultados con todos los años, si no se regresa un resultado específico para ese 
año
  
Todas las consultas se pueden combinar, colocando todos los filtros o solo los que se requieran según las necesidades.

##Explicación de la funcionalidad de like
Se planea tener una tabla de usuarios (user) y otra de like que relacione a la tabla de usuarios con la tabla de
propiedades (like_user_property), la tabla de like debe tener un campo de fecha, y un campo de status, ese campo de 
status sirve para que si el usuario le da like a una propiedad, y después quita ese like, ese campo de status debe
pasar a 0, (0 si quito el like, 1 si tiene like), asi también agregue un campo en la tabla property llamado like_count
este campo es para ver de manera global cuantos likes tiene la propiedad, esto podría servir para obtener las propiedades
con más likes (se podría filtrar por el campo status) y así poder tener las propiedades con más likes dependiendo el estatus
de la misma por ejemplo.

##Explicación del nuevo diagrama
Se agregan las siguientes tablas:
- country: Se agrega la tabla pais, ya que la ciudad no es suficientemente explícita como para conocer cuál es el pais al 
  que pertenece, si a mexico o colombia, con esa tabla se solventa esa parte
- city: Para la tabla property, se utiliza el id de la tabla city, esto para acelerar las búsquedas por ciudad, ya que es más
rápido para la base de datos buscar un entero que un string, como esta actualmente
  
Adicional a eso, se agrega un campo a la tabla property, en el cual se relaciona el status directamente, eso para que ese campo
sirva para manejar el último status de la propiedad, y la tabla status_history solo sirva como un histórico y no tener que ir a
esa tabla para traer el último status que tiene la propiedad

También se pusieron los campos como no nulos, esto porque los nulos generalmente causan muchos problemas al trabajar con ellos en
código.

##Dudas
###¿Cómo se relacionan la información en base de datos?
Tuve que revisar y hacer un diagrama de la base de datos actual para saber como estaba relacionada, y en base a eso ver de donde y como
iba a obtener la información para mostrarla al cliente.

###¿Cómo funciona SQLALCHEMY, y como se hacen consultas a la bd por ORM?
Tuve que investigar en la documentación tanto de fastapi como de SQLALCHEMY como está implementado esa parte, una vez vi varios
ejemplos lo que hice fue implementarlo como en el ejemplo y realice pruebas para ver como se filtraba una tabla, al final se pudo 
resolver investigando e implementando modelos de SQLAlchemy como representacion a código de las tablas de la base de datos y sus
relaciones.

Revise que SQLAlchemy utiliza un pool de conexiones, para generar sesiones y no estarse conectando directamente a la bd cada vez que
se requiera, sino se conecta por medio del pool de conexiones, las cuales son menos costosas de administrar.

###¿Cómo se implementa la inyección de dependencias en fastapi?
Tenía la duda de si fastapi implementaba la inyección de dependencias o tenía que utilizar una librería de terceros, al final encontre
algunos ejemplos en la documentación de fastapi y vi que era con la palabra DEPENDS, lo que me facilito mucho el implementar esa parte.

###¿Cómo se deben relacionar los filtros entre si y que deben hacer en cada caso?
Vi que existen 2 tipos de filtros, uno es para el status de la propiedad, y el otro es para filtrar por los demas parámetros,
al final considere que si no se aplicaba ningún filtro, debería traerme todos los registros que hay en la base de datos, junto con su 
último status, pero si hay uno o más filtros, debe filtrar por los filtros aplicados, si no se define el status de la propiedad, pero si el 
año debe traerme todos los registros.