# Registro Compra Externa:

> Microservicio que Registra una compra externa. 

| **ID**:021                                                                                                                             | **Nombre**: Registro de compra externa                                                                                                                                              |
|:-------------------------------------------------------------------------------------------------------------------------------------- |:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Prioridad**: Alta                                                                                                                    | **Historia de usuario**: Es necesario poder registrar la transacción de compra realizada por un sistema externo (previo a esto la compra debió ser autorizada por el administrador) |
| **Estimado**: 3                                                                                                                        |                                                                                                                                                                                     |
| **Módulo**: Compra                                                                                                                     |                                                                                                                                                                                     |
| **Criterios de Aceptación**: Luego de que el administrador autorice la compra externa, el sistema registrará la transacción realizada. |                                                                                                                                                                                     |
| Ruta:                                                                                                                                  | /carrito/registro-externo                                                                                                                                                           |
| Método:                                                                                                                                | POST                                                                                                                                                                                |
| Formato de entrada:                                                                                                                    | JSON                                                                                                                                                                                |

| Header:        |          |                  |
|:-------------- |:-------- |:---------------- |
| **Atributo**   | **Tipo** | **Descripción**  |
| Content type   | Header   | application/json |
| Authentication | Header   | token <TOKEN>    |

| Body            |          |                                                                         |
|:---------------:|:--------:|:-----------------------------------------------------------------------:|
| **Atributo**    | **Tipo** | **Descripción**                                                         |
| Fecha           | Date     | Fecha cuando se autorizó la venta con el siguiente formato "YYYY-MM-DD" |
| Productos       | Array    | Arreglo de objetos JSON con informacion de los productos                |
| Sku             | Entero   | identificador único del producto seleccionado.                          |
| cantidad        | Entero   | Cantidad deseada del producto seleccionado.                             |
| precio_unitario | decimal  | Precio unitario al cual se compró el producto.                          |

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

```json
{
    "Fecha":"2023-02-12",
    "productos":[
        {
            "Sku":3,
            "cantidad":10,
            "precio_unitario":10
        },
        {
            "Sku":5,
            "cantidad":2,
            "precio_unitario":10
        }
    ]
}
```

| Ejemplo de parámetros de salida exitosa |     |
|:---------------------------------------:|:---:|

```
{
    "status":201,
    "Mensaje":"Transacción realizada con éxito"
}
```

| Ejemplo de parámetros de salida fallida |     |
|:---------------------------------------:|:---:|

```json
{
    "status":400,
    "Mensaje":"Formato invalido"
}

{
    "status":401,
    "Mensaje":"Token no válido"
}

{
    "status":500,
    "Mensaje":"Error interno en el servidor"
}
```

| Ejemplo de parámetros de token |     |
|:------------------------------:|:---:|

```json
{
    "id_grupo":<identificador de la tienda que nos vendió los productos>,
    "Mensaje":<Sección de la tienda de la tienda que nos vendió los productos>
}
```

## [Regresar al Contrato](../servicio_compra.md)