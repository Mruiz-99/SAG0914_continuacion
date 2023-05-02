# Eliminar Personal

<!--########################################################################################################## -->

| **ID**:                                                                                     | **Nombre**: Eliminar Personal                                                 |
|:------------------------------------------------------------------------------------------- |:----------------------------------------------------------------------------- |
| **Prioridad**: Media                                                                        | **Historia de usuario**: Eliminar un registro de un empleado en la plantilla. |
| **Estimado**: 3                                                                             |                                                                               |
| **Módulo**: Recursos Humanos                                                                |                                                                               |
| <p>**Criterios de Aceptación**: si el proceso se realizó con exito, se  elimina el empleado |                                                                               |
| Ruta:                                                                                       | /rrhh/eliminarEmpleado                                                        |
| Método:                                                                                     | DELETE                                                                        |
| Formato de entrada:                                                                         | JSON                                                                          |

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
       <td>id_empleado</td>
       <td>Number</td>
       <td>Correlativo del empleado</td>
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
    "id_empleado": 10,
}
```

Ejemplo de parámetros de salida exitosa

```JSON
{
    "status":200,
    "Mensaje":"Se eliminó el empleado correctamente",
}
```

Ejemplo de parámetros de salida fallida

```JSON
{
    "status":400,
    "Mensaje":"Error al eliminar el empleado"
}
```



## [Regresar al Contrato](../servicio_recursos_humanos.md)