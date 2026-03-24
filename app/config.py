from dotenv import load_dotenv
import os
load_dotenv()

class config():
    URL_DATABASE = os.getenv("URL_DATABASE")
    SECRET_KEY = os.getenv("SECRET_KEY")
    ALGORITHM = os.getenv("ALGORITHM")
    ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))
    GMAIL_USERNAME = os.getenv("GMAIL_USERNAME")
    GMAIL_APP_PASSWORD = os.getenv("GMAIL_APP_PASSWORD")
config = config()