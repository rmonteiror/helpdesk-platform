from app.repositories.user_repository import (
    get_user_by_email,
    create_user
)

from app.core.security import (
    verify_password
)


def register_user(
    db,
    name,
    email,
    password_hash,
    role="user"
):
    existing_user = get_user_by_email(
        db,
        email
    )

    if existing_user:
        raise Exception(
            "Email already registered"
        )

    return create_user(
        db,
        name,
        email,
        password_hash,
        role
    )


def authenticate_user(
    db,
    email,
    password
):
    user = get_user_by_email(
        db,
        email
    )

    if not user:
        return None

    if not verify_password(
        password,
        user.password_hash
    ):
        return None

    return user