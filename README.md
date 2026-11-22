# Network Intrusion Detection — Baseline Classifier

## 1. Project Objective

The objective of this experiment is to develop a simple machine-learning baseline for binary network traffic classification, distinguishing benign traffic from attack traffic using selected flow-level features from CIC-IDS2017.

## 2. Dataset

This experiment uses processed CSV data derived from CIC-IDS2017:

- Friday-WorkingHours-Afternoon-PortScan
- Tuesday-WorkingHours

The dataset was combined and converted into a binary classification dataset:

- 0 = Benign
- 1 = Attack

The combined dataset contains 732,376 records.

## 3. Selected Features

The model uses the following 11 features:

- Destination Port
- Total Fwd Packets
- Total Backward Packets
- Total Length of Fwd Packets
- Total Length of Bwd Packets
- Fwd Packet Length Mean
- Bwd Packet Length Mean
- Packet Length Mean
- SYN Flag Count
- ACK Flag Count
- RST Flag Count

## 4. Model and Method

- Model: Decision Tree Classifier
- Maximum depth: 10
- Train/test split: 80/20
- Random state: 42
- Stratified splitting: Enabled
- Classification: Binary

## 5. Results

- Accuracy: 99.81%
- Precision: 99.32%
- Recall: 99.88%
- F1-score: 99.60%

Confusion Matrix:

| | Predicted Benign | Predicted Attack |
|---|---:|---:|
| Actual Benign | 111,687 | 236 |
| Actual Attack | 41 | 34,512 |

## 6. Error Analysis

The model produced:

- 236 false positives
- 41 false negatives

Among the 41 false-negative records, 29 had destination port 80. This is an observed pattern in the errors and does not establish the cause of misclassification.

## 7. Limitations

- The experiment uses precomputed flow-level features from processed CSV files, not features extracted directly from the first few packets of a live flow.
- The random train/test split may allow similar or duplicate records to appear in both sets, potentially inflating performance.
- The dataset contains a substantial number of duplicate records.
- The experiment does not validate performance on live network traffic or on an independent network environment.
- The selected model and depth were used as a baseline and were not systematically optimized.

## 8. Project Structure

```text
Network_Intrusion_Detection/
├── data/
│   ├── raw/
│   └── processed/
├── src/
│   ├── inspect_data.py
│   ├── inspect_labels.py
│   ├── prepare_dataset.py
│   ├── check_processed_data.py
│   ├── train_model.py
│   ├── analyze_errors.py
│   └── inspect_false_negatives.py
├── results/
│   ├── false_positives.csv
│   ├── false_negatives.csv
│   └── model_results.txt
├── .gitignore
└── README.md
```

## 9. Reproducibility

The Python scripts are located in the `src/` directory.

The training script can be executed using:

```bash
python src/train_model.py
```

Error analysis can be executed using:

```bash
python src/analyze_errors.py
```

False-negative inspection can be executed using:

```bash
python src/inspect_false_negatives.py
```

The raw and processed datasets are excluded from Git tracking.

## 10. Future Work

Future work will focus on extracting features from the first few packets of network flows, evaluating the model on independent data, investigating false positives and false negatives, and exploring more robust evaluation methods.
