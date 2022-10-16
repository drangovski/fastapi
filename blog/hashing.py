from passlib.context import CryptContext

# Password Hashing Crypt Context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_pwd(password: str):
    return pwd_context.hash(password)


def verify(hashed_password, plain_password):
    return pwd_context.verify(plain_password, hashed_password)