import pandas as pd 
from pathlib import Path
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

project_folder = Path(__file__).resolve().parent.parent

data_path = project_folder/"data"/"processed"/"binary_dataset.csv"
data = pd.read_csv(data_path)

x = data.drop("Label", axis=1)
y = data["Label"]

x_train, x_test, y_train, y_test, = train_test_split(
    x,y, test_size=0.20, random_state=91, stratify=y
)

model = DecisionTreeClassifier(
    max_depth=10, random_state=91
)

model.fit(x_train, y_train)

y_pred = model.predict(x_test)

accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, zero_division=0)
recall = recall_score(y_test, y_pred, zero_division=0)
f1 = f1_score(y_test, y_pred, zero_division=0)

print("\n Model Evaluation Results")
print("Accuracy:", accuracy)
print("Precision:", precision)
print("recall:", recall)
print("F1-score:", f1)

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("\ncalssification report:")
print(classification_report(y_test, y_pred))

print("\nModel training completed!")

print("\nTraining records:", len(x_train))
print("testing records:", len(x_test))

print("\nTraining class distribution:")
print(y_train.value_counts())

print("\nTesting class distribution:")
print(y_test.value_counts())