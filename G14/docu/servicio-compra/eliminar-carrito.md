# Eliminar productos de carrito:

> Microservicio que elimina un producto de un carrito de compras. 

| **ID**:021                                                                                            | **Nombre**: Eliminar productos de carrito de compras                                   |
|:----------------------------------------------------------------------------------------------------- |:-------------------------------------------------------------------------------------- |
| **Prioridad**: Baja                                                                                   | **Historia de usuario**: El usuario podrá quitar un producto de su carrito de compras. |
| **Estimado**: 3                                                                                       |                                                                                        |
| **Módulo**: Compra                                                                                    |                                                                                        |
| **Criterios de Aceptación**: Se enviará el Código de producto para eliminarlo del carrito de compras. |                                                                                        |
| Ruta:                                                                                                 | /api/Carrito?CodigoCarrito=12&Sku=10                                                   |
| Método:                                                                                               | DELETE                                                                                 |
| Formato de entrada:                                                                                   | JSON                                                                                   |

| Header:        |          |                  |
|:-------------- |:-------- |:---------------- |
| **Atributo**   | **Tipo** | **Descripción**  |
| Content type   | Header   | application/json |
| Authentication | Header   | token <TOKEN>    |

| Body         |          |                 |
|:------------:|:--------:|:---------------:|
| **Atributo** | **Tipo** | **Descripción** |
| N/A          | N/A      | N/A             |

| Parámetros    |          |                                               |
|:-------------:|:--------:|:---------------------------------------------:|
| **Atributo**  | **Tipo** | **Descripción**                               |
| CodigoCarrito | Entero   | Código de carrito                             |
| Sku           | Entero   | Código de producto que se elimina del carrito |

| Formato de salida: JSON                                                  |                            |                                                                                 |     |
|:------------------------------------------------------------------------ |:-------------------------- |:------------------------------------------------------------------------------- |:--- |
| Código de respuesta exitosa: HTTP 200                                    |                            |                                                                                 |     |
| Salida:                                                                  |                            |                                                                                 |     |
| **Atributo**                                                             | **Tipo**                   | **Descripción**                                                                 |     |
| status                                                                   | Entero                     | Código de respuesta del servidor                                                |     |
| Mensaje                                                                  | Cadena                     | Mensaje de respuesta del servidor                                               |     |
| Data                                                                     | Arreglo                    | Aquí ira toda la información, que devuelva el servidor al devolver una petición |     |
| Código de respuesta fallida:                                             |                            |                                                                                 |     |
| Se utilizará la siguiente lista de errores como referencia:              |                            |                                                                                 |     |
| <https://learn.microsoft.com/es-es/partner-center/developer/error-codes> |                            |                                                                                 |     |
| **Código**                                                               | **Descripción**            |                                                                                 |     |
| 400                                                                      | Solicitud incorrecta       |                                                                                 |     |
| 401                                                                      | No autorizado              |                                                                                 |     |
| 500                                                                      | Fallo interno del servidor |                                                                                 |     |

| Body de Salida |          |                                           |
|:--------------:|:--------:|:-----------------------------------------:|
| **Atributo**   | **Tipo** | **Descripción**                           |
| Codigo         | Entero   | Código de salida devuelto por el servidor |
| Mensaje        | String   | Mensaje que indica que hubo un error      |

| Ejemplo de parámetros de entrada |     |     |
|:--------------------------------:|:---:|:---:|
| N/A                              |     |     |

| Ejemplo de parámetros de salida exitosa |     |
|:---------------------------------------:|:---:|

```json
{
    "status":200,
    "Mensaje":"Eliminación de producto de carrito exitoso",
    "Data":[ ]
}
```

| Ejemplo de parámetros de salida fallida |     |
|:---------------------------------------:|:---:|

```json
{
    "status":400,
    "Mensaje":"Solicitud incorrecta"
}

{
    "status":401,
    "Mensaje":"No autorizado"
}

{
    "status":500,
    "Mensaje":"Error interno en el servidor"
}
```
## [Regresar al Contrato](../servicio_compra.md)