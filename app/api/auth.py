from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)

from sqlalchemy.orm import Session

from app.schemas.user import (
    UserCreate,
    UserLogin
)

from app.database.connection import get_db

from app.core.security import (
    hash_password,
    create_access_token
)

from app.services.auth_service import (
    register_user,
    authenticate_user
)

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.get("/test")
def test():
    return {
        "message": "Auth OK"
    }


@router.post("/register")
def register(
    user: UserCreate,
    db: Session = Depends(get_db)
):
    try:

        password_hash = hash_password(
            user.password
        )

        new_user = register_user(
            db=db,
            name=user.name,
            email=user.email,
            password_hash=password_hash,
            role=user.role
        )

        return {
            "id": new_user.id,
            "name": new_user.name,
            "email": new_user.email,
            "role": new_user.role
        }

    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


@router.post("/login")
def login(
    credentials: UserLogin,
    db: Session = Depends(get_db)
):
    user = authenticate_user(
        db,
        credentials.email,
        credentials.password
    )

    if not user:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    token = create_access_token(
        {
            "sub": user.email
        }
    )

    return {
        "access_token": token,
        "token_type": "bearer",
        "user": {
            "id": user.id,
            "name": user.name,
            "email": user.email,
            "role": user.role
        }
    }