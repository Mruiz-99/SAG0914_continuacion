# Descripción de la seguridad de la aplicación

## JSON Web Tokens
Se implementerá JWT para que cada inicio de sesión sea único por cada usuario, este es un estándar abierto (RFC 7519) que define un formato compacto y permitirá transmitir información entre diferentes partes en forma de un objeto JSON firmado digitalmente. Los tokens JWT se utilizan para autenticar y autorizar solicitudes HTTP en aplicaciones web y servicios API RESTful.

## Gateway
El gateway es una pieza clave en la arquitectura de microservicios, ya que es el punto de entrada para todas las solicitudes externas que llegan a nuestra aplicación. Por lo tanto, la seguridad en el gateway es un aspecto crítico que debe ser abordado cuidadosamente para garantizar la protección de nuestros servicios y la privacidad de nuestros usuarios.

## Encriptación de Contraseñas
Para este apartado el sistema contará con la encriptación de las contraseñas desde la fase del cliente hasta el servidor, por lo que ningún usuario ni siquiera los desarrolladores podrán identificar la contraseña de cualquier usuario registrado dentro de la plataforma.

## Red de acceso privado en la base de datos
Para realizar una conexión a la base de datos, sólo se podrá desde las ip's de los desarrolladores por lo que cualquier ip que no esté establecida no podrá realizar peticiones TCP/IP. También para la comunicación con el backend sólo podrá realizar peticiones al puerto de la instancia donde se aloja la base de datos.


### [Regresar al índice](/README.md)