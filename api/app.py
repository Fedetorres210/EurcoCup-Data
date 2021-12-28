from fastapi import FastAPI
from routes.Eurocup import euro

print("holla")

app =  FastAPI()

app.include_router(euro)