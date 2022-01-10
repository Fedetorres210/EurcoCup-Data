from fastapi import FastAPI
from routes.Eurocup import euro
import uvicorn



app =  FastAPI()
@app.get("/")
def root():
    return {"hello world": "Hola mundo"}

app.include_router(euro)

