# Actualizar producto

| **ID**:                                                                                                     | **Nombre**: Actualización de producto                                               |
|:----------------------------------------------------------------------------------------------------------- |:----------------------------------------------------------------------------------- |
| **Prioridad**: Media                                                                                        | **Historia de usuario**: se quiere modificar o actualizar los productos registrados |
| **Estimado**: 2                                                                                             |                                                                                     |
| **Módulo**: Inventario                                                                                      |                                                                                     |
| <p>**Criterios de Aceptación**: El servicio debe de retornar que la actualización se hizo sin ningún error. |                                                                                     |
| Ruta:                                                                                                       | /inventario/modproducto                                                             |
| Método:                                                                                                     | PUT                                                                                 |
| Formato de entrada:                                                                                         | JSON                                                                                |

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
     <tr> <td>nombre</td> <td>Sting</td> <td>nombre del producto</td>
     </tr>   
     <tr> <td>precio</td> <td>Decimal</td> <td> precio del producto </td>
     </tr> 
          <tr> <td>costo</td> <td>Decimal</td> <td> Costo del producto </td>
     </tr>       
          <tr> <td>stock</td> <td>Entero</td> <td> stock del producto </td>
     </tr>   
     <tr> <td>idcategoria</td> <td>Entero</td> <td> Categoria que pertenece el producto </td>
     </tr>  
    <tr> <td>idproducto</td> <td>Entero</td> <td> id interno del producto </td>
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

```json
{
    "nombre": "Pizza peperoni",
    "idcategoria": 3,
    "precio": 275,
    "costo": 200,
    "stock": 10,
    "idproducto": 2
}
```

Ejemplo de parámetros de salida exitosa

```json
{
    "status":200,
    "Mensaje":"se actualizó registro correctamente",
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