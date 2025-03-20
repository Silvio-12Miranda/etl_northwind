import os
import psycopg2
from etl_northwind.config import DATABASE_CONFIG

def execute_sql_file():
    """Ejecuta `Northwind.sql` solo si las tablas no existen y las crea en mayúsculas."""
    try:
        print("📜 [Paso 1] Verificando y creando tablas en PostgreSQL si no existen...")
        base_dir = os.path.dirname(os.path.dirname(__file__))  
        sql_path = os.path.join(base_dir, "postgres-docker", "scripts", "Northwind.sql")

        if not os.path.exists(sql_path):
            print(f"No se encontró el archivo SQL en: {sql_path}")
            return

        conn = psycopg2.connect(
            dbname=DATABASE_CONFIG['dbname'],
            user=DATABASE_CONFIG['user'],
            password=DATABASE_CONFIG['password'],
            host=DATABASE_CONFIG['host'],
            port=DATABASE_CONFIG['port']
        )
        cur = conn.cursor()
        
        # Obtener las tablas existentes
        cur.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public';")
        existing_tables = {row[0].upper() for row in cur.fetchall()}  # Convertir nombres a mayúsculas
        
        with open(sql_path, "r") as file:
            sql_script = file.read()

        statements = sql_script.split(";")
        for statement in statements:
            if statement.strip():
                table_name = statement.split("(")[0].split()[-1].replace("\"", "").upper()
                if table_name not in existing_tables:
                    cur.execute(statement + ";")
                    print(f"✅ Tabla {table_name} creada.")
                else:
                    print(f"🔹 Tabla {table_name} ya existe, no se vuelve a crear.")

        conn.commit()
        cur.close()
        conn.close()
        print("[Paso 1] Tablas verificadas y creadas si no existían en PostgreSQL.")
    except Exception as e:
        print(f"Error en [Paso 1] Creación de tablas: {e}")

if __name__ == "__main__":
    execute_sql_file()