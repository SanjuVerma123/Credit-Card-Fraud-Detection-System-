# # ==============================
# # 🚀 IMPORT LIBRARIES
# # ==============================
# import streamlit as st
# import numpy as np
# import joblib
# import pandas as pd

# # ==============================
# # 📂 LOAD SAVED FILES
# # ==============================
# model = joblib.load("model.pkl")
# scaler = joblib.load("scaler.pkl")
# threshold = joblib.load("threshold.pkl")

# # ==============================
# # PAGE CONFIG
# # ==============================
# st.set_page_config(page_title="Fraud Detection", layout="wide")

# # ==============================
# # TITLE
# # ==============================
# st.title("💳 Credit Card Fraud Detection System")
# st.markdown("### 🔍 Enter Transaction Details")

# # ==============================
# # FEATURE NAMES (IMPORTANT)
# # ==============================
# features = ['Time','V1','V2','V3','V4','V5','V6','V7','V8','V9','V10',
#             'V11','V12','V13','V14','V15','V16','V17','V18','V19','V20',
#             'V21','V22','V23','V24','V25','V26','V27','V28','Amount']

# # ==============================
# # INPUT UI (CLEAN GRID)
# # ==============================
# cols = st.columns(3)
# inputs = []

# for i, feature in enumerate(features):
#     with cols[i % 3]:
#         val = st.number_input(f"{feature}", value=0.0)
#         inputs.append(val)

# # Convert to array
# input_data = np.array(inputs).reshape(1, -1)

# # Apply scaling
# input_data = scaler.transform(input_data)

# # ==============================
# # PREDICTION BUTTON
# # ==============================
# if st.button("🚀 Predict Transaction"):

#     prob = model.predict_proba(input_data)[0][1]

#     st.subheader("📊 Prediction Result")

#     # Probability bar
#     st.progress(float(prob))

#     st.write(f"### Fraud Probability: {prob:.4f}")

#     # Result
#     if prob >= threshold:
#         st.error("🚨 Fraud Transaction Detected!")
#     else:
#         st.success("✅ Normal Transaction")

#     # Show threshold
#     st.write(f"Model Threshold: {threshold:.4f}")

# # ==============================
# # SIDEBAR INFO
# # ==============================
# st.sidebar.title("ℹ️ About Project")
# st.sidebar.write("""
# This project uses Machine Learning to detect fraudulent credit card transactions.

# Features:
# - XGBoost Model
# - SMOTE (Imbalance Handling)
# - Hyperparameter Tuning
# - Threshold Optimization
# - Real-time Prediction
# """)





# # ==============================
# # 🚀 IMPORT LIBRARIES
# # ==============================
# import streamlit as st
# import numpy as np
# import joblib

# # ==============================
# # 📂 LOAD SAVED FILES
# # ==============================
# model = joblib.load("model.pkl")
# scaler = joblib.load("scaler.pkl")
# threshold = joblib.load("threshold.pkl")

# # ==============================
# # ⚙️ PAGE CONFIG
# # ==============================
# st.set_page_config(page_title="Fraud Detection", layout="wide")

# # ==============================
# # 🎯 TITLE
# # ==============================
# st.title("💳 Credit Card Fraud Detection System")
# st.markdown("### 🔍 Enter Transaction Details")

# # ==============================
# # 📌 FEATURE NAMES
# # ==============================
# features = ['Time','V1','V2','V3','V4','V5','V6','V7','V8','V9','V10',
#             'V11','V12','V13','V14','V15','V16','V17','V18','V19','V20',
#             'V21','V22','V23','V24','V25','V26','V27','V28','Amount']

# # ==============================
# # 🧠 SESSION STATE INIT
# # ==============================
# if "inputs" not in st.session_state:
#     st.session_state.inputs = {feature: 0.0 for feature in features}

# # ==============================
# # 🎯 SAMPLE DATA BUTTON
# # ==============================
# if st.button("🎯 Fill Sample Data"):
#     for key in st.session_state.inputs:
#         st.session_state.inputs[key] = 0.5

# # ==============================
# # 📥 INPUT UI (STABLE)
# # ==============================
# cols = st.columns(3)

# for i, feature in enumerate(features):
#     with cols[i % 3]:
#         st.session_state.inputs[feature] = st.number_input(
#             label=feature,
#             value=st.session_state.inputs[feature],
#             key=feature
#         )

# # ==============================
# # 🔄 PREPARE INPUT DATA
# # ==============================
# input_values = list(st.session_state.inputs.values())
# input_data = np.array(input_values).reshape(1, -1)

# # Apply scaling
# input_data = scaler.transform(input_data)

# # ==============================
# # 🚀 PREDICTION BUTTON
# # ==============================
# if st.button("🚀 Predict Transaction"):

#     prob = model.predict_proba(input_data)[0][1]

#     st.subheader("📊 Prediction Result")

#     # Probability bar
#     st.progress(float(prob))

#     st.write(f"### Fraud Probability: {prob:.4f}")

#     # Final decision
#     if prob >= threshold:
#         st.error("🚨 Fraud Transaction Detected!")
#     else:
#         st.success("✅ Normal Transaction")

#     st.write(f"Model Threshold: {threshold:.4f}")

# # ==============================
# # 📊 SIDEBAR
# # ==============================
# st.sidebar.title("ℹ️ About Project")
# st.sidebar.write("""
# This project uses Machine Learning to detect fraudulent credit card transactions.

# 🔹 XGBoost Model  
# 🔹 SMOTE for Imbalance  
# 🔹 Hyperparameter Tuning  
# 🔹 Threshold Optimization  
# 🔹 Real-time Prediction  
# """)

# st.sidebar.markdown("---")
# st.sidebar.write("👨‍💻 Developed for Final Year Project")



# ==============================
# 🚀 IMPORT LIBRARIES
# ==============================
import streamlit as st
import numpy as np
import joblib

# ==============================
# ⚡ PAGE CONFIG (FIRST LINE)
# ==============================
st.set_page_config(page_title="Fraud Detection", layout="wide")

# ==============================
# ⚡ LOAD MODEL (CACHED)
# ==============================
@st.cache_resource
def load_artifacts():
    model = joblib.load("model.pkl")
    scaler = joblib.load("scaler.pkl")
    threshold = joblib.load("threshold.pkl")
    return model, scaler, threshold

model, scaler, threshold = load_artifacts()

# ==============================
# 🎯 TITLE
# ==============================
st.title("💳 Credit Card Fraud Detection System")
st.markdown("### 🔍 Enter Transaction Details")

# ==============================
# 📌 FEATURES
# ==============================
features = ['Time','V1','V2','V3','V4','V5','V6','V7','V8','V9','V10',
            'V11','V12','V13','V14','V15','V16','V17','V18','V19','V20',
            'V21','V22','V23','V24','V25','V26','V27','V28','Amount']

# ==============================
# 🧠 SESSION STATE INIT
# ==============================
if "inputs" not in st.session_state:
    st.session_state.inputs = {f: 0.0 for f in features}

# ==============================
# 🎯 SAMPLE BUTTON
# ==============================
if st.button("🎯 Fill Sample Data"):
    for key in st.session_state.inputs:
        st.session_state.inputs[key] = 0.5

# ==============================
# ⚡ FORM (NO RERUN ON INPUT)
# ==============================
with st.form("prediction_form"):

    cols = st.columns(3)

    for i, feature in enumerate(features):
        with cols[i % 3]:
            st.session_state.inputs[feature] = st.number_input(
                feature,
                value=st.session_state.inputs[feature],
                key=feature
            )

    submit = st.form_submit_button("🚀 Predict Transaction")

# ==============================
# 🚀 PREDICTION (ONLY ON CLICK)
# ==============================
if submit:
    input_values = list(st.session_state.inputs.values())
    input_data = np.array(input_values).reshape(1, -1)

    # Apply scaling ONLY HERE (fast)
    input_scaled = scaler.transform(input_data)

    prob = model.predict_proba(input_scaled)[0][1]

    st.subheader("📊 Prediction Result")

    # Progress bar
    st.progress(float(prob))

    st.write(f"### Fraud Probability: {prob:.4f}")

    if prob >= threshold:
        st.error("🚨 Fraud Transaction Detected!")
    else:
        st.success("✅ Normal Transaction")

    st.write(f"Model Threshold: {threshold:.4f}")

# ==============================
# 📊 SIDEBAR
# ==============================
st.sidebar.title("ℹ️ About Project")
st.sidebar.write("""
This project uses Machine Learning to detect fraudulent credit card transactions.

🔹 XGBoost Model  
🔹 SMOTE  
🔹 Hyperparameter Tuning  
🔹 Threshold Optimization  
🔹 Real-time Prediction  
""")