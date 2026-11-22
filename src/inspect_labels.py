import pandas as pd 
from pathlib import Path

project_folder = Path(__file__).resolve().parent.parent

data_folder = project_folder/"data"/"raw"/"PCAPs"

files = list(data_folder.glob("*.csv"))

for file in files:
    print("Dataset:", file.name)
    
    data = pd.read_csv(file, usecols=[" Label"])
    
    label_counts = data[" Label"].value_counts()
    
    print("\nLabel distribution:")
    print(label_counts)