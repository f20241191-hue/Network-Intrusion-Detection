import pandas as pd 
from pathlib import Path 

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

project_folder = Path(__file__).resolve().parent.parent

data_path = project_folder / "data" / "processed" / "binary_dataset.csv"
data = pd.read_csv(data_path)

x = data.drop("Label", axis=1)
y = data["Label"]

x_train, x_test, y_train, y_test, = train_test_split(
    x,y, test_size=0.20, random_state=42, stratify=y
)

model = DecisionTreeClassifier(
    max_depth=10, random_state=42
)
model.fit(x_train, y_train)
y_pred = model.predict(x_test)

test_data = x_test.copy()

test_data["Actual"] = y_test
test_data["Predicted"] = y_pred

False_positives = test_data[
    (test_data["Actual"] == 0) & (test_data["Predicted"] == 1)
]

flase_negatives = test_data[
    (test_data["Actual"] == 1)&(test_data["Predicted"] == 0)
]

results_folder = project_folder/"results"
results_folder.mkdir(parents=True, exist_ok=True)

False_positives.to_csv(results_folder/"false_positives.csv", index=False)
flase_negatives.to_csv(results_folder/"false_negatives.csv", index=False)

print("Error analysis completed!")
print("False negatives:", len(flase_negatives))
print("False positives:", len(False_positives))
print("Error files saved in results folder.")