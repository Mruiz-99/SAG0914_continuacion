# Obtener carrito:

> Microservicio que devuelve los productos que se ingresaron en un carrito de compras.

| **ID**:019                                                                                                                                                                                                                                     | **Nombre**: Obtener carrito                                                                                                       |
|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |:--------------------------------------------------------------------------------------------------------------------------------- |
| **Prioridad**:Media                                                                                                                                                                                                                            | **Historia de usuario**: El usuario podrá obtener el carrito de compra para poder modificarlo con los datos pendientes de comprar |
| **Estimado**:3                                                                                                                                                                                                                                 |                                                                                                                                   |
| **Módulo**: Compra                                                                                                                                                                                                                             |                                                                                                                                   |
| **Criterios de Aceptación**: El usuario podría obtener los datos de los productos que estuvo pendiente de comprar y se encuentra en el carrito de compras, el usuario debe estar logueado para poder ingresar productos al carrito de compras. |                                                                                                                                   |
| Ruta:                                                                                                                                                                                                                                          | /api/compra/carrito                                                                                                               |
| Método:                                                                                                                                                                                                                                        | GET                                                                                                                               |
| Formato de entrada:                                                                                                                                                                                                                            | JSON                                                                                                                              |

| Header:        |          |                  |
|:-------------- |:-------- |:---------------- |
| **Atributo**   | **Tipo** | **Descripción**  |
| Content type   | Header   | application/json |
| Authentication | header   | token <TOKEN>    |

| Body         |          |                 |
|:------------:|:--------:|:---------------:|
| **Atributo** | **Tipo** | **Descripción** |
| N/A          | N/A      | N/A             |

| Parámetros   |          |                 |
|:------------:|:--------:|:---------------:|
| **Atributo** | **Tipo** | **Descripción** |
| N/A          | N/A      | N/A             |

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

| Body de Salida |          |                                                  |
|:--------------:|:--------:|:------------------------------------------------:|
| **Atributo**   | **Tipo** | **Descripción**                                  |
| Codigo         | Entero   | Código de salida devuelto por el servidor        |
| Mensaje        | Cadena   | Mensaje que indica que hubo un error             |
| Data           | Arreglo  | Arreglo con los datos devueltos                  |
| CodigoCarrito  | Entero   | Codigo de carrito                                |
| Productos      | Arreglo  | Arreglo con los datos de producto devueltos      |
| Sku            | Entero   | Codigo del producto                              |
| Nombre         | Cadena   | Nombre del producto                              |
| Cantidad       | Entero   | Cantidad de productos agregados al carrito       |
| Precio         | Decimal  | Precio del producto (cantidad * precio unitario) |

| Ejemplo de parámetros de entrada |     |
|:--------------------------------:|:---:|
| N/A                              |     |

| Ejemplo de parámetros de salida exitosa |     |
|:---------------------------------------:|:---:|

```json
{
    "status":200,
    "Mensaje":"Obtención de carrito exitoso",
    "Data":[
                CodigoCarrito: 1,
                Productos:[
                    {
                        "Sku": 10,
                        "Nombre": "Shampoo palmolive",
                        "Cantidad":20,
                        "Precio": 410.00
                    } ,
                    {
                        "Sku": 11,
                        "Nombre": "Jabon harmony",
                        "Cantidad": 5,
                        "Precio": 25.00
                    }
                ]
            ]
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
    "Mensaje":"No Autorizado"
}

{
    "status":500,
    "Mensaje":"Error interno en el servidor"
}
```


## [Regresar al Contrato](../servicio_compra.md)