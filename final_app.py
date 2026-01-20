from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import numpy as np
import joblib

app = Flask(__name__)
CORS(app)

try:
    model = joblib.load('heart_model.pkl')
    scaler = joblib.load('scaler.pkl')
except:
    print("Error: Model or Scaler files not found!")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        raw_features = data['features']
        features = np.array(raw_features).reshape(1, -1)
        
        scaled_data = scaler.transform(features)
        prob_value = model.predict_proba(scaled_data)[0][1]
        
        oldpeak = raw_features[9]
        major_vessels = raw_features[11]

        # --- التصنيف الجديد (4 مستويات) ---
        if prob_value < 0.30:
            status = "Low Risk"
            rec = "Your cardiac parameters are within healthy ranges. Maintain a balanced diet."
        elif prob_value < 0.60:
            status = "Moderate Risk"
            rec = "Borderline results detected. Lifestyle changes and a follow-up in 6 months are recommended."
        elif prob_value < 0.85:
            status = "High Risk"
            rec = "High risk detected. Please consult a cardiologist soon for further tests."
        else:
            status = "Very High Risk"
            rec = "CRITICAL ALERT: Statistical probability is very high. Immediate medical attention is required."

        # --- صمام الأمان السريري (يرفع الحالة فوراً إلى Very High) ---
        # إذا كان هناك انسداد في وعائين أو أكثر، نعتبرها خطورة قصوى فوراً
        if (major_vessels >= 2 or oldpeak >= 2.5) and prob_value < 0.85:
            status = "Very High Risk (Clinical Priority)"
            display_prob = f"Critical Indicators Detected ({prob_value * 100:.2f}%)"
            rec = "URGENT: Severe clinical signs (Blocked Vessels/ST Depression) detected regardless of AI score. Go to ER or Cardiologist immediately."
        else:
            display_prob = f"{prob_value * 100:.2f}%"

        return jsonify({
            'status': 'success',
            'diagnosis': status,
            'probability': display_prob,
            'recommendation': rec
        })
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

if __name__ == '__main__':
    # تشغيل السيرفر على منفذ 8080 لتجنب التعارض
    app.run(debug=True, use_reloader=False, port=8080)