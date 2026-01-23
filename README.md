# HeartAI - Clinical Diagnosis Support System 🏥

An AI-powered system designed to predict heart disease risk levels by combining machine learning probabilities with critical clinical markers.

---

## 🛠️ Installation & Setup (Required)

To avoid library conflicts (such as `numpy` or `pkgutil` errors), please follow these steps to set up a clean Virtual Environment:

### 1. Create a Virtual Environment
Navigate to the project folder in your terminal and run:
```bash
python -m venv venv 
Activate the Environment
Windows:

Bash

venv\Scripts\activate
Mac/Linux:

Bash

source venv/bin/activate
3. Install Dependencies
Once the environment is active, install the stable library versions:

Bash

pip install --upgrade pip
pip install -r requirements.txt
4. Run the Application
Bash

python final_app.py
The system will be accessible at: http://127.0.0.1:8080.

📊 Diagnostic Logic & Risk Levels
The system uses a 4-level classification logic to ensure patient safety and clinical accuracy:

🟢 Low Risk: Probability < 30%. Indicators are within normal clinical ranges.

🟡 Moderate Risk: Probability between 30% - 60%. Suggests follow-up and lifestyle monitoring.

🟠 High Risk: Probability between 60% - 85%. Requires consultation with a specialist.

🔴 Very High Risk: Probability > 85% OR Clinical Red Flags (e.g., Major Vessels ca >= 2 or Oldpeak >= 2.5).

🎨 Visual Indicators
The UI dynamically changes colors based on the risk level to provide immediate visual feedback to healthcare providers:

Green: Safe/Routine.

Yellow: Caution/Observation.

Orange: Warning/Action Required.

Dark Red: Critical/Emergency.

📂 Project Structure
data sets: the raw data 

datanalysis (1).ipynb:cleaned data

final_app.py: The main Flask server and prediction logic.

heart_model.pkl: Trained Machine Learning model.

scaler.pkl: Feature scaling file for data normalization.

templates/: Contains index.html for the user interface.

requirements.txt: List of required libraries with stable versions.