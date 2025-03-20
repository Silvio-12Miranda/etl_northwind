CREATE TABLE D_Tiempo (
    Fecha_ID SERIAL PRIMARY KEY,
    Fecha DATE NOT NULL,
    Dia INT NOT NULL,
    Mes INT NOT NULL,
    Año INT NOT NULL
);

CREATE TABLE D_Clientes (
    Cliente_ID TEXT PRIMARY KEY,
    Nombre_Cliente TEXT NOT NULL,
    Pais TEXT NOT NULL,
    Ciudad TEXT NOT NULL
);

CREATE TABLE D_Productos (
    Producto_ID SERIAL PRIMARY KEY,
    Nombre_Producto TEXT NOT NULL,
    Categoria_ID INT NOT NULL REFERENCES D_Categorias(Categoria_ID)
);

CREATE TABLE D_Categorias (
    Categoria_ID SERIAL PRIMARY KEY,
    Nombre_Categoria TEXT NOT NULL
);

CREATE TABLE D_Empleados (
    Empleado_ID SERIAL PRIMARY KEY,
    Nombre_Empleado TEXT NOT NULL,
    Cargo TEXT NOT NULL
);

CREATE TABLE D_Regiones (
    Region_ID SERIAL PRIMARY KEY,
    Nombre_Region TEXT NOT NULL
);

CREATE TABLE Ventas (
    ID_Venta SERIAL PRIMARY KEY,
    Fecha_ID INT NOT NULL REFERENCES D_Tiempo(Fecha_ID),
    Cliente_ID TEXT NOT NULL REFERENCES D_Clientes(Cliente_ID),
    Producto_ID INT NOT NULL REFERENCES D_Productos(Producto_ID),
    Empleado_ID INT NOT NULL REFERENCES D_Empleados(Empleado_ID),
    Region_ID INT NOT NULL REFERENCES D_Regiones(Region_ID),
    Cantidad INT NOT NULL,
    Precio_Unitario NUMERIC NOT NULL,
    Total_Venta NUMERIC NOT NULL
);
