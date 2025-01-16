from http import HTTPStatus

from fastapi import FastAPI, HTTPException

from fast_api_course.schemas import (
    Message,
    UserDB,
    UserList,
    UserPublicSchema,
    UserSchema,
)

app = FastAPI()

database = []


@app.get("/", status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {"message": "Olá Mundo!"}


@app.post(
    "/users/", status_code=HTTPStatus.CREATED, response_model=UserPublicSchema
)
def create_user(user: UserSchema):
    user_with_id = UserDB(**user.model_dump(), id=len(database) + 1)

    database.append(user_with_id)

    return user_with_id


@app.get("/users/", status_code=HTTPStatus.OK, response_model=UserList)
def read_users():
    return {"users": database}


@app.put(
    "/users/{user_id}",
    status_code=HTTPStatus.OK,
    response_model=UserPublicSchema,
)
def update_user(user_id: int, user: UserSchema):
    if user_id > len(database) or user_id < 1:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail="User not found"
        )
    user_index = user_id - 1
    database[user_index] = UserDB(**user.model_dump(), id=user_id)
    return database[user_index]


@app.delete("/users/{user_id}", response_model=Message)
def delete_user(user_id: int):
    if user_id > len(database) or user_id < 1:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail="User not found"
        )
    del database[user_id - 1]
    return {"message": "User deleted successfully"}
