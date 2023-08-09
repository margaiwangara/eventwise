from config import settings
from fastapi import HTTPException, Request
from jose import jwt, JWTError
from config import settings
from starlette import status


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


def require_auth(request: Request):
    token = request.cookies.get(settings.ACCESS_TOKEN_COOKIE_KEY)

    if token is None:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED,
                            "Unauthorized access")

    user = get_current_user(token.split(' ')[1])

    if user is None:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED,
                            "Unauthorized access")
    return user
