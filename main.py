from fastapi import FastAPI
import json

app = FastAPI()


def load_data():
    with open("data.json") as json_file:
        data =  json.load(json_file)
        return data



def save_data(data):
    with open("data.json", "x") as json_file:
        json.dump(data,json_file)


