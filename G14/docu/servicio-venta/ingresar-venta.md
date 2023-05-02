# Ingresar Venta:

## Microservicio que ingresa la venta para despues confirmarla

| **ID**:017                                                                                                                                                                                                                                                                                                         | **Nombre**: Ingresar Venta                                                                                                                                                                                            |
|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Prioridad**:Media                                                                                                                                                                                                                                                                                                | **Historia de usuario**: El cliente necesita ingresar su compra de productos, para que se vaya a una cola de confirmación (Esto solo si la compra es empresarial), si es una compra normal la venta se realiza normal |
| **Estimado**:5                                                                                                                                                                                                                                                                                                     |                                                                                                                                                                                                                       |
| **Módulo**: Venta                                                                                                                                                                                                                                                                                                  |                                                                                                                                                                                                                       |
| **Criterios de Aceptación**: El cliente hara una compra de producto, el cual presionara un boton para que ingrese en una cola  hasta la confirmacion de la compra por un usuario administrador (si es empresarial), de lo contrario hace la compra directamente, se necesita estar registrado para hacer la compra |                                                                                                                                                                                                                       |
| Ruta:                                                                                                                                                                                                                                                                                                              | /api/Venta                                                                                                                                                                                                            |
| Método:                                                                                                                                                                                                                                                                                                            | POST                                                                                                                                                                                                                  |
| Formato de entrada:                                                                                                                                                                                                                                                                                                | JSON                                                                                                                                                                                                                  |

| Header:        |          |                  |
|:-------------- |:-------- |:---------------- |
| **Atributo**   | **Tipo** | **Descripción**  |
| Content type   | Header   | application/json |
| Authentication | header   | token            |

| Body          |          |                                                     |
|:-------------:|:--------:|:---------------------------------------------------:|
| **Atributo**  | **Tipo** | **Descripción**                                     |
| Total         | Decimal  | El total de una compra de productos                 |
| CodigoCarrito | Entero   | Código de carrito de compras                        |
| TipoVenta     | Entero   | Codigo de tipo de venta: 1. Empresarial , 2. Normal |

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
| 202                                                                      | Usuario no registrado      |                                                                                 |     |
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
    "Total":10000.00,
    "CodigoCarrito":12
}
```

| Ejemplo de parámetros de salida exitosa |     |
|:---------------------------------------:|:---:|

```json
{
    "status":200,
    "Mensaje":"Compra exitosa",
    "Data":[ ]
}
```

| Ejemplo de parámetros de salida fallida |     |
|:---------------------------------------:|:---:|

```json
{
    "status":202,
    "Mensaje":"Usuario no registrado"
}

{
    "status":400,
    "Mensaje":"Solicitud incorrecta"
}

{
    "status":400,
    "Mensaje":"Solicitud incorrecta"
}

{
    "status":500,
    "Mensaje":"Error interno en el servidor"
}
```

## [Regresar al Contrato](../servicio_venta.md)