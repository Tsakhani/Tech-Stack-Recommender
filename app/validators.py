"""
This script is responsible for the input validation
"""

class InputValidator:

    @staticmethod
    def validate(skills):

        if not isinstance(skills, list):
            raise TypeError(
                "Skills must be provided as a list."
            )

        if len(skills) < 3:
            raise ValueError(
                "Please provide at least three skills."
            )

        return True