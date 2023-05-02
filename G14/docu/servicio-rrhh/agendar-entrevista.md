# Agendar Entrevista

| **ID**:                                                                                                                    | **Nombre**: Agendar Entrevista                                                         |
|:-------------------------------------------------------------------------------------------------------------------------- |:------------------------------------------------------------------------------------ |
| **Prioridad**: Media                                                                                                       | **Historia de usuario**: Agendar una entrevista para la contratación de un empleado. |
| **Estimado**: 3                                                                                                            |                                                                                      |
| **Módulo**: Recursos Humanos                                                                                               |                                                                                      |
| <p>**Criterios de Aceptación**: si el proceso se realizó con exito, se debe de agendar la entrevista para la contratación. |                                                                                      |
| Ruta:                                                                                                                      | /rrhh/agendarEmpleado                                                                |
| Método:                                                                                                                    | POST                                                                                 |
| Formato de entrada:                                                                                                        | JSON                                                                                 |

## Header:

<table>
     <tr><td> <b> Atributo </b></td> <td> <b> Tipo </b></td> <td> <b>Descripcion</b> </td> </tr>
     <tr> <td>Content type</td> <td>Header</td> <td>application/json</td>
     </tr>   
     <tr> <td>Authentication</td> <td>Header</td> <td> bearer token </td>
     </tr>    
</table>

## Body:

<table>
    <tr>
        <td><b> Atributo </b></td>
        <td><b> Tipo </b></td>
        <td><b>Descripcion</b></td>
    </tr>
    <tr>
       <td>hora</td>
       <td>String</td>
       <td>Hora en la que se realizará la entrevista</td>
    </tr>
    <tr>
       <td>fecha</td>
       <td>String</td>
       <td>Fecha en la que se realizará la entrevista</td>
    </tr>
    <tr>
       <td>id_empelado</td>
       <td>Number</td>
       <td>Empleado de recursos humanos que realizará la entrevista</td>
    </tr>
    <tr>
       <td>nombre</td>
       <td>String</td>
       <td>Nombre del empleado de la entrevista</td>
    </tr>
    <tr>
       <td>email</td>
       <td>String</td>
       <td>Correo del empleado de la entrevista</td>
    </tr>
    <tr>
       <td>telefono</td>
       <td>String</td>
       <td>Teléfono del empleado de la entrevista</td>
    </tr>
</table>

## Parámetros:

<table>
     <tr><td> <b> Atributo </b></td> <td> <b> Tipo </b></td> <td> <b>Descripcion</b> </td> </tr>
     <tr> <td> N/A </td> <td>N/A</td> <td>N/A</td>
     </tr>    
</table>

| Formato de salida: JSON                                                  |                            |                                   |     |
|:------------------------------------------------------------------------ |:-------------------------- |:--------------------------------- |:--- |
| Código de respuesta exitosa: HTTP 200                                    |                            |                                   |     |
| Salida:                                                                  |                            |                                   |     |
| **Atributo**                                                             | **Tipo**                   | **Descripción**                   |     |
| status                                                                   | Entero                     | Código de respuesta del servidor  |     |
| Mensaje                                                                  | String                     | Mensaje de respuesta del servidor |     |
| Código de respuesta fállida:                                             |                            |                                   |     |
| Se utilizará la siguiente lista de errores como referencia:              |                            |                                   |     |
| <https://learn.microsoft.com/es-es/partner-center/developer/error-codes> |                            |                                   |     |
| **Código**                                                               | **Descripción**            |                                   |     |
| 400                                                                      | Solicitud incorrecta       |                                   |     |
| 401                                                                      | No autorizado              |                                   |     |
| 500                                                                      | Fallo interno del servidor |                                   |     |

| Body de Salida                    |          |                                           |     |
|:--------------------------------- |:-------- |:----------------------------------------- |:--- |
| **Atributo**                      | **Tipo** | **Descripción**                           |     |
| Codigo                            | Entero   | Código de salida devuelto por el servidor |     |
| Mensaje                           | String   | Mensaje que indica que hubo un error      |     |
| Ejemplo de parámetros de entrada: |          |                                           |     |

```JSON
{
    "hora": "10:20",
    "hora": "25/02/2023",
    "id_empelado": 10,
    "nombre": "Leonardo Martínez",
    "email": "correo@example.com",
    "telefono": "+502 01010 - 01010"
}
```

Ejemplo de parámetros de salida exitosa

```JSON
{
    "status":200,
    "Mensaje":"Se agendó la entrevista correctamente",
}
```

Ejemplo de parámetros de salida fallida

```JSON
{
    "status":400,
    "Mensaje":"Error al agendar la entrevista"
}
```
## [Regresar al Contrato](../servicio_recursos_humanos.md)