from typing import Union

from fastapi import FastAPI
from bot import chat
app = FastAPI()


@app.get("/")
def read_root():
    response =chat()
    return response


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}