from importlib.metadata import files

import pandas as pd 
from pathlib import Path 

project_folder = Path(__file__).resolve().parent.parent 

data_folder = project_folder/"data"/"raw"/"PCAPs"

output_folder = project_folder/"data"/"processed"

output_folder.mkdir(parents=True, exist_ok=True)

files = list(data_folder.glob("*.csv"))

selected_features = [
     "Destination Port",
    "Total Fwd Packets",
    "Total Backward Packets",
    "Total Length of Fwd Packets",
    "Total Length of Bwd Packets",
    "Fwd Packet Length Mean",
    "Bwd Packet Length Mean",
    "Packet Length Mean",
    "SYN Flag Count",
    "ACK Flag Count",
    "RST Flag Count"
]

all_data =[]

for file in files:
    print("\nProcessing:", file.name)
    
    data = pd.read_csv(file)
    
    data.columns = data.columns.str.strip()
    
    data = data[selected_features+["Label"]]
    
    data["Label"] = data["Label"].apply(
        lambda label: 0 if label == "BENIGN" else 1
    )
    
    all_data.append(data)
    
combined_data = pd.concat(all_data, ignore_index=True)

output_file = output_folder/"binary_dataset.csv"

combined_data.to_csv(output_file, index=False)

print("\nDataset preparation completed!")
print("Total records:", len(combined_data))
print("\nLabel distribution:")

print(combined_data["Label"].value_counts())

print("\nSaved file:", output_file)
