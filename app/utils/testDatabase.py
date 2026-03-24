from sqlalchemy import text
from app.database.connection import engine

## Testeo de conexion de base de datos al backend
def db_test():
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))
            return {"Estado":"OK"}
    except Exception as e:
        return {"Estado": "ERROR", "detail": str(e)}