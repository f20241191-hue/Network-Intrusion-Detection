Network Intrusion Detection: Benign vs Attack Classification
Objective
Build a basic binary classifier to distinguish benign network traffic from attack traffic using a public intrusion-detection dataset.
Dataset
This experiment uses selected CSV files derived from CIC-IDS2017 (Tuesday-WorkingHours and Friday-WorkingHours-Afternoon-PortScan). Records were combined and converted into binary labels: BENIGN = 0 and attack = 1.

The combined dataset has 732,376 records and 11 selected input features plus Label.
Features
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
Target: Label.
Method
- Classifier: Decision Tree
- Maximum depth: 10
- Train/test split: stratified 80% / 20%
- Random seed: 91
Results
Reported run:
- Accuracy: 99.8409%
- Precision: 99.4183%
- Recall: 99.9103%
- F1-score: 99.6637%
Confusion matrix:
	Predicted Benign	Predicted Attack
Actual Benign	111,721	202
Actual Attack	31	34,522


TN = 111,721; FP = 202; FN = 31; TP = 34,522.

Training records: 585,900. Testing records: 146,476.
Failure analysis
The model missed 31 attack records. Of these, 22 (approximately 71.0%) were associated with destination port 80. Ports 0, 21, and 22 accounted for three missed records each. The median forward-packet count among missed records was three.

In one examined missed record, destination port was 80, there were three forward packets and one backward packet, and the reported packet-length and flag-count features were all zero. The actual label was attack, but the prediction was benign. This is an observed case; the analysis does not establish the cause.
Limitations
- The experiment uses precomputed flow-level dataset features; it does not implement extraction strictly from the first few packets of each flow. The early-flow/switch-feature requirement is therefore not fully demonstrated.
- A random train/test split was used. Duplicate or highly similar records may occur across both sets and inflate performance.
- The results do not demonstrate performance on live traffic or an independently collected network.
- The dataset and selected features may not represent all real-world traffic or attacks.
Project structure
Network_Intrusion_Detection/
├── data/
│   ├── raw/        (excluded from Git)
│   └── processed/  (binary dataset excluded from Git)
├── src/
├── results/
├── docs/
└── README.md
Reproducing the experiment
From the project root:
python src/train_model.py
python src/analyze_errors.py
python src/inspect_false_negatives.py
Next steps
- Investigate features extracted from only the first few packets of each flow using packet-level data.
- Evaluate with a split that reduces duplicate/session leakage and with independent traffic.
- Inspect missed attacks and false positives in greater depth.
- Compare the decision tree with another baseline classifier.
- Explore a practical early-flow detection pipeline.