"""
Preprocessing module for the project. This module contains functions for data cleaning, 
normalization, and feature extraction.
"""
import pandas as pd
import re
#load the dataset
df = pd.read_csv("data/job_role_dataset.csv")

#------------------------------------
# Feature Engineering
#------------------------------------

# Keeping only the skills and job role columns
df =  df[["skills", "job_role"]]

# Removing duplicate rows
df = df.drop_duplicates()

#------------------------------------
# Text Preprocessing
#------------------------------------

# Convert to lowercase
df["skills"] = df["skills"].str.lower()

# Remove whitespace
df["skills"] = df["skills"].str.strip()

# Replace multiple spaces with a single space
df["skills"] = df["skills"].str.replace(r"\s+", " ", regex=True)

def clean_skills(text):
    text = text.lower()
    text = text.replace(",", " ")
    text = re.sub(r"\s+", " ", text)
    return text.strip()

df["skills"] = df["skills"].apply(clean_skills)

# save cleaned dataset
df.to_csv("data/cleaned_job_role_dataset.csv", index=False)

print("Dataset cleaned and saved successfully")
print(df.head())
