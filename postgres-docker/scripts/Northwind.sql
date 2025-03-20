CREATE TABLE d_tiempo (
    fecha_id SERIAL PRIMARY KEY,
    fecha DATE NOT NULL,
    dia INT NOT NULL,
    mes INT NOT NULL,
    año INT NOT NULL
);
-- Tabla de Dimensión Categorías
CREATE TABLE d_categorias (
    categoria_id SERIAL PRIMARY KEY,
    nombre_categoria TEXT NOT NULL
);

-- Tabla de Dimensión Productos
CREATE TABLE d_productos (
    producto_id SERIAL PRIMARY KEY,
    nombre_producto TEXT NOT NULL,
    categoria_id INT NOT NULL REFERENCES d_categorias(categoria_id) ON DELETE CASCADE
);

-- Tabla de Dimensión Clientes
CREATE TABLE d_clientes (
    cliente_id TEXT PRIMARY KEY,
    nombre_cliente TEXT NOT NULL,
    pais TEXT NOT NULL,
    ciudad TEXT NOT NULL
);

-- Tabla de Dimensión Empleados
CREATE TABLE d_empleados (
    empleado_id SERIAL PRIMARY KEY,
    nombre_empleado TEXT NOT NULL,
    cargo TEXT NOT NULL
);

-- Tabla de Dimensión Regiones
CREATE TABLE d_regiones (
    region_id SERIAL PRIMARY KEY,
    nombre_region TEXT NOT NULL
);

-- Tabla de Hechos Ventas
CREATE TABLE ventas (
    id_venta SERIAL PRIMARY KEY,
    fecha_id INT NOT NULL REFERENCES d_tiempo(fecha_id) ON DELETE CASCADE,
    cliente_id TEXT NOT NULL REFERENCES d_clientes(cliente_id) ON DELETE CASCADE,
    producto_id INT NOT NULL REFERENCES d_productos(producto_id) ON DELETE CASCADE,
    empleado_id INT NOT NULL REFERENCES d_empleados(empleado_id) ON DELETE CASCADE,
    region_id INT NOT NULL REFERENCES d_regiones(region_id) ON DELETE CASCADE,
    cantidad INT NOT NULL CHECK (cantidad > 0),
    precio_unitario NUMERIC NOT NULL CHECK (precio_unitario >= 0),
    total_venta NUMERIC NOT NULL CHECK (total_venta >= 0)
);