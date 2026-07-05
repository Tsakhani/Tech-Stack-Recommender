"""
Only for testing purposes. This script is not intended to be used in production.
"""

from data_loader import DataLoader
from recommendation_engine import RecommendationEngine
from validators import InputValidator
from database import engine, SessionLocal
from models import Base, User, Recommendation

def main():

    loader = DataLoader("../data/cleaned_job_role_dataset.csv")

    dataframe = loader.load_data()

    engine = RecommendationEngine(dataframe)

    db = SessionLocal()

    print("Welcome to the Job Role Recommendation System!")

    user_input = input("Please enter at least 3 skills separated by commas: \n")

    skills = [
        skill.strip()
        for skill in user_input.split(",")
    ]

    InputValidator.validate(skills)

    user = User(skills=",".join(skills))

    db.add(user)

    db.commit()

    db.refresh(user)

    recommendations = engine.recommend(skills)

    for _, row in recommendations.iterrows():
        recommendation = Recommendation(
            user_id=user.id,
            job_role=row["job_role"],
            similarity_score=row["score"]
        )

        db.add(recommendation)

    db.commit()

    print("\nTop Recommendations:\n")

    print(recommendations)

    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    main()