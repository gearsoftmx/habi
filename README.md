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

##Desarrollo

Se piensa realizar una arquitectura basada en capas para distribuir la logica
y no mezclarla, se piensa utilizar la siguiente estructura de capas:

- Controller: Tendra toda la logica para exponer el api en forma de REST y pueda
ser consumida por el usuario u otras aplicaciones
- Service: Aqui se manejara toda la logica de negocio y se conectara con el controller
para que este pueda enviar la informacion requerida al cliente
- Repository: Aqui se hara toda la logica de conexiones a base de datos, para obtener 
informacion y pasarsela al service y desde el service se procese esa informacion 
- Model: Aqui se maneja toda la parte de modelos, sirve para que el orm obtenga la informacion
por medio de la base de datos, pero sin utilizar sql nativo dentro del codigo, tambien tiene los
  modelos que se utilizaran para pedir los parametros cuando el usuario consulte el api y la respuesta
  que esta envia al usuario
    - Library: Aqui se colocan las librerias requeridas como conexiones a base de datos u alguna otra
    - Enum: Se utiliza para almacenar informacion de los status de las propiedades
    
### Inyeccion de dependencias
Se plantea el uso de inyeccion de dependencias, esto para evitar el acoplamiento del codigo que puede
provocar que en un futuro sea dificil de modificar y mantener

### Realizacion de la solucion
Se planea consultar la base de datos para revisar la informacion con la que se cuenta de primera mano,
despues se realizara un diagrama para ver la estructura de la base de datos y sus relaciones, una vez
comprendido esa parte, se planea investigar respecto a sql alchemy y como funciona el ORM, una vez realizado se haran 
algunas pruebas para ver como formar los queries exponiendo un servicio de prueba (que ese codigo no 
estara en la version final del api) y los filtros a aplicar, por ultimo se procedera a realizar cada funcionalidad
de cada capa, tambien se contempla una respuesta standard como respuesta del api.

Para la parte de los likes, se planea ver como debe funcionar y proponer una estructura en un diagrama para
solventar esa funcionalidad.

