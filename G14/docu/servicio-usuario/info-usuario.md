# Información usuario

## Descripción del microservicio

Microservicio necesario para la obtención de la información del servicio del usuario. 

| ID:007                                                                 | Nombre: Ver información usuario                                                                                                |
|:---------------------------------------------------------------------- |:------------------------------------------------------------------------------------------------------------------------------ |
| Prioridad: Alta                                                        | <p>Historia de usuario:</p><p>Se requiere poder obtener la información del usuario para poder mostrar que datos registro. </p> |
| Estimado: 5 puntos                                                     |                                                                                                                                |
| Módulo: Usuario                                                        |                                                                                                                                |
| Criterios de Aceptación:                                               |                                                                                                                                |
| El servicio debe retornar la información del usuario que está logueado |                                                                                                                                |
|                                                                        |                                                                                                                                |
|                                                                        |                                                                                                                                |
| Ruta:                                                                  | /usuario/infoUsuario                                                                                                           |
| Método:                                                                | GET                                                                                                                            |
| Formato de entrada: JSON                                               |                                                                                                                                |
|                                                                        |                                                                                                                                |

## Header:

<table>
     <tr><td> <b> Atributo </b></td> <td> <b> Tipo </b></td> <td> <b>Descripcion</b> </td> </tr>
     <tr> <td>Content type</td> <td>Header</td> <td>application/json</td>
     </tr>   
     <tr> <td>Authentication</td> <td>Header</td> <td> bearer token </td>
     </tr>    
</table>

| Body         |          |                          |
|:------------ |:-------- |:------------------------ |
| **Atributo** | **Tipo** | **Descripción**          |
| idUser       | number   | valor del id del usuario |
|              |          |                          |
|              |          |                          |

| Formato de salida: JSON                                                  |                            |                                                     |     |
|:------------------------------------------------------------------------ |:-------------------------- |:--------------------------------------------------- |:--- |
| Código de respuesta exitosa: 200                                         |                            |                                                     |     |
| Salida:                                                                  |                            |                                                     |     |
|                                                                          |                            |                                                     |     |
| **Atributo**                                                             | **Tipo**                   | **Descripción**                                     |     |
| Mensaje                                                                  | string                     | La información del usuario se ha devuelto con éxito |     |
|                                                                          |                            |                                                     |     |
|                                                                          |                            |                                                     |     |
| Código de respuesta fallida:                                             |                            |                                                     |     |
| Se utilizará la siguiente lista de errores como referencia:              |                            |                                                     |     |
| <https://learn.microsoft.com/es-es/partner-center/developer/error-codes> |                            |                                                     |     |
|                                                                          |                            |                                                     |     |
| **Código**                                                               | **Descripción**            |                                                     |     |
| 400                                                                      | Fallo en el proceso        |                                                     |     |
| 500                                                                      | Fallo interno del servidor |                                                     |     |

| Body de Salida                                                                                                                                                                                                                             |
|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|
| **Tipo**                                                                                                                                                                                                                                   |
| String                                                                                                                                                                                                                                     |
| **Descripción**                                                                                                                                                                                                                            |
| Muestra el detalle del servicio realizado                                                                                                                                                                                                  |
| **Atributo**                                                                                                                                                                                                                               |
| Mensaje                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                            |
| Ejemplo de parámetros de entrada                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                            |
| <p>{</p><p>"idUser":"25"}</p>                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                            |
| Ejemplo de parámetros de salida exitosa                                                                                                                                                                                                    |
| <p>{</p><p>"status":200,</p><p>"datos": "{'cui': '3307689530101',</p><p>"primer_nombre": "Javier",</p><p>"segundo_nombre": "luis",</p><p>"primer_apellido": "López",</p><p>"segundo_apellido": "López",</p><p>"correo": "val@gmail.com"}"} |
|                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                            |
| Ejemplo de parámetros de salida fallida                                                                                                                                                                                                    |
| <p>{</p><p>"status": 400,</p><p>"mensaje": “Ha ocurrido un error en la obtención de datos”</p><p>}</p>                                                                                                                                     |
|                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                            |


## [Regresar al Contrato](../servicio_usuario.md)