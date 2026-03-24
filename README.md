# Lubix - Backend

Backend con base de datos para el proyecto Lubix, desarrollado por **Yeinher Algarin**.

## Descripción
Este proyecto sirve como backend para Lubix, implementando operaciones CRUD y conexión con base de datos PostgreSQL.  
Se implementa autenticación y gestión de datos utilizando FastAPI y SQLAlchemy.

version alpha V0.1

## Tecnologías y Herramientas

| Tecnología / Herramienta | Uso |
|--------------------------|-----|
| Python 3.14.3 | Lenguaje principal del backend |
| venv | Entorno virtual para Python |
| FastAPI | Framework para APIs (CRUD) |
| Uvicorn | Servidor ASGI para correr FastAPI |
| SQLAlchemy | ORM (Object Relational Mapping) para manejar la base de datos |
| PostgreSQL 18.3 | Base de datos relacional |
| psycopg2-binary | Driver para conexión con PostgreSQL |
| python-dotenv | Leer variables de entorno desde archivos `.env` |

## Estructura de Carpetas

```text
LUBIX-BACKEND/
│
├─ app/
│  ├─ main.py             # Entrada principal de la aplicación FastAPI
│  ├─ database/
|  |  └─ connection.py    # Configuracion de la base de datos
│  ├─ docs/
|  |  └─ ENDPOINTS.md     # documentacion de endpoints
|  ├─ models/
|  |  ├─__init__.py       # Iniciar modelos
|  |  ├─company.py        # Define la tabla empresa
|  |  └─ user.py          # Define la tabla usuario
│  ├─ routers/            # Carpeta con routers de endpoints
│  |   └─ user.py         # routers usuario
│  ├─ schemas/            # Estructura de entrada y salida de datos en la api
|  |  ├─company.py        
|  |  └─user.py           
|  └─ utils/
|     ├─ testDatabase.py  # Prueba de conexion de base de datos
|     └─ jwt.py           # JSON WEB TOKEN (generar tokens ) no implementado todavia...
├─ .env                   # Variables de entorno
├─ requirements.txt       # Dependencias del proyecto
├─ README.md              # Documentación del proyecto
└─ venv/                  # Entorno virtual de Python
```
## Instalacion de postgresql

## Instalación

Sigue estos pasos para configurar el proyecto en tu máquina local:

1. **Clonar el repositorio**  
   ```bash
        git clone https://github.com/RehnieyAl/lubix-backend.git
   ```
   
2. **instalar entorno virtual venv afuera de la carpeta app**
    ```bash
    python -m venv venv
    ```
2. **Activar entorno virutal - usar bash**
    ```bash
    linux/macs: source venv/bin/activate
    windows: source venv/Scripts/activate
    ``` 

3. **Instalar dependencias**
    ```bash
    pip install -r requirements.txt
    ```

4. **Crear archivo .env afuera de la carpeta app y añadir este codigo**
    ```bash
    URL_DATABASE = "postgresql://tu_usuario_en_posgresql:contraseña@localhost:tupuerto/tubasededatos"
    SECRET_KEY=super_clave_secreta
    ALGORITHM=HS256
    ACCESS_TOKEN_EXPIRE_MINUTES=30
    GMAIL_USERNAME = "tucorreo@gmail.com"
    GMAIL_APP_PASSWORD = "tu_clave_app_gmail"
    ```
5. **Iniciar servidor backend**
    ```bash
    uvicorn app.main:app --reload
    ```
## Backend hecho por RehnieyAl
