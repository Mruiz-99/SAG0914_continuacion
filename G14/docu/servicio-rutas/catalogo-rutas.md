# Catálogo de rutas de entrega

<!--########################################################################################################## -->

| **ID**:                         | **Nombre**: Catálogo de Rutas de Entrega                                                                  |
|:------------------------------- |:--------------------------------------------------------------------------------------------------------- |
| **Prioridad**: Media            | **Historia de usuario**: Mostrar todas las locaciones de entrega pendientes que estén cerca del empleado. |
| **Estimado**: 4                 |                                                                                                           |
| **Módulo**: Rutas               |                                                                                                           |
| <p>**Criterios de Aceptación**: | Si la petición fue procesada con éxito                                                                    |
| Ruta:                           | /rutas/catalogo/<id_locacion>                                                                             |
| Método:                         | GET                                                                                                       |
| Formato de entrada:             | JSON                                                                                                      |

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
       <td>N/A</td>
       <td>N/A</td>
       <td>N/A</td>
    </tr>
</table>

## Parámetros:

<table>
     <tr>
        <td><b> Atributo </b></td>
        <td><b> Tipo </b></td>
        <td><b>Descripcion</b></td>
    </tr>
    <tr>
       <td>id_locacion</td>
       <td>Number</td>
       <td>Identificador del lugar o ciudad del empleado</td>
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
    // Ninguno
}
```

Ejemplo de parámetros de salida exitosa

```JSON
{
    "status":200,
    "rutas":[
        {
            "id_ruta": 22,
            "id_cliente": 12,
            "destino": "Coordenadas o lugar de destino",        
        }
        //...
    ],
}
```

Ejemplo de parámetros de salida fallida

```JSON
{
    "status":400,
    "Mensaje":"Error al agregar el empleado"
}
```

## [Regresar al Contrato](../servicio_rutas.md)