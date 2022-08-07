from typing import List
from db.connection import connection
from models.User import User


def create_user_formatted(data: dict) -> User:
    return User(
        id=data["id"],
        name=data["name"],
        username=data["username"],
        password=data["password"]
    )


def get_user_by_username(username: str) -> User:
    cursor = connection().cursor()
    cursor.execute("SELECT * FROM users WHERE username = %s", username)
    data = cursor.fetchone()

    return create_user_formatted(data)


def get_users() -> List[User]:
    cursor = connection().cursor()
    cursor.execute("SELECT * FROM users")
    data = [create_user_formatted(user) for user in cursor.fetchall()]

    return data


def get_user_by_id(user_id: str) -> User:
    cursor = connection().cursor()
    cursor.execute("SELECT * FROM users WHERE user_id = %s", user_id)
    data = cursor.fetchone()

    return create_user_formatted(data)
