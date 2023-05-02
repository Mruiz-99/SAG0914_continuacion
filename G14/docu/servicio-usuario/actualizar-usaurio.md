# Actualizar información usuario

## Descripción del microservicio

Microservicio necesario para la actualización de la información del usuario. 

| ID:008                                                                   | Nombre:Actualizar información usuario                                                       |
|:------------------------------------------------------------------------ |:------------------------------------------------------------------------------------------- |
| Prioridad: Alta                                                          | <p>Historia de usuario:</p><p>Se requiere poder actualizar la información del usuario. </p> |
| Estimado: 7 puntos                                                       |                                                                                             |
| Módulo: Usuario                                                          |                                                                                             |
| Criterios de Aceptación:                                                 |                                                                                             |
| El servicio debe actualizar la información del usuario que está logueado |                                                                                             |
|                                                                          |                                                                                             |
|                                                                          |                                                                                             |
| Ruta:                                                                    | /usuario/editUsuario/{idUsuario}                                                            |
| Método:                                                                  | PUT                                                                                         |
| Formato de entrada:                                                      | JSON                                                                                        |
|                                                                          |                                                                                             |
|                                                                          |                                                                                             |

## Header:

<table>
     <tr><td> <b> Atributo </b></td> <td> <b> Tipo </b></td> <td> <b>Descripcion</b> </td> </tr>
     <tr> <td>Content type</td> <td>Header</td> <td>application/json</td>
     </tr>   
     <tr> <td>Authentication</td> <td>Header</td> <td> bearer token </td>
     </tr>    
</table>

| Body         |          |                 |
|:------------ |:-------- |:--------------- |
| **Atributo** | **Tipo** | **Descripción** |
| idUsuario    | number   | id del cliente  |
|              |          |                 |
|              |          |                 |
|              |          |                 |

| Formato de salida: JSON                                                  |                            |                                                        |     |
|:------------------------------------------------------------------------ |:-------------------------- |:------------------------------------------------------ |:--- |
| Código de respuesta exitosa: 200                                         |                            |                                                        |     |
| Salida:                                                                  |                            |                                                        |     |
|                                                                          |                            |                                                        |     |
| **Atributo**                                                             | **Tipo**                   | **Descripción**                                        |     |
| Mensaje                                                                  | string                     | La información del usuario se ha actualizado con éxito |     |
|                                                                          |                            |                                                        |     |
|                                                                          |                            |                                                        |     |
| Código de respuesta fallida:                                             |                            |                                                        |     |
| Se utilizará la siguiente lista de errores como referencia:              |                            |                                                        |     |
| <https://learn.microsoft.com/es-es/partner-center/developer/error-codes> |                            |                                                        |     |
|                                                                          |                            |                                                        |     |
| **Código**                                                               | **Descripción**            |                                                        |     |
| 400                                                                      | Fallo en el proceso        |                                                        |     |
| 500                                                                      | Fallo interno del servidor |                                                        |     |

| Body de Salida                                                                                                 |
|:--------------------------------------------------------------------------------------------------------------:|
| **Tipo**                                                                                                       |
| String                                                                                                         |
| **Descripción**                                                                                                |
| Muestra el detalle del servicio realizado                                                                      |
| **Atributo**                                                                                                   |
| Mensaje                                                                                                        |
|                                                                                                                |
|                                                                                                                |
| Ejemplo de parámetros de entrada                                                                               |
| <p>{</p><p>"cui": "3001629780101",</p><p>"correo": "vall@gmail.com"}</p>                                       |
|                                                                                                                |
|                                                                                                                |
|                                                                                                                |
|                                                                                                                |
| Ejemplo de parámetros de salida exitosa                                                                        |
| <p>{</p><p>"status":200,</p><p>"mensaje": “Se han actualizado los datos del usuario 3300962560101”</p><p>}</p> |
|                                                                                                                |
|                                                                                                                |
|                                                                                                                |
|                                                                                                                |
| Ejemplo de parámetros de salida fallida                                                                        |
| <p>{</p><p>"status": 400,</p><p>"mensaje": “Ha ocurrido un error en la sctualización de datos”</p><p>}</p>     |
|                                                                                                                |
|                                                                                                                |
|                                                                                                                |
|                                                                                                                |
|                                                                                                                |

## [Regresar al Contrato](../servicio_usuario.md)