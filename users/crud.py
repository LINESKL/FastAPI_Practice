from users.schemas import CreateUser

def create_user(user_in: CreateUser) -> dict:
    user_in = user_in.model_dump()
    return {
        "message": "success",
        "user": user_in
    }
