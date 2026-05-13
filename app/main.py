from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {
        "message": "Enterprise RAG AI Assistant Running"
    }

@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }
