# ETL Northwind - Prueba Técnica

Este repositorio contiene la solución de la prueba técnica para la implementación de un proceso ETL utilizando **Python, Polars y PostgreSQL**.

## Requisitos

Antes de ejecutar el proyecto, asegúrate de tener instalados los siguientes requisitos:

### Tecnologías utilizadas
- **Docker**
- **Python 3.8+**
- **PostgreSQL**
- **SQLAlchemy**
- **Polars**
- **Psycopg2**

### Instalación de dependencias
Ejecuta el siguiente comando para instalar todas las dependencias:

```bash
pip install -r requirements.txt
```
### SOLUCIONES:

1. Modelado de Data Warehouse

El modelo de datos utilizado en esta prueba técnica sigue un esquema en estrella. Este diseño es ampliamente utilizado en Data Warehouses debido a su eficiencia en consultas analíticas y de agregación.

### Tablas del modelo

Tabla de Hechos:
- **VENTAS (Ventas registradas con métricas de cantidad y precio total).**

Tablas de Dimensiones:
- **D_TIEMPO (Dimensión de tiempo con granularidad de fecha, mes y año).**
- **D_CLIENTES (Información de clientes).**
- **D_PRODUCTOS (Información de productos y sus categorías).**
- **D_CATEGORIAS (Categorías de productos).**
- **D_EMPLEADOS (Vendedores y empleados involucrados en ventas).**
- **D_REGIONES (Regiones donde ocurren las ventas).**

Ahora bien la justificacion por el cual se utilizo este tipo de esquema de estrella es el siguiente:
- Tiene un mejor rendimiento en consultas.
- Permite una rápida agregación y análisis de datos en herramientas de BI.
- El que este desnormalizada evita cruces costosos en memoria.

![Modelo Estrella](https://raw.githubusercontent.com/silviomiranda/etl_northwind/main/images/modelo_estrella.png)













## Configuración

1. **Configurar la base de datos**
   
   Crea una base de datos en PostgreSQL:
   ```sql
   CREATE DATABASE northwind;
   ```

2. **Configurar las credenciales de la base de datos**
   
   Modifica el archivo `etl_northwind/config.py` con las credenciales correctas:
   ```python
   DATABASE_CONFIG = {
       'dbname': 'northwind',
       'user': 'tu_usuario',
       'password': 'tu_contraseña',
       'host': 'localhost',
       'port': '5432'
   }
   ```

3. **Verificar la existencia del script SQL**
   
   Asegúrate de que el archivo `Northwind.sql` se encuentra en:
   ```
   postgres-docker/scripts/Northwind.sql
   ```

   Este archivo contiene la estructura de las tablas y se ejecutará automáticamente al iniciar el ETL.

## 🏗️ Estructura del Proyecto

```
📂 etl_northwind
 ├── config.py             # Configuración de la base de datos
 ├── execute_sql.py        # Creación de tablas en PostgreSQL
 ├── extract.py            # Extracción de datos desde SQLite
 ├── transform.py          # Transformación de datos usando Polars
 ├── load_data.py          # Carga de datos en PostgreSQL
 ├── main.py               # Ejecución del proceso ETL
 ├── requirements.txt      # Dependencias del proyecto
```

## Ejecución del ETL

Para ejecutar el proceso ETL, usa el siguiente comando:

```bash
python -m etl_northwind.main
```

El proceso se ejecutará en los siguientes pasos:

1️**[Paso 1] Creación de tablas**: Se verifican y crean las tablas si no existen.

2️**[Paso 2] Extracción de datos**: Se extraen datos desde la base de datos.

3️**[Paso 3] Transformación de datos**: Se transforman los datos evitando duplicados.

4️**[Paso 4] Carga de datos**: Se insertan solo los datos nuevos en PostgreSQL.
