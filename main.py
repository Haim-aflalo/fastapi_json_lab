from fastapi import FastAPI, HTTPException
import uvicorn
import json
from pydantic import BaseModel

app = FastAPI()
class Item(BaseModel):
    id:int
    name:str
    price:float

def load_data():
    with open("data.json") as json_file:
        data =  json.load(json_file)
        return data


def save_data(data):
    with open("data.json", "w") as json_file:
        json.dump(data,json_file, indent=4)


@app.get("/items")
def get_all_items():
    return load_data()


@app.put("/items")
def update_price(it:Item):
    items = load_data()
    for item in items:
        if item["id"] == it.id:
            item["price"]  = it.price
        save_data(items)
    return  "hello"

if __name__ == "__main__":
    uvicorn.run(app,host="localhost",port=8000)

