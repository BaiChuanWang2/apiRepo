from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def main():
    return {"message": "API is running"}

@app.get("/test")
def test():
    return {"message": "Hello from FastAPI!"}