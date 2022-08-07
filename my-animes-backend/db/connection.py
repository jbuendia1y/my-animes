import os
import pymysql

config = {
    "host": os.environ.get("localhost", "localhost"),
    "user": os.environ.get("user", "root"),
    "password": os.environ.get("password", "joaquin$1"),
    "port": int(os.environ.get("port", "3306")),
    "database": "my_animes"
}


def connection_generator():
    connection = pymysql.connect(**config)
    yield connection
    connection.close()


def connection():
    connection = next(connection_generator())
    return connection
