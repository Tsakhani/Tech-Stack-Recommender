"""
Only for testing purposes. This script is not intended to be used in production.
"""

from data_loader import DataLoader
from recommendation_engine import RecommendationEngine
from validators import InputValidator

def main():

    loader = DataLoader("../data/cleaned_job_role_dataset.csv")

    dataframe = loader.load_data()

    engine = RecommendationEngine(dataframe)

    print("Welcome to the Job Role Recommendation System!")

    user_input = input("Please enter at least 3 skills separated by commas: \n")

    skills = [
        skill.strip()
        for skill in user_input.split(",")
    ]

    InputValidator.validate(skills)

    recommendations = engine.recommend(skills)

    print("\nTop Recommendations:\n")

    print(recommendations)

if __name__ == "__main__":
    main()