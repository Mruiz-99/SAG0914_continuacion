# [SA] PROYECTO FASE 1

**Software Avanzado, sección N**
**GRUPO 9**

| Carnet    | Nombre                     | Porcentaje de trabajo |
| --------- | -------------------------- | --------------------- |
| 201531166 | Maynor Octavio Piló Tuy    | 100%                  |
| 201801329 | Mynor Rene Ruiz Guerra     | 100%                  |
| 201806838 | Elian Saúl Estrada Urbina  | 100%                  |
| 20180098  | Alex Fernando Méndez López | 100%                  |

---

## Comunicación de los servicios disponibles para todos los grupos.
<div align="left">
    <table>
        <tbody>
            <tr>
                <td>
                    <p>ID:&nbsp;1</p>
                </td>
                <td>
                    <p>Nombre:&nbsp;Recepci&oacute;n de productos</p>
                </td>
            </tr>
            <tr>
                <td>
                    <p>Prioridad:&nbsp;alta</p>
                </td>
                <td rowspan="3">
                    <p>HISTORIA DE USUARIO</p>
                    <p>Es importante como tienda realizar el aumento de inventario o la agregaci&oacute;n de productos nuevos con su cantidad de inventario inicial al inventario, al comprar productos a una tienda externa a trav&eacute;s de un usuario empresarial dentro de su p&aacute;gina web.</p>
                </td>
            </tr>
            <tr>
                <td>
                    <p>Estimado: 8 puntos</p>
                </td>
            </tr>
            <tr>
                <td>
                    <p>M&oacute;dulo:&nbsp;Inventario</p>
                </td>
            </tr>
            <tr>
                <td colspan="2">
                    <p>Criterios de Aceptaci&oacute;n:</p>
                    <p>Una vez realizada la entrega de productos por ruta, se actualizar&aacute; el inventario de la tienda agregando la cantidad de productos enviados en la commanda.</p><br><br>
                    <p>Ruta:&nbsp; /inventario/recepcion</p>
                    <p>M&eacute;todo:&nbsp;PUT</p>
                </td>
            </tr>
            <tr>
                <td colspan="2">
                    <p>Formado de entrada:&nbsp;JSON</p><br>
                    <p>Header:&nbsp;</p><br>
                    <div align="left">
                        <table>
                            <tbody>
                                <tr>
                                    <td>
                                        <p>Atributo</p>
                                    </td>
                                    <td>
                                        <p>Tipo</p>
                                    </td>
                                    <td>
                                        <p>Descripci&oacute;n</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>Content-Type</p>
                                    </td>
                                    <td>
                                        <p>header</p>
                                    </td>
                                    <td>
                                        <p>application/json</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>Authorization</p>
                                    </td>
                                    <td>
                                        <p>header</p>
                                    </td>
                                    <td>
                                        <p>Bearer &lt;token&gt;</p>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div><br>
                    <p>Body:&nbsp;</p><br>
                    <div align="left">
                        <table>
                            <tbody>
                                <tr>
                                    <td>
                                        <p>Atributo</p>
                                    </td>
                                    <td>
                                        <p>Tipo</p>
                                    </td>
                                    <td>
                                        <p>Descripci&oacute;n</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>productos</p>
                                    </td>
                                    <td>
                                        <p>Array</p>
                                    </td>
                                    <td>
                                        <p>Arreglo de Objetos JSON con informaci&oacute;n de los productos</p>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div><br><br>
                    <div align="left">
                        <table>
                            <tbody>
                                <tr>
                                    <td>
                                        <p>Atributo</p>
                                    </td>
                                    <td>
                                        <p>Tipo</p>
                                    </td>
                                    <td>
                                        <p>Descripci&oacute;n</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>SKU</p>
                                    </td>
                                    <td>
                                        <p>int</p>
                                    </td>
                                    <td>
                                        <p>identificador &uacute;nico del producto seleccionado.</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>cantidad</p>
                                    </td>
                                    <td>
                                        <p>int</p>
                                    </td>
                                    <td>
                                        <p>Cantidad deseada del producto seleccionado.</p>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div><br><br>
                </td>
            </tr>
            <tr>
                <td colspan="2">
                    <p>Formado de salida:&nbsp;JSON</p>
                    <p>C&oacute;digo de respuesta exitosa:&nbsp;HTTP&nbsp;200</p><br>
                    <p>Salida:&nbsp;</p><br>
                    <div align="left">
                        <table>
                            <tbody>
                                <tr>
                                    <td>
                                        <p>Atributo</p>
                                    </td>
                                    <td>
                                        <p>Tipo</p>
                                    </td>
                                    <td>
                                        <p>Descripci&oacute;n</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>status</p>
                                    </td>
                                    <td>
                                        <p>int</p>
                                    </td>
                                    <td>
                                        <p>El c&oacute;digo 200 de respuesta exitosa.</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>msg</p>
                                    </td>
                                    <td>
                                        <p>string</p>
                                    </td>
                                    <td>
                                        <p>Indicaci&oacute;n de &eacute;xito sobre la operaci&oacute;n.</p>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div><br>
                    <p>C&oacute;digo de respuesta fallida:&nbsp;</p><br>
                    <div align="left">
                        <table>
                            <tbody>
                                <tr>
                                    <td>
                                        <p>C&oacute;digo</p>
                                    </td>
                                    <td>
                                        <p>Descripci&oacute;n</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>400</p>
                                    </td>
                                    <td>
                                        <p>Datos con formato invalido dentro de la petici&oacute;n.</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>401</p>
                                    </td>
                                    <td>
                                        <p>Credenciales incorrectas dentro del token.</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>404</p>
                                    </td>
                                    <td>
                                        <p>indica que el servidor no pudo encontrar el recurso solicitado</p>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div><br>
                    <p>Body salida:&nbsp;</p><br>
                    <div align="left">
                        <table>
                            <tbody>
                                <tr>
                                    <td>
                                        <p>Atributo</p>
                                    </td>
                                    <td>
                                        <p>Tipo</p>
                                    </td>
                                    <td>
                                        <p>Descripci&oacute;n</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>status</p>
                                    </td>
                                    <td>
                                        <p>int</p>
                                    </td>
                                    <td>
                                        <p>El c&oacute;digo de respuesta fallida</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>msg</p>
                                    </td>
                                    <td>
                                        <p>string</p>
                                    </td>
                                    <td>
                                        <p>mensaje con informaci&oacute;n del error</p>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div><br><br><br>
                </td>
            </tr>
            <tr>
                <td colspan="2">
                    <p>Ejemplos de par&aacute;metros de entrada:&nbsp;&nbsp;</p><br>
                    <p>{</p>
                    <p>&nbsp; &nbsp; &nbsp;productos: [</p>
                    <p>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; {</p>
                    <p>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; sku: 3</p>
                    <p>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; cantidad: 10</p>
                    <p>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;},</p>
                    <p>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; {</p>
                    <p>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; sku: 5</p>
                    <p>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; cantidad: 2</p>
                    <p>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;},</p>
                    <p>&nbsp; &nbsp; &nbsp;]</p>
                    <p>}</p><br><br>
                    <p>Ejemplos de par&aacute;metros de salida exitosa:&nbsp;&nbsp;</p>
                    <p>{</p>
                    <p>&nbsp; &nbsp; &ldquo;status&rdquo;: 200,</p>
                    <p>&nbsp; &nbsp; &ldquo;msg&rdquo;: Stock del producto actualizado<br>}</p><br><br>
                    <p>Ejemplos de par&aacute;metros de salida fallida:&nbsp;&nbsp;</p><br>
                    <p>{</p>
                    <p>&nbsp; &nbsp;&ldquo;status&rdquo;: 400,</p>
                    <p>&nbsp; &nbsp;&ldquo;msg&rdquo;: &ldquo;Formato invalido&rdquo;</p>
                    <p>}</p><br>
                    <p>{</p>
                    <p>&nbsp; &nbsp;&ldquo;status&rdquo;: 401,</p>
                    <p>&nbsp; &nbsp;&ldquo;msg&rdquo;: &ldquo;Token no v&aacute;lido&rdquo;</p>
                    <p>}</p><br>
                    <p>{</p>
                    <p>&nbsp; &nbsp;&ldquo;status&rdquo;: 404,</p>
                    <p>&nbsp; &nbsp;&ldquo;msg&rdquo;: &ldquo;No se encontr&oacute; el recurso solicitado&rdquo;</p>
                    <p>}</p><br>
                    <p>Ejemplos de par&aacute;metros de token</p><br>
                    <p>{</p>
                    <p>&nbsp; &ldquo;id_grupo&rdquo;:&nbsp;&lt;identificador de la tienda que nos vendi&oacute; los productos&gt;</p>
                    <p>&nbsp; &ldquo;seccion&rdquo;:&nbsp;&lt;Seccion de la tienda de la tienda que nos vendi&oacute; los productos&gt;</p>
                    <p>}</p>
                </td>
            </tr>
        </tbody>
    </table>
    <div align="left">
        <table>
            <tbody>
                <tr>
                    <td>
                        <p>ID:&nbsp;02</p>
                    </td>
                    <td>
                        <p>Nombre:&nbsp;Registro de compra externa</p>
                    </td>
                </tr>
                <tr>
                    <td>
                        <p>Prioridad:&nbsp;Alta</p>
                    </td>
                    <td rowspan="3">
                        <p>HISTORIA DE USUARIO</p><br>
                        <p>Es necesario poder registrar la transacci&oacute;n de compra realizada por un sistema externo (previo a esto la compra debi&oacute; ser autorizada por el administrador).</p>
                    </td>
                </tr>
                <tr>
                    <td>
                        <p>Estimado:&nbsp;pendiente por grupo</p>
                    </td>
                </tr>
                <tr>
                    <td>
                        <p>M&oacute;dulo:&nbsp;Compra</p>
                    </td>
                </tr>
                <tr>
                    <td colspan="2">
                        <p>Criterios de Aceptaci&oacute;n:</p>
                        <p>Luego de que el administrador autorice la compra externa, el sistema registrar&aacute; la transacci&oacute;n realizada.</p><br>
                        <p>Ruta:&nbsp;/compra/registro-externo</p>
                        <p>M&eacute;todo:&nbsp;POST</p>
                    </td>
                </tr>
                <tr>
                    <td colspan="2">
                        <p>Formado de entrada:&nbsp;JSON</p><br>
                        <p>Header:&nbsp;</p><br>
                        <div align="left">
                            <table>
                                <tbody>
                                    <tr>
                                        <td>
                                            <p>Atributo</p>
                                        </td>
                                        <td>
                                            <p>Tipo</p>
                                        </td>
                                        <td>
                                            <p>Descripci&oacute;n</p>
                                        </td>
                                    </tr>
                                    <tr>
                                        <td>
                                            <p>Content-Type</p>
                                        </td>
                                        <td>
                                            <p>header</p>
                                        </td>
                                        <td>
                                            <p>application/json</p>
                                        </td>
                                    </tr>
                                    <tr>
                                        <td>
                                            <p>Authorization</p>
                                        </td>
                                        <td>
                                            <p>header</p>
                                        </td>
                                        <td>
                                            <p>Bearer &lt;token&gt;</p>
                                        </td>
                                    </tr>
                                </tbody>
                            </table>
                        </div><br>
                        <p>Body:&nbsp;</p><br>
                        <div align="left">
                            <table>
                                <tbody>
                                    <tr>
                                        <td>
                                            <p>Atributo</p>
                                        </td>
                                        <td>
                                            <p>Tipo</p>
                                        </td>
                                        <td>
                                            <p>Descripci&oacute;n</p>
                                        </td>
                                    </tr>
                                    <tr>
                                        <td>
                                            <p>Fecha</p>
                                        </td>
                                        <td>
                                            <p>Date</p>
                                        </td>
                                        <td>
                                            <p>Fecha cuando se autoriz&oacute; la venta, con el siguiente formato: &ldquo;YYYY-MM-DD&rdquo;.</p>
                                        </td>
                                    </tr>
                                    <tr>
                                        <td>
                                            <p>productos</p>
                                        </td>
                                        <td>
                                            <p>Array</p>
                                        </td>
                                        <td>
                                            <p>Arreglo de Objetos JSON con informaci&oacute;n de los productos</p>
                                        </td>
                                    </tr>
                                </tbody>
                            </table>
                        </div><br><br><br>
                        <div align="left">
                            <table>
                                <tbody>
                                    <tr>
                                        <td>
                                            <p>Atributo</p>
                                        </td>
                                        <td>
                                            <p>Tipo</p>
                                        </td>
                                        <td>
                                            <p>Descripci&oacute;n</p>
                                        </td>
                                    </tr>
                                    <tr>
                                        <td>
                                            <p>SKU</p>
                                        </td>
                                        <td>
                                            <p>int</p>
                                        </td>
                                        <td>
                                            <p>identificador &uacute;nico del producto seleccionado.</p>
                                        </td>
                                    </tr>
                                    <tr>
                                        <td>
                                            <p>cantidad</p>
                                        </td>
                                        <td>
                                            <p>int</p>
                                        </td>
                                        <td>
                                            <p>Cantidad deseada del producto seleccionado.</p>
                                        </td>
                                    </tr>
                                    <tr>
                                        <td>
                                            <p>precio_unitario</p>
                                        </td>
                                        <td>
                                            <p>decimal</p>
                                        </td>
                                        <td>
                                            <p>Precio unitario al cual se compr&oacute; el producto.</p>
                                        </td>
                                    </tr>
                                </tbody>
                            </table>
                        </div><br><br>
                    </td>
                </tr>
                <tr>
                    <td colspan="2">
                        <p>Formado de salida:&nbsp;JSON</p>
                        <p>C&oacute;digo de respuesta exitosa:&nbsp;HTTP 201</p><br>
                        <p>Salida:&nbsp;</p><br>
                        <div align="left">
                            <table>
                                <tbody>
                                    <tr>
                                        <td>
                                            <p>Atributo</p>
                                        </td>
                                        <td>
                                            <p>Tipo</p>
                                        </td>
                                        <td>
                                            <p>Descripci&oacute;n</p>
                                        </td>
                                    </tr>
                                    <tr>
                                        <td>
                                            <p>status</p>
                                        </td>
                                        <td>
                                            <p>INT</p>
                                        </td>
                                        <td>
                                            <p>c&oacute;digo de respuesta exitosa</p>
                                        </td>
                                    </tr>
                                    <tr>
                                        <td>
                                            <p>msg</p>
                                        </td>
                                        <td>
                                            <p>STRING</p>
                                        </td>
                                        <td>
                                            <p>mensaje describiendo la operaci&oacute;n realizada</p>
                                        </td>
                                    </tr>
                                </tbody>
                            </table>
                        </div><br>
                        <p>C&oacute;digo de respuesta fallida:&nbsp;</p><br>
                        <div align="left">
                            <table>
                                <tbody>
                                    <tr>
                                        <td>
                                            <p>C&oacute;digo</p>
                                        </td>
                                        <td>
                                            <p>Descripci&oacute;n</p>
                                        </td>
                                    </tr>
                                    <tr>
                                        <td>
                                            <p>400</p>
                                        </td>
                                        <td>
                                            <p>Datos con formato invalido dentro de la petici&oacute;n.</p>
                                        </td>
                                    </tr>
                                    <tr>
                                        <td>
                                            <p>401</p>
                                        </td>
                                        <td>
                                            <p>Credenciales incorrectas dentro del token.</p>
                                        </td>
                                    </tr>
                                </tbody>
                            </table>
                        </div><br>
                        <p>Body salida:&nbsp;</p><br>
                        <div align="left">
                            <table>
                                <tbody>
                                    <tr>
                                        <td>
                                            <p>Atributo</p>
                                        </td>
                                        <td>
                                            <p>Tipo</p>
                                        </td>
                                        <td>
                                            <p>Descripci&oacute;n</p>
                                        </td>
                                    </tr>
                                    <tr>
                                        <td>
                                            <p>status</p>
                                        </td>
                                        <td>
                                            <p>int</p>
                                        </td>
                                        <td>
                                            <p>El c&oacute;digo de respuesta fallida</p>
                                        </td>
                                    </tr>
                                    <tr>
                                        <td>
                                            <p>msg</p>
                                        </td>
                                        <td>
                                            <p>string</p>
                                        </td>
                                        <td>
                                            <p>mensaje con informaci&oacute;n del error</p>
                                        </td>
                                    </tr>
                                </tbody>
                            </table>
                        </div><br><br><br>
                    </td>
                </tr>
                <tr>
                    <td colspan="2">
                        <p>Ejemplos de par&aacute;metros de entrada:&nbsp;&nbsp;</p><br>
                        <p>{</p>
                        <p>&nbsp; &nbsp; &nbsp;Fecha:&rdquo;2023-02-12&rdquo;,</p>
                        <p>&nbsp; &nbsp; &nbsp;productos: [</p>
                        <p>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; {</p>
                        <p>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; sku: 3,</p>
                        <p>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; cantidad: 10,</p>
                        <p>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; precio_unitario:10</p>
                        <p>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;},</p>
                        <p>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; {</p>
                        <p>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; sku: 5</p>
                        <p>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; cantidad: 2,</p>
                        <p>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; precio_unitario:10</p>
                        <p>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;},</p>
                        <p>&nbsp; &nbsp; &nbsp;]</p>
                        <p>}</p><br>
                        <p>Ejemplos de par&aacute;metros de salida exitosa:&nbsp;&nbsp;</p>
                        <p>{</p>
                        <p>&nbsp; &nbsp; &ldquo;status&rdquo;: 201,</p>
                        <p>&nbsp; &nbsp; &ldquo;msg&rdquo;: Transacci&oacute;n realizada con &eacute;xito</p>
                        <p>}</p><br>
                        <p>Ejemplos de par&aacute;metros de salida fallida:&nbsp;&nbsp;</p>
                        <p>{</p>
                        <p>&nbsp; &nbsp;&ldquo;status&rdquo;: 400,</p>
                        <p>&nbsp; &nbsp;&ldquo;msg&rdquo;: &ldquo;Formato invalido&rdquo;</p>
                        <p>}</p><br>
                        <p>{</p>
                        <p>&nbsp; &nbsp;&ldquo;status&rdquo;: 401,</p>
                        <p>&nbsp; &nbsp;&ldquo;msg&rdquo;: &ldquo;Token no v&aacute;lido&rdquo;</p>
                        <p>}</p><br>
                        <p>Ejemplos de par&aacute;metros de token</p>
                        <p>{</p>
                        <p>&nbsp; &ldquo;id_grupo&rdquo;: &lt;identificador de la tienda que nos vendi&oacute; los productos&gt;</p>
                        <p>&nbsp; &ldquo;seccion&rdquo;: &lt;Seccion de la tienda de la tienda que nos vendi&oacute; los productos&gt;</p>
                        <p>}</p>
                    </td>
                </tr>
            </tbody>
        </table>
    </div>
</div>

## Diagrama de actividades de tres servicios

+ ### Servicio de Usuario

![](https://i.imgur.com/QDDBAwA.png)

+ ### Servicio de Ventas
![](https://i.imgur.com/prrGn2G.png)


+ ### Servicio de Compras
![](https://i.imgur.com/nKArIaP.png)

## Descripción de la seguridad de la aplicación
Para la seguridad de la aplicación se tomarán las siguientes medidas: 

+ Utilzación de Tokens de autenticación
    + El token tendrá un tiempo de expiración de 1 hora.
+ Encriptación de datos sensibles
    + Los datos sensibles como las contraseñas serán encriptados antes de ser almaceados
+ Manejo de permisos entre usuarios
    + Dependiendo el tipo de usuario ese es el nivel de permisos que tendrá para realizar ciertas acciones, esto también va apoyado del token, ya que dentro de su payload identificaremos el tipo de usuario.

## Documentación de los pipelines.

Para este proyecto habrá dos flujos de pipeline, uno para el frontend y otro flujo para backend. Ambos iniciarían cuando la rama de desarrollo o principal sufriera un cambio, para el resto de los stages habrá un script especializado para cada uno de ellos con todos los comandos a ejecutar.

### Backend Pipeline
* **Test API:** en este stage se instalará dependencias de desarrollo, y posteriormente se ejecutarán las pruebas unitarias y pruebas de integración.
* **Container API:** en este stage se construirá la imagen del contendor a partir de un archivo Dockerfile y posteriormente se estará publicando la imagen a una container registry.
* **Deploy API:** en este stage será dedicado al realizar el deploy de cada uno de los servicios y microservicios.

### Frontend Pipeline

- **Test UI:** en este stage se instalará dependencias de desarrollo, y posteriormente ser ejecutarán las pruebas unitarias y pruebas de integración.

- **Construir UI:** en este stage se instalará dependencias de producción, y posteriormente se construirá la aplicación.

- **Container API:** en este stage se construirá la imagen del contendor a partir de un archivo Dockerfile y posteriormente se estará publicando la imagen a una container registry.

- **Deploy API:** en este stage será dedicado al realizar el deploy del frontend.**


![](https://i.imgur.com/NcQUTjC.png)


## Análisis y solución de la problemática propuesta.
### Resumen:

Es requerido el desarrollo de un software para gestión de actividades empresariales. Esta  plataforma debe de brindar las facilidades básicas como el registro de usuarios, administración de recursos humanos, compra y ventas de productos, inventario, contabilidad y rutas de distribución entre otras funcionalidades, esta plataforma debe de poder conectarse con fuentes externas, de manera que existirá una amplia variedad en el catálogo de los productos que se ofrecen.

### Problema: 

El mayor desafío es  desarrollar un software que permita la gestión de diversas actividades empresariales, incluyendo el registro de usuarios, la administración de recursos humanos, la gestión de inventario, la contabilidad y la gestión de rutas de distribución, que sea escalable, seguro y eficiente, además de permitir al usuario una experiencia agradable. sin dejar por un lado que el sistema debe estar diseñado para conectarse con fuentes externas para ampliar el catálogo de productos ofrecidos.

### Solución: 

1. Requerimientos específicos del sistema: con las funcionalidades que se requieren. Se elaboran contratos específicos para cumplir  con las funcionalidades requeridas.  

2. Arquitectura de la plataforma: Considerando los requisitos de escalabilidad y modularidad, se contempla una  arquitectura basada  en SOA, en el que se trabajara con  microservicios, permitiendo  separar las diferentes funcionalidades de la plataforma en módulos independientes y escalables.

3. Tecnologías para el desarrollo de la plataforma: Se hará uso de las tecnologías;  Flask de Python para el desarrollo de los microservicios. React para la interfaz de usuario, con conexión a una base de datos relacional; con el motor PostgreSQL, JWT para la seguridad de la plataforma, ya que es un estándar ampliamente utilizado y seguro, permitiendo realizar conexión con fuentes externas. 

4. Microservicios: siguiendo la arquitectura SOA es importante desarrollar cada  microservicios de manera modular y escalable, de manera que se puedan agregar o quitar servicios cuando se requiera. 

5. Conexión con fuentes externas:  Se tendrá una conexión con fuentes externas para contar con la posibilidad de ampliar el catálogo de productos que se puedan ofrecer al usuario. 

6. Calidad: Es importante mencionar la importancia de las pruebas; pruebas unitarias, pruebas de integración,  entre otras.

7. Despliegue:  La plataforma se desplegará  en un entorno de producción, haciendo énfasis en los aspectos de seguridad, escalabilidad y disponibilidad, con la tecnología de contenedores Docker.

## Listado de microservicios con sus respectivos contratos.
<h1>Detalle y funcionalidad de los servicios por estudiante</h1>
<p><br></p>
<div align="left">
    <table>
        <tbody>
            <tr>
                <td>
                    <p>No.</p>
                </td>
                <td>
                    <p>Estudiante</p>
                </td>
                <td>
                    <p>Servicios y funcionalidades</p>
                </td>
            </tr>
            <tr>
                <td>
                    <p>1</p>
                </td>
                <td>
                    <p>Elian Estrada</p>
                </td>
                <td>
                    <p>Servicio de Usuario</p>
                    <ul>
                        <li>
                            <p>Registrar</p>
                        </li>
                        <li>
                            <p>generar c&oacute;digo</p>
                        </li>
                        <li>
                            <p>verificar correo</p>
                        </li>
                        <li>
                            <p>Login</p>
                        </li>
                        <li>
                            <p>Ver Perfil</p>
                        </li>
                        <li>
                            <p>Modificar datos personales</p>
                        </li>
                        <li>
                            <p>Modificar contrase&ntilde;a</p>
                        </li>
                        <li>
                            <p>Darse de baja</p>
                        </li>
                    </ul>
                </td>
            </tr>
            <tr>
                <td>
                    <p>2</p>
                </td>
                <td>
                    <p>Mynor Ruiz</p>
                </td>
                <td>
                    <p>Servicio Recursos Humanos</p>
                    <ul>
                        <li>
                            <p>Crear/ agregar usuarios&nbsp;</p>
                        </li>
                        <li>
                            <p>Dar de baja usuarios administrativos</p>
                        </li>
                        <li>
                            <p>Agendar entrevistas</p>
                        </li>
                    </ul>
                </td>
            </tr>
            <tr>
                <td>
                    <p>3</p>
                </td>
                <td>
                    <p>Maynor Pil&oacute;</p>
                </td>
                <td>
                    <p>Servicio Ventas</p>
                    <ul>
                        <li>
                            <p>Registro de venta</p>
                        </li>
                    </ul>
                </td>
            </tr>
            <tr>
                <td>
                    <p>4</p>
                </td>
                <td>
                    <p>Elian Estrada</p>
                </td>
                <td>
                    <p>Servicio de Compra</p>
                    <ul>
                        <li>
                            <p>Agregar producto al carrito</p>
                        </li>
                        <li>
                            <p>Eliminar producto del carrito</p>
                        </li>
                        <li>
                            <p>Eliminar/Cancelar/Vaciar carro</p>
                        </li>
                        <li>
                            <p>Registro de compra externa (interconectividad)</p>
                        </li>
                    </ul>
                </td>
            </tr>
            <tr>
                <td>
                    <p>5</p>
                </td>
                <td>
                    <p>Fernando M&eacute;ndez</p>
                </td>
                <td>
                    <p>Servicio de Inventario</p>
                    <ul>
                        <li>
                            <p>Consultar productos</p>
                        </li>
                        <li>
                            <p>Consultar producto espec&iacute;fico</p>
                        </li>
                        <li>
                            <p>Consultar stock</p>
                        </li>
                        <li>
                            <p>Actualizar inventario</p>
                        </li>
                        <li>
                            <p>Recepci&oacute;n de productos</p>
                        </li>
                    </ul>
                </td>
            </tr>
            <tr>
                <td>
                    <p>6</p>
                </td>
                <td>
                    <p>Maynor Pil&oacute;</p>
                </td>
                <td>
                    <p>Servicio de Contabilidad</p>
                    <ul>
                        <li>
                            <p>Registro de planilla</p>
                        </li>
                        <li>
                            <p>Reporte/Consulta de ganancias</p>
                        </li>
                        <li>
                            <p>Pago de planilla</p>
                        </li>
                    </ul>
                </td>
            </tr>
            <tr>
                <td>
                    <p>7</p>
                </td>
                <td>
                    <p>Mynor Ruiz</p>
                </td>
                <td>
                    <p>Servicio de Rutas</p>
                    <ul>
                        <li>
                            <p>Verificar ruta de la compra</p>
                        </li>
                    </ul>
                </td>
            </tr>
            <tr>
                <td>
                    <p>8</p>
                </td>
                <td>
                    <p>Fernando M&eacute;ndez</p>
                </td>
                <td>
                    <p>Notificaci&oacute;n</p>
                    <ul>
                        <li>
                            <p>Envi&oacute; de notificaci&oacute;n por correo electr&oacute;nico</p>
                        </li>
                    </ul>
                </td>
            </tr>
            <tr>
                <td>
                    <p>9</p>
                </td>
                <td>
                    <p>Fernando M&eacute;ndez</p>
                </td>
                <td>
                    <p>Almacenamiento de objetos</p>
                    <ul>
                        <li>
                            <p>Subir objetos</p>
                        </li>
                    </ul>
                </td>
            </tr>
        </tbody>
    </table>
</div>
<p><br></p>
<h2>Tabla de estimaciones para los story points</h2>
<p><br></p>
<p><br></p>
<div align="left">
    <table>
        <tbody>
            <tr>
                <td>
                    <p>Story point</p>
                </td>
                <td>
                    <p>Esfuerzo</p>
                </td>
            </tr>
            <tr>
                <td>
                    <p>1</p>
                </td>
                <td>
                    <p>Menos de 3 horas</p>
                </td>
            </tr>
            <tr>
                <td>
                    <p>2</p>
                </td>
                <td>
                    <p>Menos de 5 horas</p>
                </td>
            </tr>
            <tr>
                <td>
                    <p>3</p>
                </td>
                <td>
                    <p>Menos de 8 horas (1 d&iacute;a)</p>
                </td>
            </tr>
            <tr>
                <td>
                    <p>5</p>
                </td>
                <td>
                    <p>Menos de 12 horas (1 d&iacute;a y medio)</p>
                </td>
            </tr>
            <tr>
                <td>
                    <p>8</p>
                </td>
                <td>
                    <p>Cerca de 20 horas (2 d&iacute;as y med&iacute;a) podr&iacute;a ser separado en tareas m&aacute;s peque&ntilde;as</p>
                </td>
            </tr>
            <tr>
                <td>
                    <p>13</p>
                </td>
                <td>
                    <p>M&aacute;s de 4 d&iacute;as&nbsp;<br>debe ser separado en tareas m&aacute;s peque&ntilde;as</p>
                </td>
            </tr>
        </tbody>
    </table>
</div>

<div align="left">
    <table>
        <tbody>
            <tr>
                <td>
                    <p>ID:&nbsp;01</p>
                </td>
                <td>
                    <p>Nombre:&nbsp;Registrar usuario</p>
                </td>
            </tr>
            <tr>
                <td>
                    <p>Prioridad:&nbsp;Alta</p>
                </td>
                <td rowspan="3">
                    <p>Historia de usuario</p>
                    <p>Se quiere poder almacenar la informaci&oacute;n del usuario para la creaci&oacute;n de su perfil.</p>
                </td>
            </tr>
            <tr>
                <td>
                    <p>Estimado:&nbsp;8 puntos</p>
                </td>
            </tr>
            <tr>
                <td>
                    <p>M&oacute;dulo:&nbsp;Usuario</p>
                </td>
            </tr>
            <tr>
                <td colspan="2" rowspan="5">
                    <p>Criterios de Aceptaci&oacute;n</p><br>
                    <p>El usuario ingresar&aacute; la informaci&oacute;n requerida para crear su perfil para tener acceso a las compras.&nbsp;</p><br>
                    <p>El microservicio debe tener la siguiente configuraci&oacute;n:</p><br>
                    <p>Ruta:&nbsp;/user/signin</p>
                    <p>M&eacute;todo:&nbsp;POST</p>
                    <p>Formato de entrada:&nbsp;application/json</p><br>
                    <p>Header:</p><br>
                    <div align="left">
                        <table>
                            <tbody>
                                <tr>
                                    <td>
                                        <p>Atributo</p>
                                    </td>
                                    <td>
                                        <p>Tipo</p>
                                    </td>
                                    <td>
                                        <p>Descripci&oacute;n</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>Content-Type</p>
                                    </td>
                                    <td>
                                        <p>header</p>
                                    </td>
                                    <td>
                                        <p>application/json</p>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div><br>
                    <p>Body:</p><br>
                    <div align="left">
                        <table>
                            <tbody>
                                <tr>
                                    <td>
                                        <p>Atributo</p>
                                    </td>
                                    <td>
                                        <p>Tipo</p>
                                    </td>
                                    <td>
                                        <p>Descripci&oacute;n</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>cui</p>
                                    </td>
                                    <td>
                                        <p>entero</p>
                                    </td>
                                    <td>
                                        <p>cui del usuario</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>nombres</p>
                                    </td>
                                    <td>
                                        <p>cadena</p>
                                    </td>
                                    <td>
                                        <p>nombre del usuario</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>apellidos</p>
                                    </td>
                                    <td>
                                        <p>cadena</p>
                                    </td>
                                    <td>
                                        <p>apellido del usuario</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>contrasena</p>
                                    </td>
                                    <td>
                                        <p>cadena</p>
                                    </td>
                                    <td>
                                        <p>contrase&ntilde;a para el usuario</p>
                                        <p>Atributo requerido</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>correo</p>
                                    </td>
                                    <td>
                                        <p>cadena</p>
                                    </td>
                                    <td>
                                        <p>correo electr&oacute;nico del usuario</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>fecha_nacimiento</p>
                                    </td>
                                    <td>
                                        <p>cadena</p>
                                    </td>
                                    <td>
                                        <p>fecha de nacimiento del usuario,</p>
                                        <p>el formato a utilizar ser&aacute; el siguiente: &ldquo;YYYY-mm-dd&rdquo;</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>tipo</p>
                                    </td>
                                    <td>
                                        <p>cadena</p>
                                    </td>
                                    <td>
                                        <p>confirmaci&oacute;n de la contrase&ntilde;a</p>
                                        <ul><li>"C" = Usuario cliente</li>
                                        <li>"E" = Usuario empresarial</li><li>"A" = Usuario administrativo</li></ul>
                                        <p>Atributo requerido</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>numero_grupo</p>
                                    </td>
                                    <td>
                                        <p>entero</p>
                                    </td>
                                    <td>
                                        <p>Es el n&uacute;mero de grupo que representa al cliente empresarial.</p>
                                        <p>Atributo requerido si el tipo = "E"</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>seccion_grupo</p>
                                    </td>
                                    <td>
                                        <p>cadena</p>
                                    </td>
                                    <td>
                                        <p>Es la secci&oacute;n del grupo que representa al cliente empresarial</p>
                                        <p>Atributo requerido si el  tipo = "E"</p>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div><br>
                    <p>Formato de salida:&nbsp;JSON</p>
                    <p>C&oacute;digo de respuesta exitosa:&nbsp;HTTP 200</p>
                    <p>Salida:&nbsp;</p><br>
                    <div align="left">
                        <table>
                            <tbody>
                                <tr>
                                    <td>
                                        <p>Atributo</p>
                                    </td>
                                    <td>
                                        <p>Tipo</p>
                                    </td>
                                    <td>
                                        <p>Descripci&oacute;n</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>estatus</p>
                                    </td>
                                    <td>
                                        <p>entero</p>
                                    </td>
                                    <td>
                                        <p>indica el c&oacute;digo de respuesta de aceptaci&oacute;n</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>mensaje</p>
                                    </td>
                                    <td>
                                        <p>cadena</p>
                                    </td>
                                    <td>
                                        <p>muestra informaci&oacute;n del registro del usuario</p>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div><br>
                    <p>C&oacute;digo de respuesta fallida:</p><br>
                    <div align="left">
                        <table>
                            <tbody>
                                <tr>
                                    <td>
                                        <p>C&oacute;digo</p>
                                    </td>
                                    <td>
                                        <p>Descripci&oacute;n</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>400</p>
                                    </td>
                                    <td>
                                        <p>Error al interpretar la solicitud</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>404</p>
                                    </td>
                                    <td>
                                        <p>Recurso no encontrado</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>500</p>
                                    </td>
                                    <td>
                                        <p>Error interno del servidor</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>401</p>
                                    </td>
                                    <td>
                                        <p>Si es usuario empresarial debe de ingresar numero de grupo o seccion</p>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div><br>
                    <p>Body de Salida:</p><br>
                    <div align="left">
                        <table>
                            <tbody>
                                <tr>
                                    <td>
                                        <p>Atributo</p>
                                    </td>
                                    <td>
                                        <p>Tipo</p>
                                    </td>
                                    <td>
                                        <p>Descripci&oacute;n</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>estatus</p>
                                    </td>
                                    <td>
                                        <p>entero</p>
                                    </td>
                                    <td>
                                        <p>indica el c&oacute;digo de respuesta fallida</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>error</p>
                                    </td>
                                    <td>
                                        <p>cadena</p>
                                    </td>
                                    <td>
                                        <p>muestra el nombre del error</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>mensaje</p>
                                    </td>
                                    <td>
                                        <p>cadena</p>
                                    </td>
                                    <td>
                                        <p>muestra m&aacute;s informaci&oacute;n del error</p>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div><br>
                </td>
            </tr>
            <tr></tr>
            <tr></tr>
            <tr></tr>
            <tr></tr>
        </tbody>
    </table>
</div>
<p><br></p>
<p>Ejemplos de parametros de entrada:</p>

```json
{
    "cui": 2168095170407,
    "nombres": "Rafael Angel",
    "apellidos": "Chocoj Xinico",
    "contrasena": "123",
    "correo": "rafaelcliveguitar@gmail.com",
    "fecha_nacimiento": "2020-11-25",
    "tipo": "E",
    "numero_grupo": 914,
    "seccion_grupo": "N"
}
```

<p>Ejemplos de parametros de salida exitosa:</p>

```json
{
    "estatus": 200,
    "mensaje": "Se ha registrado el usuario exitosamente"
}
```

<p>Ejemplo de par&aacute;metros de salida fallida:</p>

```json
{
    "estatus": 401,
    "mensaje": "Si es usuario empresarial debe de ingresar numero de grupo o seccion"
}
{
    "estatus": 500, "error": "Error interno del servidor", 
    "mensaje": "Error, ya existe usuario con el mismo cui. "
}

{
    "estatus": 400, "error":"error",  "mensaje": "error al enviar correo"
}

{
    "estatus": 400, "error":"error server",  "mensaje": "Error al interpretar la solicitud"
}

```
<p>Servicio de usuario consume envio de correo:</p>
<p>/notification/sendEmail</p>

```json
{
    "para": "rafael@gmail.com",
    "asunto": "CONFIRMAR CUENTA",
    "mensaje": "bienvenido ",
    "plantilla": "confirmEmail",
    "data": {"code": "enlace"}
}
```

<div align="left">
    <table>
        <tbody>
            <tr>
                <td>
                    <p>ID:&nbsp;02</p>
                </td>
                <td>
                    <p>Nombre:&nbsp;Generar c&oacute;digo de verificaci&oacute;n</p>
                </td>
            </tr>
            <tr>
                <td>
                    <p>Prioridad:&nbsp;Alta</p>
                </td>
                <td rowspan="3">
                    <p>Historia de usuario</p>
                    <p>Se desea generar c&oacute;digos de verificaci&oacute;n para poder validar la veracidad de la informaci&oacute;n ingresada por el usuario.</p>
                </td>
            </tr>
            <tr>
                <td>
                    <p>Estimado: &nbsp;1 puntos</p>
                </td>
            </tr>
            <tr>
                <td>
                    <p>M&oacute;dulo:&nbsp;Usuario</p>
                </td>
            </tr>
            <tr>
                <td colspan="2" rowspan="5">
                    <p>Criterios de Aceptaci&oacute;n</p><br>
                    <p>Se generar&aacute; un c&oacute;digo de verificaci&oacute;n, una vez teniendo este se conectar&aacute; con el servicio de notificaciones para enviar un correo a la direcci&oacute;n proporcionada por el usuario con el c&oacute;digo generado, a su vez, este c&oacute;digo generado se guardar&aacute; en una base de datos &ldquo;Redis&rdquo; y este c&oacute;digo expirar&aacute; en 5 minutos.</p><br>
                    <p>El microservicio debe tener la siguiente configuraci&oacute;n:</p><br>
                    <p>Ruta:&nbsp;/user/verifyCode</p>
                    <p>M&eacute;todo:&nbsp;POST</p>
                    <p>Formato de entrada:&nbsp;JSON</p><br>
                    <p>Header:</p><br>
                    <div align="left">
                        <table>
                            <tbody>
                                <tr>
                                    <td>
                                        <p>Atributo</p>
                                    </td>
                                    <td>
                                        <p>Tipo</p>
                                    </td>
                                    <td>
                                        <p>Descripci&oacute;n</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>Content-Type</p>
                                    </td>
                                    <td>
                                        <p>header</p>
                                    </td>
                                    <td>
                                        <p>application/json</p>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div><br>
                    <p>Body:</p><br>
                    <div align="left">
                        <table>
                            <tbody>
                                <tr>
                                    <td>
                                        <p>Atributo</p>
                                    </td>
                                    <td>
                                        <p>Tipo</p>
                                    </td>
                                    <td>
                                        <p>Descripci&oacute;n</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>para</p>
                                    </td>
                                    <td>
                                        <p>cadena</p>
                                    </td>
                                    <td>
                                        <p>correo electr&oacute;nico del usuario</p>
                                        <p>Atributo requerido</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>asunto</p>
                                    </td>
                                    <td>
                                        <p>cadena</p>
                                    </td>
                                    <td>
                                        <p>asunto del correo electr&oacute;nico</p>
                                        <p>Atributo requerido</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>mensaje</p>
                                    </td>
                                    <td>
                                        <p>cadena</p>
                                    </td>
                                    <td>
                                        <p>Texto del mensaje del correo electr&oacute;nico, debe tener una longitud mayor a 10 caracteres</p>
                                        <p>Atributo requerido</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>plantilla</p>
                                    </td>
                                    <td>
                                        <p>cadena</p>
                                    </td>
                                    <td>
                                        <p>plantilla que se utilizara para el correo, el valor de este campo &nbsp;puede ser alguna de las siguientes opciones:</p>
                                        <ul>
                                            <li>
                                                <p>confirmEmail</p>
                                            </li>
                                            <li>
                                                <p>resetPassword</p>
                                            </li>
                                        </ul>
                                        <p>Atributo requerido</p>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div><br>
                    <p>Formato de salida:&nbsp;JSON</p>
                    <p>C&oacute;digo de respuesta exitosa:&nbsp;HTTP 200</p>
                    <p>Salida:&nbsp;</p><br>
                    <div align="left">
                        <table>
                            <tbody>
                                <tr>
                                    <td>
                                        <p>Atributo</p>
                                    </td>
                                    <td>
                                        <p>Tipo</p>
                                    </td>
                                    <td>
                                        <p>Descripci&oacute;n</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>estatus</p>
                                    </td>
                                    <td>
                                        <p>entero</p>
                                    </td>
                                    <td>
                                        <p>indica el c&oacute;digo de respuesta de aceptaci&oacute;n</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>mensaje</p>
                                    </td>
                                    <td>
                                        <p>cadena</p>
                                    </td>
                                    <td>
                                        <p>muestra informaci&oacute;n de la generaci&oacute;n del c&oacute;digo</p>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div><br>
                    <p>C&oacute;digo de respuesta fallida:</p><br>
                    <div align="left">
                        <table>
                            <tbody>
                                <tr>
                                    <td>
                                        <p>C&oacute;digo</p>
                                    </td>
                                    <td>
                                        <p>Descripci&oacute;n</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>400</p>
                                    </td>
                                    <td>
                                        <p>Error al interpretar la solicitud</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>500</p>
                                    </td>
                                    <td>
                                        <p>Error interno del servidor</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>503</p>
                                    </td>
                                    <td>
                                        <p>Servicio no disponible</p>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div><br>
                    <p>Body de Salida:</p><br>
                    <div align="left">
                        <table>
                            <tbody>
                                <tr>
                                    <td>
                                        <p>Atributo</p>
                                    </td>
                                    <td>
                                        <p>Tipo</p>
                                    </td>
                                    <td>
                                        <p>Descripci&oacute;n</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>estatus</p>
                                    </td>
                                    <td>
                                        <p>entero</p>
                                    </td>
                                    <td>
                                        <p>indica el c&oacute;digo de respuesta fallido</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>error</p>
                                    </td>
                                    <td>
                                        <p>cadena</p>
                                    </td>
                                    <td>
                                        <p>muestra el nombre del error</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>mensaje</p>
                                    </td>
                                    <td>
                                        <p>cadena</p>
                                    </td>
                                    <td>
                                        <p>muestra m&aacute;s informaci&oacute;n del error</p>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div><br>
                    <p>Ejemplos de par&aacute;metros de entrada:</p>
                    <p>{</p>
                    <p>&nbsp; &nbsp; &ldquo;para&rdquo;:&rdquo;elian.estrada@gmail.com&rdquo;,</p>
                    <p>&nbsp; &nbsp; &ldquo;asunto&rdquo;: &ldquo;Verificar correo&rdquo;,</p>
                    <p>&nbsp; &nbsp; &ldquo;mensaje:&rdquo;: &ldquo;C&oacute;digo de confirmaci&oacute;n de correo&rdquo;,</p>
                    <p>&nbsp; &nbsp; &ldquo;plantilla&rdquo;: &ldquo;confirmEmail&rdquo;</p>
                    <p>}</p>
                    <p>Ejemplos de par&aacute;metros de salida exitosa:</p>
                    <p>{</p>
                    <p>&nbsp; &nbsp; &ldquo;estatus&rdquo;: 200,</p>
                    <p>&nbsp; &nbsp; &ldquo;mensaje&rdquo;: &ldquo;Se gener&oacute; el c&oacute;digo de verificaci&oacute;n exitosamente&rdquo;</p>
                    <p>}</p>
                    <p>Ejemplo de par&aacute;metros de salida fallida:</p>
                    <p>{</p>
                    <p>&nbsp; &nbsp; &ldquo;estatus&rdquo;: 400</p>
                    <p>&nbsp; &nbsp; &ldquo;error&rdquo;:&rdquo;Par&aacute;metro requerido&rdquo;,</p>
                    <p>&nbsp; &nbsp; &ldquo;mensaje&rdquo;:&rdquo;Falt&oacute; alg&uacute;n par&aacute;metro requerido para generar el c&oacute;digo&rdquo;</p>
                    <p>}</p><br>
                    <p>{</p>
                    <p>&nbsp; &nbsp; &ldquo;estatus&rdquo;: 500</p>
                    <p>&nbsp; &nbsp; &ldquo;error&rdquo;:&rdquo;Error al conectarse a la redis&rdquo;,</p>
                    <p>&nbsp; &nbsp; &ldquo;mensaje&rdquo;:&rdquo;No se pudo establecer una conecci&oacute;n con la Base de Datos&rdquo;</p>
                    <p>}</p><br>
                    <p>{</p>
                    <p>&nbsp; &nbsp; &ldquo;estatus&rdquo;: 503</p>
                    <p>&nbsp; &nbsp; &ldquo;error&rdquo;:&rdquo;Servicio no disponible&rdquo;,</p>
                    <p>&nbsp; &nbsp; &ldquo;mensaje&rdquo;:&rdquo;El servicio solicitado no se encuentra disponible ahora, intentelo mas<br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; tarde&rdquo;</p>
                    <p>}</p>
                </td>
            </tr>
            <tr></tr>
            <tr></tr>
            <tr></tr>
            <tr></tr>
        </tbody>
    </table>
</div>
<p><br></p>
<p><br></p>
<div align="left">
    <table>
        <tbody>
            <tr>
                <td>
                    <p>ID:&nbsp;03</p>
                </td>
                <td>
                    <p>Nombre:&nbsp;Verificar correo</p>
                </td>
            </tr>
            <tr>
                <td>
                    <p>Prioridad:&nbsp;Alta</p>
                </td>
                <td rowspan="3">
                    <p>Historia de usuario</p>
                    <p>Es importante verificar que la direcci&oacute;n de correo electr&oacute;nico exista y el usuario tenga acceso a ella.</p>
                </td>
            </tr>
            <tr>
                <td>
                    <p>Estimado:&nbsp;1 punto</p>
                </td>
            </tr>
            <tr>
                <td>
                    <p>M&oacute;dulo:&nbsp;Usuario</p>
                </td>
            </tr>
            <tr>
                <td colspan="2" rowspan="5">
                    <p>Criterios de Aceptaci&oacute;n</p><br>
                    <p>Se deber&aacute; ingresar al link que fue enviado por correo, para verificar que este exista correo.</p><br>
                    <p>El microservicio debe tener la siguiente configuraci&oacute;n:</p><br>
                    <p>Ruta:&nbsp;/user/verifyemail</p>
                    <p>M&eacute;todo:&nbsp;POST</p>
                    <p>Formato de entrada:&nbsp;JSON</p><br>
                    <p>Header:</p><br>
                    <div align="left">
                        <table>
                            <tbody>
                                <tr>
                                    <td>
                                        <p>Atributo</p>
                                    </td>
                                    <td>
                                        <p>Tipo</p>
                                    </td>
                                    <td>
                                        <p>Descripci&oacute;n</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>Content-Type</p>
                                    </td>
                                    <td>
                                        <p>header</p>
                                    </td>
                                    <td>
                                        <p>application/json</p>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div><br>
                    <p>Body:</p><br>
                    <div align="left">
                        <table>
                            <tbody>
                                <tr>
                                    <td>
                                        <p>Atributo</p>
                                    </td>
                                    <td>
                                        <p>Tipo</p>
                                    </td>
                                    <td>
                                        <p>Descripci&oacute;n</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>token</p>
                                    </td>
                                    <td>
                                        <p>cadena</p>
                                    </td>
                                    <td>
                                        <p>cui del usuario encriptado para validar ya activar cuenta</p>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div><br>
                    <p>Formato de salida:&nbsp;JSON</p>
                    <p>C&oacute;digo de respuesta exitosa:&nbsp;HTTP 200</p>
                    <p>Salida:&nbsp;</p><br>
                    <div align="left">
                        <table>
                            <tbody>
                                <tr>
                                    <td>
                                        <p>Atributo</p>
                                    </td>
                                    <td>
                                        <p>Tipo</p>
                                    </td>
                                    <td>
                                        <p>Descripci&oacute;n</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>estatus</p>
                                    </td>
                                    <td>
                                        <p>entero</p>
                                    </td>
                                    <td>
                                        <p>indica el c&oacute;digo de respuesta de aceptaci&oacute;n</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>mensaje</p>
                                    </td>
                                    <td>
                                        <p>cadena</p>
                                    </td>
                                    <td>
                                        <p>muestra informaci&oacute;n de la verificaci&oacute;n del correo</p>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div><br>
                    <p>C&oacute;digo de respuesta fallida:</p><br>
                    <div align="left">
                        <table>
                            <tbody>
                                <tr>
                                    <td>
                                        <p>C&oacute;digo</p>
                                    </td>
                                    <td>
                                        <p>Descripci&oacute;n</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>400</p>
                                    </td>
                                    <td>
                                        <p>Error al interpretar la solicitud, Error en token invalido</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>404</p>
                                    </td>
                                    <td>
                                        <p>no existe usuario</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>300</p>
                                    </td>
                                    <td>
                                        <p>JWT ya expiro</p>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div><br>
                    <p>Body de Salida:</p><br>
                    <div align="left">
                        <table>
                            <tbody>
                                <tr>
                                    <td>
                                        <p>Atributo</p>
                                    </td>
                                    <td>
                                        <p>Tipo</p>
                                    </td>
                                    <td>
                                        <p>Descripci&oacute;n</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>estatus</p>
                                    </td>
                                    <td>
                                        <p>entero</p>
                                    </td>
                                    <td>
                                        <p>indica el c&oacute;digo de respuesta fallido</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>error</p>
                                    </td>
                                    <td>
                                        <p>cadena</p>
                                    </td>
                                    <td>
                                        <p>muestra el nombre del error</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>mensaje</p>
                                    </td>
                                    <td>
                                        <p>cadena</p>
                                    </td>
                                    <td>
                                        <p>muestra m&aacute;s informaci&oacute;n del error</p>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div><br>
                    <p>Ejemplos de par&aacute;metros de entrada:</p>

```json
{
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjdWkiOjIxNjgwOTUxNzA0MDcsImV4cCI6MTY4MjM3MzI5OX0.zzV7IShwEIgG6iRe5D11dMFiMuNTONWlBBYwKNfaYeo"
}
```

<p>Ejemplos de par&aacute;metros de salida exitosa:</p>

```json
{
    "estatus": 200,
    "mensaje": "se activó cuenta correctamente"
}
```    
<p>Ejemplo de par&aacute;metros de salida fallida:</p>
                    
```json
{
    "estatus": 404, "error": "activacion cuenta", 
    "mensaje": "no existe usuario"
}

{
    "estatus": 300,
    "error": "JWT ya expiro",
    "mensaje": "ya expiro invitacion",
}

{
    "estatus": 400,
    "error": "Error en token enviado",
    "mensaje": "Error en token invalido",
}
{
    "estatus": 400, "error":"error servidor",  "mensaje": "Error al interpretar la solicitud"
}
``` 
</td>
            </tr>
            <tr></tr>
            <tr></tr>
            <tr></tr>
            <tr></tr>
        </tbody>
    </table>
</div>
<p><br></p>
<p><br></p>
<div align="left">
    <table>
        <tbody>
            <tr>
                <td>
                    <p>ID:&nbsp;04</p>
                </td>
                <td>
                    <p>Nombre:&nbsp;Iniciar sesi&oacute;n</p>
                </td>
            </tr>
            <tr>
                <td>
                    <p>Prioridad:&nbsp;Alta</p>
                </td>
                <td rowspan="3">
                    <p>Historia de usuario</p>
                    <p>Es importante tener un medio por el cual los usuarios puedan ingresar a la plataforma de manera segura.</p>
                </td>
            </tr>
            <tr>
                <td>
                    <p>Estimado:&nbsp;2 punto</p>
                </td>
            </tr>
            <tr>
                <td>
                    <p>M&oacute;dulo:&nbsp;Usuario</p>
                </td>
            </tr>
            <tr>
                <td colspan="2" rowspan="5">
                    <p>Criterios de Aceptaci&oacute;n</p>
                    <p>Al validar las credenciales se deber&aacute;, mediante al est&aacute;ndar JWT, crear un token v&aacute;lido que ser&aacute; devuelto para que el usuario est&eacute; autenticado.</p><br>
                    <p>El microservicio debe tener la siguiente configuraci&oacute;n:</p><br>
                    <p>Ruta:&nbsp;/user/login</p>
                    <p>M&eacute;todo:&nbsp;POST</p>
                    <p>Formato de entrada:&nbsp;JSON</p><br>
                    <p>Payload:&nbsp;</p><br>
                    <div align="left">
                        <table>
                            <tbody>
                                <tr>
                                    <td>
                                        <p>Atributo</p>
                                    </td>
                                    <td>
                                        <p>Tipo</p>
                                    </td>
                                    <td>
                                        <p>Descripci&oacute;n</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>idUsuario</p>
                                    </td>
                                    <td>
                                        <p>entero</p>
                                    </td>
                                    <td>
                                        <p>el n&uacute;mero que identifica al &nbsp;usuario en el sistema.</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>tipoUsuario</p>
                                    </td>
                                    <td>
                                        <p>entero</p>
                                    </td>
                                    <td>
                                        <p>El tipo de usuario dentro de la plataforma, este puede ser:&nbsp;</p>
                                        <ul>
                                            <li>
                                                <p>0</p>
                                            </li>
                                            <li>
                                                <p>1&nbsp;</p>
                                            </li>
                                            <li>
                                                <p>2</p>
                                            </li>
                                        </ul>
                                        <p>Donde:&nbsp;</p>
                                        <p>0 = administradores</p>
                                        <p>1 = &nbsp;clientes normales</p>
                                        <p>2 = clientes empresariales</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>exp</p>
                                    </td>
                                    <td>
                                        <p>entero</p>
                                    </td>
                                    <td>
                                        <p>Este representa la fecha de expiraci&oacute;n del token.</p>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div><br><br>
                    <p>Header:</p><br>
                    <div align="left">
                        <table>
                            <tbody>
                                <tr>
                                    <td>
                                        <p>Atributo</p>
                                    </td>
                                    <td>
                                        <p>Tipo</p>
                                    </td>
                                    <td>
                                        <p>Descripci&oacute;n</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>Content-Type</p>
                                    </td>
                                    <td>
                                        <p>header</p>
                                    </td>
                                    <td>
                                        <p>application/json</p>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div><br>
                    <p>Body:</p><br>
                    <div align="left">
                        <table>
                            <tbody>
                                <tr>
                                    <td>
                                        <p>Atributo</p>
                                    </td>
                                    <td>
                                        <p>Tipo</p>
                                    </td>
                                    <td>
                                        <p>Descripci&oacute;n</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>correo</p>
                                    </td>
                                    <td>
                                        <p>cadena</p>
                                    </td>
                                    <td>
                                        <p>correo electr&oacute;nico del usuario</p>
                                        <p>Atributo requerido</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>contrase&ntilde;a</p>
                                    </td>
                                    <td>
                                        <p>cadena</p>
                                    </td>
                                    <td>
                                        <p>contrase&ntilde;a del usuario</p>
                                        <p>Atributo requerido</p>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div><br>
                    <p>Formato de salida:&nbsp;JSON</p>
                    <p>C&oacute;digo de respuesta exitosa:&nbsp;HTTP 200</p>
                    <p>Salida:&nbsp;</p><br>
                    <div align="left">
                        <table>
                            <tbody>
                                <tr>
                                    <td>
                                        <p>Atributo</p>
                                    </td>
                                    <td>
                                        <p>Tipo</p>
                                    </td>
                                    <td>
                                        <p>Descripci&oacute;n</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>estatus</p>
                                    </td>
                                    <td>
                                        <p>entero</p>
                                    </td>
                                    <td>
                                        <p>indica el c&oacute;digo de respuesta de aceptaci&oacute;n</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>mensaje</p>
                                    </td>
                                    <td>
                                        <p>cadena</p>
                                    </td>
                                    <td>
                                        <p>muestra informaci&oacute;n del inicio de sesi&oacute;n</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>token</p>
                                    </td>
                                    <td>
                                        <p>cadena</p>
                                    </td>
                                    <td>
                                        <p>token v&aacute;lido para la autenticaci&oacute;n</p>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div><br>
                    <p>C&oacute;digo de respuesta fallida:</p><br>
                    <div align="left">
                        <table>
                            <tbody>
                                <tr>
                                    <td>
                                        <p>C&oacute;digo</p>
                                    </td>
                                    <td>
                                        <p>Descripci&oacute;n</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>400</p>
                                    </td>
                                    <td>
                                        <p>Error al interpretar la solicitud</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>404</p>
                                    </td>
                                    <td>
                                        <p>Recurso no encontrado</p>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div><br>
                    <p>Body de Salida:</p><br>
                    <div align="left">
                        <table>
                            <tbody>
                                <tr>
                                    <td>
                                        <p>Atributo</p>
                                    </td>
                                    <td>
                                        <p>Tipo</p>
                                    </td>
                                    <td>
                                        <p>Descripci&oacute;n</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>estatus</p>
                                    </td>
                                    <td>
                                        <p>entero</p>
                                    </td>
                                    <td>
                                        <p>indica el c&oacute;digo de respuesta fallido</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>error</p>
                                    </td>
                                    <td>
                                        <p>cadena</p>
                                    </td>
                                    <td>
                                        <p>muestra el nombre del error</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>mensaje</p>
                                    </td>
                                    <td>
                                        <p>cadena</p>
                                    </td>
                                    <td>
                                        <p>muestra m&aacute;s informaci&oacute;n del error</p>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                    <p>Ejemplos de par&aacute;metros de entrada:</p>
                    <p>{</p>
                    <p>&nbsp; &nbsp; &ldquo;correo&rdquo;:&rdquo;elian.estrada@gmail.com&rdquo;,</p>
                    <p>&nbsp; &nbsp; &ldquo;contrase&ntilde;a&rdquo;:&rdquo;Lib2023@Lian&rdquo;</p>
                    <p>}</p>
                    <p>Ejemplos de par&aacute;metros de salida exitosa:</p>
                    <p>{</p>
                    <p>&nbsp; &nbsp; &ldquo;estatus&rdquo;: 200,</p>
                    <p>&nbsp; &nbsp; &ldquo;mensaje&rdquo;: &ldquo;Se inici&oacute; sesi&oacute;n correctamente&rdquo;,</p>
                    <p>&nbsp; &nbsp; &ldquo;token&rdquo;:&lt;token_generado&gt;,</p>
                    <p>&nbsp; &nbsp; &ldquo;idUsuario&rdquo;: 1</p>
                    <p>}</p>
                    <p>Ejemplo de par&aacute;metros de salida fallida:</p>
                    <p>{</p>
                    <p>&nbsp; &nbsp; &ldquo;estatus&rdquo;: 400</p>
                    <p>&nbsp; &nbsp; &ldquo;error&rdquo;:&rdquo;Fall&oacute; la autenticaci&oacute;n&rdquo;,</p>
                    <p>&nbsp; &nbsp; &ldquo;mensaje&rdquo;:&rdquo;El correo o contrase&ntilde;a no son correctos&rdquo;</p>
                    <p>}</p><br>
                    <p>{</p>
                    <p>&nbsp; &nbsp; &ldquo;estatus&rdquo;: 404</p>
                    <p>&nbsp; &nbsp; &ldquo;error&rdquo;:&rdquo;Usuario inexistente&rdquo;,</p>
                    <p>&nbsp; &nbsp; &ldquo;mensaje&rdquo;:&rdquo;No hay ning&uacute;n usuario con el correo: elian@gmail.com&rdquo;</p>
                    <p>}</p>
                </td>
            </tr>
            <tr></tr>
            <tr></tr>
            <tr></tr>
            <tr></tr>
        </tbody>
    </table>
</div>
<p><br></p>
<p><br></p>
<p><br></p>
<div align="left">
    <table>
        <tbody>
            <tr>
                <td>
                    <p>ID:&nbsp;05</p>
                </td>
                <td>
                    <p>Nombre:&nbsp;Ver Perfil</p>
                </td>
            </tr>
            <tr>
                <td>
                    <p>Prioridad:&nbsp;Media</p>
                </td>
                <td rowspan="3">
                    <p>Historia de usuario</p>
                    <p>Es importante que el usuario pueda ver la informaci&oacute;n que fue ingresada para ser revisada por &eacute;l.</p>
                </td>
            </tr>
            <tr>
                <td>
                    <p>Estimado:&nbsp;2 puntos</p>
                </td>
            </tr>
            <tr>
                <td>
                    <p>M&oacute;dulo:&nbsp;Usuario</p>
                </td>
            </tr>
            <tr>
                <td colspan="2" rowspan="5">
                    <p>Criterios de Aceptaci&oacute;n</p><br>
                    <p>Se solicitar&aacute; la informaci&oacute;n del usuario logueado a la BD, y se mostrar&aacute; la informaci&oacute;n que sea necesaria para el usuario.</p><br>
                    <p>El microservicio debe tener la siguiente configuraci&oacute;n:</p><br>
                    <p>Ruta:&nbsp;/user/profile</p>
                    <p>M&eacute;todo:&nbsp;POST</p>
                    <p>Formato de entrada:&nbsp;JSON</p><br>
                    <p>Payload:&nbsp;</p><br>
                    <div align="left">
                        <table>
                            <tbody>
                                <tr>
                                    <td>
                                        <p>Atributo</p>
                                    </td>
                                    <td>
                                        <p>Tipo</p>
                                    </td>
                                    <td>
                                        <p>Descripci&oacute;n</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>cui</p>
                                    </td>
                                    <td>
                                        <p>cadena</p>
                                    </td>
                                    <td>
                                        <p>el n&uacute;mero de identificaci&oacute;n del usuario.</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>tipoUsuario</p>
                                    </td>
                                    <td>
                                        <p>entero</p>
                                    </td>
                                    <td>
                                        <p>El tipo de usuario dentro de la plataforma, este puede ser:&nbsp;</p>
                                        <ul>
                                            <li>
                                                <p>1&nbsp;</p>
                                            </li>
                                            <li>
                                                <p>2</p>
                                            </li>
                                        </ul>
                                        <p>Donde:&nbsp;</p>
                                        <p>1 representa administradores</p>
                                        <p>2 clientes normales</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>exp</p>
                                    </td>
                                    <td>
                                        <p>entero</p>
                                    </td>
                                    <td>
                                        <p>Este representa la fecha de expiraci&oacute;n del token.</p>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div><br>
                    <p>Header:</p><br>
                    <div align="left">
                        <table>
                            <tbody>
                                <tr>
                                    <td>
                                        <p>Atributo</p>
                                    </td>
                                    <td>
                                        <p>Tipo</p>
                                    </td>
                                    <td>
                                        <p>Descripci&oacute;n</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>Content-Type</p>
                                    </td>
                                    <td>
                                        <p>header</p>
                                    </td>
                                    <td>
                                        <p>application/json</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>Authorization</p>
                                    </td>
                                    <td>
                                        <p>header</p>
                                    </td>
                                    <td>
                                        <p>Bearer &lt;token&gt;</p>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div><br>
                    <p>Body:</p><br>
                    <div align="left">
                        <table>
                            <tbody>
                                <tr>
                                    <td>
                                        <p>Atributo</p>
                                    </td>
                                    <td>
                                        <p>Tipo</p>
                                    </td>
                                    <td>
                                        <p>Descripci&oacute;n</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>idUsuario</p>
                                    </td>
                                    <td>
                                        <p>entero</p>
                                    </td>
                                    <td>
                                        <p>identificaci&oacute;n del usuario</p>
                                        <p>Atributo Requerido</p>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div><br>
                    <p>Formato de salida:&nbsp;JSON</p>
                    <p>C&oacute;digo de respuesta exitosa:&nbsp;HTTP 200</p>
                    <p>Salida:&nbsp;</p><br>
                    <div align="left">
                        <table>
                            <tbody>
                                <tr>
                                    <td>
                                        <p>Atributo</p>
                                    </td>
                                    <td>
                                        <p>Tipo</p>
                                    </td>
                                    <td>
                                        <p>Descripci&oacute;n</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>estatus</p>
                                    </td>
                                    <td>
                                        <p>entero</p>
                                    </td>
                                    <td>
                                        <p>indica el c&oacute;digo de respuesta</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>data</p>
                                    </td>
                                    <td>
                                        <p>objeto</p>
                                    </td>
                                    <td>
                                        <p>Objeto que contiene la informaci&oacute;n del usuario</p>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div><br>
                    <p>usuario:&nbsp;</p><br>
                    <div align="left">
                        <table>
                            <tbody>
                                <tr>
                                    <td>
                                        <p>Atributo</p>
                                    </td>
                                    <td>
                                        <p>Tipo</p>
                                    </td>
                                    <td>
                                        <p>Descripci&oacute;n</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>nombre</p>
                                    </td>
                                    <td>
                                        <p>cadena</p>
                                    </td>
                                    <td>
                                        <p>nombre del usuario</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>apellido</p>
                                    </td>
                                    <td>
                                        <p>cadena</p>
                                    </td>
                                    <td>
                                        <p>apellido del usuario</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>correo</p>
                                    </td>
                                    <td>
                                        <p>cadena</p>
                                    </td>
                                    <td>
                                        <p>correo electr&oacute;nico del usuario</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>fechaNacimiento</p>
                                    </td>
                                    <td>
                                        <p>cadena</p>
                                    </td>
                                    <td>
                                        <p>fecha de nacimiento del usuario con el formato: &ldquo;%d/%m/%Y&rdquo;</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>foto</p>
                                    </td>
                                    <td>
                                        <p>cadena</p>
                                    </td>
                                    <td>
                                        <p>foto de perfil del usuario</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>departamento</p>
                                    </td>
                                    <td>
                                        <p>cadena</p>
                                    </td>
                                    <td>
                                        <p>nombre del departamento proporcionado</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>ciudad</p>
                                    </td>
                                    <td>
                                        <p>cadena</p>
                                    </td>
                                    <td>
                                        <p>nombre de la ciudad proporcionada</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>zona</p>
                                    </td>
                                    <td>
                                        <p>entero</p>
                                    </td>
                                    <td>
                                        <p>n&uacute;mero de zona proporcionada</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>direcci&oacute;n</p>
                                    </td>
                                    <td>
                                        <p>cadena</p>
                                    </td>
                                    <td>
                                        <p>direcci&oacute;n m&aacute;s profunda proporcionada</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>numeroGrupo</p>
                                    </td>
                                    <td>
                                        <p>entero</p>
                                    </td>
                                    <td>
                                        <p>n&uacute;mero del grupo</p>
                                        <p>Se devolver&aacute; solo si el usuario es de tipo empresarial</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>seccion</p>
                                    </td>
                                    <td>
                                        <p>cadena</p>
                                    </td>
                                    <td>
                                        <p>secci&oacute;n del grupo</p>
                                        <p>Se devolver&aacute; solo si el usuario es de tipo empresarial</p>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div><br><br>
                    <p>C&oacute;digo de respuesta fallida:</p><br>
                    <div align="left">
                        <table>
                            <tbody>
                                <tr>
                                    <td>
                                        <p>C&oacute;digo</p>
                                    </td>
                                    <td>
                                        <p>Descripci&oacute;n</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>400</p>
                                    </td>
                                    <td>
                                        <p>Error al interpretar la solicitud</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>401</p>
                                    </td>
                                    <td>
                                        <p>Error, usuario no autorizado</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>404</p>
                                    </td>
                                    <td>
                                        <p>Error, usuario no existe</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>500</p>
                                    </td>
                                    <td>
                                        <p>Error interno del servidor</p>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div><br>
                    <p>Body de Salida:</p><br>
                    <div align="left">
                        <table>
                            <tbody>
                                <tr>
                                    <td>
                                        <p>Atributo</p>
                                    </td>
                                    <td>
                                        <p>Tipo</p>
                                    </td>
                                    <td>
                                        <p>Descripci&oacute;n</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>estatus</p>
                                    </td>
                                    <td>
                                        <p>entero</p>
                                    </td>
                                    <td>
                                        <p>Indica el c&oacute;digo de respuesta</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>error</p>
                                    </td>
                                    <td>
                                        <p>cadena</p>
                                    </td>
                                    <td>
                                        <p>muestra el nombre del error</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>mensaje</p>
                                    </td>
                                    <td>
                                        <p>cadena</p>
                                    </td>
                                    <td>
                                        <p>muestra m&aacute;s informaci&oacute;n del error</p>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div><br>
                    <p>Ejemplos de par&aacute;metros de entrada:</p>
                    <p>{</p>
                    <p>&nbsp; &nbsp; &ldquo;idUsuario&rdquo;: 1</p>
                    <p>}</p>
                    <p>Ejemplos de par&aacute;metros de salida exitosa:</p>
                    <p>{</p>
                    <p>&nbsp; &nbsp; &quot;estatus&quot;: 200,</p>
                    <p>&nbsp; &nbsp; &ldquo;data&rdquo;: {</p>
                    <p>&nbsp; &nbsp; &nbsp; &nbsp; &ldquo;nombre&rdquo;:&rdquo;Elian&rdquo;,</p>
                    <p>&nbsp; &nbsp; &nbsp; &nbsp; &ldquo;apellido&rdquo;:&rdquo;Estrada&rdquo;,</p>
                    <p>&nbsp; &nbsp; &nbsp; &nbsp; &ldquo;correo&rdquo;:&rdquo;elian@gmail.com&rdquo;,</p>
                    <p>&nbsp; &nbsp; &nbsp; &nbsp; &ldquo;fechaNacimiento&rdquo;:&rdquo;26/08/2000&rdquo;,</p>
                    <p>&nbsp; &nbsp; &nbsp; &nbsp; &ldquo;foto&rdquo;:&rdquo;https://s3.amazonaws.com/my-bucket/images/image1.jpg&rdquo;,</p>
                    <p>&nbsp; &nbsp; &nbsp; &nbsp; &ldquo;departamento&rdquo;: &ldquo;Guatemala&rdquo;,</p>
                    <p>&nbsp; &nbsp; &nbsp; &nbsp; &ldquo;ciudad&rdquo;: &ldquo;Guatemala&rdquo;,</p>
                    <p>&nbsp; &nbsp; &nbsp; &nbsp; &ldquo;zona&rdquo;: 1,</p>
                    <p>&nbsp; &nbsp; &nbsp; &nbsp; &ldquo;direccion&rdquo;: &ldquo;18ca-6av&rdquo;,</p>
                    <p>&nbsp; &nbsp; }</p>
                    <p>}</p><br>
                    <p>{</p>
                    <p>&nbsp; &nbsp; &quot;estatus&quot;: 200,</p>
                    <p>&nbsp; &nbsp; &ldquo;data&rdquo;: {</p>
                    <p>&nbsp; &nbsp; &nbsp; &nbsp; &ldquo;nombre&rdquo;:&rdquo;Elian&rdquo;,</p>
                    <p>&nbsp; &nbsp; &nbsp; &nbsp; &ldquo;apellido&rdquo;:&rdquo;Estrada&rdquo;,</p>
                    <p>&nbsp; &nbsp; &nbsp; &nbsp; &ldquo;correo&rdquo;:&rdquo;elian@gmail.com&rdquo;,</p>
                    <p>&nbsp; &nbsp; &nbsp; &nbsp; &ldquo;fechaNacimiento&rdquo;:&rdquo;26/08/2000&rdquo;,</p>
                    <p>&nbsp; &nbsp; &nbsp; &nbsp; &ldquo;foto&rdquo;:&rdquo;https://s3.amazonaws.com/my-bucket/images/image1.jpg&rdquo;,</p>
                    <p>&nbsp; &nbsp; &nbsp; &nbsp; &ldquo;departamento&rdquo;: &ldquo;Guatemala&rdquo;,</p>
                    <p>&nbsp; &nbsp; &nbsp; &nbsp; &ldquo;ciudad&rdquo;: &ldquo;Guatemala&rdquo;,</p>
                    <p>&nbsp; &nbsp; &nbsp; &nbsp; &ldquo;zona&rdquo;: 1,</p>
                    <p>&nbsp; &nbsp; &nbsp; &nbsp; &ldquo;direccion&rdquo;: &ldquo;18ca-6av&rdquo;,</p>
                    <p>&nbsp; &nbsp; &nbsp; &nbsp; &ldquo;numeroGrupo&rdquo;: 5,</p>
                    <p>&nbsp; &nbsp; &nbsp; &nbsp; &ldquo;seccion&rdquo;: &ldquo;N&rdquo;</p>
                    <p>&nbsp; &nbsp; }</p>
                    <p>}</p><br>
                    <p>Ejemplo de par&aacute;metros de salida fallida:</p>
                    <p>{</p>
                    <p>&nbsp; &nbsp; &ldquo;estatus&rdquo;: 400,</p>
                    <p>&nbsp; &nbsp; &ldquo;error&rdquo;:&rdquo;Error al hacer la petici&oacute;n&rdquo;,</p>
                    <p>&nbsp; &nbsp; &ldquo;mensaje&rdquo;: &ldquo;Se produjo un error al realizar la petici&oacute;n&rdquo;</p>
                    <p>}</p><br>
                    <p>{</p>
                    <p>&nbsp; &nbsp; &ldquo;estatus&rdquo;: 401,</p>
                    <p>&nbsp; &nbsp; &ldquo;error&rdquo;:&rdquo;No autorizado&rdquo;,</p>
                    <p>&nbsp; &nbsp; &ldquo;mensaje&rdquo;: &ldquo;Error, se ha expirado la sesi&oacute;n, usuario no autorizado&rdquo;</p>
                    <p>}</p><br>
                    <p>{</p>
                    <p>&nbsp; &nbsp; &ldquo;estatus&rdquo;: 404,</p>
                    <p>&nbsp; &nbsp; &ldquo;error&rdquo;:&rdquo;Usuario no encontrado&rdquo;,</p>
                    <p>&nbsp; &nbsp; &ldquo;mensaje&rdquo;: &ldquo;El usuario no existe en el sistema&rdquo;</p>
                    <p>}</p><br>
                    <p>{</p>
                    <p>&nbsp; &nbsp; &ldquo;estatus&rdquo;: 500,</p>
                    <p>&nbsp; &nbsp; &ldquo;error&rdquo;:&rdquo;Error en el servidor&rdquo;,</p>
                    <p>&nbsp; &nbsp; &ldquo;mensaje&rdquo;: &ldquo;No se pudo conectar a la Base de Datos&rdquo;</p>
                    <p>}</p>
                </td>
            </tr>
            <tr></tr>
            <tr></tr>
            <tr></tr>
            <tr></tr>
        </tbody>
    </table>
</div>
<p><br></p>
<p><br></p>
<div align="left">
    <table>
        <tbody>
            <tr>
                <td>
                    <p>ID:&nbsp;06</p>
                </td>
                <td>
                    <p>Nombre:&nbsp;Modificar datos personales</p>
                </td>
            </tr>
            <tr>
                <td>
                    <p>Prioridad:&nbsp;Media</p>
                </td>
                <td rowspan="3">
                    <p>Historia de usuario</p>
                    <p>Se requiere tener la posibilidad de modificar la informaci&oacute;n personal del usuario</p>
                </td>
            </tr>
            <tr>
                <td>
                    <p>Estimado:&nbsp;5 puntos</p>
                </td>
            </tr>
            <tr>
                <td>
                    <p>M&oacute;dulo:&nbsp;Usuario</p>
                </td>
            </tr>
            <tr>
                <td colspan="2" rowspan="5">
                    <p>Criterios de Aceptaci&oacute;n</p><br>
                    <p>El usuario podr&aacute; modificar su informaci&oacute;n personal a trav&eacute;s de un formulario, si cambia su foto de perfil este servicio deber&aacute; conectarse al servicio de almacenamiento para hacer la carga de su archivo.</p><br>
                    <p>El microservicio debe tener la siguiente configuraci&oacute;n:</p>
                    <p>Ruta:&nbsp;/user/modifyProfile</p>
                    <p>M&eacute;todo:&nbsp;PUT</p>
                    <p>Formato de entrada:&nbsp;form-data</p><br>
                    <p>Payload:&nbsp;</p><br>
                    <div align="left">
                        <table>
                            <tbody>
                                <tr>
                                    <td>
                                        <p>Atributo</p>
                                    </td>
                                    <td>
                                        <p>Tipo</p>
                                    </td>
                                    <td>
                                        <p>Descripci&oacute;n</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>cui</p>
                                    </td>
                                    <td>
                                        <p>cadena</p>
                                    </td>
                                    <td>
                                        <p>el n&uacute;mero de identificaci&oacute;n del usuario.</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>tipoUsuario</p>
                                    </td>
                                    <td>
                                        <p>entero</p>
                                    </td>
                                    <td>
                                        <p>El tipo de usuario dentro de la plataforma, este puede ser:&nbsp;</p>
                                        <ul>
                                            <li>
                                                <p>1&nbsp;</p>
                                            </li>
                                            <li>
                                                <p>2</p>
                                            </li>
                                        </ul>
                                        <p>Donde:&nbsp;</p>
                                        <p>1 representa administradores</p>
                                        <p>2 clientes normales</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>exp</p>
                                    </td>
                                    <td>
                                        <p>entero</p>
                                    </td>
                                    <td>
                                        <p>Este representa la fecha de expiraci&oacute;n del token.</p>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div><br>
                    <p>Header:</p><br>
                    <div align="left">
                        <table>
                            <tbody>
                                <tr>
                                    <td>
                                        <p>Atributo</p>
                                    </td>
                                    <td>
                                        <p>Tipo</p>
                                    </td>
                                    <td>
                                        <p>Descripci&oacute;n</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>Content-Type</p>
                                    </td>
                                    <td>
                                        <p>header</p>
                                    </td>
                                    <td>
                                        <p>multipart/form-data</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>Authorization</p>
                                    </td>
                                    <td>
                                        <p>header</p>
                                    </td>
                                    <td>
                                        <p>Bearer &lt;token&gt;</p>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div><br>
                    <p>Body:</p><br>
                    <div align="left">
                        <table>
                            <tbody>
                                <tr>
                                    <td>
                                        <p>Atributo</p>
                                    </td>
                                    <td>
                                        <p>Tipo</p>
                                    </td>
                                    <td>
                                        <p>Descripci&oacute;n</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>idUsuario</p>
                                    </td>
                                    <td>
                                        <p>entero</p>
                                    </td>
                                    <td>
                                        <p>N&uacute;mero de identificaci&oacute;n del usuario en el sistema</p>
                                        <p>Atributo requerido</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>nombre</p>
                                    </td>
                                    <td>
                                        <p>cadena</p>
                                    </td>
                                    <td>
                                        <p>nombre del usuario</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>apellido</p>
                                    </td>
                                    <td>
                                        <p>cadena</p>
                                    </td>
                                    <td>
                                        <p>apellido del usuario</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>fechaNacimiento</p>
                                    </td>
                                    <td>
                                        <p>cadena</p>
                                    </td>
                                    <td>
                                        <p>fecha de nacimiento del usuario</p>
                                        <p>formato a usar: &ldquo;%d/%m/%Y&rdquo;</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>foto</p>
                                    </td>
                                    <td>
                                        <p>file</p>
                                    </td>
                                    <td>
                                        <p>Archivo de imagen, ser&aacute;n soportados las extensiones:&nbsp;</p>
                                        <ul>
                                            <li>
                                                <p>.jpg</p>
                                            </li>
                                            <li>
                                                <p>.png</p>
                                            </li>
                                        </ul>
                                        <p>Atributo opcional</p>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div><br>
                    <p>Formato de salida:&nbsp;JSON</p>
                    <p>C&oacute;digo de respuesta exitosa:&nbsp;HTTP 200</p>
                    <p>Salida:&nbsp;</p><br>
                    <div align="left">
                        <table>
                            <tbody>
                                <tr>
                                    <td>
                                        <p>Atributo</p>
                                    </td>
                                    <td>
                                        <p>Tipo</p>
                                    </td>
                                    <td>
                                        <p>Descripci&oacute;n</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>estatus</p>
                                    </td>
                                    <td>
                                        <p>entero</p>
                                    </td>
                                    <td>
                                        <p>Indica el c&oacute;digo de respuesta</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>mensaje</p>
                                    </td>
                                    <td>
                                        <p>cadena</p>
                                    </td>
                                    <td>
                                        <p>mensaje del proceso realizado</p>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div><br>
                    <p>C&oacute;digo de respuesta fallida:</p><br>
                    <div align="left">
                        <table>
                            <tbody>
                                <tr>
                                    <td>
                                        <p>C&oacute;digo</p>
                                    </td>
                                    <td>
                                        <p>Descripci&oacute;n</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>400</p>
                                    </td>
                                    <td>
                                        <p>Error al interpretar la solicitud</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>401</p>
                                    </td>
                                    <td>
                                        <p>Error, usuario no autorizado</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>404</p>
                                    </td>
                                    <td>
                                        <p>Error, usuario no encontrado o no existe</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>500</p>
                                    </td>
                                    <td>
                                        <p>Error interno del servidor</p>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div><br>
                    <p>Body de Salida:</p><br>
                    <div align="left">
                        <table>
                            <tbody>
                                <tr>
                                    <td>
                                        <p>Atributo</p>
                                    </td>
                                    <td>
                                        <p>Tipo</p>
                                    </td>
                                    <td>
                                        <p>Descripci&oacute;n</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>estatus</p>
                                    </td>
                                    <td>
                                        <p>entero</p>
                                    </td>
                                    <td>
                                        <p>Indica el c&oacute;digo de respuesta</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>error</p>
                                    </td>
                                    <td>
                                        <p>cadena</p>
                                    </td>
                                    <td>
                                        <p>muestra el nombre del error</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>mensaje</p>
                                    </td>
                                    <td>
                                        <p>cadena</p>
                                    </td>
                                    <td>
                                        <p>muestra m&aacute;s informaci&oacute;n del error</p>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div><br>
                    <p>Ejemplos de par&aacute;metros de entrada:</p><br>
                    <div align="left">
                        <table>
                            <tbody>
                                <tr>
                                    <td>
                                        <p>clave</p>
                                    </td>
                                    <td>
                                        <p>valor</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>idUsuario</p>
                                    </td>
                                    <td>
                                        <p>1</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>nombre</p>
                                    </td>
                                    <td>
                                        <p>Elian</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>apellido</p>
                                    </td>
                                    <td>
                                        <p>Estrada</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>fechaNacimiento</p>
                                    </td>
                                    <td>
                                        <p>26/08/2000</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>foto</p>
                                    </td>
                                    <td>
                                        <p>https://s3.amazonaws.com/nombre-del-bucket/nombre-de-la-imagen.jpg</p><br>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div><br>
                    <p>Ejemplos de par&aacute;metros de salida exitosa:</p>
                    <p>{</p>
                    <p>&nbsp; &nbsp; &ldquo;estatus&rdquo;: 200,</p>
                    <p>&nbsp; &nbsp; &ldquo;mensaje&rdquo;: &ldquo;Usuario modificado exitosamente&rdquo;</p>
                    <p>}</p>
                    <p>Ejemplo de par&aacute;metros de salida fallida:</p>
                    <p>{</p>
                    <p>&nbsp; &nbsp; &ldquo;estatus&rdquo;: 401,</p>
                    <p>&nbsp; &nbsp; &ldquo;error&rdquo;:&rdquo;Usuario no Autenticado&rdquo;,</p>
                    <p>&nbsp; &nbsp; &ldquo;mensaje&rdquo;: &ldquo;El token proporcionado no es v&aacute;lido o ya expi&oacute;&rdquo;</p>
                    <p>}</p>
                </td>
            </tr>
            <tr></tr>
            <tr></tr>
            <tr></tr>
            <tr></tr>
        </tbody>
    </table>
</div>
<p><br></p>
<p><br></p>
<div align="left">
    <table>
        <tbody>
            <tr>
                <td>
                    <p>ID:&nbsp;07</p>
                </td>
                <td>
                    <p>Nombre:&nbsp;Cambiar contrase&ntilde;a</p>
                </td>
            </tr>
            <tr>
                <td>
                    <p>Prioridad:&nbsp;Alta</p>
                </td>
                <td rowspan="3">
                    <p>Historia de usuario</p>
                    <p>Es necesario que el usuario pueda actualizar su contrase&ntilde;a cuando lo requiera.</p>
                </td>
            </tr>
            <tr>
                <td>
                    <p>Estimado:&nbsp;3 puntos</p>
                </td>
            </tr>
            <tr>
                <td>
                    <p>M&oacute;dulo:&nbsp;Usuario</p>
                </td>
            </tr>
            <tr>
                <td colspan="2" rowspan="5">
                    <p>Criterios de Aceptaci&oacute;n</p><br>
                    <p>Se podr&aacute; cambiar la contrase&ntilde;a para ingresar al sistema, para ello debe ingresar la contrase&ntilde;a actual para corroborar que sea el usuario.</p><br>
                    <p>El microservicio debe tener la siguiente configuraci&oacute;n:</p><br>
                    <p>Ruta:&nbsp;/user/modifyPassword</p>
                    <p>M&eacute;todo:&nbsp;PUT</p>
                    <p>Formato de entrada:&nbsp;JSON</p><br>
                    <p>Payload:&nbsp;</p><br>
                    <div align="left">
                        <table>
                            <tbody>
                                <tr>
                                    <td>
                                        <p>Atributo</p>
                                    </td>
                                    <td>
                                        <p>Tipo</p>
                                    </td>
                                    <td>
                                        <p>Descripci&oacute;n</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>cui</p>
                                    </td>
                                    <td>
                                        <p>cadena</p>
                                    </td>
                                    <td>
                                        <p>el n&uacute;mero de identificaci&oacute;n del usuario.</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>tipoUsuario</p>
                                    </td>
                                    <td>
                                        <p>entero</p>
                                    </td>
                                    <td>
                                        <p>El tipo de usuario dentro de la plataforma, este puede ser:&nbsp;</p>
                                        <ul>
                                            <li>
                                                <p>1&nbsp;</p>
                                            </li>
                                            <li>
                                                <p>2</p>
                                            </li>
                                        </ul>
                                        <p>Donde:&nbsp;</p>
                                        <p>1 representa administradores</p>
                                        <p>2 clientes normales</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>exp</p>
                                    </td>
                                    <td>
                                        <p>entero</p>
                                    </td>
                                    <td>
                                        <p>Este representa la fecha de expiraci&oacute;n del token.</p>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div><br>
                    <p>Header:</p><br>
                    <div align="left">
                        <table>
                            <tbody>
                                <tr>
                                    <td>
                                        <p>Atributo</p>
                                    </td>
                                    <td>
                                        <p>Tipo</p>
                                    </td>
                                    <td>
                                        <p>Descripci&oacute;n</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>Content-Type</p>
                                    </td>
                                    <td>
                                        <p>header</p>
                                    </td>
                                    <td>
                                        <p>application/json</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>Authorization</p>
                                    </td>
                                    <td>
                                        <p>header</p>
                                    </td>
                                    <td>
                                        <p>Bearer &lt;token&gt;</p>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div><br>
                    <p>Body:</p><br>
                    <div align="left">
                        <table>
                            <tbody>
                                <tr>
                                    <td>
                                        <p>Atributo</p>
                                    </td>
                                    <td>
                                        <p>Tipo</p>
                                    </td>
                                    <td>
                                        <p>Descripci&oacute;n</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>idUsuario</p>
                                    </td>
                                    <td>
                                        <p>entero</p>
                                    </td>
                                    <td>
                                        <p>N&uacute;mero que identifica al usuario</p>
                                        <p>Atributo Requerido</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>passwordActual</p>
                                    </td>
                                    <td>
                                        <p>cadena</p>
                                    </td>
                                    <td>
                                        <p>Se debe ingresar la contrase&ntilde;a actual del usuario</p>
                                        <p>Atributo Requerido</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>passwordNueva</p>
                                    </td>
                                    <td>
                                        <p>cadena</p>
                                    </td>
                                    <td>
                                        <p>Se debe ingresar la nueva contrase&ntilde;a del usuario</p>
                                        <p>Atributo Requerido</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>confirmarPassword</p>
                                    </td>
                                    <td>
                                        <p>cadena</p>
                                    </td>
                                    <td>
                                        <p>Se debe ingresar nuevamente la contrase&ntilde;a del campo &ldquo;nueva contrase&ntilde;a&rdquo; para asegurar la cadena propuesta por el usuario</p>
                                        <p>Atributo Requerido</p>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div><br>
                    <p>Formato de salida:&nbsp;JSON</p>
                    <p>C&oacute;digo de respuesta exitosa:&nbsp;HTTP 200</p>
                    <p>Salida:&nbsp;</p><br>
                    <div align="left">
                        <table>
                            <tbody>
                                <tr>
                                    <td>
                                        <p>Atributo</p>
                                    </td>
                                    <td>
                                        <p>Tipo</p>
                                    </td>
                                    <td>
                                        <p>Descripci&oacute;n</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>estatus</p>
                                    </td>
                                    <td>
                                        <p>entero</p>
                                    </td>
                                    <td>
                                        <p>Indica el c&oacute;digo de respuesta</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>mensaje</p>
                                    </td>
                                    <td>
                                        <p>cadena</p>
                                    </td>
                                    <td>
                                        <p>mensaje del proceso realizado</p>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div><br>
                    <p>C&oacute;digo de respuesta fallida:</p><br>
                    <div align="left">
                        <table>
                            <tbody>
                                <tr>
                                    <td>
                                        <p>C&oacute;digo</p>
                                    </td>
                                    <td>
                                        <p>Descripci&oacute;n</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>400</p>
                                    </td>
                                    <td>
                                        <p>Error al interpretar la solicitud</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>401</p>
                                    </td>
                                    <td>
                                        <p>Error, usuario no autorizado</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>404</p>
                                    </td>
                                    <td>
                                        <p>Error, usuario no encontrado o no existe</p>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div><br><br>
                    <p>Body de Salida:</p><br>
                    <div align="left">
                        <table>
                            <tbody>
                                <tr>
                                    <td>
                                        <p>Atributo</p>
                                    </td>
                                    <td>
                                        <p>Tipo</p>
                                    </td>
                                    <td>
                                        <p>Descripci&oacute;n</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>estatus</p>
                                    </td>
                                    <td>
                                        <p>entero</p>
                                    </td>
                                    <td>
                                        <p>Indica el c&oacute;digo de respuesta</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>error</p>
                                    </td>
                                    <td>
                                        <p>cadena</p>
                                    </td>
                                    <td>
                                        <p>muestra el nombre del error</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>mensaje</p>
                                    </td>
                                    <td>
                                        <p>cadena</p>
                                    </td>
                                    <td>
                                        <p>muestra m&aacute;s informaci&oacute;n del error</p>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div><br>
                    <p>Ejemplos de par&aacute;metros de entrada:</p>
                    <p>{</p>
                    <p>&nbsp; &quot;idUsuario&quot;: 1,</p>
                    <p>&nbsp; &quot;passwordActual&quot;: &quot;123456&quot;,</p>
                    <p>&nbsp; &quot;passwordNueva&quot;: &quot;789456&quot;,</p>
                    <p>&nbsp; &quot;confirmarPassword&quot;: &quot;789456&quot;</p>
                    <p>}</p><br>
                    <p>Ejemplos de par&aacute;metros de salida exitosa:</p>
                    <p>{</p>
                    <p>&nbsp; &nbsp; &ldquo;estatus&rdquo;: 200,</p>
                    <p>&nbsp; &nbsp; &ldquo;mensaje&rdquo;: &ldquo;La nueva contrase&ntilde;a se han configurado con &eacute;xito&rdquo;</p>
                    <p>}</p>
                    <p>Ejemplo de par&aacute;metros de salida fallida:</p>
                    <p>{</p>
                    <p>&nbsp; &nbsp; &ldquo;estatus&rdquo;: 401,</p>
                    <p>&nbsp; &nbsp; &ldquo;error&rdquo;:&rdquo;Usuario no autenticado&rdquo;,</p>
                    <p>&nbsp; &nbsp; &ldquo;mensaje&rdquo;: &ldquo;El token del usuario no es v&aacute;lido o ya expir&oacute;&rdquo;</p>
                    <p>}</p>
                </td>
            </tr>
            <tr></tr>
            <tr></tr>
            <tr></tr>
            <tr></tr>
        </tbody>
    </table>
</div>
<p><br></p>
<p><br></p>
<div align="left">
    <table>
        <tbody>
            <tr>
                <td>
                    <p>ID:&nbsp;08</p>
                </td>
                <td>
                    <p>Nombre:&nbsp;Dar de baja la cuenta</p>
                </td>
            </tr>
            <tr>
                <td>
                    <p>Prioridad:&nbsp;Media</p>
                </td>
                <td rowspan="3">
                    <p>Historia de usuario</p>
                    <p>Es importante que el usuario pueda darse de baja en cualquier momento</p>
                </td>
            </tr>
            <tr>
                <td>
                    <p>Estimado:&nbsp;2 puntos</p>
                </td>
            </tr>
            <tr>
                <td>
                    <p>M&oacute;dulo:&nbsp;Usuario</p>
                </td>
            </tr>
            <tr>
                <td colspan="2" rowspan="5">
                    <p>Criterios de Aceptaci&oacute;n</p><br>
                    <p>El usuario podr&aacute; darse de baja del sistema, sin embargo, en el sistema &uacute;nicamente estar&aacute; deshabilitado, esto con el fin de no perder la informaci&oacute;n generada por este usuario, como compras, entregas, etc.</p><br>
                    <p>El microservicio debe tener la siguiente configuraci&oacute;n:</p><br>
                    <p>Ruta:&nbsp;/user/unsubscribe</p>
                    <p>M&eacute;todo:&nbsp;PUT</p>
                    <p>Formato de entrada:&nbsp;JSON</p><br>
                    <p>Payload:&nbsp;</p><br>
                    <div align="left">
                        <table>
                            <tbody>
                                <tr>
                                    <td>
                                        <p>Atributo</p>
                                    </td>
                                    <td>
                                        <p>Tipo</p>
                                    </td>
                                    <td>
                                        <p>Descripci&oacute;n</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>cui</p>
                                    </td>
                                    <td>
                                        <p>cadena</p>
                                    </td>
                                    <td>
                                        <p>el n&uacute;mero de identificaci&oacute;n del usuario.</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>tipoUsuario</p>
                                    </td>
                                    <td>
                                        <p>entero</p>
                                    </td>
                                    <td>
                                        <p>El tipo de usuario dentro de la plataforma, este puede ser:&nbsp;</p>
                                        <ul>
                                            <li>
                                                <p>1&nbsp;</p>
                                            </li>
                                            <li>
                                                <p>2</p>
                                            </li>
                                        </ul>
                                        <p>Donde:&nbsp;</p>
                                        <p>1 representa administradores</p>
                                        <p>2 clientes normales</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>exp</p>
                                    </td>
                                    <td>
                                        <p>entero</p>
                                    </td>
                                    <td>
                                        <p>Este representa la fecha de expiraci&oacute;n del token.</p>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div><br>
                    <p>Header:</p><br>
                    <div align="left">
                        <table>
                            <tbody>
                                <tr>
                                    <td>
                                        <p>Atributo</p>
                                    </td>
                                    <td>
                                        <p>Tipo</p>
                                    </td>
                                    <td>
                                        <p>Descripci&oacute;n</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>Content-Type</p>
                                    </td>
                                    <td>
                                        <p>header</p>
                                    </td>
                                    <td>
                                        <p>application/json</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>Authorization</p>
                                    </td>
                                    <td>
                                        <p>header</p>
                                    </td>
                                    <td>
                                        <p>Bearer &lt;token&gt;</p>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div><br>
                    <p>Body:</p><br>
                    <div align="left">
                        <table>
                            <tbody>
                                <tr>
                                    <td>
                                        <p>Atributo</p>
                                    </td>
                                    <td>
                                        <p>Tipo</p>
                                    </td>
                                    <td>
                                        <p>Descripci&oacute;n</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>idUsuario</p>
                                    </td>
                                    <td>
                                        <p>entero</p>
                                    </td>
                                    <td>
                                        <p>N&uacute;mero que identifica al usuario</p>
                                        <p>Atributo Requerido</p>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div><br>
                    <p>Formato de salida:&nbsp;JSON</p>
                    <p>C&oacute;digo de respuesta exitosa:&nbsp;HTTP 200</p>
                    <p>Salida:&nbsp;</p><br>
                    <div align="left">
                        <table>
                            <tbody>
                                <tr>
                                    <td>
                                        <p>Atributo</p>
                                    </td>
                                    <td>
                                        <p>Tipo</p>
                                    </td>
                                    <td>
                                        <p>Descripci&oacute;n</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>estatus</p>
                                    </td>
                                    <td>
                                        <p>entero</p>
                                    </td>
                                    <td>
                                        <p>Indica el c&oacute;digo de respuesta</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>mensaje</p>
                                    </td>
                                    <td>
                                        <p>cadena</p>
                                    </td>
                                    <td>
                                        <p>mensaje del proceso realizado</p>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div><br>
                    <p>C&oacute;digo de respuesta fallida:</p><br>
                    <div align="left">
                        <table>
                            <tbody>
                                <tr>
                                    <td>
                                        <p>C&oacute;digo</p>
                                    </td>
                                    <td>
                                        <p>Descripci&oacute;n</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>400</p>
                                    </td>
                                    <td>
                                        <p>Error al interpretar la solicitud</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>401</p>
                                    </td>
                                    <td>
                                        <p>Error, usuario no autorizado</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>404</p>
                                    </td>
                                    <td>
                                        <p>Error, usuario no encontrado o no existe</p>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div><br><br>
                    <p>Body de Salida:</p><br>
                    <div align="left">
                        <table>
                            <tbody>
                                <tr>
                                    <td>
                                        <p>Atributo</p>
                                    </td>
                                    <td>
                                        <p>Tipo</p>
                                    </td>
                                    <td>
                                        <p>Descripci&oacute;n</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>estatus</p>
                                    </td>
                                    <td>
                                        <p>entero</p>
                                    </td>
                                    <td>
                                        <p>Indica el c&oacute;digo de respuesta</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>error</p>
                                    </td>
                                    <td>
                                        <p>cadena</p>
                                    </td>
                                    <td>
                                        <p>muestra el nombre del error</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>mensaje</p>
                                    </td>
                                    <td>
                                        <p>cadena</p>
                                    </td>
                                    <td>
                                        <p>muestra m&aacute;s informaci&oacute;n del error</p>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div><br>
                    <p>Ejemplos de par&aacute;metros de entrada:</p>
                    <p>{</p>
                    <p>&nbsp; &quot;idUsuario&quot;: 1</p>
                    <p>}</p><br>
                    <p>Ejemplos de par&aacute;metros de salida exitosa:</p>
                    <p>{</p>
                    <p>&nbsp; &nbsp; &ldquo;estatus&rdquo;: 200,</p>
                    <p>&nbsp; &nbsp; &ldquo;mensaje&rdquo;: &ldquo;El usuario ha sido de baja exitosamente&rdquo;</p>
                    <p>}</p>
                    <p>Ejemplo de par&aacute;metros de salida fallida:</p>
                    <p>{</p>
                    <p>&nbsp; &nbsp; &ldquo;estatus&rdquo;: 401,</p>
                    <p>&nbsp; &nbsp; &ldquo;error&rdquo;:&rdquo;Usuario no autenticado&rdquo;,</p>
                    <p>&nbsp; &nbsp; &ldquo;mensaje&rdquo;: &ldquo;El token del usuario no es v&aacute;lido o ya expir&oacute;&rdquo;</p>
                    <p>}</p>
                </td>
            </tr>
            <tr></tr>
            <tr></tr>
            <tr></tr>
            <tr></tr>
        </tbody>
    </table>
</div>
<p><br></p>
<p><br></p>
<div align="left">
    <table>
        <tbody>
            <tr>
                <td>
                    <p>ID:&nbsp;09</p>
                </td>
                <td>
                    <p>Nombre:&nbsp;Agregar usuario</p>
                </td>
            </tr>
            <tr>
                <td>
                    <p>Prioridad:&nbsp;Alta</p>
                </td>
                <td rowspan="3">
                    <p>Historia de usuario</p>
                    <p>Es necesario que los usuarios administrativos sean creados a trav&eacute;s del m&oacute;dulo de recursos humanos, para registrar los nuevos ingresos</p>
                </td>
            </tr>
            <tr>
                <td>
                    <p>Estimado:&nbsp;3 puntos</p>
                </td>
            </tr>
            <tr>
                <td>
                    <p>M&oacute;dulo:&nbsp;Recursos humanos</p>
                </td>
            </tr>
            <tr>
                <td colspan="2" rowspan="5">
                    <p>Criterios de Aceptaci&oacute;n</p><br>
                    <p>El microservicio retorna un c&oacute;digo 200 con un mensaje satisfactorio al agregar de manera exitosa un usuario administrativos, para los siguientes casos se retornar&aacute; un c&oacute;digo de error con informaci&oacute;n del mismo:</p>
                    <ul>
                        <li>
                            <p>No se llenen los campos obligatorios</p>
                        </li>
                        <li>
                            <p>El usuario ya existe en el sistema</p>
                        </li>
                        <li>
                            <p>La confirmaci&oacute;n del password no coincide.</p>
                        </li>
                    </ul><br>
                    <p>El microservicio debe tener la siguiente configuraci&oacute;n:</p>
                    <p>Ruta:&nbsp;/rrhh/agregarUsuario</p>
                    <p>M&eacute;todo:&nbsp;POST</p>
                    <p>Formato de entrada:&nbsp;form-data</p><br>
                    <p>Payload:&nbsp;</p>
                    <div align="left">
                        <table>
                            <tbody>
                                <tr>
                                    <td>
                                        <p>Atributo</p>
                                    </td>
                                    <td>
                                        <p>Tipo</p>
                                    </td>
                                    <td>
                                        <p>Descripci&oacute;n</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>cui</p>
                                    </td>
                                    <td>
                                        <p>cadena</p>
                                    </td>
                                    <td>
                                        <p>el n&uacute;mero de identificaci&oacute;n del usuario.</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>tipoUsuario</p>
                                    </td>
                                    <td>
                                        <p>entero</p>
                                    </td>
                                    <td>
                                        <p>El tipo de usuario dentro de la plataforma, este puede ser:&nbsp;</p>
                                        <ul>
                                            <li>
                                                <p>1&nbsp;</p>
                                            </li>
                                            <li>
                                                <p>2</p>
                                            </li>
                                        </ul>
                                        <p>Donde:&nbsp;</p>
                                        <p>1 representa administradores</p>
                                        <p>2 clientes normales</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>exp</p>
                                    </td>
                                    <td>
                                        <p>entero</p>
                                    </td>
                                    <td>
                                        <p>Este representa la fecha de expiraci&oacute;n del token.</p>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div><br><br>
                    <p>Header:</p>
                    <div align="left">
                        <table>
                            <tbody>
                                <tr>
                                    <td>
                                        <p>Atributo</p>
                                    </td>
                                    <td>
                                        <p>Tipo</p>
                                    </td>
                                    <td>
                                        <p>Descripci&oacute;n</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>Content-Type</p>
                                    </td>
                                    <td>
                                        <p>header</p>
                                    </td>
                                    <td>
                                        <p>multipart/form-data</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>Authorization</p>
                                    </td>
                                    <td>
                                        <p>header</p>
                                    </td>
                                    <td>
                                        <p>Bearer &lt;token&gt;</p>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                    <p>Body:</p>
                    <div align="left">
                        <table>
                            <tbody>
                                <tr>
                                    <td>
                                        <p>Atributo</p>
                                    </td>
                                    <td>
                                        <p>Tipo</p>
                                    </td>
                                    <td>
                                        <p>Descripci&oacute;n</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>cui</p>
                                    </td>
                                    <td>
                                        <p>entero</p>
                                    </td>
                                    <td>
                                        <p>identificaci&oacute;n del usuario</p>
                                        <p>Campo obligatorio</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>correo</p>
                                    </td>
                                    <td>
                                        <p>cadena</p>
                                    </td>
                                    <td>
                                        <p>correo electr&oacute;nico del usuario</p>
                                        <p>Campo obligatorio</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>nombre</p>
                                    </td>
                                    <td>
                                        <p>cadena</p>
                                    </td>
                                    <td>
                                        <p>contrase&ntilde;a del usuario</p>
                                        <p>Campo obligatorio</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>password</p>
                                    </td>
                                    <td>
                                        <p>cadena</p>
                                    </td>
                                    <td>
                                        <p>contrase&ntilde;a del usuario</p>
                                        <p>Campo obligatorio</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>confirmacionPassword</p>
                                    </td>
                                    <td>
                                        <p>cadena</p>
                                    </td>
                                    <td>
                                        <p>confirmaci&oacute;n de la contrase&ntilde;a del usuario</p>
                                        <p>Campo obligatorio</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>areaAsignada</p>
                                    </td>
                                    <td>
                                        <p>cadena</p>
                                    </td>
                                    <td>
                                        <p>&aacute;rea que se le asignar&aacute; al usuario administrativo</p>
                                        <p>Campo obligatorio</p>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div><br>
                    <p>Formato de salida:&nbsp;JSON</p>
                    <p>C&oacute;digo de respuesta exitosa:&nbsp;HTTP 200</p>
                    <p>Salida:&nbsp;</p><br>
                    <div align="left">
                        <table>
                            <tbody>
                                <tr>
                                    <td>
                                        <p>Atributo</p>
                                    </td>
                                    <td>
                                        <p>Tipo</p>
                                    </td>
                                    <td>
                                        <p>Descripci&oacute;n</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>estatus</p>
                                    </td>
                                    <td>
                                        <p>entero</p>
                                    </td>
                                    <td>
                                        <p>indica el c&oacute;digo de respuesta de aceptaci&oacute;n</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>mensaje</p>
                                    </td>
                                    <td>
                                        <p>cadena</p>
                                    </td>
                                    <td>
                                        <p>muestra informaci&oacute;n del registro del usuario administrativo</p>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div><br>
                    <p>C&oacute;digo de respuesta fallida:</p><br>
                    <div align="left">
                        <table>
                            <tbody>
                                <tr>
                                    <td>
                                        <p>C&oacute;digo</p>
                                    </td>
                                    <td>
                                        <p>Descripci&oacute;n</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>400</p>
                                    </td>
                                    <td>
                                        <p>Error al interpretar la solicitud</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>401</p>
                                    </td>
                                    <td>
                                        <p>Usuario no autenticado</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>403</p>
                                    </td>
                                    <td>
                                        <p>Usuario sin permisos</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>500</p>
                                    </td>
                                    <td>
                                        <p>Error interno del servidor</p>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div><br>
                    <p>Body de Salida:</p><br>
                    <div align="left">
                        <table>
                            <tbody>
                                <tr>
                                    <td>
                                        <p>Atributo</p>
                                    </td>
                                    <td>
                                        <p>Tipo</p>
                                    </td>
                                    <td>
                                        <p>Descripci&oacute;n</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>estatus</p>
                                    </td>
                                    <td>
                                        <p>entero</p>
                                    </td>
                                    <td>
                                        <p>indica el c&oacute;digo de respuesta fallido</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>error</p>
                                    </td>
                                    <td>
                                        <p>cadena</p>
                                    </td>
                                    <td>
                                        <p>muestra el nombre del error</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>mensaje</p>
                                    </td>
                                    <td>
                                        <p>cadena</p>
                                    </td>
                                    <td>
                                        <p>muestra m&aacute;s informaci&oacute;n del error</p>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div><br>
                    <p>Ejemplos de par&aacute;metros de entrada:</p><br>
                    <div align="left">
                        <table>
                            <tbody>
                                <tr>
                                    <td>
                                        <p>cui</p>
                                    </td>
                                    <td>
                                        <p>2994902460101</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>correo</p>
                                    </td>
                                    <td>
                                        <p>m@gmail.com</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>nombre</p>
                                    </td>
                                    <td>
                                        <p>Mynor</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>password</p>
                                    </td>
                                    <td>
                                        <p>P@$$w0rD</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>confirmacionPassword</p>
                                    </td>
                                    <td>
                                        <p>P@$$w0rD</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>areaAsignada</p>
                                    </td>
                                    <td>
                                        <p>contabilidad</p>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div><br>
                    <p>Ejemplos de par&aacute;metros de salida exitosa:</p>
                    <p>{</p>
                    <p>&nbsp; &nbsp; &ldquo;estatus&rdquo;: 200,</p>
                    <p>&nbsp; &nbsp; &ldquo;mensaje&rdquo;: &ldquo;Se creo el usuario administrativo de manera exitosa&rdquo;</p>
                    <p>}</p>
                    <p>Ejemplo de par&aacute;metros de salida fallida:</p>
                    <p>{</p>
                    <p>&nbsp; &nbsp; &ldquo;estatus&rdquo;: 400</p>
                    <p>&nbsp; &nbsp; &ldquo;error&rdquo;:&rdquo;Fall&oacute; la confirmaci&oacute;n del password&rdquo;,</p>
                    <p>&nbsp; &nbsp; &ldquo;mensaje&rdquo;:&rdquo;Las contrase&ntilde;as deben de coincidir&rdquo;</p>
                    <p>}</p><br>
                    <p>{</p>
                    <p>&nbsp; &nbsp; &ldquo;estatus&rdquo;: 403</p>
                    <p>&nbsp; &nbsp; &ldquo;error&rdquo;:&rdquo;Usuario sin permisos&rdquo;,</p>
                    <p>&nbsp; &nbsp; &ldquo;mensaje&rdquo;:&rdquo;El usuario no tiene permisos para crear usuarios administrativos, solamente el personal de rrhh tiene permisos asignados&rdquo;</p>
                    <p>}</p>
                </td>
            </tr>
            <tr></tr>
            <tr></tr>
            <tr></tr>
            <tr></tr>
        </tbody>
    </table>
</div>
<p><br></p>
<p><br></p>
<p><br></p>
<div align="left">
    <table>
        <tbody>
            <tr>
                <td>
                    <p>ID:&nbsp;10</p>
                </td>
                <td>
                    <p>Nombre:&nbsp;Dar de baja usuarios administrativos</p>
                </td>
            </tr>
            <tr>
                <td>
                    <p>Prioridad:&nbsp;Media</p>
                </td>
                <td rowspan="3">
                    <p>Historia de usuario</p>
                    <p>Es necesario que el personal de recursos humanos pueda dar de baja a los usuarios administrativos necesarios.</p>
                </td>
            </tr>
            <tr>
                <td>
                    <p>Estimado:&nbsp;2 puntos</p>
                </td>
            </tr>
            <tr>
                <td>
                    <p>M&oacute;dulo:&nbsp;Recursos humanos</p>
                </td>
            </tr>
            <tr>
                <td colspan="2" rowspan="5">
                    <p>Criterios de Aceptaci&oacute;n</p><br>
                    <p>El microservicio retorna un c&oacute;digo 200 con un mensaje satisfactorio al dar de baja a un usuario administrativo de manera exitosa, para los siguientes casos se retornar&aacute; un c&oacute;digo de error con informaci&oacute;n del mismo:</p>
                    <ul>
                        <li>
                            <p>No exista el usuario administrativo</p>
                        </li>
                        <li>
                            <p>El usuario administrativo est&eacute; en un estado inactivo</p>
                        </li>
                    </ul><br>
                    <p>El microservicio debe tener la siguiente configuraci&oacute;n:</p><br>
                    <p>Ruta:&nbsp;/rrhh/eliminarUsuarioAdmin</p>
                    <p>M&eacute;todo:&nbsp;Put</p>
                    <p>Formato de entrada:&nbsp;form-data</p><br>
                    <p>Payload:&nbsp;</p>
                    <div align="left">
                        <table>
                            <tbody>
                                <tr>
                                    <td>
                                        <p>Atributo</p>
                                    </td>
                                    <td>
                                        <p>Tipo</p>
                                    </td>
                                    <td>
                                        <p>Descripci&oacute;n</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>cui</p>
                                    </td>
                                    <td>
                                        <p>cadena</p>
                                    </td>
                                    <td>
                                        <p>el n&uacute;mero de identificaci&oacute;n del usuario.</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>tipoUsuario</p>
                                    </td>
                                    <td>
                                        <p>entero</p>
                                    </td>
                                    <td>
                                        <p>El tipo de usuario dentro de la plataforma, este puede ser:&nbsp;</p>
                                        <ul>
                                            <li>
                                                <p>1&nbsp;</p>
                                            </li>
                                            <li>
                                                <p>2</p>
                                            </li>
                                        </ul>
                                        <p>Donde:&nbsp;</p>
                                        <p>1 representa administradores</p>
                                        <p>2 clientes normales</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>exp</p>
                                    </td>
                                    <td>
                                        <p>entero</p>
                                    </td>
                                    <td>
                                        <p>Este representa la fecha de expiraci&oacute;n del token.</p>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div><br><br>
                    <p>Header:</p><br>
                    <div align="left">
                        <table>
                            <tbody>
                                <tr>
                                    <td>
                                        <p>Atributo</p>
                                    </td>
                                    <td>
                                        <p>Tipo</p>
                                    </td>
                                    <td>
                                        <p>Descripci&oacute;n</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>Content-Type</p>
                                    </td>
                                    <td>
                                        <p>header</p>
                                    </td>
                                    <td>
                                        <p>multipart/form-data</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>Authorization</p>
                                    </td>
                                    <td>
                                        <p>header</p>
                                    </td>
                                    <td>
                                        <p>Bearer &lt;token&gt;</p>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                    <p>Body:</p><br>
                    <div align="left">
                        <table>
                            <tbody>
                                <tr>
                                    <td>
                                        <p>Atributo</p>
                                    </td>
                                    <td>
                                        <p>Tipo</p>
                                    </td>
                                    <td>
                                        <p>Descripci&oacute;n</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>cui</p>
                                    </td>
                                    <td>
                                        <p>entero</p>
                                    </td>
                                    <td>
                                        <p>identificaci&oacute;n del usuario</p>
                                        <p>Campo obligatorio</p>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div><br>
                    <p>Formato de salida:&nbsp;JSON</p>
                    <p>C&oacute;digo de respuesta exitosa:&nbsp;HTTP 200</p>
                    <p>Salida:&nbsp;</p><br>
                    <div align="left">
                        <table>
                            <tbody>
                                <tr>
                                    <td>
                                        <p>Atributo</p>
                                    </td>
                                    <td>
                                        <p>Tipo</p>
                                    </td>
                                    <td>
                                        <p>Descripci&oacute;n</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>estatus</p>
                                    </td>
                                    <td>
                                        <p>entero</p>
                                    </td>
                                    <td>
                                        <p>indica el c&oacute;digo de respuesta de aceptaci&oacute;n</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>mensaje</p>
                                    </td>
                                    <td>
                                        <p>cadena</p>
                                    </td>
                                    <td>
                                        <p>muestra informaci&oacute;n de la eliminaci&oacute;n del usuario administrativo</p>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div><br>
                    <p>C&oacute;digo de respuesta fallida:</p><br>
                    <div align="left">
                        <table>
                            <tbody>
                                <tr>
                                    <td>
                                        <p>C&oacute;digo</p>
                                    </td>
                                    <td>
                                        <p>Descripci&oacute;n</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>400</p>
                                    </td>
                                    <td>
                                        <p>Error al interpretar la solicitud</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>401</p>
                                    </td>
                                    <td>
                                        <p>Usuario no autenticado</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>403</p>
                                    </td>
                                    <td>
                                        <p>Usuario sin permisos</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>500</p>
                                    </td>
                                    <td>
                                        <p>Error interno del servidor</p>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div><br>
                    <p>Body de Salida:</p><br>
                    <div align="left">
                        <table>
                            <tbody>
                                <tr>
                                    <td>
                                        <p>Atributo</p>
                                    </td>
                                    <td>
                                        <p>Tipo</p>
                                    </td>
                                    <td>
                                        <p>Descripci&oacute;n</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>estatus</p>
                                    </td>
                                    <td>
                                        <p>entero</p>
                                    </td>
                                    <td>
                                        <p>indica el c&oacute;digo de respuesta fallido</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>error</p>
                                    </td>
                                    <td>
                                        <p>cadena</p>
                                    </td>
                                    <td>
                                        <p>muestra el nombre del error</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>mensaje</p>
                                    </td>
                                    <td>
                                        <p>cadena</p>
                                    </td>
                                    <td>
                                        <p>muestra m&aacute;s informaci&oacute;n del error</p>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div><br><br><br>
                    <p>Ejemplos de par&aacute;metros de entrada:</p><br>
                    <div align="left">
                        <table>
                            <tbody>
                                <tr>
                                    <td>
                                        <p>cui</p>
                                    </td>
                                    <td>
                                        <p>2994902460101</p>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div><br>
                    <p>Ejemplos de par&aacute;metros de salida exitosa:</p>
                    <p>{</p>
                    <p>&nbsp; &nbsp; &ldquo;estatus&rdquo;: 200,</p>
                    <p>&nbsp; &nbsp; &ldquo;mensaje&rdquo;: &ldquo;Se dio de baja a el usuario administrativo de manera exitosa&rdquo;</p>
                    <p>}</p>
                    <p>Ejemplo de par&aacute;metros de salida fallida:</p>
                    <p>{</p>
                    <p>&nbsp; &nbsp; &ldquo;estatus&rdquo;: 400</p>
                    <p>&nbsp; &nbsp; &ldquo;error&rdquo;:&rdquo;Fall&oacute; de cui&rdquo;,</p>
                    <p>&nbsp; &nbsp; &ldquo;mensaje&rdquo;:&rdquo;El CUI no es v&aacute;lido, debe ser un n&uacute;mero de 13 d&iacute;gitos&rdquo;</p>
                    <p>}</p><br>
                    <p>{</p>
                    <p>&nbsp; &nbsp; &ldquo;estatus&rdquo;: 403</p>
                    <p>&nbsp; &nbsp; &ldquo;error&rdquo;:&rdquo;Usuario sin permisos&rdquo;,</p>
                    <p>&nbsp; &nbsp; &ldquo;mensaje&rdquo;:&rdquo;El usuario no tiene permisos para dar de baja a los usuarios administrativos, solamente el personal de rrhh tiene permisos asignados&rdquo;</p>
                    <p>}</p>
                </td>
            </tr>
            <tr></tr>
            <tr></tr>
            <tr></tr>
            <tr></tr>
        </tbody>
    </table>
</div>
<p><br></p>
<p><br></p>
<div align="left">
    <table>
        <tbody>
            <tr>
                <td>
                    <p>ID:&nbsp;11</p>
                </td>
                <td>
                    <p>Nombre:&nbsp;Agendar entrevistas</p>
                </td>
            </tr>
            <tr>
                <td>
                    <p>Prioridad:&nbsp;Media</p>
                </td>
                <td rowspan="3">
                    <p>Historia de usuario</p>
                    <p>Es necesario que el personal de recursos humanos pueda agendar las citas de las entrevistas con los candidatos para los puestos laborales.</p>
                </td>
            </tr>
            <tr>
                <td>
                    <p>Estimado:&nbsp;3 puntos</p>
                </td>
            </tr>
            <tr>
                <td>
                    <p>M&oacute;dulo:&nbsp;Recursos humanos</p>
                </td>
            </tr>
            <tr>
                <td colspan="2" rowspan="5">
                    <p>Criterios de Aceptaci&oacute;n</p>
                    <p>El microservicio retorna un c&oacute;digo 200 con un mensaje satisfactorio al agendar la entrevista y enviar un correo electr&oacute;nico de manera exitosa al candidato con la informaci&oacute;n de la entrevista, para los siguientes casos se retornar&aacute; un c&oacute;digo de error con informaci&oacute;n del mismo:</p>
                    <ul>
                        <li>
                            <p>No exista el correo electr&oacute;nico</p>
                        </li>
                        <li>
                            <p>Se ingrese una fecha no v&aacute;lida para la cita</p>
                        </li>
                    </ul><br>
                    <p>El microservicio debe tener la siguiente configuraci&oacute;n:</p>
                    <p>Ruta:&nbsp;/rrhh/agendarEntrevista</p>
                    <p>M&eacute;todo:&nbsp;POST</p>
                    <p>Formato de entrada:&nbsp;form-data</p><br>
                    <p>Payload:&nbsp;</p><br>
                    <div align="left">
                        <table>
                            <tbody>
                                <tr>
                                    <td>
                                        <p>Atributo</p>
                                    </td>
                                    <td>
                                        <p>Tipo</p>
                                    </td>
                                    <td>
                                        <p>Descripci&oacute;n</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>cui</p>
                                    </td>
                                    <td>
                                        <p>cadena</p>
                                    </td>
                                    <td>
                                        <p>el n&uacute;mero de identificaci&oacute;n del usuario.</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>tipoUsuario</p>
                                    </td>
                                    <td>
                                        <p>entero</p>
                                    </td>
                                    <td>
                                        <p>El tipo de usuario dentro de la plataforma, este puede ser:&nbsp;</p>
                                        <ul>
                                            <li>
                                                <p>1&nbsp;</p>
                                            </li>
                                            <li>
                                                <p>2</p>
                                            </li>
                                        </ul>
                                        <p>Donde:&nbsp;</p>
                                        <p>1 representa administradores</p>
                                        <p>2 clientes normales</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>exp</p>
                                    </td>
                                    <td>
                                        <p>entero</p>
                                    </td>
                                    <td>
                                        <p>Este representa la fecha de expiraci&oacute;n del token.</p>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div><br>
                    <p>Header:</p><br>
                    <div align="left">
                        <table>
                            <tbody>
                                <tr>
                                    <td>
                                        <p>Atributo</p>
                                    </td>
                                    <td>
                                        <p>Tipo</p>
                                    </td>
                                    <td>
                                        <p>Descripci&oacute;n</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>Content-Type</p>
                                    </td>
                                    <td>
                                        <p>header</p>
                                    </td>
                                    <td>
                                        <p>multipart/form-data</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>Authorization</p>
                                    </td>
                                    <td>
                                        <p>header</p>
                                    </td>
                                    <td>
                                        <p>Bearer &lt;token&gt;</p>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div><br>
                    <p>Body:</p>
                    <div align="left">
                        <table>
                            <tbody>
                                <tr>
                                    <td>
                                        <p>Atributo</p>
                                    </td>
                                    <td>
                                        <p>Tipo</p>
                                    </td>
                                    <td>
                                        <p>Descripci&oacute;n</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>cui</p>
                                    </td>
                                    <td>
                                        <p>entero</p>
                                    </td>
                                    <td>
                                        <p>identificaci&oacute;n del candidato a entrevistar</p>
                                        <p>Campo obligatorio</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>nombre</p>
                                    </td>
                                    <td>
                                        <p>cadena</p>
                                    </td>
                                    <td>
                                        <p>nombre del candidato a entrevistar</p>
                                        <p>Campo obligatorio</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>correo</p>
                                    </td>
                                    <td>
                                        <p>cadena</p>
                                    </td>
                                    <td>
                                        <p>correo del candidato a entrevistar</p>
                                        <p>Campo obligatorio</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>fecha</p>
                                    </td>
                                    <td>
                                        <p>cadena</p>
                                    </td>
                                    <td>
                                        <p>fecha de la entrevista</p>
                                        <p>Campo obligatorio</p>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div><br><br><br>
                    <p>Formato de salida:&nbsp;JSON</p>
                    <p>C&oacute;digo de respuesta exitosa:&nbsp;HTTP 200</p>
                    <p>Salida:&nbsp;</p><br>
                    <div align="left">
                        <table>
                            <tbody>
                                <tr>
                                    <td>
                                        <p>Atributo</p>
                                    </td>
                                    <td>
                                        <p>Tipo</p>
                                    </td>
                                    <td>
                                        <p>Descripci&oacute;n</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>estatus</p>
                                    </td>
                                    <td>
                                        <p>entero</p>
                                    </td>
                                    <td>
                                        <p>indica el c&oacute;digo de respuesta de aceptaci&oacute;n</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>mensaje</p>
                                    </td>
                                    <td>
                                        <p>cadena</p>
                                    </td>
                                    <td>
                                        <p>muestra informaci&oacute;n del registro de la entrevista</p>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div><br>
                    <p>C&oacute;digo de respuesta fallida:</p><br>
                    <div align="left">
                        <table>
                            <tbody>
                                <tr>
                                    <td>
                                        <p>C&oacute;digo</p>
                                    </td>
                                    <td>
                                        <p>Descripci&oacute;n</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>400</p>
                                    </td>
                                    <td>
                                        <p>Error al interpretar la solicitud</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>401</p>
                                    </td>
                                    <td>
                                        <p>Usuario no autenticado</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>403</p>
                                    </td>
                                    <td>
                                        <p>Usuario sin permisos</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>500</p>
                                    </td>
                                    <td>
                                        <p>Error interno del servidor</p>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div><br>
                    <p>Body de Salida:</p><br>
                    <div align="left">
                        <table>
                            <tbody>
                                <tr>
                                    <td>
                                        <p>Atributo</p>
                                    </td>
                                    <td>
                                        <p>Tipo</p>
                                    </td>
                                    <td>
                                        <p>Descripci&oacute;n</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>estatus</p>
                                    </td>
                                    <td>
                                        <p>entero</p>
                                    </td>
                                    <td>
                                        <p>indica el c&oacute;digo de respuesta fallido</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>error</p>
                                    </td>
                                    <td>
                                        <p>cadena</p>
                                    </td>
                                    <td>
                                        <p>muestra el nombre del error</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>mensaje</p>
                                    </td>
                                    <td>
                                        <p>cadena</p>
                                    </td>
                                    <td>
                                        <p>muestra m&aacute;s informaci&oacute;n del error</p>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div><br>
                    <p>Ejemplos de par&aacute;metros de entrada:</p><br>
                    <div align="left">
                        <table>
                            <tbody>
                                <tr>
                                    <td>
                                        <p>cui</p>
                                    </td>
                                    <td>
                                        <p>2994902460101</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>nombre</p>
                                    </td>
                                    <td>
                                        <p>Mynor</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>correo</p>
                                    </td>
                                    <td>
                                        <p>m@gmail.com</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>fecha</p>
                                    </td>
                                    <td>
                                        <p>18/04/2023</p>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div><br>
                    <p>Ejemplos de par&aacute;metros de salida exitosa:</p>
                    <p>{</p>
                    <p>&nbsp; &nbsp; &ldquo;estatus&rdquo;: 200,</p>
                    <p>&nbsp; &nbsp; &ldquo;mensaje&rdquo;: &ldquo;Se agend&oacute; la entrevista con el candidato &nbsp;de manera exitosa&rdquo;</p>
                    <p>}</p>
                    <p>Ejemplo de par&aacute;metros de salida fallida:</p>
                    <p>{</p>
                    <p>&nbsp; &nbsp; &ldquo;estatus&rdquo;: 400</p>
                    <p>&nbsp; &nbsp; &ldquo;error&rdquo;:&rdquo;Correo electr&oacute;nico invalido&rdquo;,</p>
                    <p>&nbsp; &nbsp; &ldquo;mensaje&rdquo;:&rdquo;El correo electr&oacute;nico no se pudo enviar&rdquo;</p>
                    <p>}</p><br>
                    <p>{</p>
                    <p>&nbsp; &nbsp; &ldquo;estatus&rdquo;: 403</p>
                    <p>&nbsp; &nbsp; &ldquo;error&rdquo;:&rdquo;Usuario sin permisos&rdquo;,</p>
                    <p>&nbsp; &nbsp; &ldquo;mensaje&rdquo;:&rdquo;El usuario no tiene permisos para agendar entrevistas,, solamente el personal de rrhh tiene permisos asignados&rdquo;</p>
                    <p>}</p>
                </td>
            </tr>
            <tr></tr>
            <tr></tr>
            <tr></tr>
            <tr></tr>
        </tbody>
    </table>
</div>
<p><br></p>
<p><br></p>
<p><br></p>
<div align="left">
    <table>
        <tbody>
            <tr>
                <td>
                    <p>ID:&nbsp;12</p>
                </td>
                <td>
                    <p>Nombre:&nbsp;Registrar de ventas</p>
                </td>
            </tr>
            <tr>
                <td>
                    <p>Prioridad:&nbsp;Alta</p>
                </td>
                <td rowspan="3">
                    <p>Historia de usuario</p>
                    <p>Se quiere poder registrar cada una de las ventas que un determinado usuario realice</p>
                </td>
            </tr>
            <tr>
                <td>
                    <p>Estimado:&nbsp;5</p>
                </td>
            </tr>
            <tr>
                <td>
                    <p>M&oacute;dulo:&nbsp;Ventas</p>
                </td>
            </tr>
            <tr>
                <td colspan="2" rowspan="5">
                    <p>Criterios de Aceptaci&oacute;n</p><br>
                    <p>El usuario por medio &nbsp;del carrito de compras , agregara los productos a comprar, se validar&aacute; &nbsp;la compra y &nbsp;se seleccionar&aacute; el m&eacute;todo de pago ya sea por tarjeta de cr&eacute;dito o por medio de puntos, se mostrar&aacute; el resultado satisfactorio o en caso de no completarse el proceso se mostrar&aacute; el mensaje del problema en pantalla.&nbsp;</p><br>
                    <p>El microservicio debe tener la siguiente configuraci&oacute;n:</p><br>
                    <p>Ruta:&nbsp;/sales/recordsales</p>
                    <p>M&eacute;todo:&nbsp;POST</p>
                    <p>Formato de entrada:&nbsp;JSON</p><br>
                    <p>Payload:&nbsp;</p><br>
                    <div align="left">
                        <table>
                            <tbody>
                                <tr>
                                    <td>
                                        <p>Atributo</p>
                                    </td>
                                    <td>
                                        <p>Tipo</p>
                                    </td>
                                    <td>
                                        <p>Descripci&oacute;n</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>cui</p>
                                    </td>
                                    <td>
                                        <p>cadena</p>
                                    </td>
                                    <td>
                                        <p>el n&uacute;mero de identificaci&oacute;n del usuario.</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>tipoUsuario</p>
                                    </td>
                                    <td>
                                        <p>entero</p>
                                    </td>
                                    <td>
                                        <p>El tipo de usuario dentro de la plataforma, este puede ser:&nbsp;</p>
                                        <ul>
                                            <li>
                                                <p>1&nbsp;</p>
                                            </li>
                                            <li>
                                                <p>2</p>
                                            </li>
                                        </ul>
                                        <p>Donde:&nbsp;</p>
                                        <p>1 representa administradores</p>
                                        <p>2 clientes normales</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>exp</p>
                                    </td>
                                    <td>
                                        <p>entero</p>
                                    </td>
                                    <td>
                                        <p>Este representa la fecha de expiraci&oacute;n del token.</p>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div><br>
                    <p>Header:</p><br>
                    <div align="left">
                        <table>
                            <tbody>
                                <tr>
                                    <td>
                                        <p>Atributo</p>
                                    </td>
                                    <td>
                                        <p>Tipo</p>
                                    </td>
                                    <td>
                                        <p>Descripci&oacute;n</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>Content-Type</p>
                                    </td>
                                    <td>
                                        <p>header</p>
                                    </td>
                                    <td>
                                        <p>application/json</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>Authorization</p>
                                    </td>
                                    <td>
                                        <p>header</p>
                                    </td>
                                    <td>
                                        <p>Bearer &lt;token&gt;</p>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div><br>
                    <p>Body:</p><br>
                    <div align="left">
                        <table>
                            <tbody>
                                <tr>
                                    <td>
                                        <p>Atributo</p>
                                    </td>
                                    <td>
                                        <p>Tipo</p>
                                    </td>
                                    <td>
                                        <p>Descripci&oacute;n</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>cui</p>
                                    </td>
                                    <td>
                                        <p>entero</p>
                                    </td>
                                    <td>
                                        <p>identificaci&oacute;n del usuario</p>
                                        <p>Atributo requerido</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>productos</p>
                                    </td>
                                    <td>
                                        <p>Arreglo</p>
                                    </td>
                                    <td>
                                        <p>Un arreglo con cada uno de los productos agregados al carro de compra, cada uno de los productos tendra los atributos siguientes:</p>
                                        <ul>
                                            <li>
                                                <p>idProducto</p>
                                            </li>
                                            <li>
                                                <p>cantidad &nbsp; &nbsp;</p>
                                            </li>
                                        </ul>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>metodoPago</p>
                                    </td>
                                    <td>
                                        <p>Arreglo</p>
                                    </td>
                                    <td>
                                        <p>Arreglo que tendr&aacute; los/el m&eacute;todo de pago de los productos:&nbsp;</p>
                                        <ul>
                                            <li>
                                                <p>tarjeta de cr&eacute;dito (1)</p>
                                            </li>
                                            <li>
                                                <p>puntos &nbsp; &nbsp; (2)</p>
                                            </li>
                                        </ul><br>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>direccion</p>
                                    </td>
                                    <td>
                                        <p>cadena&nbsp;</p>
                                    </td>
                                    <td>
                                        <p>Direcci&oacute;n de env&iacute;o de los productos.&nbsp;</p>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div><br>
                    <p>Formato de salida:&nbsp;JSON</p>
                    <p>C&oacute;digo de respuesta exitosa:&nbsp;HTTP 201</p>
                    <p>Salida:&nbsp;</p><br>
                    <div align="left">
                        <table>
                            <tbody>
                                <tr>
                                    <td>
                                        <p>Atributo</p>
                                    </td>
                                    <td>
                                        <p>Tipo</p>
                                    </td>
                                    <td>
                                        <p>Descripci&oacute;n</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>estatus</p>
                                    </td>
                                    <td>
                                        <p>entero</p>
                                    </td>
                                    <td>
                                        <p>indica el c&oacute;digo de respuesta de aceptaci&oacute;n</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>mensaje</p>
                                    </td>
                                    <td>
                                        <p>cadena</p>
                                    </td>
                                    <td>
                                        <p>muestra informaci&oacute;n de registro de venta exitoso</p>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div><br>
                    <p>C&oacute;digo de respuesta fallida:</p><br>
                    <div align="left">
                        <table>
                            <tbody>
                                <tr>
                                    <td>
                                        <p>C&oacute;digo</p>
                                    </td>
                                    <td>
                                        <p>Descripci&oacute;n</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>400</p>
                                    </td>
                                    <td>
                                        <p>Error al interpretar la solicitud</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>401</p>
                                    </td>
                                    <td>
                                        <p>El usuario no est&aacute; autenticado</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>403</p>
                                    </td>
                                    <td>
                                        <p>Usuario sin permisos</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>500</p>
                                    </td>
                                    <td>
                                        <p>Error interno del servidor</p>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div><br>
                    <p>Body de Salida:</p><br>
                    <div align="left">
                        <table>
                            <tbody>
                                <tr>
                                    <td>
                                        <p>Atributo</p>
                                    </td>
                                    <td>
                                        <p>Tipo</p>
                                    </td>
                                    <td>
                                        <p>Descripci&oacute;n</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>estatus</p>
                                    </td>
                                    <td>
                                        <p>entero</p>
                                    </td>
                                    <td>
                                        <p>indica el c&oacute;digo de respuesta fallida</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>error</p>
                                    </td>
                                    <td>
                                        <p>cadena</p>
                                    </td>
                                    <td>
                                        <p>muestra el nombre del error</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>mensaje</p>
                                    </td>
                                    <td>
                                        <p>cadena</p>
                                    </td>
                                    <td>
                                        <p>muestra m&aacute;s informaci&oacute;n del error</p>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div><br><br>
                    <p>Ejemplos de par&aacute;metros de entrada:</p>
                    <p>{</p>
                    <p>cui:1234567989,</p>
                    <p>productos: [</p>
                    <p>&nbsp; {</p>
                    <p>&nbsp; &nbsp; &quot;idProducto&quot;: 1,</p>
                    <p>&nbsp; &nbsp; &quot;cantidad&quot;: 10</p>
                    <p>&nbsp; },</p>
                    <p>&nbsp; {</p>
                    <p>&nbsp; &nbsp; &quot;idProducto&quot;: 2,</p>
                    <p>&nbsp; &nbsp; &quot;cantidad&quot;: 5</p>
                    <p>&nbsp; },</p>
                    <p>&nbsp; {</p>
                    <p>&nbsp; &nbsp; &quot;idProducto&quot;: 3,</p>
                    <p>&nbsp; &nbsp; &quot;cantidad&quot;: 20</p>
                    <p>&nbsp; }</p>
                    <p>],</p>
                    <p>metodoPago:</p>
                    <p>[</p>
                    <p>{</p>
                    <p>&ldquo;tipo&rdquo;:1</p>
                    <p>&ldquo;monto&rdquo;: 200</p>
                    <p>},</p>
                    <p>{</p>
                    <p>&ldquo;tipo&rdquo;:2</p>
                    <p>&ldquo;monto&rdquo;: 35.5</p>
                    <p>}</p>
                    <p>],</p>
                    <p>direccion: &ldquo;John Doe, 123 Main Street New York, NY 10001 United States&rdquo;</p>
                    <p>}</p><br>
                    <p>Ejemplos de par&aacute;metros de salida exitosa:</p>
                    <p>{</p>
                    <p>&quot;estatus&quot;: 200, &nbsp;</p>
                    <p>&quot;mensaje&quot;: &ldquo;Informaci&oacute;n actualizado con &eacute;xito&rdquo;</p>
                    <p>}</p><br>
                    <p>Ejemplo de par&aacute;metros de salida fallida:</p>
                    <p>{</p>
                    <p>&quot;estatus&quot;:401,&nbsp;</p>
                    <p>&quot;mensaje&quot;: &ldquo;Usuario no autenticado&rdquo;&nbsp;</p>
                    <p>&quot;error&quot;: &nbsp;&ldquo;Token invalido&rdquo;</p>
                    <p>}</p>
                </td>
            </tr>
            <tr></tr>
            <tr></tr>
            <tr></tr>
            <tr></tr>
        </tbody>
    </table>
</div>
<p><br></p>
<p><br></p>
<div align="left">
    <table>
        <tbody>
            <tr>
                <td>
                    <p>ID:&nbsp;13</p>
                </td>
                <td>
                    <p>Nombre:&nbsp;Agregar producto al carrito</p>
                </td>
            </tr>
            <tr>
                <td>
                    <p>Prioridad:&nbsp;Alta</p>
                </td>
                <td rowspan="3">
                    <p>Historia de usuario</p>
                    <p>El sistema requiere que los usuarios puedan agregar los productos de su inter&eacute;s a un carrito de compras</p>
                </td>
            </tr>
            <tr>
                <td>
                    <p>Estimado:&nbsp;3 puntos</p>
                </td>
            </tr>
            <tr>
                <td>
                    <p>M&oacute;dulo:&nbsp;Compras</p>
                </td>
            </tr>
            <tr>
                <td colspan="2" rowspan="5">
                    <p>Criterios de Aceptaci&oacute;n</p><br>
                    <p>Este microservicio le permitir&aacute; al cliente agregar un producto al carrito de compras, por defecto la cantidad de este producto ser&aacute; de 1.</p><br>
                    <p>El microservicio debe tener la siguiente configuraci&oacute;n:</p><br>
                    <p>Ruta:&nbsp;/buy/addShoppingCart</p>
                    <p>M&eacute;todo:&nbsp;POST</p>
                    <p>Formato de entrada:&nbsp;form-data</p><br>
                    <p>Header:</p><br>
                    <div align="left">
                        <table>
                            <tbody>
                                <tr>
                                    <td>
                                        <p>Atributo</p>
                                    </td>
                                    <td>
                                        <p>Tipo</p>
                                    </td>
                                    <td>
                                        <p>Descripci&oacute;n</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>Content-Type</p>
                                    </td>
                                    <td>
                                        <p>header</p>
                                    </td>
                                    <td>
                                        <p>multipart/form-data</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>Authorization</p>
                                    </td>
                                    <td>
                                        <p>header</p>
                                    </td>
                                    <td>
                                        <p>Bearer &lt;token&gt;</p>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div><br><br>
                    <p>Body:</p><br>
                    <div align="left">
                        <table>
                            <tbody>
                                <tr>
                                    <td>
                                        <p>Atributo</p>
                                    </td>
                                    <td>
                                        <p>Tipo</p>
                                    </td>
                                    <td>
                                        <p>Descripci&oacute;n</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>id_producto</p>
                                    </td>
                                    <td>
                                        <p>entero</p>
                                    </td>
                                    <td>
                                        <p>N&uacute;mero que identifica al producto.</p>
                                    </td>
                                </tr>
                                   <tr>
                                    <td>
                                        <p>cantidad</p>
                                    </td>
                                    <td>
                                        <p>entero</p>
                                    </td>
                                    <td>
                                        <p>N&uacute;mero que indica la exactitud del pedido</p>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div><br><br>
                    <p>Formato de salida:&nbsp;JSON</p>
                    <p>C&oacute;digo de respuesta exitosa:&nbsp;HTTP 200</p>
                    <p>Salida:&nbsp;</p><br>
                    <div align="left">
                        <table>
                            <tbody>
                                <tr>
                                    <td>
                                        <p>Atributo</p>
                                    </td>
                                    <td>
                                        <p>Tipo</p>
                                    </td>
                                    <td>
                                        <p>Descripci&oacute;n</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>estatus</p>
                                    </td>
                                    <td>
                                        <p>entero</p>
                                    </td>
                                    <td>
                                        <p>estatus del env&iacute;o de correo electr&oacute;nico</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>mensaje</p>
                                    </td>
                                    <td>
                                        <p>cadena</p>
                                    </td>
                                    <td>
                                        <p>mensaje descriptivo</p>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div><br><br>
                    <p>C&oacute;digo de respuesta fallida:</p><br>
                    <div align="left">
                        <table>
                            <tbody>
                                <tr>
                                    <td>
                                        <p>C&oacute;digo</p>
                                    </td>
                                    <td>
                                        <p>Descripci&oacute;n</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>400</p>
                                    </td>
                                    <td>
                                        <p>Fallo en el proceso al intentar enviar el correo</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>500</p>
                                    </td>
                                    <td>
                                        <p>Error interno del servidor</p>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div><br>
                    <p>Body de Salida:</p><br>
                    <div align="left">
                        <table>
                            <tbody>
                                <tr>
                                    <td>
                                        <p>Atributo</p>
                                    </td>
                                    <td>
                                        <p>Tipo</p>
                                    </td>
                                    <td>
                                        <p>Descripci&oacute;n</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>estatus</p>
                                    </td>
                                    <td>
                                        <p>entero</p>
                                    </td>
                                    <td>
                                        <p>Indica el c&oacute;digo de respuesta</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>error</p>
                                    </td>
                                    <td>
                                        <p>cadena</p>
                                    </td>
                                    <td>
                                        <p>muestra m&aacute;s informaci&oacute;n del error</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>mensaje</p>
                                    </td>
                                    <td>
                                        <p>cadena</p>
                                    </td>
                                    <td>
                                        <p>muestra el nombre del error</p>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div><br>
                    <p>Ejemplos de par&aacute;metros de entrada:</p>
                    <p>{</p>
                    <p>&nbsp; &quot;id_producto&quot;: 1,</p>
                    <p>&nbsp; &quot;cantidad&quot;: 3</p>
                    <p>}</p>
                    <p>&nbsp;</p>
                    <p>Ejemplos de par&aacute;metros de salida exitosa:</p>
                    <p>{</p>
                    <p>&nbsp; &nbsp;&ldquo;estatus&rdquo;: 200,</p>
                    <p>&nbsp; &nbsp;&ldquo;mensaje&rdquo;: &ldquo;Producto agregado correctamente&rdquo;</p>
                    <p>}</p>
                    <p>Ejemplo de par&aacute;metros de salida fallida:</p>
                    <p>{</p>
                    <p>&nbsp; &nbsp; &quot;estatus&quot;: 400,</p>
                    <p>&nbsp; &nbsp; &quot;mensaje&quot;: &quot;Error con los campos.&quot;</p>
                    <p>}</p><br>
                    <p>{</p>
                    <p>&nbsp; &nbsp; &quot;estatus&quot;: 500,</p>
                    <p>&nbsp; &nbsp; &quot;error&quot;: &ldquo;Error del servidor&rdquo;</p>
                    <p>&nbsp; &nbsp; &quot;mensaje&quot;: &quot;No se pudo conectar a la base de datos&quot;</p>
                    <p>}</p><br>
                </td>
            </tr>
            <tr></tr>
            <tr></tr>
            <tr></tr>
            <tr></tr>
        </tbody>
    </table>
</div>
<p><br></p>
<p><br></p>
<p><br></p>
<div align="left">
    <table>
        <tbody>
            <tr>
                <td>
                    <p>ID:&nbsp;14</p>
                </td>
                <td>
                    <p>Nombre:&nbsp;Ver Carrito de Compras</p>
                </td>
            </tr>
            <tr>
                <td>
                    <p>Prioridad:&nbsp;Alta</p>
                </td>
                <td rowspan="3">
                    <p>Historia de usuario</p>
                    <p>El sistema debe permitirle al cliente visualizar los productos de su carrito de compras.</p>
                </td>
            </tr>
            <tr>
                <td>
                    <p>Estimado:&nbsp;3 puntos</p>
                </td>
            </tr>
            <tr>
                <td>
                    <p>M&oacute;dulo:&nbsp;Compras</p>
                </td>
            </tr>
            <tr>
                <td colspan="2" rowspan="5">
                    <p>Criterios de Aceptaci&oacute;n</p><br>
                    <p>Este microservicio se debe conectar con el microservicio de consultar producto espec&iacute;fico por cada uno de los productos agregados al carrito, para mostrar la informaci&oacute;n de este.</p><br>
                    <p>El microservicio debe tener la siguiente configuraci&oacute;n:</p><br>
                    <p>Ruta:&nbsp;/buy/getShoppingCart</p>
                    <p>M&eacute;todo:&nbsp;GET</p>
                    <p>Header:</p><br>
                    <div align="left">
                        <table>
                            <tbody>
                                <tr>
                                    <td>
                                        <p>Atributo</p>
                                    </td>
                                    <td>
                                        <p>Tipo</p>
                                    </td>
                                    <td>
                                        <p>Descripci&oacute;n</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>Authorization</p>
                                    </td>
                                    <td>
                                        <p>header</p>
                                    </td>
                                    <td>
                                        <p>Bearer &lt;token&gt;</p>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div><br><br>
                    <p>Formato de salida:&nbsp;JSON</p>
                    <p>C&oacute;digo de respuesta exitosa:&nbsp;HTTP 200</p>
                    <p>Salida:&nbsp;</p><br>
                    <div align="left">
                        <table>
                            <tbody>
                                <tr>
                                    <td>
                                        <p>Atributo</p>
                                    </td>
                                    <td>
                                        <p>Tipo</p>
                                    </td>
                                    <td>
                                        <p>Descripci&oacute;n</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>estatus</p>
                                    </td>
                                    <td>
                                        <p>entero</p>
                                    </td>
                                    <td>
                                        <p>c&oacute;digo devuelto al obtener una respuesta satisfactoria</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>mensaje</p>
                                    </td>
                                    <td>
                                        <p>cadena</p>
                                    </td>
                                    <td>
                                        <p>mensaje descriptivo</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>data</p>
                                    </td>
                                    <td>
                                        <p>arreglo</p>
                                    </td>
                                    <td>
                                        <p>arreglo de objetos con la informaci&oacute;n de los productos solicitados</p>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div><br><br>
                    <p>C&oacute;digo de respuesta fallida:</p><br>
                    <div align="left">
                        <table>
                            <tbody>
                                <tr>
                                    <td>
                                        <p>C&oacute;digo</p>
                                    </td>
                                    <td>
                                        <p>Descripci&oacute;n</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>404</p>
                                    </td>
                                    <td>
                                        <p>Recurso no encontrado</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>500</p>
                                    </td>
                                    <td>
                                        <p>Error interno del servidor</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>503</p>
                                    </td>
                                    <td>
                                        <p>Servicio no disponible</p>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div><br>
                    <p>Body de Salida:</p><br>
                    <div align="left">
                        <table>
                            <tbody>
                                <tr>
                                    <td>
                                        <p>Atributo</p>
                                    </td>
                                    <td>
                                        <p>Tipo</p>
                                    </td>
                                    <td>
                                        <p>Descripci&oacute;n</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>estatus</p>
                                    </td>
                                    <td>
                                        <p>entero</p>
                                    </td>
                                    <td>
                                        <p>Indica el c&oacute;digo de respuesta</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>error</p>
                                    </td>
                                    <td>
                                        <p>cadena</p>
                                    </td>
                                    <td>
                                        <p>muestra m&aacute;s informaci&oacute;n del error</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>mensaje</p>
                                    </td>
                                    <td>
                                        <p>cadena</p>
                                    </td>
                                    <td>
                                        <p>muestra el nombre del error</p>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div><br>
                    <p>&nbsp;</p>
                    <p>Ejemplos de par&aacute;metros de salida exitosa:</p>
                    <p>{</p>
                    <p>&nbsp; &nbsp;&ldquo;estatus&rdquo;: 200,</p>
                    <p>&nbsp; &nbsp;&ldquo;mensaje&rdquo;: &ldquo;Productos consultados exitosamente&rdquo;,</p>
                    <p>&nbsp; &nbsp;&ldquo;data&rdquo;: [ { &lt;producto1&gt; }, { &lt;producto2&gt; } ]</p>
                    <p>}</p>
                    <p>Ejemplo de par&aacute;metros de salida fallida:</p>
                    <p>{</p>
                    <p>&nbsp; &nbsp; &quot;estatus&quot;: 400,</p>
                    <p>&nbsp; &nbsp; &quot;error&quot;: &quot;Error con los campos.&quot;</p>
                    <p>&nbsp; &nbsp; &quot;mensaje&quot;: &quot;No se enviaron campos requeridos&quot;</p>
                    <p>}</p><br>
                    <p>{</p>
                    <p>&nbsp; &nbsp; &quot;estatus&quot;: 404,</p>
                    <p>&nbsp; &nbsp; &ldquo;error&rdquo;: &quot;Producto inexistente&quot;</p>
                    <p>&nbsp; &nbsp; &quot;mensaje&quot;: &quot;El producto solicitado no existe&quot;</p>
                    <p>}</p><br>
                    <p>{</p>
                    <p>&nbsp; &nbsp; &quot;estatus&quot;: 500,</p>
                    <p>&nbsp; &nbsp; &quot;error&quot;: &ldquo;Error del servidor&rdquo;</p>
                    <p>&nbsp; &nbsp; &quot;mensaje&quot;: &quot;No se pudo conectar a la base de datos&quot;</p>
                    <p>}</p>
                </td>
            </tr>
            <tr></tr>
            <tr></tr>
            <tr></tr>
            <tr></tr>
        </tbody>
    </table>
</div>
<p><br></p>
<p><br></p>
<div align="left">
    <table>
        <tbody>
            <tr>
                <td>
                    <p>ID:&nbsp;15</p>
                </td>
                <td>
                    <p>Nombre:&nbsp;Eliminar producto del carrito</p>
                </td>
            </tr>
            <tr>
                <td>
                    <p>Prioridad:&nbsp;Media</p>
                </td>
                <td rowspan="3">
                    <p>Historia de usuario</p>
                    <p>Es importante permitir que se elimine un producto del carrito de compras, ya que un cliente puede cambiar de opinion.</p>
                </td>
            </tr>
            <tr>
                <td>
                    <p>Estimado:&nbsp;2 puntos</p>
                </td>
            </tr>
            <tr>
                <td>
                    <p>M&oacute;dulo:&nbsp;Compras</p>
                </td>
            </tr>
            <tr>
                <td colspan="2" rowspan="5">
                    <p>Criterios de Aceptaci&oacute;n</p><br>
                    <p>Este microservicio le permitir&aacute; al cliente eliminar un producto de su carrito de compras para ya no visualizarlo y evitar un cobro adicional.&nbsp;</p><br>
                    <p>El microservicio debe tener la siguiente configuraci&oacute;n:</p><br>
                    <p>Ruta:&nbsp;/buy/deleteProductCart</p>
                    <p>M&eacute;todo:&nbsp;DELETE</p>
                    <p>Formato de entrada:&nbsp;form-data</p><br>
                    <p>Header:</p><br>
                    <div align="left">
                        <table>
                            <tbody>
                                <tr>
                                    <td>
                                        <p>Atributo</p>
                                    </td>
                                    <td>
                                        <p>Tipo</p>
                                    </td>
                                    <td>
                                        <p>Descripci&oacute;n</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>Content-Type</p>
                                    </td>
                                    <td>
                                        <p>header</p>
                                    </td>
                                    <td>
                                        <p>multipart/form-data</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>Authorization</p>
                                    </td>
                                    <td>
                                        <p>header</p>
                                    </td>
                                    <td>
                                        <p>Bearer &lt;token&gt;</p>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div><br><br>
                    <p>Body:</p><br>
                    <div align="left">
                        <table>
                            <tbody>
                                <tr>
                                    <td>
                                        <p>Atributo</p>
                                    </td>
                                    <td>
                                        <p>Tipo</p>
                                    </td>
                                    <td>
                                        <p>Descripci&oacute;n</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>idProducto</p>
                                    </td>
                                    <td>
                                        <p>entero</p>
                                    </td>
                                    <td>
                                        <p>N&uacute;mero que identifica al producto.</p>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div><br><br>
                    <p>Formato de salida:&nbsp;JSON</p>
                    <p>C&oacute;digo de respuesta exitosa:&nbsp;HTTP 200</p>
                    <p>Salida:&nbsp;</p><br>
                    <div align="left">
                        <table>
                            <tbody>
                                <tr>
                                    <td>
                                        <p>Atributo</p>
                                    </td>
                                    <td>
                                        <p>Tipo</p>
                                    </td>
                                    <td>
                                        <p>Descripci&oacute;n</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>estatus</p>
                                    </td>
                                    <td>
                                        <p>entero</p>
                                    </td>
                                    <td>
                                        <p>C&oacute;digo devuelto al recibir una respuesta satisfactoria</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>mensaje</p>
                                    </td>
                                    <td>
                                        <p>cadena</p>
                                    </td>
                                    <td>
                                        <p>mensaje descriptivo</p>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div><br><br>
                    <p>C&oacute;digo de respuesta fallida:</p><br>
                    <div align="left">
                        <table>
                            <tbody>
                                <tr>
                                    <td>
                                        <p>C&oacute;digo</p>
                                    </td>
                                    <td>
                                        <p>Descripci&oacute;n</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>400</p>
                                    </td>
                                    <td>
                                        <p>Fallo en el proceso al intentar enviar el correo</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>500</p>
                                    </td>
                                    <td>
                                        <p>Error interno del servidor</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>401</p>
                                    </td>
                                    <td>
                                        <p>Usuario no autenticado</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>403</p>
                                    </td>
                                    <td>
                                        <p>Usuario sin permisos</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>502</p>
                                    </td>
                                    <td>
                                        <p>Error en parametros de entrada</p>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div><br>
                    <p>Body de Salida:</p><br>
                    <div align="left">
                        <table>
                            <tbody>
                                <tr>
                                    <td>
                                        <p>Atributo</p>
                                    </td>
                                    <td>
                                        <p>Tipo</p>
                                    </td>
                                    <td>
                                        <p>Descripci&oacute;n</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>estatus</p>
                                    </td>
                                    <td>
                                        <p>entero</p>
                                    </td>
                                    <td>
                                        <p>Indica el c&oacute;digo de respuesta</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>error</p>
                                    </td>
                                    <td>
                                        <p>cadena</p>
                                    </td>
                                    <td>
                                        <p>muestra m&aacute;s informaci&oacute;n del error</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>mensaje</p>
                                    </td>
                                    <td>
                                        <p>cadena</p>
                                    </td>
                                    <td>
                                        <p>muestra el nombre del error</p>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div><br>
                    <p>Ejemplos de par&aacute;metros de entrada:</p>
                    <p>{</p>
                    <p>&nbsp; &quot;idProducto&quot;: 1,</p>
                    <p>}</p>
                    <p>&nbsp;</p>
                    <p>Ejemplos de par&aacute;metros de salida exitosa:</p>
                    <p>{</p>
                    <p>&nbsp; &nbsp;&ldquo;estatus&rdquo;: 200,</p>
                    <p>&nbsp; &nbsp;&ldquo;mensaje&rdquo;: &ldquo;Producto eliminado del carrito correctamente&rdquo;</p>
                    <p>}</p>
                    <p>Ejemplo de par&aacute;metros de salida fallida:</p>
                    <p>{</p>
                    <p>&nbsp; &nbsp; &quot;estatus&quot;: 400,</p>
                    <p>&nbsp; &nbsp; &quot;error&quot;: &quot;Error con los campos.&quot;,</p>
                    <p>&nbsp; &nbsp; &quot;mensaje&quot;: &quot;Campos requeridos&quot;</p>
                    <p>}</p><br>
                    <p>{</p>
                    <p>&nbsp; &nbsp; &quot;estatus&quot;: 500,</p>
                    <p>&nbsp; &nbsp; &quot;error&quot;: &ldquo;Error del servidor&rdquo;</p>
                    <p>&nbsp; &nbsp; &quot;mensaje&quot;: &quot;No se pudo conectar a la base de datos&quot;</p>
                    <p>}</p>
                </td>
            </tr>
            <tr></tr>
            <tr></tr>
            <tr></tr>
            <tr></tr>
        </tbody>
    </table>
</div>
<p><br></p>
<p><br></p>
<p><br></p>
<div align="left">
    <table>
        <tbody>
            <tr>
                <td>
                    <p>ID:&nbsp;16</p>
                </td>
                <td>
                    <p>Nombre:&nbsp;Cancelar compra</p>
                </td>
            </tr>
            <tr>
                <td>
                    <p>Prioridad:&nbsp;Media</p>
                </td>
                <td rowspan="3">
                    <p>Historia de usuario</p>
                    <p>Es requerido que el cliente pueda vaciar por completo su carrito (cancelar compra).</p>
                </td>
            </tr>
            <tr>
                <td>
                    <p>Estimado:&nbsp;3 puntos</p>
                </td>
            </tr>
            <tr>
                <td>
                    <p>M&oacute;dulo:&nbsp;Compras</p>
                </td>
            </tr>
            <tr>
                <td colspan="2" rowspan="5">
                    <p>Criterios de Aceptaci&oacute;n</p><br>
                    <p>Este microservicio le permitir&aacute; al cliente eliminar todos los productos de su carrito de compras para ya no visualizarlos.&nbsp;</p><br>
                    <p>El microservicio debe tener la siguiente configuraci&oacute;n:</p><br>
                    <p>Ruta:&nbsp;/buy/emptyShoppingCart</p>
                    <p>M&eacute;todo:&nbsp;DELETE</p>
                    <p>Header:</p><br>
                    <div align="left">
                        <table>
                            <tbody>
                                <tr>
                                    <td>
                                        <p>Atributo</p>
                                    </td>
                                    <td>
                                        <p>Tipo</p>
                                    </td>
                                    <td>
                                        <p>Descripci&oacute;n</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>Authorization</p>
                                    </td>
                                    <td>
                                        <p>header</p>
                                    </td>
                                    <td>
                                        <p>Bearer &lt;token&gt;</p>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div><br><br>
                    <p>Formato de salida:&nbsp;JSON</p>
                    <p>C&oacute;digo de respuesta exitosa:&nbsp;HTTP 200</p>
                    <p>Salida:&nbsp;</p><br>
                    <div align="left">
                        <table>
                            <tbody>
                                <tr>
                                    <td>
                                        <p>Atributo</p>
                                    </td>
                                    <td>
                                        <p>Tipo</p>
                                    </td>
                                    <td>
                                        <p>Descripci&oacute;n</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>estatus</p>
                                    </td>
                                    <td>
                                        <p>entero</p>
                                    </td>
                                    <td>
                                        <p>C&oacute;digo devuelto al obtener una respuesta satisfactoria</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>mensaje</p>
                                    </td>
                                    <td>
                                        <p>cadena</p>
                                    </td>
                                    <td>
                                        <p>mensaje descriptivo</p>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div><br><br>
                    <p>C&oacute;digo de respuesta fallida:</p><br>
                    <div align="left">
                        <table>
                            <tbody>
                                <tr>
                                    <td>
                                        <p>C&oacute;digo</p>
                                    </td>
                                    <td>
                                        <p>Descripci&oacute;n</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>400</p>
                                    </td>
                                    <td>
                                        <p>Fallo en el proceso al intentar enviar el correo</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>500</p>
                                    </td>
                                    <td>
                                        <p>Error interno del servidor</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>502</p>
                                    </td>
                                    <td>
                                        <p>Error del requerimiento</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>401</p>
                                    </td>
                                    <td>
                                        <p>Usuario no autenticado</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>403</p>
                                    </td>
                                    <td>
                                        <p>Usuario sin permisos</p>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div><br>
                    <p>Body de Salida:</p><br>
                    <div align="left">
                        <table>
                            <tbody>
                                <tr>
                                    <td>
                                        <p>Atributo</p>
                                    </td>
                                    <td>
                                        <p>Tipo</p>
                                    </td>
                                    <td>
                                        <p>Descripci&oacute;n</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>estatus</p>
                                    </td>
                                    <td>
                                        <p>entero</p>
                                    </td>
                                    <td>
                                        <p>Indica el c&oacute;digo de respuesta</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>error</p>
                                    </td>
                                    <td>
                                        <p>cadena</p>
                                    </td>
                                    <td>
                                        <p>muestra m&aacute;s informaci&oacute;n del error</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>mensaje</p>
                                    </td>
                                    <td>
                                        <p>cadena</p>
                                    </td>
                                    <td>
                                        <p>muestra el nombre del error</p>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div><br>
                    <p>&nbsp;</p>
                    <p>Ejemplos de par&aacute;metros de salida exitosa:</p>
                    <p>{</p>
                    <p>&nbsp; &nbsp;&ldquo;estatus&rdquo;: 200,</p>
                    <p>&nbsp; &nbsp;&ldquo;mensaje&rdquo;: &ldquo;Compra cancelada exitosamente&rdquo;</p>
                    <p>}</p>
                    <p>Ejemplo de par&aacute;metros de salida fallida:</p>
                    <p>{</p>
                    <p>&nbsp; &nbsp; &quot;estatus&quot;: 400,</p>
                    <p>&nbsp; &nbsp; &quot;error&quot;: &quot;Error con los campos.&quot;,</p>
                    <p>&nbsp; &nbsp; &ldquo;mensaje&rdquo;: &ldquo;No vienen campos requeridos&rdquo;</p>
                    <p>}</p><br>
                    <p>{</p>
                    <p>&nbsp; &nbsp; &quot;estatus&quot;: 500,</p>
                    <p>&nbsp; &nbsp; &quot;error&quot;: &ldquo;Error del servidor&rdquo;</p>
                    <p>&nbsp; &nbsp; &quot;mensaje&quot;: &quot;No se pudo conectar a la base de datos&quot;</p>
                    <p>}</p>
                </td>
            </tr>
            <tr></tr>
            <tr></tr>
            <tr></tr>
            <tr></tr>
        </tbody>
    </table>
</div>
<p><br></p>
<p><br></p>
<div align="left">
    <table>
        <tbody>
            <tr>
                <td>
                    <p>ID:&nbsp;17</p>
                </td>
                <td>
                    <p>Nombre:&nbsp;Enviar notificaciones por correo</p>
                </td>
            </tr>
            <tr>
                <td>
                    <p>Prioridad:&nbsp;Alta</p>
                </td>
                <td rowspan="3">
                    <p>Historia de usuario</p>
                    <p>Como usuario quiero recibir notificaciones por correo electr&oacute;nico, por diferentes motivos como son noticias, recepci&oacute;n de alguna solicitud.&nbsp;</p>
                </td>
            </tr>
            <tr>
                <td>
                    <p>Estimado:&nbsp;5 puntos</p>
                </td>
            </tr>
            <tr>
                <td>
                    <p>M&oacute;dulo:&nbsp;Notificaci&oacute;n</p>
                </td>
            </tr>
            <tr>
                <td colspan="2" rowspan="5">
                    <p>Criterios de Aceptaci&oacute;n</p>
                    <p>El servicio debe conectarse a un servidor de correo y retorna un c&oacute;digo 200 y un mensaje satisfactorio cuando la notificaci&oacute;n haya sido enviada, en caso contrario retorna un c&oacute;digo de error y descripci&oacute;n del mismo.</p><br>
                    <p>El microservicio debe tener la siguiente configuraci&oacute;n:</p><br>
                    <p>Ruta:&nbsp;/notification/sendEmail</p>
                    <p>M&eacute;todo:&nbsp;POST</p>
                    <p>Formato de entrada:&nbsp;form-data</p><br>
                    <p>Header:</p><br>
                    <div align="left">
                        <table>
                            <tbody>
                                <tr>
                                    <td>
                                        <p>Atributo</p>
                                    </td>
                                    <td>
                                        <p>Tipo</p>
                                    </td>
                                    <td>
                                        <p>Descripci&oacute;n</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>Content-Type</p>
                                    </td>
                                    <td>
                                        <p>header</p>
                                    </td>
                                    <td>
                                        <p>multipart/form-data</p>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div><br><br>
                    <p>Body:</p><br>
                    <div align="left">
                        <table>
                            <tbody>
                                <tr>
                                    <td>
                                        <p>Atributo</p>
                                    </td>
                                    <td>
                                        <p>Tipo</p>
                                    </td>
                                    <td>
                                        <p>Descripci&oacute;n</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>para</p>
                                    </td>
                                    <td>
                                        <p>texto</p>
                                    </td>
                                    <td>
                                        <p>Correo electr&oacute;nico de destino.</p>
                                        <p>Atributo requerido.</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>asunto</p>
                                    </td>
                                    <td>
                                        <p>texto</p>
                                    </td>
                                    <td>
                                        <p>Asunto del correo electr&oacute;nico.</p>
                                        <p>Atributo requerido.</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>adjuntos</p>
                                    </td>
                                    <td>
                                        <p>archivo</p>
                                    </td>
                                    <td>
                                        <p>Arreglo de archivos adjuntos.&nbsp;</p>
                                        <p>Los archivos no deben superar los 10MB.&nbsp;</p>
                                        <p>Atributo opcional.</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>mensaje</p>
                                    </td>
                                    <td>
                                        <p>texto</p>
                                    </td>
                                    <td>
                                        <p>Texto del mensaje del correo electr&oacute;nico, usar&aacute; la plantilla seleccionada en campo plantilla, caso contrario usar&aacute; la plantilla por defecto.&nbsp;</p>
                                        <p>La cadena de este campo puede llevar sintaxis html.</p>
                                        <p>Atributo requerido si no se env&iacute;a el atributo html.</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>plantilla</p>
                                    </td>
                                    <td>
                                        <p>texto</p>
                                    </td>
                                    <td>
                                        <p>Plantilla del correo para enviar el correo, el valor de este campo &nbsp;puede ser alguna de las siguientes opciones:</p>
                                        <ul>
                                            <li>
                                                <p>confirmEmail</p>
                                            </li>
                                            <li>
                                                <p>resetPassword</p>
                                            </li>
                                            <li>
                                                <p>notification (valor por defecto)</p>
                                            </li>
                                        </ul><br>
                                        <p>Atributo opcional s&iacute; se env&iacute;a el atributo mensaje.</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>titulo</p>
                                    </td>
                                    <td>
                                        <p>texto</p>
                                    </td>
                                    <td>
                                        <p>T&iacute;tulo del mensaje.&nbsp;</p>
                                        <p>Atributo opcional s&iacute; se env&iacute;a el atributo mensaje.</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>html</p>
                                    </td>
                                    <td>
                                        <p>texto</p>
                                    </td>
                                    <td>
                                        <p>Contenido personalizado del correo, al enviar este campo no se tomar&aacute; los valores en de los campos de mensaje, plantilla y t&iacute;tulo.</p>
                                        <p>Atributo requerido si no se env&iacute;a el atributo mensaje.</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>data</p>
                                    </td>
                                    <td>
                                        <p>texto</p>
                                    </td>
                                    <td>
                                        <p>Datos para los correos, este debe tener formato de JSON de lo contrario dar&aacute; error.</p><br>
                                        <p>Por el momento no las plantillas que necesitan este campo es confirmEmail y resetPassword</p><br>
                                        <p>Atributo opcional</p>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div><br><br>
                    <p>Formato de salida:&nbsp;JSON</p>
                    <p>C&oacute;digo de respuesta exitosa:&nbsp;HTTP 200</p>
                    <p>Salida:&nbsp;</p><br>
                    <div align="left">
                        <table>
                            <tbody>
                                <tr>
                                    <td>
                                        <p>Atributo</p>
                                    </td>
                                    <td>
                                        <p>Tipo</p>
                                    </td>
                                    <td>
                                        <p>Descripci&oacute;n</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>estatus</p>
                                    </td>
                                    <td>
                                        <p>entero</p>
                                    </td>
                                    <td>
                                        <p>estatus del env&iacute;o de correo electr&oacute;nico</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>mensaje</p>
                                    </td>
                                    <td>
                                        <p>cadena</p>
                                    </td>
                                    <td>
                                        <p>mensaje descriptivo</p>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div><br><br>
                    <p>C&oacute;digo de respuesta fallida:</p><br>
                    <div align="left">
                        <table>
                            <tbody>
                                <tr>
                                    <td>
                                        <p>C&oacute;digo</p>
                                    </td>
                                    <td>
                                        <p>Descripci&oacute;n</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>400</p>
                                    </td>
                                    <td>
                                        <p>Fallo en el proceso al intentar enviar el correo</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>403</p>
                                    </td>
                                    <td>
                                        <p>Error por exceder el l&iacute;mite de peso de los archivos adjuntos</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>500</p>
                                    </td>
                                    <td>
                                        <p>Error interno del servidor</p>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div><br>
                    <p>Body de Salida:</p><br>
                    <div align="left">
                        <table>
                            <tbody>
                                <tr>
                                    <td>
                                        <p>Atributo</p>
                                    </td>
                                    <td>
                                        <p>Tipo</p>
                                    </td>
                                    <td>
                                        <p>Descripci&oacute;n</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>estatus</p>
                                    </td>
                                    <td>
                                        <p>entero</p>
                                    </td>
                                    <td>
                                        <p>Indica el c&oacute;digo de respuesta</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>error</p>
                                    </td>
                                    <td>
                                        <p>cadena</p>
                                    </td>
                                    <td>
                                        <p>muestra m&aacute;s informaci&oacute;n del error</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>mensaje</p>
                                    </td>
                                    <td>
                                        <p>cadena</p>
                                    </td>
                                    <td>
                                        <p>muestra el nombre del error</p>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div><br>
                    <p>Ejemplos de par&aacute;metros de entrada:</p><br>
                    <div align="left">
                        <table>
                            <tbody>
                                <tr>
                                    <td>
                                        <p>clave</p>
                                    </td>
                                    <td>
                                        <p>valor</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>para</p>
                                    </td>
                                    <td>
                                        <p>correo1@gmail.com</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>asunto</p>
                                    </td>
                                    <td>
                                        <p>notificaci&oacute;n</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>adjuntos</p>
                                    </td>
                                    <td>
                                        <p>file.pdf</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>mensaje</p>
                                    </td>
                                    <td>
                                        <p>&lt;b&gt;mensaje del correo&lt;/b&gt;</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>titulo</p>
                                    </td>
                                    <td>
                                        <p>Titulo del Correo</p>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div><br>
                    <p>&nbsp;</p>
                    <div align="left">
                        <table>
                            <tbody>
                                <tr>
                                    <td>
                                        <p>clave</p>
                                    </td>
                                    <td>
                                        <p>valor</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>para</p>
                                    </td>
                                    <td>
                                        <p>correo1@gmail.com</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>asunto</p>
                                    </td>
                                    <td>
                                        <p>notificaci&oacute;n</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>adjuntos</p>
                                    </td>
                                    <td>
                                        <p>file.pdf</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>html</p>
                                    </td>
                                    <td>
                                        <p>&lt;html&gt;&lt;h1&gt;Mensaje Personalizado&lt;/h1&gt;&lt;b&gt;mensaje del correo&lt;/b&gt;&lt;/html&gt;</p>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div><br>
                    <p>Ejemplos de par&aacute;metros de salida exitosa:</p>
                    <p>{</p>
                    <p>&nbsp; &nbsp;&ldquo;estatus&rdquo;: 200,</p>
                    <p>&nbsp; &nbsp;&ldquo;mensaje&rdquo;: &ldquo;Correo enviado&rdquo;</p>
                    <p>}</p>
                    <p>Ejemplo de par&aacute;metros de salida fallida:</p>
                    <p>{</p>
                    <p>&nbsp; &nbsp; &quot;error&quot;: {</p>
                    <p>&nbsp; &nbsp; &nbsp; &nbsp; &quot;asunto&quot;: [</p>
                    <p>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &quot;Este campo es requerido.&quot;</p>
                    <p>&nbsp; &nbsp; &nbsp; &nbsp; ],</p>
                    <p>&nbsp; &nbsp; &nbsp; &nbsp; &quot;para&quot;: [</p>
                    <p>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &quot;Este campo es requerido y debe ser un correo.&quot;</p>
                    <p>&nbsp; &nbsp; &nbsp; &nbsp; ]</p>
                    <p>&nbsp; &nbsp; },</p>
                    <p>&nbsp; &nbsp; &quot;estatus&quot;: 400,</p>
                    <p>&nbsp; &nbsp; &quot;mensaje&quot;: &quot;Error con los campos.&quot;</p>
                    <p>}</p><br>
                    <p>{</p>
                    <p>&nbsp; &nbsp; &quot;error&quot;: {</p>
                    <p>&nbsp; &nbsp; &nbsp; &nbsp; &quot;html&quot;: [</p>
                    <p>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &quot;html es requerido, si no se env&iacute;a el par&aacute;metro mensaje&quot;</p>
                    <p>&nbsp; &nbsp; &nbsp; &nbsp; ],</p>
                    <p>&nbsp; &nbsp; &nbsp; &nbsp; &quot;mensaje&quot;: [</p>
                    <p>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &quot;mensaje es requerido, si no se env&iacute;a el par&aacute;metro html&quot;</p>
                    <p>&nbsp; &nbsp; &nbsp; &nbsp; ]</p>
                    <p>&nbsp; &nbsp; },</p>
                    <p>&nbsp; &nbsp; &quot;estatus&quot;: 400,</p>
                    <p>&nbsp; &nbsp; &quot;mensaje&quot;: &quot;Error con los campos.&quot;</p>
                    <p>}</p><br><br>
                    <p>{</p>
                    <p>&nbsp; &nbsp; &quot;error&quot;: &quot;413 Request Entity Too Large: The data value transmitted exceeds the capacity limit.&quot;,</p>
                    <p>&nbsp; &nbsp; &quot;estatus&quot;: 413,</p>
                    <p>&nbsp; &nbsp; &quot;mensaje&quot;: &quot;Error al enviar correo&quot;</p>
                    <p>}</p><br>
                </td>
            </tr>
            <tr></tr>
            <tr></tr>
            <tr></tr>
            <tr></tr>
        </tbody>
    </table>
</div>
<p><br></p>
<p><br></p>
<div align="left">
    <table>
        <tbody>
            <tr>
                <td>
                    <p>ID:&nbsp;18</p>
                </td>
                <td>
                    <p>Nombre:&nbsp;Subir objetos al bucket</p>
                </td>
            </tr>
            <tr>
                <td>
                    <p>Prioridad:&nbsp;Alta</p>
                </td>
                <td rowspan="3">
                    <p>Historia de usuario</p>
                    <p>Como instituci&oacute;n quiero poder almacenar objetos est&aacute;ticos necesarios para el aplicativo y tambi&eacute;n para los usuarios.</p>
                </td>
            </tr>
            <tr>
                <td>
                    <p>Estimado:&nbsp;3 puntos</p>
                </td>
            </tr>
            <tr>
                <td>
                    <p>M&oacute;dulo:&nbsp;Almacenamiento de objetos</p>
                </td>
            </tr>
            <tr>
                <td colspan="2" rowspan="5">
                    <p>Criterios de Aceptaci&oacute;n</p>
                    <p>El servicio debe conectarse a un servicio de almacenamientos de objetos, retornar un c&oacute;digo 200, un mensaje satisfactorio y la ruta del objeto donde fue almacenado, caso contrario retorna un c&oacute;digo de error y descripci&oacute;n del mismo.</p><br>
                    <p>El microservicio debe tener la siguiente configuraci&oacute;n:</p><br>
                    <p>Ruta:&nbsp;/bucket/upload</p>
                    <p>M&eacute;todo:&nbsp;POST</p>
                    <p>Formato de entrada:&nbsp;form-data</p><br>
                    <p>Header:</p><br>
                    <div align="left">
                        <table>
                            <tbody>
                                <tr>
                                    <td>
                                        <p>Atributo</p>
                                    </td>
                                    <td>
                                        <p>Tipo</p>
                                    </td>
                                    <td>
                                        <p>Descripci&oacute;n</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>Content-Type</p>
                                    </td>
                                    <td>
                                        <p>header</p>
                                    </td>
                                    <td>
                                        <p>multipart/form-data</p>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div><br>
                    <p>Body:</p><br>
                    <div align="left">
                        <table>
                            <tbody>
                                <tr>
                                    <td>
                                        <p>Atributo</p>
                                    </td>
                                    <td>
                                        <p>Tipo</p>
                                    </td>
                                    <td>
                                        <p>Descripci&oacute;n</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>archivo</p>
                                    </td>
                                    <td>
                                        <p>archivo o arreglo de archivos</p>
                                    </td>
                                    <td>
                                        <p>Archivos a almacenar.</p>
                                        <p>Atributo requerido.</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>directorio</p>
                                    </td>
                                    <td>
                                        <p>texto</p>
                                    </td>
                                    <td>
                                        <p>Directorio donde se almacenar&aacute; el o los archivos.</p>
                                        <p>Atributo opcional.</p>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div><br>
                    <p>Formato de salida:&nbsp;JSON</p>
                    <p>C&oacute;digo de respuesta exitosa: HTTP &nbsp;200</p>
                    <p>Salida:&nbsp;</p><br>
                    <div align="left">
                        <table>
                            <tbody>
                                <tr>
                                    <td>
                                        <p>Atributo</p>
                                    </td>
                                    <td>
                                        <p>Tipo</p>
                                    </td>
                                    <td>
                                        <p>Descripci&oacute;n</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>estatus</p>
                                    </td>
                                    <td>
                                        <p>entero</p>
                                    </td>
                                    <td>
                                        <p>estatus del env&iacute;o de correo electr&oacute;nico</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>mensaje</p>
                                    </td>
                                    <td>
                                        <p>cadena</p>
                                    </td>
                                    <td>
                                        <p>mensaje descriptivo</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>data</p>
                                    </td>
                                    <td>
                                        <p>cadena o arreglo de cadena</p>
                                    </td>
                                    <td>
                                        <p>Direcciones URL p&uacute;blicas del archivo o archivos subidos.</p>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div><br>
                    <p>C&oacute;digo de respuesta fallida:</p><br>
                    <div align="left">
                        <table>
                            <tbody>
                                <tr>
                                    <td>
                                        <p>C&oacute;digo</p>
                                    </td>
                                    <td>
                                        <p>Descripci&oacute;n</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>400</p>
                                    </td>
                                    <td>
                                        <p>Fallo en el proceso</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>413</p>
                                    </td>
                                    <td>
                                        <p>Error por exceder el l&iacute;mite de peso de los archivos adjuntos</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>500</p>
                                    </td>
                                    <td>
                                        <p>error interno del servidor</p>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div><br>
                    <p>Body de Salida:</p><br>
                    <div align="left">
                        <table>
                            <tbody>
                                <tr>
                                    <td>
                                        <p>Atributo</p>
                                    </td>
                                    <td>
                                        <p>Tipo</p>
                                    </td>
                                    <td>
                                        <p>Descripci&oacute;n</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>estatus</p>
                                    </td>
                                    <td>
                                        <p>entero</p>
                                    </td>
                                    <td>
                                        <p>Indica el c&oacute;digo de respuesta</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>error</p>
                                    </td>
                                    <td>
                                        <p>cadena</p>
                                    </td>
                                    <td>
                                        <p>muestra m&aacute;s informaci&oacute;n del error</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>mensaje</p>
                                    </td>
                                    <td>
                                        <p>cadena</p>
                                    </td>
                                    <td>
                                        <p>muestra el nombre del error</p>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div><br>
                    <p>Ejemplos de par&aacute;metros de entrada:</p><br>
                    <div align="left">
                        <table>
                            <tbody>
                                <tr>
                                    <td>
                                        <p>clave</p>
                                    </td>
                                    <td>
                                        <p>valor</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>archivo</p>
                                    </td>
                                    <td>
                                        <p>imagen.png</p>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div><br>
                    <p>&nbsp;</p>
                    <div align="left">
                        <table>
                            <tbody>
                                <tr>
                                    <td>
                                        <p>clave</p>
                                    </td>
                                    <td>
                                        <p>valor</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>archivo</p>
                                    </td>
                                    <td>
                                        <p>[imagen.png, imagen2.jpg]</p>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div><br>
                    <p>Ejemplos de par&aacute;metros de salida exitosa:</p>
                    <p>{</p>
                    <p>&nbsp; &nbsp;&ldquo;estatus&rdquo;: 200,</p>
                    <p>&nbsp; &nbsp;&ldquo;mensaje&rdquo;: &ldquo;Objeto almacenado&rdquo;,</p>
                    <p>&nbsp; &nbsp;&ldquo;data&rdquo;: &ldquo;https://bucket.com/archivos/imagen.png&rdquo;</p>
                    <p>}</p>
                    <p>Ejemplo de par&aacute;metros de salida fallida:</p>
                    <p>{</p>
                    <p>&nbsp; &quot;error&quot;: &quot;No hay archivos por subir&quot;,</p>
                    <p>&nbsp; &quot;estatus&quot;: 400,</p>
                    <p>&nbsp; &quot;mensaje&quot;: &quot;Archivo es requerido&quot;</p>
                    <p>}</p>
                    <p>{</p>
                    <p>&nbsp; &nbsp; &quot;error&quot;: &quot;413 Request Entity Too Large: The data value transmitted exceeds the capacity limit.&quot;,</p>
                    <p>&nbsp; &nbsp; &quot;estatus&quot;: 413,</p>
                    <p>&nbsp; &nbsp; &quot;mensaje&quot;: &quot;Error al almacenar el objeto&quot;</p>
                    <p>}</p><br>
                </td>
            </tr>
            <tr></tr>
            <tr></tr>
            <tr></tr>
            <tr></tr>
        </tbody>
    </table>
</div>
<p><br></p>
<p><br></p>
<div align="left">
    <table>
        <tbody>
            <tr>
                <td>
                    <p>ID:&nbsp;19</p>
                </td>
                <td>
                    <p>Nombre:&nbsp;Consultar productos</p>
                </td>
            </tr>
            <tr>
                <td>
                    <p>Prioridad: Baja</p>
                </td>
                <td rowspan="3">
                    <p>Historia de usuario</p>
                    <p>Como usuario quiero poder consultar y visualizar todos los productos que se tiene en inventario.&nbsp;</p>
                </td>
            </tr>
            <tr>
                <td>
                    <p>Estimado:&nbsp;3 puntos</p>
                </td>
            </tr>
            <tr>
                <td>
                    <p>M&oacute;dulo: Inventario</p>
                </td>
            </tr>
            <tr>
                <td colspan="2" rowspan="5">
                    <p>Criterios de Aceptaci&oacute;n</p>
                    <p>El microservicio &nbsp;por medio de una petici&oacute;n de tipo get, solicita la informaci&oacute;n de todos los productos en inventario con c&oacute;digo 200, en caso de alg&uacute;n error retornar&aacute; un c&oacute;digo de error y mas informaci&oacute;n del mismo.</p><br>
                    <p>El microservicio debe tener la siguiente configuraci&oacute;n:</p><br>
                    <p>Ruta:&nbsp;/inventario/productos</p>
                    <p>M&eacute;todo:&nbsp;GET</p>
                    <p>Formato de entrada:&nbsp;</p><br>
                    <p>Header:</p><br>
                    <div align="left">
                        <table>
                            <tbody>
                                <tr>
                                    <td>
                                        <p>Atributo</p>
                                    </td>
                                    <td>
                                        <p>Tipo</p>
                                    </td>
                                    <td>
                                        <p>Descripci&oacute;n</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td><br></td>
                                    <td><br></td>
                                    <td><br></td>
                                </tr>
                            </tbody>
                        </table>
                    </div><br>
                    <p>Body:</p><br>
                    <div align="left">
                        <table>
                            <tbody>
                                <tr>
                                    <td>
                                        <p>Atributo</p>
                                    </td>
                                    <td>
                                        <p>Tipo</p>
                                    </td>
                                    <td>
                                        <p>Descripci&oacute;n</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td><br></td>
                                    <td><br></td>
                                    <td><br></td>
                                </tr>
                            </tbody>
                        </table>
                    </div><br>
                    <p>Formato de salida:&nbsp;JSON</p>
                    <p>C&oacute;digo de respuesta exitosa:&nbsp;HTTP 200</p>
                    <p>Salida:&nbsp;</p><br>
                    <div align="left">
                        <table>
                            <tbody>
                                <tr>
                                    <td>
                                        <p>Atributo</p>
                                    </td>
                                    <td>
                                        <p>Tipo</p>
                                    </td>
                                    <td>
                                        <p>Descripci&oacute;n</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>estatus</p>
                                    </td>
                                    <td>
                                        <p>entero</p>
                                    </td>
                                    <td>
                                        <p>estatus del env&iacute;o de correo electr&oacute;nico</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>mensaje</p>
                                    </td>
                                    <td>
                                        <p>cadena</p>
                                    </td>
                                    <td>
                                        <p>mensaje descriptivo</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>data</p>
                                    </td>
                                    <td>
                                        <p>arreglo</p>
                                    </td>
                                    <td>
                                        <p>listado de productos</p>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div><br>
                    <p>C&oacute;digo de respuesta fallida:</p><br>
                    <div align="left">
                        <table>
                            <tbody>
                                <tr>
                                    <td>
                                        <p>C&oacute;digo</p>
                                    </td>
                                    <td>
                                        <p>Descripci&oacute;n</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>400</p>
                                    </td>
                                    <td>
                                        <p>Error al interpretar la solicitud</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>500</p>
                                    </td>
                                    <td>
                                        <p>Error interno del servidor</p>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div><br>
                    <p>Body de Salida:</p><br>
                    <div align="left">
                        <table>
                            <tbody>
                                <tr>
                                    <td>
                                        <p>Atributo</p>
                                    </td>
                                    <td>
                                        <p>Tipo</p>
                                    </td>
                                    <td>
                                        <p>Descripci&oacute;n</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>estatus</p>
                                    </td>
                                    <td>
                                        <p>entero</p>
                                    </td>
                                    <td>
                                        <p>Indica el c&oacute;digo de respuesta</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>mensaje</p>
                                    </td>
                                    <td>
                                        <p>cadena</p>
                                    </td>
                                    <td>
                                        <p>muestra el nombre del error</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>error</p>
                                    </td>
                                    <td>
                                        <p>cadena</p>
                                    </td>
                                    <td>
                                        <p>muestra m&aacute;s informaci&oacute;n del error</p>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div><br>
                    <p>Ejemplos de par&aacute;metros de entrada:</p><br>
                    <p>Ejemplos de par&aacute;metros de salida exitosa:</p>
                    <p>{</p>
                    <p>&nbsp; &nbsp;&ldquo;estatus&rdquo;: 200,</p>
                    <p>&nbsp; &nbsp;&ldquo;mensaje&rdquo;: &ldquo;Productos&rdquo;,&nbsp;</p>
                    <p>&nbsp; &nbsp;&ldquo;data&rdquo;: []</p>
                    <p>}</p><br>
                    <p>Ejemplo de par&aacute;metros de salida fallida:</p>
                    <p>{</p>
                    <p>&nbsp; &quot;estatus&quot;:500,&nbsp;</p>
                    <p>&nbsp; &quot;mensaje&quot;: &ldquo;Error al obtener productos&rdquo;&nbsp;</p>
                    <p>&nbsp; &quot;error&quot;: &ldquo;Error al conectarse a la base de datos&rdquo;</p>
                    <p>}</p><br>
                </td>
            </tr>
            <tr></tr>
            <tr></tr>
            <tr></tr>
            <tr></tr>
        </tbody>
    </table>
</div>
<p><br></p>
<p><br></p>
<p><br></p>
<div align="left">
    <table>
        <tbody>
            <tr>
                <td>
                    <p>ID:&nbsp;20</p>
                </td>
                <td>
                    <p>Nombre:&nbsp;Consultar producto espec&iacute;fico</p>
                </td>
            </tr>
            <tr>
                <td>
                    <p>Prioridad: Baja</p>
                </td>
                <td rowspan="3">
                    <p>Historia de usuario</p>
                    <p>Como usuario quiero poder consultar y visualizar un producto en espec&iacute;fico que se tiene en inventario.&nbsp;</p>
                </td>
            </tr>
            <tr>
                <td>
                    <p>Estimado:&nbsp;3 puntos</p>
                </td>
            </tr>
            <tr>
                <td>
                    <p>M&oacute;dulo: Inventario</p>
                </td>
            </tr>
            <tr>
                <td colspan="2" rowspan="5">
                    <p>Criterios de Aceptaci&oacute;n</p>
                    <p>El microservicio &nbsp;por medio de una petici&oacute;n de tipo get, solicita la informaci&oacute;n de un producto en espec&iacute;fico del inventario con c&oacute;digo 200, en caso de alg&uacute;n error retornar&aacute; un c&oacute;digo de error y mas informaci&oacute;n del mismo.</p><br>
                    <p>El microservicio debe tener la siguiente configuraci&oacute;n:</p><br>
                    <p>Ruta:&nbsp;/inventario/productos/&lt;idProducto&gt;</p>
                    <p>M&eacute;todo:&nbsp;GET</p>
                    <p>Formato de entrada:&nbsp;</p><br>
                    <p>Header:</p><br>
                    <div align="left">
                        <table>
                            <tbody>
                                <tr>
                                    <td>
                                        <p>Atributo</p>
                                    </td>
                                    <td>
                                        <p>Tipo</p>
                                    </td>
                                    <td>
                                        <p>Descripci&oacute;n</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td><br></td>
                                    <td><br></td>
                                    <td><br></td>
                                </tr>
                            </tbody>
                        </table>
                    </div><br>
                    <p>Variables en el URL:</p><br>
                    <div align="left">
                        <table>
                            <tbody>
                                <tr>
                                    <td>
                                        <p>Atributo</p>
                                    </td>
                                    <td>
                                        <p>Tipo</p>
                                    </td>
                                    <td>
                                        <p>Descripci&oacute;n</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>idProducto</p>
                                    </td>
                                    <td>
                                        <p>cadena</p>
                                    </td>
                                    <td>
                                        <p>Identificador del producto</p>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div><br>
                    <p>Formato de salida:&nbsp;JSON</p>
                    <p>C&oacute;digo de respuesta exitosa:&nbsp;HTTP 200</p>
                    <p>Salida:&nbsp;</p><br>
                    <div align="left">
                        <table>
                            <tbody>
                                <tr>
                                    <td>
                                        <p>Atributo</p>
                                    </td>
                                    <td>
                                        <p>Tipo</p>
                                    </td>
                                    <td>
                                        <p>Descripci&oacute;n</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>estatus</p>
                                    </td>
                                    <td>
                                        <p>entero</p>
                                    </td>
                                    <td>
                                        <p>estatus del env&iacute;o de correo electr&oacute;nico</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>mensaje</p>
                                    </td>
                                    <td>
                                        <p>cadena</p>
                                    </td>
                                    <td>
                                        <p>mensaje descriptivo</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>data</p>
                                    </td>
                                    <td>
                                        <p>arreglo</p>
                                    </td>
                                    <td>
                                        <p>listado de productos</p>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div><br>
                    <p>C&oacute;digo de respuesta fallida:</p><br>
                    <div align="left">
                        <table>
                            <tbody>
                                <tr>
                                    <td>
                                        <p>C&oacute;digo</p>
                                    </td>
                                    <td>
                                        <p>Descripci&oacute;n</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>400</p>
                                    </td>
                                    <td>
                                        <p>Error al interpretar la solicitud</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>500</p>
                                    </td>
                                    <td>
                                        <p>Error interno del servidor</p>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div><br>
                    <p>Body de Salida:</p><br>
                    <div align="left">
                        <table>
                            <tbody>
                                <tr>
                                    <td>
                                        <p>Atributo</p>
                                    </td>
                                    <td>
                                        <p>Tipo</p>
                                    </td>
                                    <td>
                                        <p>Descripci&oacute;n</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>estatus</p>
                                    </td>
                                    <td>
                                        <p>entero</p>
                                    </td>
                                    <td>
                                        <p>Indica el c&oacute;digo de respuesta</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>mensaje</p>
                                    </td>
                                    <td>
                                        <p>cadena</p>
                                    </td>
                                    <td>
                                        <p>muestra el nombre del error</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>error</p>
                                    </td>
                                    <td>
                                        <p>cadena</p>
                                    </td>
                                    <td>
                                        <p>muestra m&aacute;s informaci&oacute;n del error</p>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div><br>
                    <p>Ejemplos de par&aacute;metros de entrada:</p><br>
                    <p>Ejemplos de par&aacute;metros de salida exitosa:</p>
                    <p>{</p>
                    <p>&nbsp; &nbsp;&ldquo;estatus&rdquo;: 200,</p>
                    <p>&nbsp; &nbsp;&ldquo;mensaje&rdquo;: &ldquo;Producto&rdquo;,&nbsp;</p>
                    <p>&nbsp; &nbsp;&ldquo;data&rdquo;: { }</p>
                    <p>}</p><br>
                    <p>Ejemplo de par&aacute;metros de salida fallida:</p>
                    <p>{</p>
                    <p>&nbsp; &quot;estatus&quot;: 500,&nbsp;</p>
                    <p>&nbsp; &quot;mensaje&quot;: &ldquo;Error al obtener productos&rdquo;&nbsp;</p>
                    <p>&nbsp; &quot;error&quot;: &ldquo;Error al conectarse a la base de datos&rdquo;</p>
                    <p>}</p><br>
                </td>
            </tr>
            <tr></tr>
            <tr></tr>
            <tr></tr>
            <tr></tr>
        </tbody>
    </table>
</div>
<p><br></p>
<p><br></p>
<div align="left">
    <table>
        <tbody>
            <tr>
                <td>
                    <p>ID:&nbsp;21</p>
                </td>
                <td>
                    <p>Nombre:&nbsp;Consultar stock</p>
                </td>
            </tr>
            <tr>
                <td>
                    <p>Prioridad: Baja</p>
                </td>
                <td rowspan="3">
                    <p>Historia de usuario</p>
                    <p>Como usuario quiero poder consultar el stock de un producto en espec&iacute;fico en tiempo real..&nbsp;</p>
                </td>
            </tr>
            <tr>
                <td>
                    <p>Estimado:&nbsp;3 puntos</p>
                </td>
            </tr>
            <tr>
                <td>
                    <p>M&oacute;dulo: Inventario</p>
                </td>
            </tr>
            <tr>
                <td colspan="2" rowspan="5">
                    <p>Criterios de Aceptaci&oacute;n</p>
                    <p>El microservicio &nbsp;retorna el stock de un producto en espec&iacute;fico del inventario y un c&oacute;digo 200, en caso de alg&uacute;n error retornar&aacute; un c&oacute;digo de error y mas informaci&oacute;n del mismo.</p><br>
                    <p>El microservicio debe tener la siguiente configuraci&oacute;n:</p><br>
                    <p>Ruta:&nbsp;/inventario/producto/stock/&lt;idProducto&gt;</p>
                    <p>M&eacute;todo:&nbsp;GET</p>
                    <p>Formato de entrada:&nbsp;</p><br>
                    <p>Header:</p><br>
                    <div align="left">
                        <table>
                            <tbody>
                                <tr>
                                    <td>
                                        <p>Atributo</p>
                                    </td>
                                    <td>
                                        <p>Tipo</p>
                                    </td>
                                    <td>
                                        <p>Descripci&oacute;n</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td><br></td>
                                    <td><br></td>
                                    <td><br></td>
                                </tr>
                            </tbody>
                        </table>
                    </div><br>
                    <p>Variables en el URL:</p><br>
                    <div align="left">
                        <table>
                            <tbody>
                                <tr>
                                    <td>
                                        <p>Atributo</p>
                                    </td>
                                    <td>
                                        <p>Tipo</p>
                                    </td>
                                    <td>
                                        <p>Descripci&oacute;n</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>idProducto</p>
                                    </td>
                                    <td>
                                        <p>cadena</p>
                                    </td>
                                    <td>
                                        <p>Identificador del producto</p>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div><br>
                    <p>Formato de salida:&nbsp;JSON</p>
                    <p>C&oacute;digo de respuesta exitosa:&nbsp;HTTP 200</p>
                    <p>Salida:&nbsp;</p><br>
                    <div align="left">
                        <table>
                            <tbody>
                                <tr>
                                    <td>
                                        <p>Atributo</p>
                                    </td>
                                    <td>
                                        <p>Tipo</p>
                                    </td>
                                    <td>
                                        <p>Descripci&oacute;n</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>estatus</p>
                                    </td>
                                    <td>
                                        <p>entero</p>
                                    </td>
                                    <td>
                                        <p>estatus del env&iacute;o de correo electr&oacute;nico</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>mensaje</p>
                                    </td>
                                    <td>
                                        <p>cadena</p>
                                    </td>
                                    <td>
                                        <p>mensaje descriptivo</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>data</p>
                                    </td>
                                    <td>
                                        <p>numero</p>
                                    </td>
                                    <td>
                                        <p>stock del producto</p>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div><br>
                    <p>C&oacute;digo de respuesta fallida:</p><br>
                    <div align="left">
                        <table>
                            <tbody>
                                <tr>
                                    <td>
                                        <p>C&oacute;digo</p>
                                    </td>
                                    <td>
                                        <p>Descripci&oacute;n</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>400</p>
                                    </td>
                                    <td>
                                        <p>Error al interpretar la solicitud</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>500</p>
                                    </td>
                                    <td>
                                        <p>Error interno del servidor</p>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div><br>
                    <p>Body de Salida:</p><br>
                    <div align="left">
                        <table>
                            <tbody>
                                <tr>
                                    <td>
                                        <p>Atributo</p>
                                    </td>
                                    <td>
                                        <p>Tipo</p>
                                    </td>
                                    <td>
                                        <p>Descripci&oacute;n</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>estatus</p>
                                    </td>
                                    <td>
                                        <p>entero</p>
                                    </td>
                                    <td>
                                        <p>Indica el c&oacute;digo de respuesta</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>mensaje</p>
                                    </td>
                                    <td>
                                        <p>cadena</p>
                                    </td>
                                    <td>
                                        <p>muestra el nombre del error</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>error</p>
                                    </td>
                                    <td>
                                        <p>cadena</p>
                                    </td>
                                    <td>
                                        <p>muestra m&aacute;s informaci&oacute;n del error</p>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div><br>
                    <p>Ejemplos de par&aacute;metros de entrada:</p><br>
                    <p>Ejemplos de par&aacute;metros de salida exitosa:</p>
                    <p>{</p>
                    <p>&nbsp; &nbsp;&ldquo;estatus&rdquo;: 200,</p>
                    <p>&nbsp; &nbsp;&ldquo;mensaje&rdquo;: &ldquo;Stock del Producto&rdquo;,&nbsp;</p>
                    <p>&nbsp; &nbsp;&ldquo;data&rdquo;: 10</p>
                    <p>}</p><br>
                    <p>Ejemplo de par&aacute;metros de salida fallida:</p>
                    <p>{</p>
                    <p>&nbsp; &quot;estatus&quot;: 500,&nbsp;</p>
                    <p>&nbsp; &quot;mensaje&quot;: &ldquo;Error al obtener productos&rdquo;&nbsp;</p>
                    <p>&nbsp; &quot;error&quot;: &ldquo;Error al conectarse a la base de datos&rdquo;</p>
                    <p>}</p><br>
                </td>
            </tr>
            <tr></tr>
            <tr></tr>
            <tr></tr>
            <tr></tr>
        </tbody>
    </table>
</div>
<p><br></p>
<p><br></p>
<div align="left">
    <table>
        <tbody>
            <tr>
                <td>
                    <p>ID:&nbsp;22</p>
                </td>
                <td>
                    <p>Nombre:&nbsp;Actualizar inventario</p>
                </td>
            </tr>
            <tr>
                <td>
                    <p>Prioridad: Baja</p>
                </td>
                <td rowspan="3">
                    <p>Historia de usuario</p>
                    <p>Como usuario quiero poder modificar alg&uacute;n producto en espec&iacute;fico que se tiene en inventario.&nbsp;</p>
                </td>
            </tr>
            <tr>
                <td>
                    <p>Estimado:&nbsp;4 puntos</p>
                </td>
            </tr>
            <tr>
                <td>
                    <p>M&oacute;dulo: Inventario</p>
                </td>
            </tr>
            <tr>
                <td colspan="2" rowspan="5">
                    <p>Criterios de Aceptaci&oacute;n</p>
                    <p>El microservicio &nbsp;retorna un c&oacute;digo 200 con un mensaje satisfactorio al realizar la actualizaci&oacute;n satisfactoriamente, en caso de alg&uacute;n error retornar&aacute; un c&oacute;digo de error y mas informaci&oacute;n del mismo.</p><br>
                    <p>El microservicio debe tener la siguiente configuraci&oacute;n:</p><br>
                    <p>Ruta:&nbsp;/inventario/actualizarProducto/&lt;idProducto&gt;</p>
                    <p>M&eacute;todo:&nbsp;PUT</p>
                    <p>Formato de entrada:&nbsp;form-data</p><br>
                    <p>Header:</p><br>
                    <div align="left">
                        <table>
                            <tbody>
                                <tr>
                                    <td>
                                        <p>Atributo</p>
                                    </td>
                                    <td>
                                        <p>Tipo</p>
                                    </td>
                                    <td>
                                        <p>Descripci&oacute;n</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>Content-Type</p>
                                    </td>
                                    <td>
                                        <p>header</p>
                                    </td>
                                    <td>
                                        <p>multipart/form-data</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>Authorization</p>
                                    </td>
                                    <td>
                                        <p>header</p>
                                    </td>
                                    <td>
                                        <p>Bearer &lt;token&gt;</p>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div><br>
                    <p>Body:</p><br>
                    <div align="left">
                        <table>
                            <tbody>
                                <tr>
                                    <td>
                                        <p>Atributo</p>
                                    </td>
                                    <td>
                                        <p>Tipo</p>
                                    </td>
                                    <td>
                                        <p>Descripci&oacute;n</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>imagen</p>
                                    </td>
                                    <td>
                                        <p>archivo</p>
                                    </td>
                                    <td>
                                        <p>Archivo de imagen, ser&aacute;n soportados las extensiones:&nbsp;</p>
                                        <ul>
                                            <li>
                                                <p>.jpg</p>
                                            </li>
                                            <li>
                                                <p>.png</p>
                                            </li>
                                        </ul>
                                        <p>Atributo opcional</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>nombre</p>
                                    </td>
                                    <td>
                                        <p>texto</p>
                                    </td>
                                    <td>
                                        <p>nombre del producto</p>
                                        <p>Atributo obligatorio</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>descripci&oacute;n</p>
                                    </td>
                                    <td>
                                        <p>texto</p>
                                    </td>
                                    <td>
                                        <p>descripci&oacute;n del producto</p>
                                        <p>Atributo opcional</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>stock</p>
                                    </td>
                                    <td>
                                        <p>n&uacute;mero</p>
                                    </td>
                                    <td>
                                        <p>cantidad en stock del producto</p>
                                        <p>Atributo obligatorio</p>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div><br><br>
                    <p>Variables en el URL:</p><br>
                    <div align="left">
                        <table>
                            <tbody>
                                <tr>
                                    <td>
                                        <p>Atributo</p>
                                    </td>
                                    <td>
                                        <p>Tipo</p>
                                    </td>
                                    <td>
                                        <p>Descripci&oacute;n</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>idProducto</p>
                                    </td>
                                    <td>
                                        <p>cadena</p>
                                    </td>
                                    <td>
                                        <p>Identificador del producto</p>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div><br>
                    <p>Formato de salida:&nbsp;JSON</p>
                    <p>C&oacute;digo de respuesta exitosa:&nbsp;HTTP 200</p>
                    <p>Salida:&nbsp;</p><br>
                    <div align="left">
                        <table>
                            <tbody>
                                <tr>
                                    <td>
                                        <p>Atributo</p>
                                    </td>
                                    <td>
                                        <p>Tipo</p>
                                    </td>
                                    <td>
                                        <p>Descripci&oacute;n</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>estatus</p>
                                    </td>
                                    <td>
                                        <p>entero</p>
                                    </td>
                                    <td>
                                        <p>estatus del env&iacute;o de correo electr&oacute;nico</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>mensaje</p>
                                    </td>
                                    <td>
                                        <p>cadena</p>
                                    </td>
                                    <td>
                                        <p>mensaje descriptivo</p>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div><br>
                    <p>C&oacute;digo de respuesta fallida:</p><br><br>
                    <div align="left">
                        <table>
                            <tbody>
                                <tr>
                                    <td>
                                        <p>C&oacute;digo</p>
                                    </td>
                                    <td>
                                        <p>Descripci&oacute;n</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>400</p>
                                    </td>
                                    <td>
                                        <p>Error al interpretar la solicitud</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>401</p>
                                    </td>
                                    <td>
                                        <p>Usuario no autenticado</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>403</p>
                                    </td>
                                    <td>
                                        <p>Usuario sin permisos</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>500</p>
                                    </td>
                                    <td>
                                        <p>Error interno del servidor</p>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div><br><br>
                    <p>Body de Salida:</p><br>
                    <div align="left">
                        <table>
                            <tbody>
                                <tr>
                                    <td>
                                        <p>Atributo</p>
                                    </td>
                                    <td>
                                        <p>Tipo</p>
                                    </td>
                                    <td>
                                        <p>Descripci&oacute;n</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>estatus</p>
                                    </td>
                                    <td>
                                        <p>entero</p>
                                    </td>
                                    <td>
                                        <p>Indica el c&oacute;digo de respuesta</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>mensaje</p>
                                    </td>
                                    <td>
                                        <p>cadena</p>
                                    </td>
                                    <td>
                                        <p>muestra el nombre del error</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>error</p>
                                    </td>
                                    <td>
                                        <p>cadena</p>
                                    </td>
                                    <td>
                                        <p>muestra m&aacute;s informaci&oacute;n del error</p>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div><br>
                    <p>Ejemplos de par&aacute;metros de entrada:</p><br>
                    <div align="left">
                        <table>
                            <tbody>
                                <tr>
                                    <td>
                                        <p>clave</p>
                                    </td>
                                    <td>
                                        <p>valor</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>imagen</p>
                                    </td>
                                    <td>
                                        <p>file.png</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>nombre</p>
                                    </td>
                                    <td>
                                        <p>Producto 1</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>descripci&oacute;n</p>
                                    </td>
                                    <td>
                                        <p>Lorem ipsum</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>stock</p>
                                    </td>
                                    <td>
                                        <p>100</p>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div><br><br>
                    <p>Ejemplos de par&aacute;metros de salida exitosa:</p>
                    <p>{</p>
                    <p>&nbsp; &nbsp;&ldquo;estatus&rdquo;: 200,</p>
                    <p>&nbsp; &nbsp;&ldquo;mensaje&rdquo;: &ldquo;Producto modificado&rdquo;</p>
                    <p>}</p><br>
                    <p>Ejemplo de par&aacute;metros de salida fallida:</p>
                    <p>{</p>
                    <p>&nbsp; &quot;estatus&quot;: 500,&nbsp;</p>
                    <p>&nbsp; &quot;mensaje&quot;: &ldquo;Error al modificar producto&rdquo;&nbsp;</p>
                    <p>&nbsp; &quot;error&quot;: &ldquo;Error al conectarse a la base de datos&rdquo;</p>
                    <p>}</p><br>
                </td>
            </tr>
            <tr></tr>
            <tr></tr>
            <tr></tr>
            <tr></tr>
        </tbody>
    </table>
</div>
<p><br></p>
<p><br></p>
<p><br></p>
<div align="left">
    <table>
        <tbody>
            <tr>
                <td>
                    <p>ID:&nbsp;23</p>
                </td>
                <td>
                    <p>Nombre:&nbsp;Registro de planilla</p>
                </td>
            </tr>
            <tr>
                <td>
                    <p>Prioridad:&nbsp;Alta</p>
                </td>
                <td rowspan="3">
                    <p>Historia de usuario</p>
                    <p>Se quiere poder registrar una planilla para cada trabajador de la organizaci&oacute;n, y poder llevar el control de los mismos.&nbsp;</p>
                </td>
            </tr>
            <tr>
                <td>
                    <p>Estimado:&nbsp;5</p>
                </td>
            </tr>
            <tr>
                <td>
                    <p>M&oacute;dulo:&nbsp;Contabilidad</p>
                </td>
            </tr>
            <tr>
                <td colspan="2" rowspan="5">
                    <p>Criterios de Aceptaci&oacute;n</p><br>
                    <p>Poder visualizar de manera detallada cu&aacute;l es la retribuci&oacute;n que el empleado que se registra,por las tareas que realiza dentro de la compa&ntilde;&iacute;a,</p><br>
                    <p>El microservicio debe tener la siguiente configuraci&oacute;n:</p><br>
                    <p>Ruta:&nbsp;/accounting/payrollrecord</p>
                    <p>M&eacute;todo:&nbsp;POST</p>
                    <p>Formato de entrada:&nbsp;JSON</p><br>
                    <p>Payload:&nbsp;</p><br>
                    <div align="left">
                        <table>
                            <tbody>
                                <tr>
                                    <td>
                                        <p>Atributo</p>
                                    </td>
                                    <td>
                                        <p>Tipo</p>
                                    </td>
                                    <td>
                                        <p>Descripci&oacute;n</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>cui</p>
                                    </td>
                                    <td>
                                        <p>cadena</p>
                                    </td>
                                    <td>
                                        <p>el n&uacute;mero de identificaci&oacute;n del usuario.</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>tipoUsuario</p>
                                    </td>
                                    <td>
                                        <p>entero</p>
                                    </td>
                                    <td>
                                        <p>El tipo de usuario dentro de la plataforma, este puede ser:&nbsp;</p>
                                        <ul>
                                            <li>
                                                <p>1&nbsp;</p>
                                            </li>
                                            <li>
                                                <p>2</p>
                                            </li>
                                        </ul>
                                        <p>Donde:&nbsp;</p>
                                        <p>1 representa administradores</p>
                                        <p>2 clientes normales</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>exp</p>
                                    </td>
                                    <td>
                                        <p>entero</p>
                                    </td>
                                    <td>
                                        <p>Este representa la fecha de expiraci&oacute;n del token.</p>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div><br><br>
                    <p>Header:</p><br>
                    <div align="left">
                        <table>
                            <tbody>
                                <tr>
                                    <td>
                                        <p>Atributo</p>
                                    </td>
                                    <td>
                                        <p>Tipo</p>
                                    </td>
                                    <td>
                                        <p>Descripci&oacute;n</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>Content-Type</p>
                                    </td>
                                    <td>
                                        <p>header</p>
                                    </td>
                                    <td>
                                        <p>application/json</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>Authorization</p>
                                    </td>
                                    <td>
                                        <p>header</p>
                                    </td>
                                    <td>
                                        <p>Bearer &lt;token&gt;</p>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div><br>
                    <p>Body:</p><br>
                    <div align="left">
                        <table>
                            <tbody>
                                <tr>
                                    <td>
                                        <p>Atributo</p>
                                    </td>
                                    <td>
                                        <p>Tipo</p>
                                    </td>
                                    <td>
                                        <p>Descripci&oacute;n</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>cui</p>
                                    </td>
                                    <td>
                                        <p>entero</p>
                                    </td>
                                    <td>
                                        <p>identificaci&oacute;n del usuario</p>
                                        <p>Atributo requerido</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>idEmpleo</p>
                                    </td>
                                    <td>
                                        <p>entero</p>
                                    </td>
                                    <td>
                                        <p>identificador del tipo de empleo de la persona</p>
                                        <p>Atributo requerido</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>bonificaci&oacute;n</p>
                                    </td>
                                    <td>
                                        <p>arreglo</p>
                                    </td>
                                    <td>
                                        <p>arreglo con las actividades acreedoras correspondientes a un empleado correspondientes seg&uacute;n la ley</p>
                                        <p>Atributo opcional</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>extras</p>
                                    </td>
                                    <td>
                                        <p>arreglo</p>
                                    </td>
                                    <td>
                                        <p>arreglo con las actividades acreedoras correspondientes a un empleado</p>
                                        <p>Atributo opcional</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>retenci&oacute;n</p>
                                    </td>
                                    <td>
                                        <p>arreglo</p>
                                    </td>
                                    <td>
                                        <p>arreglo con las actividades que ameriten un descuento o retenci&oacute;n monetaria del empleado.</p>
                                        <p>Atributo opcional</p>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div><br>
                    <p>Formato de salida:&nbsp;JSON</p>
                    <p>C&oacute;digo de respuesta exitosa:&nbsp;HTTP 201</p>
                    <p>Salida:&nbsp;</p><br>
                    <div align="left">
                        <table>
                            <tbody>
                                <tr>
                                    <td>
                                        <p>Atributo</p>
                                    </td>
                                    <td>
                                        <p>Tipo</p>
                                    </td>
                                    <td>
                                        <p>Descripci&oacute;n</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>estatus</p>
                                    </td>
                                    <td>
                                        <p>entero</p>
                                    </td>
                                    <td>
                                        <p>indica el c&oacute;digo de respuesta de aceptaci&oacute;n</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>mensaje</p>
                                    </td>
                                    <td>
                                        <p>cadena</p>
                                    </td>
                                    <td>
                                        <p>muestra informaci&oacute;n de registro de de planilla exitoso</p>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div><br>
                    <p>C&oacute;digo de respuesta fallida:</p><br>
                    <div align="left">
                        <table>
                            <tbody>
                                <tr>
                                    <td>
                                        <p>C&oacute;digo</p>
                                    </td>
                                    <td>
                                        <p>Descripci&oacute;n</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>400</p>
                                    </td>
                                    <td>
                                        <p>Error al interpretar la solicitud</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>401</p>
                                    </td>
                                    <td>
                                        <p>El usuario no est&aacute; autenticado</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>403</p>
                                    </td>
                                    <td>
                                        <p>Usuario sin permisos</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>500</p>
                                    </td>
                                    <td>
                                        <p>Error interno del servidor</p>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div><br>
                    <p>Body de Salida:</p><br>
                    <div align="left">
                        <table>
                            <tbody>
                                <tr>
                                    <td>
                                        <p>Atributo</p>
                                    </td>
                                    <td>
                                        <p>Tipo</p>
                                    </td>
                                    <td>
                                        <p>Descripci&oacute;n</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>estatus</p>
                                    </td>
                                    <td>
                                        <p>entero</p>
                                    </td>
                                    <td>
                                        <p>indica el c&oacute;digo de respuesta fallida</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>error</p>
                                    </td>
                                    <td>
                                        <p>cadena</p>
                                    </td>
                                    <td>
                                        <p>muestra el nombre del error</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>mensaje</p>
                                    </td>
                                    <td>
                                        <p>cadena</p>
                                    </td>
                                    <td>
                                        <p>muestra m&aacute;s informaci&oacute;n del error</p>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div><br><br>
                    <p>Ejemplos de par&aacute;metros de entrada:</p>
                    <p>{</p>
                    <p>&nbsp; &quot;cui&quot;: &quot;123456789&quot;,</p>
                    <p>&nbsp; &quot;idEmpleo&quot;: 4567,</p>
                    <p>&nbsp; &quot;bonificacion&quot;: [</p>
                    <p>&nbsp; &nbsp; {</p>
                    <p>&nbsp; &nbsp; &nbsp; &quot;tipo&quot;: &quot;productividad&quot;,</p>
                    <p>&nbsp; &nbsp; &nbsp; &quot;monto&quot;: 1000.0</p>
                    <p>&nbsp; &nbsp; },</p>
                    <p>&nbsp; &nbsp; {</p>
                    <p>&nbsp; &nbsp; &nbsp; &quot;tipo&quot;: &quot;asistencia&quot;,</p>
                    <p>&nbsp; &nbsp; &nbsp; &quot;monto&quot;: 500.0</p>
                    <p>&nbsp; &nbsp; }</p>
                    <p>&nbsp; ],</p>
                    <p>&nbsp; &quot;extras&quot;: [</p>
                    <p>&nbsp; &nbsp; {</p>
                    <p>&nbsp; &nbsp; &nbsp; &quot;tipo&quot;: &quot;capacitaci&oacute;n&quot;,</p>
                    <p>&nbsp; &nbsp; &nbsp; &quot;descripcion&quot;: &quot;Curso de ventas&quot;</p>
                    <p>&nbsp; &nbsp; },</p>
                    <p>&nbsp; &nbsp; {</p>
                    <p>&nbsp; &nbsp; &nbsp; &quot;tipo&quot;: &quot;proyecto especial&quot;,</p>
                    <p>&nbsp; &nbsp; &nbsp; &quot;descripcion&quot;: &quot;Desarrollo de una nueva aplicaci&oacute;n&quot;</p>
                    <p>&nbsp; &nbsp; }</p>
                    <p>&nbsp; ],</p>
                    <p>&nbsp; &quot;retencion&quot;: [</p>
                    <p>&nbsp; &nbsp; {</p>
                    <p>&nbsp; &nbsp; &nbsp; &quot;tipo&quot;: &quot;impuestos&quot;,</p>
                    <p>&nbsp; &nbsp; &nbsp; &quot;monto&quot;: 800.0</p>
                    <p>&nbsp; &nbsp; },</p>
                    <p>&nbsp; &nbsp; {</p>
                    <p>&nbsp; &nbsp; &nbsp; &quot;tipo&quot;: &quot;pr&eacute;stamos&quot;,</p>
                    <p>&nbsp; &nbsp; &nbsp; &quot;monto&quot;: 300.0</p>
                    <p>&nbsp; &nbsp; }</p>
                    <p>&nbsp; ]</p>
                    <p>}</p><br>
                    <p>Ejemplos de par&aacute;metros de salida exitosa:</p>
                    <p>{</p>
                    <p>&quot;estatus&quot;: 201, &nbsp;</p>
                    <p>&quot;mensaje&quot;: &ldquo;Registro de planilla realizado con &eacute;xito&rdquo;</p>
                    <p>}</p><br>
                    <p>Ejemplo de par&aacute;metros de salida fallida:</p>
                    <p>{</p>
                    <p>&nbsp; &quot;estatus&quot;: 401,</p>
                    <p>&nbsp; &quot;mensaje&quot;: &quot;Acceso denegado&quot;,</p>
                    <p>&nbsp; &quot;error&quot;: &quot;Credenciales inv&aacute;lidas&quot;</p>
                    <p>}</p>
                </td>
            </tr>
            <tr></tr>
            <tr></tr>
            <tr></tr>
            <tr></tr>
        </tbody>
    </table>
</div>
<p><br></p>
<p><br></p>
<p><br></p>
<div align="left">
    <table>
        <tbody>
            <tr>
                <td>
                    <p>ID:&nbsp;24</p>
                </td>
                <td>
                    <p>Nombre:&nbsp;Reporte / Consulta de ganancias</p>
                </td>
            </tr>
            <tr>
                <td>
                    <p>Prioridad:&nbsp;Alta</p>
                </td>
                <td rowspan="3">
                    <p>Historia de usuario</p>
                    <p>Se quiere poder consultar el estado de cuentas de la empresa, los activos, pasivos y saldo de la empresa&nbsp;</p>
                </td>
            </tr>
            <tr>
                <td>
                    <p>Estimado:&nbsp;5</p>
                </td>
            </tr>
            <tr>
                <td>
                    <p>M&oacute;dulo:&nbsp;Contabilidad</p>
                </td>
            </tr>
            <tr>
                <td colspan="2" rowspan="5">
                    <p>Criterios de Aceptaci&oacute;n</p><br>
                    <p>Poder visualizar un reporte de los activos y pasivos de la empresa, para visualizar el estado de cuentas de la empresa.&nbsp;</p><br>
                    <p>El microservicio debe tener la siguiente configuraci&oacute;n:</p><br>
                    <p>Ruta:&nbsp;/accounting/report</p>
                    <p>M&eacute;todo:&nbsp;GET</p>
                    <p>Formato de entrada:&nbsp;</p><br>
                    <p>Payload:&nbsp;</p><br>
                    <div align="left">
                        <table>
                            <tbody>
                                <tr>
                                    <td>
                                        <p>Atributo</p>
                                    </td>
                                    <td>
                                        <p>Tipo</p>
                                    </td>
                                    <td>
                                        <p>Descripci&oacute;n</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>cui</p>
                                    </td>
                                    <td>
                                        <p>cadena</p>
                                    </td>
                                    <td>
                                        <p>el n&uacute;mero de identificaci&oacute;n del usuario.</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>tipoUsuario</p>
                                    </td>
                                    <td>
                                        <p>entero</p>
                                    </td>
                                    <td>
                                        <p>El tipo de usuario dentro de la plataforma, este puede ser:&nbsp;</p>
                                        <ul>
                                            <li>
                                                <p>1&nbsp;</p>
                                            </li>
                                            <li>
                                                <p>2</p>
                                            </li>
                                        </ul>
                                        <p>Donde:&nbsp;</p>
                                        <p>1 representa administradores</p>
                                        <p>2 clientes normales</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>exp</p>
                                    </td>
                                    <td>
                                        <p>entero</p>
                                    </td>
                                    <td>
                                        <p>Este representa la fecha de expiraci&oacute;n del token.</p>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div><br><br>
                    <p>Header:</p><br>
                    <div align="left">
                        <table>
                            <tbody>
                                <tr>
                                    <td>
                                        <p>Atributo</p>
                                    </td>
                                    <td>
                                        <p>Tipo</p>
                                    </td>
                                    <td>
                                        <p>Descripci&oacute;n</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>Authorization</p>
                                    </td>
                                    <td>
                                        <p>header</p>
                                    </td>
                                    <td>
                                        <p>Bearer &lt;token&gt;</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>Content-Type</p>
                                    </td>
                                    <td>
                                        <p>header</p>
                                    </td>
                                    <td>
                                        <p>application/json</p>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div><br>
                    <p>Body:</p><br>
                    <div align="left">
                        <table>
                            <tbody>
                                <tr>
                                    <td>
                                        <p>Atributo</p>
                                    </td>
                                    <td>
                                        <p>Tipo</p>
                                    </td>
                                    <td>
                                        <p>Descripci&oacute;n</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>anio</p>
                                    </td>
                                    <td>
                                        <p>entero</p>
                                    </td>
                                    <td>
                                        <p>A&ntilde;o del cual se desea conocer el reporte de ganancias.&nbsp;</p>
                                        <p>Atributo requerido</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>tipo</p>
                                    </td>
                                    <td>
                                        <p>entero</p>
                                    </td>
                                    <td>
                                        <p>se podr&aacute; obtener el rango de tiempo del reporte, los cuales ser&aacute;n estas opciones:&nbsp;</p>
                                        <ul>
                                            <li>
                                                <p>mes = 1</p>
                                            </li>
                                            <li>
                                                <p>trimestre = 2</p>
                                            </li>
                                            <li>
                                                <p>a&ntilde;o = 3</p>
                                            </li>
                                        </ul>
                                        <p>Atributo requerido</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>periodo</p>
                                    </td>
                                    <td>
                                        <p>entero</p>
                                    </td>
                                    <td>
                                        <p>se podr&aacute; obtener ingresar el periodo de tiempo seg&uacute;n el tipo seleccionado.</p>
                                        <p>mes = n&uacute;mero del mes</p>
                                        <p>trimestre = n&uacute;mero de trimestre&nbsp;</p>
                                        <p>a&ntilde;o = no aplica&nbsp;</p>
                                        <p>Atributo opcional</p>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div><br>
                    <p>Formato de salida:&nbsp;JSON</p>
                    <p>C&oacute;digo de respuesta exitosa:&nbsp;HTTP 200</p>
                    <p>Salida:&nbsp;</p><br>
                    <div align="left">
                        <table>
                            <tbody>
                                <tr>
                                    <td>
                                        <p>Atributo</p>
                                    </td>
                                    <td>
                                        <p>Tipo</p>
                                    </td>
                                    <td>
                                        <p>Descripci&oacute;n</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>estatus</p>
                                    </td>
                                    <td>
                                        <p>entero</p>
                                    </td>
                                    <td>
                                        <p>indica el c&oacute;digo de respuesta de aceptaci&oacute;n</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>mensaje</p>
                                    </td>
                                    <td>
                                        <p>cadena</p>
                                    </td>
                                    <td>
                                        <p>muestra informaci&oacute;n de registro de de planilla exitoso</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>data</p>
                                    </td>
                                    <td>
                                        <p>arreglo</p>
                                    </td>
                                    <td>
                                        <p>los datos que se obtuvieron de la consulta en formato de arreglo de JSONs</p>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div><br>
                    <p>C&oacute;digo de respuesta fallida:</p><br>
                    <div align="left">
                        <table>
                            <tbody>
                                <tr>
                                    <td>
                                        <p>C&oacute;digo</p>
                                    </td>
                                    <td>
                                        <p>Descripci&oacute;n</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>400</p>
                                    </td>
                                    <td>
                                        <p>Error al interpretar la solicitud</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>401</p>
                                    </td>
                                    <td>
                                        <p>El usuario no est&aacute; autenticado</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>403</p>
                                    </td>
                                    <td>
                                        <p>Usuario sin permisos</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>500</p>
                                    </td>
                                    <td>
                                        <p>Error interno del servidor</p>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div><br>
                    <p>Body de Salida:</p><br>
                    <div align="left">
                        <table>
                            <tbody>
                                <tr>
                                    <td>
                                        <p>Atributo</p>
                                    </td>
                                    <td>
                                        <p>Tipo</p>
                                    </td>
                                    <td>
                                        <p>Descripci&oacute;n</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>estatus</p>
                                    </td>
                                    <td>
                                        <p>entero</p>
                                    </td>
                                    <td>
                                        <p>indica el c&oacute;digo de respuesta fallida</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>error</p>
                                    </td>
                                    <td>
                                        <p>cadena</p>
                                    </td>
                                    <td>
                                        <p>muestra el nombre del error</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>mensaje</p>
                                    </td>
                                    <td>
                                        <p>cadena</p>
                                    </td>
                                    <td>
                                        <p>muestra m&aacute;s informaci&oacute;n del error</p>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div><br><br>
                    <p>Ejemplos de par&aacute;metros de entrada:</p>
                    <p>{</p>
                    <p>&nbsp; &nbsp; &ldquo;anio&rdquo;: 2023,</p>
                    <p>&nbsp; &nbsp; &ldquo;tipo&rdquo;: 1,</p>
                    <p>&nbsp; &nbsp; &ldquo;periodo&rdquo;:1&nbsp;</p>
                    <p>}</p>
                    <p>Ejemplos de par&aacute;metros de salida exitosa:</p>
                    <p>{</p>
                    <p>&nbsp; &quot;nombreEmpresa&quot;: &quot;Nombre de la empresa&quot;,</p>
                    <p>&nbsp; &quot;a&ntilde;o&quot;: 2023,</p>
                    <p>&nbsp; &quot;periodo&quot;: &quot;Enero&quot;,</p>
                    <p>&nbsp; &quot;Ingresosoperativos&quot;: {</p>
                    <p>&nbsp; &nbsp; &quot;Ventasdeproductos&quot;: &quot;Q12,000&quot;,</p>
                    <p>&nbsp; &nbsp; &quot;Ventasdeservicios&quot;: &quot;Q3,000&quot;,</p>
                    <p>&nbsp; &nbsp; &quot;TotalOperatingRevenue&quot;: &quot;Q15,000&quot;</p>
                    <p>&nbsp; },</p>
                    <p>&nbsp; &quot;Gastosoperativos&quot;: {</p>
                    <p>&nbsp; &nbsp; &quot;Costodemercanc&iacute;asvendidas&quot;: &quot;Q7,000&quot;,</p>
                    <p>&nbsp; &nbsp; &quot;Gananciabruta&quot;: &quot;Q8,000&quot;</p>
                    <p>&nbsp; },</p>
                    <p>&nbsp; &quot;Gastosfijos&quot;: {</p>
                    <p>&nbsp; &nbsp; &quot;Alquiler&quot;: &quot;Q1,500&quot;,</p>
                    <p>&nbsp; &nbsp; &quot;Seguro&quot;: &quot;Q250&quot;,</p>
                    <p>&nbsp; &nbsp; &quot;Art&iacute;culosdeoficina&quot;: &quot;Q150&quot;,</p>
                    <p>&nbsp; &nbsp; &quot;Serviciosp&uacute;blicos&quot;: &quot;Q100&quot;,</p>
                    <p>&nbsp; &nbsp; &quot;Totaldegastosfijos&quot;: &quot;Q2,000&quot;,</p>
                    <p>&nbsp; &nbsp; &quot;Ingresosoperativos&quot;: &quot;Q6,000&quot;</p>
                    <p>&nbsp; },</p>
                    <p>&nbsp; &quot;Otrosgastos&quot;: {</p>
                    <p>&nbsp; &nbsp; &quot;Inter&eacute;sporpr&eacute;stamos&quot;: &quot;Q500&quot;,</p>
                    <p>&nbsp; &nbsp; &quot;Gananciasantesdeimpuestos&quot;: &quot;Q5,500&quot;,</p>
                    <p>&nbsp; &nbsp; &quot;Impuestosalarenta&quot;: &quot;Q500&quot;</p>
                    <p>&nbsp; },</p>
                    <p>&nbsp; &quot;Gananciasnetas&quot;: &quot;Q5,000&quot;</p>
                    <p>}</p><br>
                    <p>Ejemplo de par&aacute;metros de salida fallida:</p>
                    <p>{</p>
                    <p>&nbsp; &nbsp; &ldquo;estatus&rdquo;: 401,</p>
                    <p>&nbsp; &nbsp; &ldquo;error&rdquo;: &ldquo;Usuario no autenticado&rdquo;,</p>
                    <p>&nbsp; &nbsp; &ldquo;mensaje&rdquo;: &ldquo;La sesi&oacute;n del usuario a expirado o no se a iniciado sesi&oacute;n&rdquo;</p>
                    <p>}</p><br>
                </td>
            </tr>
            <tr></tr>
            <tr></tr>
            <tr></tr>
            <tr></tr>
        </tbody>
    </table>
</div>
<p><br></p>
<p><br></p>
<p><br></p>
<div align="left">
    <table>
        <tbody>
            <tr>
                <td>
                    <p>ID:&nbsp;25</p>
                </td>
                <td>
                    <p>Nombre:&nbsp;Pago de planilla</p>
                </td>
            </tr>
            <tr>
                <td>
                    <p>Prioridad:&nbsp;Alta</p>
                </td>
                <td rowspan="3">
                    <p>Historia de usuario</p>
                    <p>Se requiere poder realizar el pago de planilla de cada trabajador de la empresa. y llevar un control de los pagos.&nbsp;</p>
                </td>
            </tr>
            <tr>
                <td>
                    <p>Estimado:&nbsp;5</p>
                </td>
            </tr>
            <tr>
                <td>
                    <p>M&oacute;dulo:&nbsp;Contabilidad</p>
                </td>
            </tr>
            <tr>
                <td colspan="2" rowspan="5">
                    <p>Criterios de Aceptaci&oacute;n</p><br>
                    <p>Poder generar los pagos de planilla de cada trabajador y llevar el respectivo control de los mismos.&nbsp;</p><br>
                    <p>El microservicio debe tener la siguiente configuraci&oacute;n:</p><br>
                    <p>Ruta:&nbsp;/accounting/payroll</p>
                    <p>M&eacute;todo:&nbsp;POST</p>
                    <p>Formato de entrada:&nbsp;</p><br>
                    <p>Payload:&nbsp;</p><br>
                    <div align="left">
                        <table>
                            <tbody>
                                <tr>
                                    <td>
                                        <p>Atributo</p>
                                    </td>
                                    <td>
                                        <p>Tipo</p>
                                    </td>
                                    <td>
                                        <p>Descripci&oacute;n</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>cui</p>
                                    </td>
                                    <td>
                                        <p>cadena</p>
                                    </td>
                                    <td>
                                        <p>el n&uacute;mero de identificaci&oacute;n del usuario.</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>tipoUsuario</p>
                                    </td>
                                    <td>
                                        <p>entero</p>
                                    </td>
                                    <td>
                                        <p>El tipo de usuario dentro de la plataforma, este puede ser:&nbsp;</p>
                                        <ul>
                                            <li>
                                                <p>1&nbsp;</p>
                                            </li>
                                            <li>
                                                <p>2</p>
                                            </li>
                                        </ul>
                                        <p>Donde:&nbsp;</p>
                                        <p>1 representa administradores</p>
                                        <p>2 clientes normales</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>exp</p>
                                    </td>
                                    <td>
                                        <p>entero</p>
                                    </td>
                                    <td>
                                        <p>Este representa la fecha de expiraci&oacute;n del token.</p>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div><br><br>
                    <p>Header:</p><br>
                    <div align="left">
                        <table>
                            <tbody>
                                <tr>
                                    <td>
                                        <p>Atributo</p>
                                    </td>
                                    <td>
                                        <p>Tipo</p>
                                    </td>
                                    <td>
                                        <p>Descripci&oacute;n</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>Authorization</p>
                                    </td>
                                    <td>
                                        <p>header</p>
                                    </td>
                                    <td>
                                        <p>Bearer &lt;token&gt;</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>Content-Type</p>
                                    </td>
                                    <td>
                                        <p>header</p>
                                    </td>
                                    <td>
                                        <p>application/json</p>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div><br>
                    <p>Body:</p><br>
                    <div align="left">
                        <table>
                            <tbody>
                                <tr>
                                    <td>
                                        <p>Atributo</p>
                                    </td>
                                    <td>
                                        <p>Tipo</p>
                                    </td>
                                    <td>
                                        <p>Descripci&oacute;n</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>cui</p>
                                    </td>
                                    <td>
                                        <p>entero</p>
                                    </td>
                                    <td>
                                        <p>id del empleado a pagar.&nbsp;</p>
                                        <p>Atributo requerido</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>metodo</p>
                                    </td>
                                    <td>
                                        <p>entero</p>
                                    </td>
                                    <td>
                                        <p>m&eacute;todo de pago:</p>
                                        <p>transferencia bancaria = 1</p>
                                        <p>cheque = 2</p>
                                        <p>Atributo requerido</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>mes&nbsp;</p>
                                    </td>
                                    <td>
                                        <p>entero</p>
                                    </td>
                                    <td>
                                        <p>N&uacute;mero del mes a pagar</p>
                                        <p>Atributo requerido</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>anio</p>
                                    </td>
                                    <td>
                                        <p>entero</p>
                                    </td>
                                    <td>
                                        <p>a&ntilde;o del pago en que se hace el pago.</p>
                                        <p>Atributo requerido</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>moneda</p>
                                    </td>
                                    <td>
                                        <p>cadena</p>
                                    </td>
                                    <td>
                                        <p>tipo de moneda para realizar el pago.&nbsp;</p>
                                        <p>Atributo requerido</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>descripcion</p>
                                    </td>
                                    <td>
                                        <p>cadena</p>
                                    </td>
                                    <td>
                                        <p>Descripci&oacute;n del pago de planilla.</p>
                                        <p>Atributo requerido</p>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div><br>
                    <p>Formato de salida:&nbsp;JSON</p>
                    <p>C&oacute;digo de respuesta exitosa:&nbsp;HTTP 200</p>
                    <p>Salida:&nbsp;</p><br>
                    <div align="left">
                        <table>
                            <tbody>
                                <tr>
                                    <td>
                                        <p>Atributo</p>
                                    </td>
                                    <td>
                                        <p>Tipo</p>
                                    </td>
                                    <td>
                                        <p>Descripci&oacute;n</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>estatus</p>
                                    </td>
                                    <td>
                                        <p>entero</p>
                                    </td>
                                    <td>
                                        <p>indica el c&oacute;digo de respuesta de aceptaci&oacute;n</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>mensaje</p>
                                    </td>
                                    <td>
                                        <p>cadena</p>
                                    </td>
                                    <td>
                                        <p>muestra informaci&oacute;n de la planilla pagada con &eacute;xito.&nbsp;</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>data</p>
                                    </td>
                                    <td>
                                        <p>objeto</p>
                                    </td>
                                    <td>
                                        <p>contiene la informaci&oacute;n de toda la planilla de un empleado, el nombre, puesto, saldo l&iacute;quido, y los detalles del pago.&nbsp;</p>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div><br>
                    <p>C&oacute;digo de respuesta fallida:</p><br>
                    <div align="left">
                        <table>
                            <tbody>
                                <tr>
                                    <td>
                                        <p>C&oacute;digo</p>
                                    </td>
                                    <td>
                                        <p>Descripci&oacute;n</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>400</p>
                                    </td>
                                    <td>
                                        <p>Error al interpretar la solicitud</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>401</p>
                                    </td>
                                    <td>
                                        <p>El usuario no est&aacute; autenticado</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>403</p>
                                    </td>
                                    <td>
                                        <p>Usuario sin permisos</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>500</p>
                                    </td>
                                    <td>
                                        <p>Error interno del servidor</p>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div><br>
                    <p>Body de Salida:</p><br>
                    <div align="left">
                        <table>
                            <tbody>
                                <tr>
                                    <td>
                                        <p>Atributo</p>
                                    </td>
                                    <td>
                                        <p>Tipo</p>
                                    </td>
                                    <td>
                                        <p>Descripci&oacute;n</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>estatus</p>
                                    </td>
                                    <td>
                                        <p>entero</p>
                                    </td>
                                    <td>
                                        <p>indica el c&oacute;digo de respuesta fallida</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>error</p>
                                    </td>
                                    <td>
                                        <p>cadena</p>
                                    </td>
                                    <td>
                                        <p>muestra el nombre del error</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>mensaje</p>
                                    </td>
                                    <td>
                                        <p>cadena</p>
                                    </td>
                                    <td>
                                        <p>muestra m&aacute;s informaci&oacute;n del error</p>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div><br><br>
                    <p>Ejemplos de par&aacute;metros de entrada:</p>
                    <p>{</p>
                    <p>&nbsp; &quot;cui&quot;: &quot;1234567890123&quot;,</p>
                    <p>&nbsp; &quot;metodo&quot;: &quot;1&quot;,</p>
                    <p>&nbsp; &quot;mes&quot;: 12,</p>
                    <p>&nbsp; &quot;anio&quot;: 2023,</p>
                    <p>&nbsp; &quot;moneda&quot;: &quot;GTQ&quot;,</p>
                    <p>&nbsp; &quot;descripcion&quot;: &quot;Pago de planilla del mes de diciembre 2023&quot;</p>
                    <p>}</p><br><br>
                    <p>Ejemplos de par&aacute;metros de salida exitosa:</p>
                    <p>{</p>
                    <p>&nbsp; &quot;estatus&quot;: 201,</p>
                    <p>&nbsp; &quot;mensaje&quot;: &quot;Planilla pagada con &eacute;xito&quot;,</p>
                    <p>&nbsp; &quot;data&quot;: {</p>
                    <p>&nbsp; &nbsp; &quot;nombreEmpresa&quot;: &quot;ACME Corporation&quot;,</p>
                    <p>&nbsp; &nbsp; &quot;mes&quot;: &quot;enero&quot;,</p>
                    <p>&nbsp; &nbsp; &quot;a&ntilde;o&quot;: 2023,</p>
                    <p>&nbsp; &nbsp; &quot;empleado&quot;: {</p>
                    <p>&nbsp; &nbsp; &nbsp; &quot;nombre&quot;: &quot;Juan P&eacute;rez&quot;,</p>
                    <p>&nbsp; &nbsp; &nbsp; &quot;cui&quot;: &quot;1234567890123&quot;,</p>
                    <p>&nbsp; &nbsp; &nbsp; &quot;puesto&quot;: &quot;desarrollador frontend&quot;,</p>
                    <p>&nbsp; &nbsp; &nbsp; &quot;tipoPago&quot;: &quot;transferencia bancaria&quot;,</p>
                    <p>&nbsp; &nbsp; &nbsp; &quot;sueldoBase&quot;: 5000,</p>
                    <p>&nbsp; &nbsp; &nbsp; &quot;bonificacion&quot;: [</p>
                    <p>&nbsp; &nbsp; &nbsp; &nbsp; {</p>
                    <p>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &quot;tipo&quot;: &quot;productividad&quot;,</p>
                    <p>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &quot;monto&quot;: 1000.0</p>
                    <p>&nbsp; &nbsp; &nbsp; &nbsp; },</p>
                    <p>&nbsp; &nbsp; &nbsp; &nbsp; {</p>
                    <p>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &quot;tipo&quot;: &quot;asistencia&quot;,</p>
                    <p>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &quot;monto&quot;: 500.0</p>
                    <p>&nbsp; &nbsp; &nbsp; &nbsp; }</p>
                    <p>&nbsp; &nbsp; &nbsp; ],</p>
                    <p>&nbsp; &nbsp; &nbsp; &quot;extras&quot;: [</p>
                    <p>&nbsp; &nbsp; &nbsp; &nbsp; {</p>
                    <p>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &quot;tipo&quot;: &quot;capacitaci&oacute;n&quot;,</p>
                    <p>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &quot;descripcion&quot;: &quot;Curso de ventas&quot;</p>
                    <p>&nbsp; &nbsp; &nbsp; &nbsp; },</p>
                    <p>&nbsp; &nbsp; &nbsp; &nbsp; {</p>
                    <p>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &quot;tipo&quot;: &quot;proyecto especial&quot;,</p>
                    <p>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &quot;descripcion&quot;: &quot;Desarrollo de una nueva aplicaci&oacute;n&quot;</p>
                    <p>&nbsp; &nbsp; &nbsp; &nbsp; }</p>
                    <p>&nbsp; &nbsp; &nbsp; ],</p>
                    <p>&nbsp; &nbsp; &nbsp; &quot;retencion&quot;: [</p>
                    <p>&nbsp; &nbsp; &nbsp; &nbsp; {</p>
                    <p>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &quot;tipo&quot;: &quot;impuestos&quot;,</p>
                    <p>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &quot;monto&quot;: 800.0</p>
                    <p>&nbsp; &nbsp; &nbsp; &nbsp; },</p>
                    <p>&nbsp; &nbsp; &nbsp; &nbsp; {</p>
                    <p>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &quot;tipo&quot;: &quot;pr&eacute;stamos&quot;,</p>
                    <p>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &quot;monto&quot;: 300.0</p>
                    <p>&nbsp; &nbsp; &nbsp; &nbsp; }</p>
                    <p>&nbsp; &nbsp; &nbsp; ],</p>
                    <p>&nbsp; &nbsp; &nbsp; &quot;total&quot;: 8000</p>
                    <p>&nbsp; &nbsp; }</p>
                    <p>&nbsp; }</p>
                    <p>}</p>
                    <p>Ejemplo de par&aacute;metros de salida fallida:</p>
                    <p>{</p>
                    <p>&nbsp; &nbsp; &ldquo;estatus&rdquo;: 401,</p>
                    <p>&nbsp; &nbsp; &ldquo;error&rdquo;: &ldquo;Usuario no autenticado&rdquo;,</p>
                    <p>&nbsp; &nbsp; &ldquo;mensaje&rdquo;: &ldquo;La sesi&oacute;n del usuario a expirado o no se a iniciado sesi&oacute;n&rdquo;</p>
                    <p>}</p><br>
                </td>
            </tr>
            <tr></tr>
            <tr></tr>
            <tr></tr>
            <tr></tr>
        </tbody>
    </table>
</div>
<p><br></p>
<p><br></p>
<p><br></p>
<p><br></p>
<p><br></p>
<p><br></p>
<div align="left">
    <table>
        <tbody>
            <tr>
                <td>
                    <p>ID:&nbsp;26</p>
                </td>
                <td>
                    <p>Nombre:&nbsp;Verificar ruta de la compra</p>
                </td>
            </tr>
            <tr>
                <td>
                    <p>Prioridad:&nbsp;Media</p>
                </td>
                <td rowspan="3">
                    <p>Historia de usuario</p>
                    <p>Es necesario que la ubicaci&oacute;n sea v&aacute;lida para su posterior entrega, en la compra se debe validar y registrar la ruta de entrega si es que es v&aacute;lida la ubicaci&oacute;n e informar en el caso que no lo sea.</p>
                </td>
            </tr>
            <tr>
                <td>
                    <p>Estimado:&nbsp;2 puntos</p>
                </td>
            </tr>
            <tr>
                <td>
                    <p>M&oacute;dulo:&nbsp;Rutas</p>
                </td>
            </tr>
            <tr>
                <td colspan="2" rowspan="5">
                    <p>Criterios de Aceptaci&oacute;n</p>
                    <p>El microservicio retorna un c&oacute;digo 200 con un mensaje satisfactorio al agregar la ruta de la entrega y verificar la ubicaci&oacute;n de manera exitosa, para los siguientes casos se retornar&aacute; un c&oacute;digo de error con informaci&oacute;n del mismo:</p>
                    <ul>
                        <li>
                            <p>La ubicaci&oacute;n no sea v&aacute;lida</p>
                        </li>
                    </ul><br>
                    <p>El microservicio debe tener la siguiente configuraci&oacute;n:</p>
                    <p>Ruta:&nbsp;/rutas/verificarRuta</p>
                    <p>M&eacute;todo:&nbsp;POST</p>
                    <p>Formato de entrada:&nbsp;form-data</p><br>
                    <p>Payload:&nbsp;</p><br>
                    <div align="left">
                        <table>
                            <tbody>
                                <tr>
                                    <td>
                                        <p>Atributo</p>
                                    </td>
                                    <td>
                                        <p>Tipo</p>
                                    </td>
                                    <td>
                                        <p>Descripci&oacute;n</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>cui</p>
                                    </td>
                                    <td>
                                        <p>cadena</p>
                                    </td>
                                    <td>
                                        <p>el n&uacute;mero de identificaci&oacute;n del usuario.</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>exp</p>
                                    </td>
                                    <td>
                                        <p>entero</p>
                                    </td>
                                    <td>
                                        <p>Este representa la fecha de expiraci&oacute;n del token.</p>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div><br>
                    <p>Header:</p><br>
                    <div align="left">
                        <table>
                            <tbody>
                                <tr>
                                    <td>
                                        <p>Atributo</p>
                                    </td>
                                    <td>
                                        <p>Tipo</p>
                                    </td>
                                    <td>
                                        <p>Descripci&oacute;n</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>Content-Type</p>
                                    </td>
                                    <td>
                                        <p>header</p>
                                    </td>
                                    <td>
                                        <p>multipart/form-data</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>Authorization</p>
                                    </td>
                                    <td>
                                        <p>header</p>
                                    </td>
                                    <td>
                                        <p>Bearer &lt;token&gt;</p>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div><br>
                    <p>Body:</p>
                    <div align="left">
                        <table>
                            <tbody>
                                <tr>
                                    <td>
                                        <p>Atributo</p>
                                    </td>
                                    <td>
                                        <p>Tipo</p>
                                    </td>
                                    <td>
                                        <p>Descripci&oacute;n</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>Ubicaci&oacute;n</p>
                                    </td>
                                    <td>
                                        <p>cadena</p>
                                    </td>
                                    <td>
                                        <p>ubicaci&oacute;n de la compra</p>
                                        <p>Campo obligatorio</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>idCompra</p>
                                    </td>
                                    <td>
                                        <p>entero</p>
                                    </td>
                                    <td>
                                        <p>identificador de la compra</p>
                                        <p>Campo obligatorio</p>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div><br><br>
                    <p>Formato de salida:&nbsp;JSON</p>
                    <p>C&oacute;digo de respuesta exitosa:&nbsp;HTTP 200</p>
                    <p>Salida:&nbsp;</p><br>
                    <div align="left">
                        <table>
                            <tbody>
                                <tr>
                                    <td>
                                        <p>Atributo</p>
                                    </td>
                                    <td>
                                        <p>Tipo</p>
                                    </td>
                                    <td>
                                        <p>Descripci&oacute;n</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>estatus</p>
                                    </td>
                                    <td>
                                        <p>entero</p>
                                    </td>
                                    <td>
                                        <p>indica el c&oacute;digo de respuesta de aceptaci&oacute;n</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>mensaje</p>
                                    </td>
                                    <td>
                                        <p>cadena</p>
                                    </td>
                                    <td>
                                        <p>muestra informaci&oacute;n de la verificaci&oacute;n de la ruta de entrega</p>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div><br><br><br><br><br><br>
                    <p>C&oacute;digo de respuesta fallida:</p><br>
                    <div align="left">
                        <table>
                            <tbody>
                                <tr>
                                    <td>
                                        <p>C&oacute;digo</p>
                                    </td>
                                    <td>
                                        <p>Descripci&oacute;n</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>400</p>
                                    </td>
                                    <td>
                                        <p>Error al interpretar la solicitud</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>401</p>
                                    </td>
                                    <td>
                                        <p>Usuario no autenticado</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>500</p>
                                    </td>
                                    <td>
                                        <p>Error interno del servidor</p>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div><br>
                    <p>Body de Salida:</p><br>
                    <div align="left">
                        <table>
                            <tbody>
                                <tr>
                                    <td>
                                        <p>Atributo</p>
                                    </td>
                                    <td>
                                        <p>Tipo</p>
                                    </td>
                                    <td>
                                        <p>Descripci&oacute;n</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>estatus</p>
                                    </td>
                                    <td>
                                        <p>entero</p>
                                    </td>
                                    <td>
                                        <p>indica el c&oacute;digo de respuesta fallido</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>error</p>
                                    </td>
                                    <td>
                                        <p>cadena</p>
                                    </td>
                                    <td>
                                        <p>muestra el nombre del error</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>mensaje</p>
                                    </td>
                                    <td>
                                        <p>cadena</p>
                                    </td>
                                    <td>
                                        <p>muestra m&aacute;s informaci&oacute;n del error</p>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div><br>
                    <p>Ejemplos de par&aacute;metros de entrada:</p><br>
                    <div align="left">
                        <table>
                            <tbody>
                                <tr>
                                    <td>
                                        <p>ubicaci&oacute;n</p>
                                    </td>
                                    <td>
                                        <p>14 AV. 6-29 zona 3, Ciudad de Guatemala&nbsp;</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>idCompra</p>
                                    </td>
                                    <td>
                                        <p>26</p>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div><br>
                    <p>Ejemplos de par&aacute;metros de salida exitosa:</p>
                    <p>{</p>
                    <p>&nbsp; &nbsp; &ldquo;estatus&rdquo;: 200,</p>
                    <p>&nbsp; &nbsp; &ldquo;mensaje&rdquo;: &ldquo;Se registr&oacute; la ruta de la entrega de la compra de manera exitosa&rdquo;</p>
                    <p>}</p>
                    <p>Ejemplo de par&aacute;metros de salida fallida:</p>
                    <p>{</p>
                    <p>&nbsp; &nbsp; &ldquo;estatus&rdquo;: 400</p>
                    <p>&nbsp; &nbsp; &ldquo;error&rdquo;:&rdquo;Ubicaci&oacute;n &nbsp;invalido&rdquo;,</p>
                    <p>&nbsp; &nbsp; &ldquo;mensaje&rdquo;:&rdquo;La ubicaci&oacute;n es incorrecta&rdquo;</p>
                    <p>}</p><br>
                    <p>{</p>
                    <p>&nbsp; &nbsp; &ldquo;estatus&rdquo;: 401</p>
                    <p>&nbsp; &nbsp; &ldquo;error&rdquo;:&rdquo;Token expirado&rdquo;,</p>
                    <p>&nbsp; &nbsp; &ldquo;mensaje&rdquo;:&rdquo;El token es invalido o a expirado, vuelva a autenticarse&rdquo;</p>
                    <p>}</p>
                </td>
            </tr>
            <tr></tr>
            <tr></tr>
            <tr></tr>
            <tr></tr>
        </tbody>
    </table>
</div>

## Bitácora de las tareas.
+ ### Sprint Planning
    | Fecha             | 23 de febrero 2023                                  |
    | ----------------- | --------------------------------------------------- |
    | **Participantes** | Alex Méndez <br /> Mynor Ruiz <br /> Maynor Piló <br /> Elian Estrada |


    ### Temas Discutidos
    + Definición el tablero a utilizar
    + Creación de Epics y sus respesctivas Task
    + Crear el BackLog
    + Creación del Sprint
    + Asignación de tareas
    
    ### Anexo 
    + [Sprint Planning](https://drive.google.com/file/d/1bzAjlQmTejVXNaSav36Zf00gpgBSUApS/view?usp=sharing)

+ ### Daily 1
    | Fecha             | 23 de febrero 2023                                  |
    | ----------------- | --------------------------------------------------- |
    | **Participantes** | Alex Méndez <br /> Maynor Piló <br /> Elian Estrada |


    ### Temas Discutidos
    + Herramientas a utilizar para documentar los contratos
    + Avance indivual de los tickets del Jira
    
    ### Anexo 
    + [Daily 1](https://drive.google.com/file/d/19qtssmcHWycgK6lszpV5F7K3t7cL8Gtl/view?usp=share_link)

### BackLog

![](https://i.imgur.com/Uc3xaPx.png)

![](https://i.imgur.com/yS0B6Ai.png)

## Metodología de ágil justificada del porqué de su selección con sus respectivas etapas.

La elección de la metodología de desarrollo adecuada es importante para garantizar el éxito de un proyecto de software. En el caso de nuestro grupo, hemos optado por la metodología ágil Scrum debido a sus múltiples ventajas.

Scrum es una metodología altamente flexible y adaptable, lo que es especialmente útil en proyectos como el nuestro, donde se espera que haya cambios y ajustes frecuentes. Scrum nos permitirá responder rápidamente a los cambios en los requisitos del proyecto y asegurarnos de que siempre estamos entregando el valor más alto posible.

Además, fomenta la comunicación continua y la colaboración efectiva entre los miembros del grupo. Para un desarrollo efectivo del trabajo, es crucial que todos los integrantes realicemos juntos el trabajo de manera efectiva y que podamos comunicarnos y colaborar activamente para lograr nuestros objetivos.

Esta metodología nos permitirá trabajar de manera incremental y entregable. Esto significa que podemos entregar valor al proyecto desde las primeras etapas y seguir entregando valor en pequeñas iteraciones. Esto garantiza que tengamos avances significativos por cada iteración.

La metodología Scrum es altamente visual y transparente. Esto significa que todo el equipo puede ver en qué se está trabajando, qué se ha completado y qué sigue pendiente. Esto fomenta la responsabilidad y el compromiso del equipo.Nos permitirá hacer un seguimiento y medir nuestro progreso de mejor manera. Esto significa que podemos realizar ajustes y mejoras en el proyecto según sea necesario para asegurarnos de que estamos cumpliendo nuestros objetivos en tiempo y forma.

El proceso de SCRUM se divide en varias etapas que se repiten en cada sprint o ciclo de trabajo. Estas etapas son:

**Planificación del Sprint:** al comienzo de cada sprint, el equipo de desarrollo se reúne con el Product Owner para definir el objetivo del sprint y el conjunto de historias de usuario que se abordarán durante ese sprint.

**Sprint Backlog:** una vez que se ha definido el objetivo del sprint y el conjunto de historias de usuario, el equipo de desarrollo crea un backlog de tareas específicas necesarias para completar cada historia de usuario.

**Sprint:** en esta fase, el equipo de desarrollo trabaja en las tareas del Sprint Backlog para completar las historias de usuario. El equipo realiza reuniones diarias cortas para revisar el progreso, discutir cualquier problema y actualizar el plan de trabajo.

**Revisión del Sprint:** al final del sprint, el equipo de desarrollo realiza una demostración de los elementos del producto completados durante ese sprint. El Product Owner y los stakeholders dan su feedback sobre el trabajo completado.

**Retrospectiva del Sprint:** después de la revisión del sprint, el equipo de desarrollo celebra una retrospectiva para analizar lo que funcionó bien y lo que no funcionó bien durante el sprint. Se identifican oportunidades de mejora y se implementan cambios para el siguiente sprint.

## Diagrama de arquitectura


![](https://i.imgur.com/DxqCZPK.png)