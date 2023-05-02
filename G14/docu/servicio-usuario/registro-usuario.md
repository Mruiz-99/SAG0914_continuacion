# Registro de usuario

# Descripción del microservicio

Microservicio necesario para el registro de datos de un nuevo usuario.

| ID:002                                                                                                     | Nombre: Registro de usuario                                                                                                                        |
|:---------------------------------------------------------------------------------------------------------- |:-------------------------------------------------------------------------------------------------------------------------------------------------- |
| Prioridad:  Alta                                                                                           | <p>Historia de usuario:</p><p>Se requiere registrar usuarios para poder ser logueados en la aplicación y ser registrados en la base de datos. </p> |
| Estimado: 5 puntos                                                                                         |                                                                                                                                                    |
| Módulo: Usuario                                                                                            |                                                                                                                                                    |
| Criterios de Aceptación:                                                                                   |                                                                                                                                                    |
| <p>El servicio debe retornar el usuario registrado </p><p>El servicio tiene la siguiente configuración</p> |                                                                                                                                                    |
|                                                                                                            |                                                                                                                                                    |
|                                                                                                            |                                                                                                                                                    |
| Ruta:                                                                                                      | /usuario/addUsuario                                                                                                                                |
| Método:                                                                                                    | POST                                                                                                                                               |
| Formato de entrada: JSON                                                                                   |                                                                                                                                                    |
|                                                                                                            |                                                                                                                                                    |
|                                                                                                            |                                                                                                                                                    |

## Header:

<table>
     <tr><td> <b> Atributo </b></td> <td> <b> Tipo </b></td> <td> <b>Descripcion</b> </td> </tr>
     <tr> <td>Content type</td> <td>Header</td> <td>application/json</td>
     </tr>      
</table>

| Body             |          |                                    |
|:---------------- |:-------- |:---------------------------------- |
| **Atributo**     | **Tipo** | **Descripción**                    |
| cui              | string   | nombre del usuario del cliente     |
| primer_nombre    | string   | primer nombre del usuario          |
| segundo_nombre   | string   | segundo nombre del usuario         |
| primer_apellido  | string   | primer apellido del usuario        |
| segundo_apellido | string   | segundo apellido del usuario       |
| contra           | string   | contraseña del usuario del cliente |
| correo           | string   | correo del usuario                 |
|                  |          |                                    |

| Body de Salida                                                                                                                                                                                                                           |
|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|
| **Tipo**                                                                                                                                                                                                                                 |
| String                                                                                                                                                                                                                                   |
| **Descripción**                                                                                                                                                                                                                          |
| Muestra el detalle del servicio realizado                                                                                                                                                                                                |
| **Atributo**                                                                                                                                                                                                                             |
| -------------------------------------------------------------------------------------------------------                                                                                                                                  |
| Mensaje                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                          |
| Ejemplo de parámetros de entrada                                                                                                                                                                                                         |
| <p>{</p><p>"cui": "3001629780101",</p><p>"contra": "passUsu",</p><p>"primer_nombre": "Javier",</p><p>"segundo_nombre": "luis",</p><p>"primer_apellido": "López",</p><p>"segundo_apellido": "López",</p><p>"correo": "val@gmail.com"}</p> |
|                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                          |
| Ejemplo de parámetros de salida exitosa                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                          |
| Ejemplo de parámetros de salida fallida                                                                                                                                                                                                  |
| <p>{</p><p>"status":200,</p><p>"mensaje: “usuario 33007629530101 correctamente registrado”</p><p>}</p>                                                                                                                                   |
| <p>{</p><p>"status": 400,</p><p>"mensaje": “Ha ocurrido un error en el ingreso del usuario”</p><p>}</p>                                                                                                                                  |
|                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                          |



## [Regresar al Contrato](../servicio_usuario.md)