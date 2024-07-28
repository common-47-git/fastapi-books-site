from dotenv import load_dotenv
from os import getenv

load_dotenv()

# Auth config
SECRET_KEY = str(getenv("SECRET_KEY"))
ALGORITHM = str(getenv("ALGORITHM"))
ACCESS_TOKEN_EXPIRE_MINUTES = int(getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))

# Database config
LOGIN_USER = "books_site_login"
PASSWORD = str(getenv("PASSWORD"))
SERVERNAME = str(getenv("SERVERNAME"))
DBNAME = str(getenv("DBNAME"))
DRIVER = str(getenv("DRIVER"))