CREATE DATABASE sa_p; 
USE sa_p;

/*recursos humanos*/
CREATE TABLE departamento(
    iddepartamento INT NOT NULL AUTO_INCREMENT,
    departamento VARCHAR(50),
    PRIMARY KEY (iddepartamento)
);
CREATE TABLE empleado(
    id_empleado INT NOT NULL AUTO_INCREMENT,
    cui VARCHAR(25) not null COMMENT 'Número de Identificación del empleado',
    nombres VARCHAR(85) COMMENT 'Nombres del empleado',
	apellidos VARCHAR(85) COMMENT 'Apellidos del empleado',
	email VARCHAR(75) COMMENT 'Correo del empleado',
    telefono VARCHAR(20) COMMENT 'Teléfono del empleado',
    direccion VARCHAR(250) COMMENT 'Dirección del empleado',
    estado CHAR(1) default 'P' COMMENT 'P = pendiente, A = agendado cita, B = de baja/no aceptado, C = contrato',
    
    iddepartamento INT COMMENT 'FK departamento',
    
    PRIMARY KEY (id_empleado),
    UNIQUE u_cuiempleado (cui),
    
    FOREIGN KEY (iddepartamento)
    REFERENCES departamento(iddepartamento)
);


/*rutas*/
CREATE TABLE ruta(
    idruta INT NOT NULL AUTO_INCREMENT,
    nombre VARCHAR(50) COMMENT 'nombre como z1',
    direccion VARCHAR(250) COMMENT 'direccion guatemala zona1',
    PRIMARY KEY (idruta)
);

/*usuario*/
CREATE TABLE Usuario(
    iduser INT NOT NULL AUTO_INCREMENT,
    cui VARCHAR(25) not null COMMENT 'nombre del usuario del cliente',
    nombres VARCHAR(85) COMMENT 'primer nombre del usuario',
	apellidos VARCHAR(85) COMMENT 'primer apellido del usuario',
	contra VARCHAR(50) COMMENT 'contraseña del usuario del cliente',
	correo VARCHAR(75) COMMENT 'string correo del usuario',
	tipo CHAR(1) default 'U' COMMENT 'A = Administrativo, U = usuario, E = empresarial',
    estado CHAR(1) default 'P' COMMENT 'P = pendiente, A = activo, B = de baja',  
    
    idruta INT COMMENT 'FK ruta',
    id_empleado INT COMMENT 'FK empleado',
    
    FOREIGN KEY (idruta)
    REFERENCES ruta(idruta),
    
    FOREIGN KEY (id_empleado)
    REFERENCES empleado(id_empleado),
    
    PRIMARY KEY (iduser),
    UNIQUE u_cui (cui)
);

/*inventario*/
CREATE TABLE categoria(
    idcategoria INT NOT NULL AUTO_INCREMENT,
    categoria VARCHAR(50),
    PRIMARY KEY (idcategoria)
);

CREATE TABLE producto(
	sku INT NOT NULL AUTO_INCREMENT, /*idproducto*/
    
    nombre VARCHAR(75) COMMENT 'nombre del producto',
	precio DECIMAL(9,2) COMMENT 'precio del producto',
	costo DECIMAL(9,2) COMMENT 'Costo del producto',
	stock INT COMMENT 'stock del producto',
    idcategoria INT COMMENT 'FK Categoria que pertenece el producto',
    UNIQUE u_nombre (nombre),
    PRIMARY KEY (sku), /*sku*/
    FOREIGN KEY (idcategoria)
    REFERENCES categoria(idcategoria)
);

/*recursos humanos*/
CREATE TABLE agenda(
    idagenda INT NOT NULL AUTO_INCREMENT,
    fecha DATETIME COMMENT 'Fecha y hora en la que se realizará la entrevista',
    
    iduser INT COMMENT 'FK empleado de recursos humanos que realizará la entrevista',
    id_empleado INT COMMENT 'empleado de la entrevista',
    
    PRIMARY KEY (idagenda),
    
    FOREIGN KEY (iduser)
    REFERENCES Usuario(iduser),
    FOREIGN KEY (id_empleado)
    REFERENCES empleado(id_empleado)
);


/*venta*/
CREATE TABLE venta(
    idventa INT NOT NULL AUTO_INCREMENT,
    fecha DATETIME COMMENT 'fecha venta',
    tipoventa INT default 2 COMMENT 'Codigo de tipo de venta: 1. Empresarial , 2. Normal',
    estado CHAR(1) default 'P' COMMENT 'P = pedido, E = entregado',
    
    iduser INT COMMENT 'FK usuario',
    FOREIGN KEY (iduser)
    REFERENCES Usuario(iduser),

    PRIMARY KEY (idventa)
);

CREATE TABLE venta_productos(
    idventadet INT NOT NULL AUTO_INCREMENT,
    idventa INT COMMENT 'FK venta',
    sku INT COMMENT 'FK producto',
    cantidad INT,
    precio DECIMAL(9,2) COMMENT 'precio del producto',
    FOREIGN KEY (idventa)
    REFERENCES venta(idventa),
    FOREIGN KEY (sku)
    REFERENCES producto(sku),

    PRIMARY KEY (idventadet)
);

CREATE TABLE carrito(
    idcarrito INT NOT NULL AUTO_INCREMENT,
    iduser INT COMMENT 'FK usuario',
    
    sku INT COMMENT 'FK producto',
    cantidad INT,
    precio DECIMAL(9,2) COMMENT 'precio del producto',
    
    PRIMARY KEY (idcarrito),
    
    FOREIGN KEY (iduser)
    REFERENCES Usuario(iduser),
    FOREIGN KEY (sku)
    REFERENCES producto(sku)
);

/*rutas*/
CREATE TABLE ruta_entrega(
    idruta_entrega INT NOT NULL AUTO_INCREMENT,
    fecha DATETIME COMMENT 'fecha de entrega',
	idruta INT COMMENT 'FK ruta',
    idventa INT COMMENT 'FK venta que se va enviar ',
    FOREIGN KEY (idventa)
    REFERENCES venta(idventa),
    
    FOREIGN KEY (idruta)
    REFERENCES ruta(idruta),
    
    PRIMARY KEY (idruta_entrega)
);

/*compra*/
CREATE TABLE proveedor(
    idproveedor INT NOT NULL AUTO_INCREMENT,
    nit VARCHAR(25) not null COMMENT 'nit proveedor',
    nombre VARCHAR(85) COMMENT 'nombre proveedor',
    
    idruta INT COMMENT 'FK ruta',
    
    FOREIGN KEY (idruta)
    REFERENCES ruta(idruta),
    
    PRIMARY KEY (idproveedor),
    UNIQUE u_nit (nit)
);

CREATE TABLE compra(
    idcompra INT NOT NULL AUTO_INCREMENT,
    fecha DATETIME COMMENT 'fecha venta',
    compra INT default 2 COMMENT 'Codigo de tipo de compra: 1. Empresarial , 2. Normal',
    
    idproveedor INT COMMENT 'FK proveedor',
    FOREIGN KEY (idproveedor)
    REFERENCES proveedor(idproveedor),

    PRIMARY KEY (idcompra)
);

CREATE TABLE compra_productos(
    idcompradet INT NOT NULL AUTO_INCREMENT,
    idcompra INT COMMENT 'FK compra',
    sku INT COMMENT 'FK producto',
    cantidad INT,
    precio DECIMAL(9,2) COMMENT 'precio del producto',
    FOREIGN KEY (idcompra)
    REFERENCES compra(idcompra),
    FOREIGN KEY (sku)
    REFERENCES producto(sku),

    PRIMARY KEY (idcompradet)
);

/*Pagos*/
CREATE TABLE cartera(
    idcartera INT NOT NULL AUTO_INCREMENT,
    iduser INT COMMENT 'FK usuario',
    cuenta VARCHAR(10) COMMENT 'cuenta cartera',
    saldo DECIMAL(9,2) COMMENT 'saldo cartera',
    
    PRIMARY KEY (idcartera),
    
    FOREIGN KEY (iduser)
    REFERENCES Usuario(iduser)
);

CREATE TABLE tarjeta(
    idtarjeta INT NOT NULL AUTO_INCREMENT,
    iduser INT COMMENT 'FK usuario',
    cuenta VARCHAR(10) COMMENT 'cuenta tarjeta',
    saldo DECIMAL(9,2) COMMENT 'saldo tarjeta',
    
    PRIMARY KEY (idtarjeta),
    
    FOREIGN KEY (iduser)
    REFERENCES Usuario(iduser)
);

CREATE TABLE pagos(
    idpago INT NOT NULL AUTO_INCREMENT,
    iduser INT COMMENT 'FK usuario',
    idtarjeta INT COMMENT 'FK tarjeta',
    idcartera INT COMMENT 'FK usuario',
    idcompra INT COMMENT 'FK compra',
    monto DECIMAL(9,2) COMMENT 'monto a pagar',
    PRIMARY KEY (idpago),
    FOREIGN KEY (iduser)
    REFERENCES Usuario(iduser),
    FOREIGN KEY (idtarjeta)
    REFERENCES tarjeta(idtarjeta),
    FOREIGN KEY (idcartera)
    REFERENCES cartera(idcartera),
    FOREIGN KEY (idcompra)
    REFERENCES compra(idcompra)
);