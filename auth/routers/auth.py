from fastapi import APIRouter, HTTPException, Response, Request
from models.user import RegisterUserRequest, LoginUserRequest, User
from passlib.context import CryptContext
from models.connect import DB_DEPENDENCY
from starlette import status
from utils.auth import authenticate_user, create_access_token, get_current_user
from config import settings
from datetime import timedelta

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

ACCESS_TOKEN_COOKIE_KEY = "access_token"


@router.post("/register", status_code=status.HTTP_201_CREATED)
def register_user(response: Response, user: RegisterUserRequest, db: DB_DEPENDENCY):
    hashed_password = bcrypt_context.hash(user.password)

    # check if email exists
    email_exists = db.query(User).filter(User.email == user.email).first()

    if email_exists is not None:
        raise HTTPException(status.HTTP_400_BAD_REQUEST,
                            "Email already exists")

    new_user = User(
        name=user.name,
        email=user.email,
        password=hashed_password
    )

    db.add(new_user)
    db.commit()

    token = create_access_token(new_user.email, new_user.id, timedelta(
        weeks=settings.JWT_EXPIRY_DURATION_IN_WEEKS))

    response.set_cookie(key=ACCESS_TOKEN_COOKIE_KEY,
                        value=f"Bearer {token}", httponly=True, expires=60*60*24*28)

    return {
        "id": new_user.id,
        "name": new_user.name,
        "email": new_user.email,
    }


@router.post("/login", status_code=status.HTTP_200_OK)
def login_user(response: Response, user: LoginUserRequest, db: DB_DEPENDENCY):
    authed_user = authenticate_user(user.email, user.password, db)

    if not authed_user:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED,
                            "Invalid email or password")

    token = create_access_token(authed_user.email, authed_user.id, timedelta(
        weeks=settings.JWT_EXPIRY_DURATION_IN_WEEKS))

    response.set_cookie(key=ACCESS_TOKEN_COOKIE_KEY,
                        value=f"Bearer {token}", httponly=True, expires=60*60*24*28)

    return {
        "access_token": token,
        "token_type": "Bearer"
    }


@router.get("/logout", status_code=status.HTTP_204_NO_CONTENT)
def logout_user(response: Response):
    response.delete_cookie(ACCESS_TOKEN_COOKIE_KEY)


@router.get("/current-user", status_code=status.HTTP_200_OK)
def current_user(request: Request, db: DB_DEPENDENCY):
    token = request.cookies.get(ACCESS_TOKEN_COOKIE_KEY)

    if token is None:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED,
                            "Unauthorized access")

    user = get_current_user(token.split(' ')[1])

    if user is None:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED,
                            "Unauthorized access")

    fetch_user = db.query(User).filter(User.id == user.get("id")).first()

    if fetch_user is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Not found")

    return {
        "id": fetch_user.id,
        "name": fetch_user.name,
        "email": fetch_user.email,
        "is_confirmed": fetch_user.is_confirmed,
        "created_at": fetch_user.created_at
    }
