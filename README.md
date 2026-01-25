HeartAI - Clinical Diagnosis Support System 🏥
An AI-powered system designed to predict heart disease risk levels by combining machine learning probabilities with critical clinical markers.

<font color="#2e86de">🛠️ Installation & Setup (Required)</font>
To avoid library conflicts (such as numpy or pkgutil errors), please follow these steps to set up a clean Virtual Environment:

1. Create a Virtual Environment
Navigate to the project folder in your terminal and run:

Bash

python -m venv venv
2. Activate the Environment
Windows:

Bash

venv\Scripts\activate
Mac/Linux:

Bash

source venv/bin/activate
3. Install Dependencies
Bash

pip install --upgrade pip
pip install -r requirements.txt
4. Run the Application
Bash

python final_app.py
The system will be accessible at:
 http://127.0.0.1:8080.

<font color="#d35400">📊 2026 Model Optimization Update</font>
We recently conducted a deep-dive analysis to enhance the system's accuracy and reliability.

✨ Latest Improvements
Data Cleaning: Resolved the KeyError by correctly mapping the target column num.

Error Handling: Implemented robust handling for NaN values and categorical encoding for variables like 'sex' and 'dataset'.

Multi-Model Benchmarking: Evaluated 4 different algorithms (Logistic Regression, Decision Tree, Random Forest, and SVM).

Data Export: Generated and exported standardized train.csv and valid.csv for reproducibility.

🏆 Best Performing Model
Based on three different visualization methods (Vertical, Horizontal, and Lollipop charts), the Random Forest model was selected as the optimal choice with an accuracy of 60.33%. This provides a realistic and reliable baseline for complex clinical diagnosis.

<font color="#27ae60">📈 Diagnostic Logic & Risk Levels</font>
The system uses a 4-level classification logic to ensure patient safety and clinical accuracy:

🟢 Low Risk: Probability < 30%. Indicators are within normal clinical ranges.

🟡 Moderate Risk: Probability between 30% - 60%. Suggests follow-up and lifestyle monitoring.

🟠 High Risk: Probability between 60% - 85%. Requires consultation with a specialist.

🔴 Very High Risk: Probability > 85% OR Clinical Red Flags (e.g., Major Vessels ca >= 2 or Oldpeak >= 2.5).

<font color="#c0392b">📂 Project Structure</font>
Data Sets/: Raw clinical data.

Heart Disease Diagnostic Analysis.ipynb: The finalized analysis notebook containing the 3 comparison charts.

train.csv / valid.csv: Standardized data subsets used for training and validation.

final_app.py: The main Flask server and prediction logic.

heart_model.pkl: Trained Machine Learning model.

scaler.pkl: Feature scaling file for data normalization.

templates/: Contains index.html for the user interface.

requirements.txt: List of required libraries with stable versions.