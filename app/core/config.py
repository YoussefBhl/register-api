from databases import Database
from dotenv import dotenv_values
import os

config = dotenv_values(".env")

def get_env() -> str:
    from_os = os.getenv("ENV")
    if from_os:
        return from_os
    return config["ENV"]

MYSQL_DATABASE_URL = config["MYSQL_DATABASE_URL"]
ENV = get_env()

if ENV == 'TEST':
    database = Database(MYSQL_DATABASE_URL, force_rollback=True)
else:
    database = Database(MYSQL_DATABASE_URL)
