from fastapi import FastAPI, HTTPException
import uvicorn
import json

app = FastAPI()


def load_data():
    with open("data.json") as json_file:
        data =  json.load(json_file)
        return data



def save_data(data):
    with open("data.json", "x") as json_file:
        json.dump(data,json_file)


@app.get("/items")
def get_all_items():
    return load_data()

# if __name__ == "__main__":
#     uvicorn.run(app,host="localhost",port=8000)

