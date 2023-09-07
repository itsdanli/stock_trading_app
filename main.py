from fastapi import FastAPI
import sqlite3, config

app = FastAPI()
@app.get("/")
def index():
    return {"hello": "world"}