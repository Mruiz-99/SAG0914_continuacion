# Arquitectura de la solución


![](https://i.imgur.com/6Lpe7Nn.png)

## Descripción

### Modelo Cliente-Sevidor
En esencia la arquitectura principal de la aplicación es una basada en el Cliente-Servidor, en donde existe un apartado del cliente(Front-end) y otro del servidor(Back-end) que se comunican através de peticiones HTTP que contienen información en formato JSON. Estas peticiones contendran todos los datos necesarios para que una función se despliegue de manera correcta en el lado del cliente.


### Cliente: Angular
Del lado del cliente se utilizará un framework para la realización de interfaces de usuario llamado Angular, el cual permite la creación de sitios web de una sóla página (SPA por sus siglas en inglés). Este permite que las peticiones al servidor sean mucho más sencillas y prácticas de implementar.

### Servidor: Servicios y Micro Servicios en Flask
En lugar de almacenar todos los endpoints en un sólo servidor, este se dividirá en lo que se conoce como un servicio. El cual es otro servidor que contiene cierta cantidad de endpoints acerca de un tema o entidad en concreto. Esto permite que el servidor posea módulos los cuales son independientes unos de otros por si el servidor llegara a fallar, la mayoría de las funcionalidades sigan en funcionamiento. Esto es posible mediante un API/Gateway el cual distribuye el tráfico de las peticiones HTTP a cada servicio correspondiente.

### Base de Datos: MYSQL
Se contará con una base de datos relacional, que almacene por medio de entidades cada uno de los datos relevantes para el funcionamiento de la aplicación.

### Kubernetes
Para la replicación de aplicación se contará con un orquestador de contenedores el cual permitira condensar todos los contenedores de cada uno de los servicios del servidor. Esto permitirá el alojamiento de la aplicación en distintos lugares para la eficiencia de las peticiones.

### CI/CD
Es un método para distribuir la aplicación principalmente del lado del cliente con frecuencia mediante el uso de la automatización en las etapas del desarrollo de las aplicaciones. Los principales conceptos que se le atribuyen son la integración, la distribución y la implementación continuas.

### Repositorio de Versiones: Gitlab
Para el desarrollo del proyecto se contará con un repositorio el cual almacenará cada una de las versiones que se realicen del proyecto, así como también, cada una de las nuevas funcionalidades o arreglo de errores que se requieran.


### [Regresar al índice](/README.md)