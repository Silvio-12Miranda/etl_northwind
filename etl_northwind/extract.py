from sqlalchemy import create_engine
import polars as pl

def extract_data():
    """Extrae los datos desde la base SQLite."""
    try:
        print("[Paso 2] Extrayendo datos desde SQLite...")
        engine = create_engine("sqlite:///data/northwind.db")
        queries = {
            "orders": "SELECT OrderID, CustomerID, EmployeeID, OrderDate FROM Orders",
            "order_details": "SELECT OrderID, ProductID, UnitPrice, Quantity FROM [Order Details]",
            "customers": "SELECT CustomerID, CompanyName, Country, City FROM Customers",
            "products": "SELECT ProductID, ProductName, CategoryID FROM Products",
            "categories": "SELECT CategoryID, CategoryName FROM Categories",
            "employees": "SELECT EmployeeID, FirstName || ' ' || LastName AS Nombre_Empleado, Title AS Cargo FROM Employees"
        }
        dataframes = {name: pl.read_database(query, engine) for name, query in queries.items()}
        for name, df in dataframes.items():
            print(f"[Paso 2] Muestra de datos extraídos de {name}:\n{df.head(5)}")
        print("✅ [Paso 2] Datos extraídos correctamente.")
        return dataframes
    except Exception as e:
        print(f"Error en [Paso 2] Extracción de datos: {e}")
        return {}