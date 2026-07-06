from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def instant():
    return "Live Production!"

@app.get("/heath")
def health_check():
    return {"status": "healthy"}