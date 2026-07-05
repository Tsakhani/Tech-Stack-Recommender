"""
This script is responsible for all database operations
"""
from models import Recommendation, User
from recommendation_engine import RecommendationEngine

class RecommendationService:

    def __init__(self, db, engine: RecommendationEngine):

        self.db = db
        self.engine = engine

    def _create_user(self, skills):

        user = User(skills=", ".join(skills))

        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)

        return user
    
    def _save_recommendations(self, user_id, recommendations):

        for _, row in recommendations.iterrows():

            recommendation = Recommendation(

                user_id=user_id,
                job_role=row["job_role"],
                similarity_score=float(row["score"])
            )

            self.db.add(recommendation)

        self.db.commit()


    def recommend(self, skills):

        recommendations = self.engine.recommend(skills)

        user = self._create_user(skills)

        self._save_recommendations(user.id, recommendations)

        return {
            "user_id": user.id,
            "recommendations": recommendations.to_dict(orient="records")
            
        }
    
