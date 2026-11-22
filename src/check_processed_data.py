import pandas as pd

from pathlib import Path

project_folder = Path(__file__).resolve().parent.parent

file_path = project_folder /"data"/"processed"/"binary_dataset.csv"

data = pd.read_csv(file_path)

print("Dataset shape:", data.shape)

print("\nFirst five rows:")
print(data.head())

print("\nMissing values:")
print(data.isnull().sum())

print("\nDuplicate rows:", data.duplicated().sum())

print("\nlabel distribution:")
print(data["Label"].value_counts())

print("\ndata types:")
print(data.dtypes)