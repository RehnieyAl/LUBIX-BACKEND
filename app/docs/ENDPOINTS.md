http://127.0.0.1:8000/


para probar conexion de base de datos desde el backend:
POSTDATA: debe tener previamente postgre sql con usuario, contraseña y base de datos
GET /health/test

-- Usuario
--  registrar usuario
POST user/register
{
  "fullName": "",
  "email": "",
  "tell": "",
  "hashed_password": ""
}
-- login 
POST user/login
{
  "email": "",
  "password": ""
}

-- forgot password
POST user/forgot-password
{
  "email": ""
}

-- reset password
POST user/reset-password
{
  "email": "",
  "code": "",
  "new_password":""
}
