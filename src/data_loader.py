"""
This modules handle the Data loading functionality.
"""

import pandas as pd

class AnimeDataLoader:
    def __init__(self, original_csv: str, processed_csv: str):
        self.original_csv = original_csv
        self.processed_csv = processed_csv

    def load_and_process_data(self) -> pd.DataFrame:
        # Load the original CSV file
        df = pd.read_csv(self.original_csv, encoding='utf-8', on_bad_lines='skip')

        # Process the data: For example, drop duplicates and handle missing values
        df = df.dropna()
        df.drop_duplicates(inplace=True)

        # Selecting only required columns
        required_columns = ['Name', 'Genres', 'sypnopsis']

        # Checking if all required columns are present
        for column in required_columns:
            if column not in df.columns:
                raise ValueError(f"Missing required column: {column}")

        # Concatentating all columns into a single text column
        df['anime_information'] = (
            "Title: " + df['Name'] + ".. Overview: " + df['sypnopsis'] + "Genres: " + df['Genres']
        )

        # Save the processed data to a new CSV file
        df[["anime_information"]].to_csv(
            self.processed_csv, index=False, 
            encoding='utf-8', header=True)

        return self.processed_csv
    