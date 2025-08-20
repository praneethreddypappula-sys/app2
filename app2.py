import streamlit as st
import requests

# Page config
st.set_page_config(page_title="Project Kisan", layout="wide")

# Title
st.title("🌾 Project Kisan – AI Assistant for Small Farmers")
st.write("This is a demo skeleton — works without any API keys.")

# Sidebar menu
menu = st.sidebar.radio(
    "Choose a feature:",
    [
        "Instant Crop Diagnosis",
        "Market Price Analysis",
        "Government Scheme Assistance",
        "Voice & Multilingual AI",
        "Personalized Reminders",
        "Weather Alerts"
    ]
)

# Hugging Face API details
HF_API_URL = "https://api-inference.huggingface.co/models/microsoft/resnet-50"
HF_API_KEY = "hf_YOUR_VALID_API_KEY_HERE"  # Replace with your valid Hugging Face API key

headers = {
    "Authorization": f"Bearer {HF_API_KEY}",
    "Content-Type": "application/octet-stream"
}

def analyze_crop(image_bytes):
    response = requests.post(HF_API_URL, headers=headers, data=image_bytes)
    if response.status_code == 200:
        try:
            predictions = response.json()
            if isinstance(predictions, list) and predictions:
                top = predictions[0]
                return f"Prediction: {top['label']} (confidence: {top['score']:.2f})"
            else:
                return "No predictions returned."
        except Exception as e:
            return f"Error parsing response: {e}"
    else:
        return f"API request failed: {response.status_code} - {response.text}"


# Instant Crop Diagnosis page
if menu == "Instant Crop Diagnosis":
    st.header("🌱 Instant Crop Diagnosis")
    uploaded_img = st.file_uploader("Upload a crop image", type=["jpg", "png", "jpeg"])
    crop_desc = st.text_area("Describe your crop problem")

    if st.button("Diagnose"):
        if uploaded_img:
            img_bytes = uploaded_img.read()
            with st.spinner("Analyzing crop..."):
                result = analyze_crop(img_bytes)
            st.success(result)
        elif crop_desc:
            st.info(f"Text diagnosis not implemented yet. Your description: {crop_desc}")
        else:
            st.warning("Please upload an image or enter a description.")

# Feature: Market Price Analysis
elif menu == "Market Price Analysis":
    st.header("💹 Market Price Analysis")
    st.write("Upload your market data to see trends.")
    file = st.file_uploader("Upload CSV", type=["csv"])
    if file:
        import pandas as pd
        df = pd.read_csv(file)
        st.dataframe(df)

# Feature: Government Scheme Assistance
elif menu == "Government Scheme Assistance":
    st.header("🏛 Government Scheme Assistance")
    query = st.text_input("Ask about schemes")
    if query:
        st.info(f"Search results for '{query}' will appear here.")

# Feature: Voice & Multilingual AI
elif menu == "Voice & Multilingual AI":
    st.header("🗣 Voice & Multilingual AI")
    st.write("Voice assistant feature placeholder.")

# Feature: Personalized Reminders
elif menu == "Personalized Reminders":
    st.header("⏰ Personalized Reminders")
    reminder = st.text_input("Enter reminder text")
    if st.button("Save Reminder"):
        st.success("Reminder saved (demo only).")

# Feature: Weather Alerts
elif menu == "Weather Alerts":
    st.header("☀ Weather Alerts")
    location = st.text_input("Enter your location")
    if location:
        st.info(f"Weather for {location} will be shown here.")
