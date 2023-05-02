# Actualización de entrega


| **ID**:                                                                    | **Nombre**: Actualización de Entrega                           |
|:-------------------------------------------------------------------------- |:-------------------------------------------------------------- |
| **Prioridad**: Media                                                       | **Historia de usuario**: Actualizar el estatus de una entrega. |
| **Estimado**: 3                                                            |                                                                |
| **Módulo**: Rutas                                                          |                                                                |
| <p>**Criterios de Aceptación**: si se realizaron los cambios a la entrega. |                                                                |
| Ruta:                                                                      | /rutas/entregaCrear                                            |
| Método:                                                                    | POST                                                           |
| Formato de entrada:                                                        | JSON                                                           |

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
       <td>id_entrega</td>
       <td>number</td>
       <td>Identificador de la entrega a realizar</td>
    </tr>
    <tr>
       <td>id_ruta</td>
       <td>number</td>
       <td>Identificador de la ruta que se realizó</td>
    </tr>
    <tr>
       <td>id_empleado</td>
       <td>number</td>
       <td>Identificador del empleado que realizó la entrega</td>
    </tr>
    <tr>
       <td>id_cliente</td>
       <td>number</td>
       <td>Identificacdor del cliente al que se realiza la entrega</td>
    </tr>
    <tr>
       <td>estatus</td>
       <td>String</td>
       <td>Estatus de la entrega</td>
    </tr>
</table>

### Parámetros:

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
    "id_entrega": 17832,
    "id_ruta": 213,
    "id_empleado": 2031,
    "id_cliente": 132,
    "estatus": "En Proceso"
}
```

Ejemplo de parámetros de salida exitosa

```JSON
{
    "status":200,
    "Mensaje":"Se actualizó la entrega correctamente",
}
```

Ejemplo de parámetros de salida fallida

```JSON
{
    "status":400,
    "Mensaje":"Error al actualizar la entrega."
}
```

## [Regresar al Contrato](../servicio_rutas.md)