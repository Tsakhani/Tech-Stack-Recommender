"""
This script is for the recommendation engine.
"""

import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from tfidf_model import TFIDFModel


class RecommendationEngine:

    def __init__(self, dataframe):

        self.df = dataframe

        self.model = TFIDFModel()

        self.model.fit(self.df["skills"])

    def recommend(self, skills):

        user_input = " ".join(skills).lower()

        user_vector = self.model.transform(user_input)

        similarity_scores = cosine_similarity(
            user_vector,
            self.model.get_matrix()
        ).flatten()

        recommendations = self.df.copy()

        recommendations["score"] = similarity_scores

        recommendations = (
            recommendations
            .sort_values(by="score", ascending=False)
            .drop_duplicates(subset=["job_role"])
            .head(5)
        )

        return recommendations[["job_role", "score"]]