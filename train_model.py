import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.ensemble import RandomForestClassifier
import joblib
import os

# الإعدادات والمسارات
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, 'heart.csv.csv')

try:
    # 1. تحميل البيانات
    df = pd.read_csv(DATA_PATH)
    print("✅ Step 1: Data loaded.")

    # 2. حذف الأعمدة غير الطبية ليتطابق العدد مع الواجهة (13 ميزة)
    # نحذف 'dataset' وأي أعمدة أخرى غير 'target' تزيد عن الـ 13 ميزة الأساسية
    cols_to_drop = ['dataset', 'id', 'Unnamed: 0'] 
    df = df.drop(columns=[col for col in cols_to_drop if col in df.columns])
    
    # 3. معالجة النصوص (Encoding)
    le = LabelEncoder()
    for col in df.columns:
        if df[col].dtype == 'object':
            df[col] = le.fit_transform(df[col])

    # 4. تحديد الهدف (Target) - نفترض أنه العمود الأخير
    target_col = df.columns[-1]
    X = df.drop(target_col, axis=1)
    y = df[target_col]
    
   
    print(f"ℹ️ Training with {X.shape[1]} medical features.")

    # 5. التدريب
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    
    model = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=42)
    model.fit(X_train_scaled, y_train)

    # 6. حفظ الملفات
    joblib.dump(model, os.path.join(BASE_DIR, 'heart_model.pkl'))
    joblib.dump(scaler, os.path.join(BASE_DIR, 'scaler.pkl'))
    
    print("✅ Step 2: Training successful. 13-feature model saved.")

except Exception as e:
    print(f"❌ Training Error: {str(e)}")