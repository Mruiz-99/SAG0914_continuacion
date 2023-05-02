# [SA] PROYECTO FASE 2

**Software Avanzado, sección N**
**GRUPO 9**

| Carnet    | Nombre                     | Porcentaje de trabajo |
|-----------|----------------------------|-----------------------|
| 201531166 | Maynor Octavio Piló Tuy    | 100%                  |
| 201801329 | Mynor Rene Ruiz Guerra     | 100%                  |
| 201806838 | Elian Saúl Estrada Urbina  | 100%                  |
| 20180098  | Alex Fernando Méndez López | 100%                  |

## Documentación de las fases anteriores.

| Documentación                      |
|------------------------------------|
| [Fase 1](../docs/fase 1/README.md) |
|                                    |

## Bitácora de la metodología

### Sprint Planning

| No. | Documento                                             | Fecha      |
|-----|-------------------------------------------------------|------------|
| 1.  | [Sprint Planning 2](./SprintPlanning2.md) | 04/03/2023 |
| 2.  | [Sprint Planning 3](./SprintPlanning3.md) | 11/03/2023 |
| 3.  | [Sprint Planning 4](./SprintPlanning4.md) | 18/03/2023 |

### Daily

| No. | Documento                            | Fecha      |
|-----|--------------------------------------|------------|
| 1.  | [Daily 1](./Daily1.md)   | 06/03/2023 |
| 2.  | [Daily 2](./Daily2.md)   | 07/03/2023 |
| 3.  | [Daily 3](./Daily3.md)   | 08/03/2023 |
| 4.  | [Daily 4](./Daily4.md)   | 09/03/2023 |
| 5.  | [Daily 5](./Daily5.md)   | 10/03/2023 |
| 6.  | [Daily 6](./Daily6.md)   | 11/03/2023 |
| 7.  | [Daily 7](./Daily7.md)   | 13/03/2023 |
| 8.  | [Daily 8](./Daily8.md)   | 14/03/2023 |
| 9.  | [Daily 9](./Daily9.md)   | 15/03/2023 |
| 10. | [Daily 10](./Daily10.md) | 16/03/2023 |
| 11. | [Daily 11](./Daily11.md) | 17/03/2023 |
| 12. | [Daily 12](./Daily12.md) | 18/03/2023 |
| 13. | [Daily 13](./Daily13.md) | 20/03/2023 |
| 14. | [Daily 14](./Daily14.md) | 21/03/2023 |
| 15. | [Daily 15](./Daily15.md) | 22/03/2023 |

### Documentación Sprint

| No. | Documento                            | Fecha      |
|-----|--------------------------------------|------------|
| 1.  | [Sprint 1](./Sprint1.md) | 04/03/2023 |
| 2.  | [Sprint 2](./Sprint2.md) | 11/03/2023 |
| 3.  | [Sprint 3](./Sprint3.md) | 18/03/2023 |

## ¿Cómo ejecutar los contenedores?

### 1. Instalar docker y docker-compose
**Mac OSX**

[Instalar Docker para Mac](https://docs.docker.com/desktop/install/mac-install/), que incluye el motor de Docker y una versión reciente de docker-compose fuera de la caja.


**Linux**

[Instale Docker en Linux ](https://docs.docker.com/engine/install/)siguiendo las instrucciones para cualquier distro de Linux que le convenga. Porque docker-compose no está instalado como parte de la instalación base de Docker en Linux, una vez que tenga un motor en funcionamiento, siga las [instrucciones de instalación de docker-compose](https://docs.docker.com/compose/install/) para Linux.

**Windows**

[Instalar Docker para Windows](https://docs.docker.com/desktop/install/windows-install/), que incluye el motor de Docker y una versión reciente de docker-compose fuera de la caja.
Desafortunadamente Docker no es compatible en todas las versiones de Windows. 
+ Una opción para los usuarios de Windows es instalar una Ubuntu Desktop VM a través de VirtualBox o cualquier Hipervisor compatible con su version de windows y proceda con el Docker en instrucciones de Linux en el interior de ese VM. 
+ Docker Desktop recientemente ha agregado [soporte para Windows Subsystem para Linux ( WSL ) 2](https://docs.docker.com/desktop/install/windows-install/), que puede ser otra opción.


### 2. Clonar repositorio del proyecto

Clonar el repositorio del proyecto usando la terminal y ejecutando el siguiente commando:
```shell
git clone https://gitlab.com/LexFer010/g9-sa-proyecto.git
```
Una vez que ese comando se complete correctamente, debería ver una carpeta nueva `g9-sa-proyect` en su directorio actual.

### 3. Iniciar el proyecto a través de docker compose

Navegue a la carpeta que se creó anteriormente:
```shell
cd g9-sa-proyecto
```

Configure el archivo .env con la siguiente información:
```dotenv
# CLOUDINARY CONFIG BUCKET
CLOUDINARY_CLOUD_NAME=
CLOUDINARY_API_KEY=
CLOUDINARY_API_SECRET=

# EMAIL CONFIG
EMAIL_USER=
EMAIL_PASS=
EMAIL_FROM=

# FLASK CONFIG
FLASK_DEBUG=
FLASK_SECRET_KEY=

#JWT
JWT_KEY=
JWT_KEY_SHARE=

# POSTGRESSQL CONFIG
PG_DATABASE=
PG_HOST=
PG_PASS=
PG_PORT=
PG_USER=

# REDIS CONFIG
REDIS_HOST=
REDIS_PASS=
REDIS_PORT=
REDIS_USER=

# URLs API
URL_NOTIFICATION=
URL_UPLOAD=
```

Ejecutar los siguientes comandos de docker-compose
```shell
docker-compose -f docker-compose.yml up --build
```
Debería ver un log de salida de registro de los contenedores que se lanzan en su máquina. Una vez ¡esta salida se ralentiza, debe tener una instancia en ejecución de este proyecto en su máquina local!

### 4. Iniciar a usar el proyecto
Usando una terminal y un cliente de PostgresSQL ejecuto el siguiente comando para crear la base de datos:
```shell
psql -d <PG_DATABASE> -h <PG_HOST> -U <PG_USER> -W -f ./db/g9_db.sql
```
Ahora a través de su navegador web visitando [http://localhost:80](http://localhost:80).Tenga en cuenta que muchos navegadores ahora están predeterminados para https - si el tuyo es uno de ellos, asegúrate de que lo use http.

## Base de datos
### Diagrama entidad relación 
![Modelo entidad relación](https://gitlab.com/LexFer010/g9-sa-proyecto/-/raw/develop/docs/fase%202/Modelo%20relacional.png)


### Script
```script
CREATE TABLE Pago_planilla (
  id_pago_planilla SERIAL PRIMARY KEY,
  total FLOAT NOT NULL,
  fecha DATE NOT NULL
);

CREATE TABLE Ruta (
  id_ruta SERIAL PRIMARY KEY,
  fecha DATE NOT NULL
);

CREATE TABLE Categoria (
  id_categoria SERIAL PRIMARY KEY,
  nombre VARCHAR(30) NOT NULL 
);

CREATE TABLE Departamento (
  id_departamento SERIAL PRIMARY KEY,
  nombre VARCHAR(45) NOT NULL
);

CREATE TABLE Usuario (
  id_usuario SERIAL PRIMARY KEY,
  nombres VARCHAR(45) NOT NULL,
  apellidos VARCHAR(45) NOT NULL,
  correo VARCHAR(70) NOT NULL,
  contrasena VARCHAR(30) NOT NULL,
  fecha_nacimiento DATE NOT NULL,
  estado INTEGER NOT NULL
);


CREATE TABLE Compra_interna (
  id_compra_interna SERIAL PRIMARY KEY,
  fecha_venta DATE NOT NULL,
  total FLOAT NOT NULL
);

CREATE TABLE Detalle_compra_interna (
  id_detalle_compra_interna SERIAL PRIMARY KEY,
  sku INTEGER NOT NULL,
  precio FLOAT NOT NULL,
  cantidad INTEGER NOT NULL,
  id_compra_interna INTEGER NOT NULL REFERENCES Compra_interna(id_compra_interna)
);

CREATE TABLE Personal_administrativo (
  id_personal_administrativo SERIAL PRIMARY KEY,
  fecha_contratacion DATE NOT NULL,
  sueldo FLOAT NOT NULL,
  id_usuario INTEGER NOT NULL REFERENCES Usuario(id_usuario),
  id_departamento INTEGER NOT NULL REFERENCES Departamento (id_departamento)
);

CREATE TABLE Cliente (
  id_cliente SERIAL PRIMARY KEY,
  nit VARCHAR (30) NOT NULL,
  id_usuario INTEGER NOT NULL REFERENCES Usuario(id_usuario)
);

CREATE TABLE Compra_externa (
  id_compra_externa SERIAL PRIMARY KEY,
  fecha_compra DATE NOT NULL,
  total FLOAT NOT NULL,
  estado INTEGER NOT NULL,
  id_cliente INTEGER NOT NULL REFERENCES Cliente(id_cliente), 
  id_ruta INTEGER NOT NULL REFERENCES Ruta(id_ruta)
);

CREATE TABLE Direccion (
  id_direccion SERIAL PRIMARY KEY,
  departamento VARCHAR(30) NOT NULL,
  municipio VARCHAR(30) NOT NULL,
  zona VARCHAR(30) NOT NULL,
  id_ruta INTEGER NOT NULL REFERENCES Ruta(id_ruta)
);

CREATE TABLE Pago (
  id_pago SERIAL PRIMARY KEY,
  saldo FLOAT NOT NULL,
  id_cliente INTEGER NOT NULL REFERENCES Cliente(id_cliente)
);

CREATE TABLE Tarjeta (
  id_tarjeta SERIAL PRIMARY KEY,
  numero INTEGER NOT NULL,
  fecha_vencimiento DATE NOT NULL,
  estado INTEGER NOT NULL,
  tipo VARCHAR(20) NOT NULL,
  cvv INTEGER NOT NULL,
  id_pago INTEGER NOT NULL REFERENCES Pago(id_pago)
);

CREATE TABLE Carrito_compra (
  id_carrito_compra SERIAL PRIMARY KEY,
  id_compra_externa INTEGER NOT NULL REFERENCES Compra_externa(id_compra_externa) 
);

CREATE TABLE Producto (
  id_producto SERIAL PRIMARY KEY,
  nombre VARCHAR (30) NOT NULL,
  descripcion VARCHAR (150) NOT NULL,
  precio_costo FLOAT NOT NULL,
  unidades_disponibles INTEGER NOT NULL,
  precio_unitario FLOAT NOT NULL,
  id_categoria INTEGER NOT NULL REFERENCES Categoria(id_categoria)
);


CREATE TABLE detalle_carrito (
  id_detalle_carrito SERIAL PRIMARY KEY,
  cantidad INTEGER NOT NULL,
  id_carrito_compra INTEGER NOT NULL REFERENCES Carrito_compra(id_carrito_compra),  
  id_producto INTEGER NOT NULL REFERENCES Producto(id_producto)
);


CREATE TABLE Entrevista (
  id_entrevista SERIAL PRIMARY KEY,
  fecha_hora_cita DATE NOT NULL,
  nombres_candidato VARCHAR(45) NOT NULL,
  apellidos_cantidato VARCHAR(45) NOT NULL,
  id_personal_administrativo INTEGER NOT NULL REFERENCES Personal_administrativo(id_personal_administrativo)
);
```

## Contratos

<div align="left">
    <table>
        <tbody>
            <tr>
                <td>
                    <p>ID:&nbsp;01</p>
                </td>
                <td>
                    <p>Nombre:&nbsp;Reordenar Inventario</p>
                </td>
            </tr>
            <tr>
                <td>
                    <p>Prioridad:&nbsp;Media</p>
                </td>
                <td rowspan="3">
                    <p>Historia de usuario</p>
                    <p>Se desea enviar notificaci&oacute;n para solicitar abastecimiento de stock de alg&uacute;n producto cuanto este si quede sin stock.&nbsp;</p>
                </td>
            </tr>
            <tr>
                <td>
                    <p>Estimado:&nbsp;&nbsp;5 puntos</p>
                </td>
            </tr>
            <tr>
                <td>
                    <p>M&oacute;dulo:&nbsp;Inventario</p>
                </td>
            </tr>
            <tr>
                <td colspan="2" rowspan="5">
                    <p>Criterios de Aceptaci&oacute;n</p><br>
                    <p>Se generar&aacute; una notificaci&oacute;n con solicitud de abastecimiento de stock de alg&uacute;n producto al enviar la notificaci&oacute;n retornar&aacute; un c&oacute;digo 200 y un mensaje satisfactorio, en caso de alg&uacute;n error retornar&aacute; un c&oacute;digo de error y m&aacute;s informaci&oacute;n del mismo.</p><br>
                    <p>El microservicio debe tener la siguiente configuraci&oacute;n:</p><br>
                    <p>Ruta:&nbsp;/inventario/solicitarStock/&lt;idProducto&gt;</p>
                    <p>M&eacute;todo:&nbsp;GET</p>
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
                                        <p>404</p>
                                    </td>
                                    <td>
                                        <p>Producto no existe</p>
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
                    <p>Ejemplos de par&aacute;metros de entrada:</p>
                    <p>/inventario/solicitarStock/150</p><br>
                    <p>Ejemplos de par&aacute;metros de salida exitosa:</p>
                    <p>{</p>
                    <p>&nbsp; &nbsp; &ldquo;estatus&rdquo;: 200,</p>
                    <p>&nbsp; &nbsp; &ldquo;mensaje&rdquo;: &ldquo;Se envi&oacute; la notificaci&oacute;n&rdquo;</p>
                    <p>}</p>
                    <p>Ejemplo de par&aacute;metros de salida fallida:</p>
                    <p>{</p>
                    <p>&nbsp; &nbsp; &ldquo;estatus&rdquo;: 400</p>
                    <p>&nbsp; &nbsp; &ldquo;error&rdquo;:&rdquo;Par&aacute;metro requerido&rdquo;,</p>
                    <p>&nbsp; &nbsp; &ldquo;mensaje&rdquo;:&rdquo;Falt&oacute; alg&uacute;n par&aacute;metro&rdquo;</p>
                    <p>}</p><br>
                    <p>{</p>
                    <p>&nbsp; &nbsp; &ldquo;estatus&rdquo;: 404</p>
                    <p>&nbsp; &nbsp; &ldquo;error&rdquo;:&rdquo;No se encontr&oacute; el producto&rdquo;,</p>
                    <p>&nbsp; &nbsp; &ldquo;mensaje&rdquo;:&rdquo;El producto no se encontr&oacute; o el c&oacute;digo del producto es incorrecto&rdquo;</p>
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
