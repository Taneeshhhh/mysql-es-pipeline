from dotenv import load_dotenv
import os
load_dotenv()
MYSQL_CONFIG = {
    "host": os.getenv("MYSQL_HOST"),
    "user": os.getenv("MYSQL_USER"),
    "password": os.getenv("MYSQL_PASSWORD"),
    "database": os.getenv("MYSQL_DATABASE")
}

ES_CONFIG = {
    "url": os.getenv("ES_URL"),
    "username": os.getenv("ES_USERNAME"),
    "password": os.getenv("ES_PASSWORD")
}