# Agregar al carrito:

> El usuario podrá ingresar sus productos a un carrito de compras.

| **ID**:018                                                                                                                                                           | **Nombre**: Agregar al carrito                                                                                                            |
|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------- |:----------------------------------------------------------------------------------------------------------------------------------------- |
| **Prioridad**:Alta                                                                                                                                                   | **Historia de usuario**: El usuario tendrá una opción para agregar todos los productos que desee a un carrito para luego, poder comprarlo |
| **Estimado**:5                                                                                                                                                       |                                                                                                                                           |
| **Módulo**: Compra                                                                                                                                                   |                                                                                                                                           |
| **Criterios de Aceptación**: El Usuario al navegar a tráves del catálogo de productos podrá agregarlo a un carrito de compras para tener la oportunidad de comprarlo |                                                                                                                                           |
| Ruta:                                                                                                                                                                | /api/compra/carrito                                                                                                                       |
| Método:                                                                                                                                                              | POST                                                                                                                                      |
| Formato de entrada:                                                                                                                                                  | JSON                                                                                                                                      |

| Header:        |          |                  |
|:-------------- |:-------- |:---------------- |
| **Atributo**   | **Tipo** | **Descripción**  |
| Content type   | Header   | application/json |
| Authentication | header   | token <TOKEN>    |

| Body         |          |                                                                               |
|:------------:|:--------:|:-----------------------------------------------------------------------------:|
| **Atributo** | **Tipo** | **Descripción**                                                               |
| "Productos"  | Arreglo  | Arreglo donde se guardará los datos de los productos que se añaden al carrito |
| "SKU"        | Entero   | Código de producto a agregar al carrito                                       |
| "Cantidad"   | Entero   | Cantidad del producto que desea comprar                                       |

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

| Body de Salida |          |                                           |
|:--------------:|:--------:|:-----------------------------------------:|
| **Atributo**   | **Tipo** | **Descripción**                           |
| Codigo         | Entero   | Código de salida devuelto por el servidor |
| Mensaje        | String   | Mensaje que indica que hubo un error      |

| Ejemplo de parámetros de entrada |     |
|:--------------------------------:|:---:|

```json
{
    "Productos":[
                {
                    "Sku": 10,
                    "Cantidad":20
                } ,
                {
                    "Sku": 11,
                    "Cantidad": 50
                } 
            ]
}
```

| Ejemplo de parámetros de salida exitosa |     |
|:---------------------------------------:|:---:|

```json
{
    "status":200,
    "Mensaje":"Ingreso de carrito exitoso",
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
