# Lubix - Backend

Backend con base de datos para el proyecto Lubix, desarrollado por **Yeinher Algarin**.

## Descripción
Este proyecto sirve como backend para Lubix, implementando operaciones CRUD y conexión con base de datos PostgreSQL.  
Se implementa autenticación y gestión de datos utilizando FastAPI, SQLAlchemy, STMP con gmail.

Initial version V1.0

## Tecnologías y Herramientas

| Tecnología / Herramienta | Uso |
|--------------------------|-----|
| Python 3.14.3 | Lenguaje principal del backend |
| venv | Entorno virtual para Python |
| FastAPI | Framework para APIs (CRUD) |
| Uvicorn | Servidor ASGI para correr FastAPI |
| SQLAlchemy | ORM (Object Relational Mapping) para manejar la base de datos |
| PostgreSQL 18.3 | Base de datos relacional |
| psycopg2-binary | Driver para conexión con PostgreSQL hacia al backend |
| Pydantic | Validación de datos y esquemas |
| python-jose | Manejo de autenticación y creacion de tokens JWT |
| bcrypt | Encriptacion de contraseña |
| SMTP (smtplib) | Envío de correos electrónicos (verificación, recuperación de contraseña) |
| python-dotenv | Leer variables de entorno desde archivos `.env` |

## Estructura de Carpetas

```text
LUBIX-BACKEND/
│
├─ app/
│  ├─ main.py             # Entrada principal de la aplicación FastAPI
│  ├─ database/           # conexion de base de datos hacia postgre SQL
|  |
│  ├─ docs/               # Documentacion
|  |
|  ├─ models/             # Modelos de tablas para la base de datos ORM
|  |
│  ├─ routers/            # Carpeta con routers de endpoints
│  |   
│  ├─ schemas/            # Estructura de entrada y salida de datos en la api  
|  |
|  ├─ schemas/            # Logica de negocio
|  |        
|  └─ utils/              # Utilidades como STMP, generador de codigos
|
├─ config,py              # Configuraciones predefinidas importada desde .env
|
├─ main.py                # Punto de entrada y ejecucion principal del backend
├─ .env                   # Variables de entorno
├─ requirements.txt       # Dependencias del proyecto
├─ README.md              # Documentación del proyecto
└─ venv/                  # Entorno virtual de Python
```

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
3. **Activar entorno virutal - usar bash**
    ```bash
    linux/macs: source venv/bin/activate
    windows: source venv/Scripts/activate
    ``` 

4. **Instalar dependencias**
    ```bash
    pip install -r requirements.txt
    ```

5. **Crear archivo .env afuera de la carpeta app y añadir este codigo**
    ```bash
    URL_DATABASE = "postgresql://tu_usuario_en_posgresql:contraseña@localhost:tupuerto/tubasededatos"
    SECRET_KEY=super_clave_secreta
    ALGORITHM=HS256
    ACCESS_TOKEN_EXPIRE_MINUTES=30
    GMAIL_USERNAME = "tucorreo@gmail.com"
    GMAIL_APP_PASSWORD = "tu_clave_app_gmail"
    URL_FRONTEND = "tu_urlfrotend"
    ```
6. **Iniciar servidor backend afuera de la carpeta app**
    ```bash
    uvicorn app.main:app --reload
    ```
## Backend hecho por RehnieyAl
