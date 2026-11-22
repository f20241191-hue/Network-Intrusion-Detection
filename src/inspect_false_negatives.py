import pandas as pd
from pathlib import Path

project_folder = Path(__file__).resolve().parent.parent

file_path = project_folder / "results" / "false_negatives.csv"

data = pd.read_csv(file_path)

print("\nFirst missed attack record (complete):")
print(data.iloc[0].to_string())

print("\nDestination port distribution among missed attacks:")
print(data["Destination Port"].value_counts())

print("\nForward packet count distribution:")
print(data["Total Fwd Packets"].describe())