from pathlib import Path
import pandas as pd 

project_folder = Path(__file__).resolve().parent.parent

data_folder = project_folder / "data" / "raw" / "PCAPs"

files = list(data_folder.glob("*.csv"))

for file in files:
    
    
    print("Dataset", file.name)
    
    data = pd.read_csv(file, nrows=5)
    print("\nColumn names:")
    print(data.columns.tolist())