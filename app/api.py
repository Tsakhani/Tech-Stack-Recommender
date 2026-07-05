"""
This script is the api code, the bridge between the frontend and the recommendation engine.
"""

from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from data_loader import DataLoader
from recommendation_engine import RecommendationEngine
from validators import InputValidator
from schemas import SkillRequest
from services import RecommendationService
from database import get_db

app = FastAPI()

app.add_middleware(
    CORSMiddleware,

    allow_origins=[
        "http://127.0.0.1:5000",
        "http://localhost:5000"
    ],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"],
)

loader = DataLoader("../data/cleaned_job_role_dataset.csv")

df = loader.load_data()

engine = RecommendationEngine(df)

@app.get("/")
def home():
    return {
        "message": "Tech Stack Recommendation API"
    }

@app.post("/recommend")
def recommend(
    request: SkillRequest,
    db: Session = Depends(get_db)
):

    InputValidator.validate(request.skills)

    service = RecommendationService(
        db=db, 
        engine=engine
    )

    return service.recommend(request.skills)

