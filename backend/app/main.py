from fastapi import FastAPI
from agents.scholarship_agent import ScholarshipAgent

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "SmartFunds API is live!"}
