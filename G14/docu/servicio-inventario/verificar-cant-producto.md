# Verificación de cantidad de producto

| **ID**:                                                                         | **Nombre**: Verificación de cantidad de producto                                      |
|:------------------------------------------------------------------------------- |:------------------------------------------------------------------------------------- |
| **Prioridad**: Media                                                            | **Historia de usuario**:  el usuario quiere obtener la cantidad de productos en stock |
| **Estimado**: 2                                                                 |                                                                                       |
| **Módulo**: Inventario                                                          |                                                                                       |
| <p>**Criterios de Aceptación**: el retorna la cantidad en stock de del producto |                                                                                       |
| Ruta:                                                                           | /inventario/getstock/:skusku                                                          |
| Método:                                                                         | GET                                                                                   |
| Formato de entrada:                                                             | JSON                                                                                  |

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
     <tr><td> <b> Atributo </b></td> <td> <b> Tipo </b></td> <td> <b>Descripcion</b> </td> </tr>

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
| stock                                                                    | Entero                     | stock disponible                  |     |
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

```
/inventario/getstock/25
```

Ejemplo de parámetros de salida exitosa

```json
{
    "status":200,
    "Mensaje":"datos obtenidos",
    "stock":25
}
```

Ejemplo de parámetros de salida fallida

```json
{
    "status":500,
    "Mensaje":"Error interno en el servidor"
}
```

## [Regresar al índice](../servicio_inventario.md)