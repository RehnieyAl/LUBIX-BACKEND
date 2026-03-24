import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from app.config import config
GMAIL_USER = config.GMAIL_USERNAME
GMAIL_APP_PASSWORD = config.GMAIL_APP_PASSWORD

def test_smtp():
    destinatario = GMAIL_USER  # puedes enviarlo a ti mismo
    asunto = "Prueba SMTP"
    cuerpo = "¡Hola! Esto es una prueba de conexión SMTP desde FastAPI."

    # Crear mensaje
    mensaje = MIMEMultipart()
    mensaje['From'] = GMAIL_USER
    mensaje['To'] = destinatario
    mensaje['Subject'] = asunto
    mensaje.attach(MIMEText(cuerpo, 'plain'))

    try:
        servidor = smtplib.SMTP('smtp.gmail.com', 587)  # Gmail SMTP
        servidor.starttls()  # activa TLS
        servidor.login(GMAIL_USER, GMAIL_APP_PASSWORD)
        servidor.sendmail(GMAIL_USER, destinatario, mensaje.as_string())
        servidor.quit()
        print("✅ Conexión SMTP exitosa, correo enviado")
    except Exception as e:
        print("❌ Error en SMTP:", e)

if __name__ == "__main__":
    test_smtp()