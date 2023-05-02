# Contrato Servicio de Login

## Autenticación

### Descripción del microservicio

Microservicio necesario para la validación de las credenciales de los usuarios. El cual tendrá uso de jwt para el token generado. 

| ID: 001                                                                                        | Nombre: Microservicio de Autenticación                                                                                    |
|:---------------------------------------------------------------------------------------------- |:------------------------------------------------------------------------------------------------------------------------- |
| Prioridad: Alta                                                                                | Historia de usuario: Se quiere poder validar las credenciales ingresadas por el usuario para poder autenticar al usuario. |
| Estimado: 5 puntos                                                                             |                                                                                                                           |
| Módulo: Autenticación                                                                          |                                                                                                                           |
| Criterios de Aceptación:                                                                       |                                                                                                                           |
| Debe poder retornar un token válido para autenticar al usuario y retornar los datos del mismo. |                                                                                                                           |
|                                                                                                |                                                                                                                           |
|                                                                                                |                                                                                                                           |
| Ruta:                                                                                          | /login/autentication                                                                                                      |
| Método:                                                                                        | POST                                                                                                                      |
| Formato de entrada: JSON                                                                       |                                                                                                                           |
|                                                                                                |                                                                                                                           |
|                                                                                                |                                                                                                                           |

### Header:

<table>
     <tr><td> <b> Atributo </b></td> <td> <b> Tipo </b></td> <td> <b>Descripcion</b> </td> </tr>
     <tr> <td>Content type</td> <td>Header</td> <td>application/json</td>
     </tr>     
</table>

### Body:

| **Atributo** | **Tipo** | **Descripción**        |
|:------------ |:-------- |:---------------------- |
| cui          | string   | nombre del usuario     |
| contra       | string   | contraseña del usuario |

| Formato de salida: JSON                                                  |                            |                       |     |
|:------------------------------------------------------------------------ |:-------------------------- |:--------------------- |:--- |
| Código de respuesta exitosa: 200                                         |                            |                       |     |
| Salida:                                                                  |                            |                       |     |
|                                                                          |                            |                       |     |
| **Atributo**                                                             | **Tipo**                   | **Descripción**       |     |
| Mensaje                                                                  | string                     | Logueado exitosamente |     |
|                                                                          |                            |                       |     |
|                                                                          |                            |                       |     |
| Código de respuesta fallida:                                             |                            |                       |     |
| Se utilizará la siguiente lista de errores como referencia:              |                            |                       |     |
| <https://learn.microsoft.com/es-es/partner-center/developer/error-codes> |                            |                       |     |
|                                                                          |                            |                       |     |
| **Código**                                                               | **Descripción**            |                       |     |
| 400                                                                      | Fallo en el proceso        |                       |     |
| 500                                                                      | Fallo interno del servidor |                       |     |

| Body de Salida                                                                                                                                                           |
|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|
| **Tipo**                                                                                                                                                                 |
| String                                                                                                                                                                   |
| **Descripción**                                                                                                                                                          |
| Muestra el detalle del servicio realizado                                                                                                                                |
| **Atributo**                                                                                                                                                             |
| Mensaje                                                                                                                                                                  |
|                                                                                                                                                                          |
|                                                                                                                                                                          |
| Ejemplo de parámetros de entrada                                                                                                                                         |
| <p>{</p><p>"cui": "3001629780101",</p><p>"contra": "passUsu"}</p>                                                                                                        |
|                                                                                                                                                                          |
|                                                                                                                                                                          |
|                                                                                                                                                                          |
|                                                                                                                                                                          |
| Ejemplo de parámetros de salida exitosa                                                                                                                                  |
| <p>{</p><p>"status":200,</p><p>"token": “i893f4fc79badea1dc5db970cf397c8248bac47cc3acf9915ba60b5d76b0e88f”,</p><p></p><p>"mensaje": “Logueado correctamente”</p><p>}</p> |
|                                                                                                                                                                          |
|                                                                                                                                                                          |
|                                                                                                                                                                          |
|                                                                                                                                                                          |
| Ejemplo de parámetros de salida fallida                                                                                                                                  |
| <p>{</p><p>"status": 400,</p><p>"mensaje": “Ha ocurrido un error en la validación de datos”</p><p>}</p>                                                                  |
|                                                                                                                                                                          |
|                                                                                                                                                                          |
|                                                                                                                                                                          |
|                                                                                                                                                                          |
|                                                                                                                                                                          |

## [Regresar al índice](/README.md)