from config import settings
from fastapi import HTTPException
from jose import jwt, JWTError


def get_current_user(token: str):
    try:
        payload = jwt.decode(token, settings.JWT_SECRET,
                             algorithms=[settings.JWT_ALGORITHM])
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
