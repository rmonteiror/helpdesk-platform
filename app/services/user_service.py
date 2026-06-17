from app.repositories.user_repository import create_user


def register_user(
    db,
    user_data
):
    return create_user(
        db=db,
        name=user_data.name,
        email=user_data.email,
        password_hash=user_data.password
    )