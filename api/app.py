from fastapi import FastAPI
from routes.Eurocup import euro



app =  FastAPI()

app.include_router(euro)