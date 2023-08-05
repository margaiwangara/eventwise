from models.connect import DB_DEPENDENCY
from models.user import User
from passlib.context import CryptContext
from jose import jwt, JWTError
from datetime import timedelta, datetime
from config import settings

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def authenticate_user(email: str, password: str, db: DB_DEPENDENCY):
    user = db.query(User).filter(User.email == email).first()

    if not user:
        return False
    if not bcrypt_context.verify(password, user.password):
        return False
    return user


def create_access_token(email: str, user_id: int, expires_delta: timedelta):
    encode = {"sub": email, "id": user_id}
    expires = datetime.utcnow() + expires_delta
    encode.update({"exp": expires})

    return jwt.encode(encode, key=settings.JWT_SECRET, algorithm="HS256")
