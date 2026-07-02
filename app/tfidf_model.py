"""
This script is responsible for building and managing the TF-IDF model for the recommendation engine.
"""

from sklearn.feature_extraction.text import TfidfVectorizer


class TFIDFModel:
    """
    Responsible for building and managing the TF-IDF model.
    """

    def __init__(self):
        self.vectorizer = TfidfVectorizer()
        self.tfidf_matrix = None

    def fit(self, documents):
        """
        Learn the vocabulary from the dataset.
        """

        self.tfidf_matrix = self.vectorizer.fit_transform(documents)

    def transform(self, text):
        """
        Transform new user input using the learned vocabulary.
        """

        return self.vectorizer.transform([text])

    def get_matrix(self):
        """
        Returns the TF-IDF matrix.
        """

        return self.tfidf_matrix