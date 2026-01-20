# HeartAI: Cardiac Risk Analysis & Decision Support System

📌 Project Overview
HeartAI is an AI-driven clinical decision-support system designed to predict the probability of heart disease based on 13 clinical parameters. This project integrates machine learning with clinical expertise through a "Clinical Override" system to ensure patient safety.

 🛠️ Tech Stack
* **Backend:** Python (Flask Framework)
* **Frontend:** HTML5, CSS3, JavaScript (Asynchronous Fetch API)
* **Machine Learning:** Random Forest Classifier (Scikit-Learn)
* **Deployment Port:** 8080

 🚀 Key Features
* **Predictive AI:** Calculates risk probability using a pre-trained model (`heart_model.pkl`).
* **Clinical Safety Layer:** Implements a safety logic that upgrades "Low Risk" to "High Risk" if critical markers like Major Vessels or Oldpeak are elevated.
* **Dynamic UI:** Real-time feedback with color-coded results (Green for Low, Yellow for Moderate, Red for High).
* **Medical Range Validation:** Input fields are restricted to clinical ranges (e.g., Cholesterol 70-400 mg/dl) to prevent data entry errors.

 📂 Project Structure
Heart_Disease_AI/ 
data sets#for raw data before analysing
datanalysis (1).ipynb#for cleaned,analysed and visualazed data
final_app.py # Main Flask Server
  templates/ # UI Components │ └── index.html # Frontend Interface
  heart_model.pkl # Trained ML Model ├── scaler.pkl # Feature Scaling File 
 requirements.txt # Library Dependencies
 readme.md
 ⚙️ Installation & Setup
1. **Clone the project** and navigate to the directory.
2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   open Terminal and run: "python final_app.py"
   
 Access the UI: Open http://127.0.0.1:8080 in your browser.

🏥 Testing Scenarios
    Low Risk: Probability < 30%.

    Moderate Risk: Probability 30% - 50%.

    High Risk: Probability > 50% OR Clinical Override (Vessels >= 2).