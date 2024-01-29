from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

@app.get("/greet/{name}")
def greet(name: str):
    return {"message": f"Hello, {name}!"}


# main execution

if __name__ == "__main__":
      import uvicorn
      uvicorn.run(app )