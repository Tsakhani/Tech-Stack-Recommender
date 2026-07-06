"""
This script is strictly to load the cleaned dataset...
"""

import pandas as pd


class DataLoader:
    """
    Responsible for loading the cleaned dataset.
    """

    def __init__(self, dataset_path):
        self.dataset_path = dataset_path

    def load_data(self):
        """
        Loads the cleaned dataset into a DataFrame.
        """

        try:
            df = pd.read_csv(self.dataset_path)

            print(f"Dataset loaded successfully ({len(df)} rows).")

            return df

        except FileNotFoundError:

            raise FileNotFoundError(
                f"Dataset not found: {self.dataset_path}"
            )
