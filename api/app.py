from fastapi import FastAPI
from routes.Eurocup import euro
import uvicorn



app =  FastAPI()
@app.get("/")
def root():
    a = "a"
    b = "b" + a
    return {"hello world": b}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=80)

app.include_router(euro)

