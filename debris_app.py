import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Page config
st.set_page_config(page_title="★ StarTrace - Space Debris Intelligence", layout="wide")

# Custom CSS for dark theme with space-purple
st.markdown("""
    <style>
    body, .stApp {
        background-color: #0d0d0d;
        color: #e0e0e0;
    }
    .stTitle, .stHeader {
        color: #ae81ff;
    }
    .css-1v3fvcr, .css-1d391kg, .css-1r6slb0 {
        background-color: #1a1a1a;
        border-radius: 10px;
        padding: 1rem;
    }
    .block-container {
        padding: 2rem;
    }
    </style>
""", unsafe_allow_html=True)

# App title with emoji logo
st.markdown("""
# ★ StarTrace
### *Space Debris Predictive Intelligence*
""")

# Load model safely
model_path = "debris_model.pkl"
model = None
if os.path.exists(model_path):
    model = joblib.load(model_path)
else:
    st.warning("⚠️ Model not found. Please make sure `debris_model.pkl` is in the directory.")

# Tabs: Upload CSV | Manual Input
option = st.radio("Choose Input Method:", ["Upload CSV", "Enter Parameters Manually"], horizontal=True)

if option == "Upload CSV":
    uploaded_file = st.file_uploader("Upload your debris data (CSV format)", type=["csv"])

    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        st.subheader("📄 Uploaded Data Preview")
        st.dataframe(df.head())

        if model:
            if all(col in df.columns for col in ['velocity', 'altitude', 'size']):
                prediction = model.predict(df[['velocity', 'altitude', 'size']])
                df['Collision Risk'] = prediction

                st.success("✅ Prediction Complete!")
                st.write(df)

                # Visualization
                st.subheader("📊 Collision Risk Chart")
                fig, ax = plt.subplots()
                sns.countplot(x='Collision Risk', data=df, palette='rocket', ax=ax)
                st.pyplot(fig)
            else:
                st.error("❌ Required columns: 'velocity', 'altitude', 'size' not found.")

else:
    st.subheader("🔧 Enter Debris Parameters:")
    velocity = st.slider("Velocity (km/s)", 0.0, 15.0, 7.8)
    altitude = st.slider("Altitude (km)", 100, 36000, 500)
    size = st.slider("Size (cm)", 1, 100, 10)

    if st.button("🚀 Predict Collision Risk"):
        if model:
            prediction = model.predict([[velocity, altitude, size]])
            result = "High Risk" if prediction[0] == 1 else "Low Risk"
            st.success(f"🚨 Collision Risk: **{result}**")

            # Show visual feedback
            fig, ax = plt.subplots()
            ax.bar(["Velocity", "Altitude", "Size"], [velocity, altitude, size], color=["#c678dd", "#61afef", "#e06c75"])
            ax.set_ylabel("Values")
            ax.set_title("Debris Parameters")
            st.pyplot(fig)

# Footer branding
st.markdown("""
---
<center>
    <h4 style='color: #888;'>Crafted with 🛰️ by <strong>Team StarTrace</strong></h4>
</center>
""", unsafe_allow_html=True)
