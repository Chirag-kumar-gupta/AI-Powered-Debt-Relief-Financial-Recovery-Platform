from fastapi import FastAPI

app = FastAPI(
    title="AI Powered Debt Relief & Financial Recovery Platform",
    description="Backend API for debt management, financial analysis, and AI-powered recommendations.",
    version="1.0.0",
)

@app.get("/")
def home():
    return {
        "message": "Welcome to the AI Powered Debt Relief & Financial Recovery Platform API!",
        "status": "Backend is running successfully."
    }

@app.get("/health")
def health():
    return {
        "status": "OK"
    }