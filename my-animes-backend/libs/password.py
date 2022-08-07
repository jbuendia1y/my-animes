import bcrypt


def encrypt_password(password: str):
    salt = bcrypt.gensalt(rounds=10, prefix=b"my-animes")
    hash = bcrypt.hashpw(password, salt)
    return hash


def decrypt_password(password, hashed_password):
    isEqual = bcrypt.checkpw(password, hashed_password)
    return isEqual
