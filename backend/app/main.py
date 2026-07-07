from fastapi import FastAPI

app = FastAPI(title="NexaFlow API")

@app.get("/")
def home():
    return {"message": "NexaFlow API Online 🚀"}