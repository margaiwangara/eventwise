from fastapi import APIRouter, HTTPException
from models.user import RegisterUserRequest, LoginUserRequest, User
from passlib.context import CryptContext
from models.connect import DB_DEPENDENCY
from starlette import status

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


@router.post("/register", status_code=status.HTTP_201_CREATED)
def register_user(user: RegisterUserRequest, db: DB_DEPENDENCY):
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

    return new_user


@router.get("/current-user")
def current_user():
    return {"message": "Current User"}
