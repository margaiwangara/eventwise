from models.connect import DB_DEPENDENCY
from models.user import User
from passlib.context import CryptContext
from jose import jwt, JWTError
from datetime import timedelta, datetime
from config import settings
from fastapi import HTTPException, Depends
from typing import Annotated

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
JWT_ALGORITHM = "HS256"


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

    return jwt.encode(encode, key=settings.JWT_SECRET, algorithm=JWT_ALGORITHM)


def get_current_user(token: str):
    try:
        payload = jwt.decode(token, settings.JWT_SECRET,
                             algorithms=[JWT_ALGORITHM])
        email: str = payload.get("sub")
        user_id: int = payload.get("id")

        if email is None or user_id is None:
            raise HTTPException(401, "Unauthorized access")

        return {
            "email": email,
            "id": user_id
        }
    except JWTError as e:
        print(e)
        raise HTTPException(401, "Unauthorized access")


USER_DEPENDENCY = Annotated[dict, Depends(get_current_user)]
