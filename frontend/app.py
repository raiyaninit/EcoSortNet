import streamlit as st
import requests
from PIL import Image

# ---------------------- PAGE CONFIG ----------------------
st.set_page_config(
    page_title="EcoSortNet ♻️",
    page_icon="♻️",
    layout="centered"
)

# ---------------------- CUSTOM CSS ----------------------
st.markdown("""
<style>
/* Global font and background */
body, .main {
    font-family: 'Segoe UI', sans-serif;
    background-color: #0d1117;
    color: #c9d1d9;
}

/* Title styling */
h1 {
    color: #58a6ff;
    text-align: center;
}

/* Subtitle styling */
h3 {
    text-align: center;
    color: #8b949e;
    font-weight: normal;
}

/* Buttons */
.stButton>button {
    background-color: #238636;
    color: white;
    border-radius: 12px;
    padding: 10px 24px;
    border: none;
    font-size: 16px;
    transition: all 0.3s ease;
    font-weight: bold;
    box-shadow: 0px 3px 6px rgba(0,0,0,0.3);
}
.stButton>button:hover {
    background-color: #2ea043;
    cursor: pointer;
    transform: scale(1.05);
}

/* Result panel */
.result-box {
    background-color: #161b22;
    padding: 25px;
    border-radius: 12px;
    margin-top: 20px;
    text-align: center;
    border: 1px solid #30363d;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.5);
}

/* Footer styling */
.footer {
    text-align: center;
    margin-top: 40px;
    padding: 10px;
    color: #8b949e;
    font-size: 14px;
}

.footer a {
    color: #58a6ff;
    text-decoration: none;
}

.footer a:hover {
    text-decoration: underline;
}

/* Center all elements */
.css-18e3th9 {
    justify-content: center;
}
</style>
""", unsafe_allow_html=True)

# ---------------------- UI ----------------------
st.markdown("<h1>EcoSortNet ♻️</h1>", unsafe_allow_html=True)
st.markdown("<h3>AI-powered Waste Classification (Organic vs Recyclable)</h3>", unsafe_allow_html=True)

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    img = Image.open(uploaded_file)
    st.image(img, caption="Uploaded Image", width=300)

    if st.button("Classify Waste"):
        with st.spinner("Analyzing image..."):
            try:
                # Send local file bytes to Flask backend
                files = {"file": (uploaded_file.name, uploaded_file.getvalue(), uploaded_file.type)}
                response = requests.post("http://127.0.0.1:5000/predict", files=files)

                if response.status_code == 200:
                    result = response.json()
                    st.markdown(f"""
                        <div class="result-box">
                            <h3 style="color:#58a6ff;">Prediction: {result['prediction']}</h3>
                        </div>
                    """, unsafe_allow_html=True)
                else:
                    st.error(f"Backend error: {response.status_code}")
            except Exception as e:
                st.error(f"Error contacting backend API: {e}")

# ---------------------- FOOTER ----------------------
st.markdown("""
<div class="footer">
    Project made by <strong>raiyaninit</strong> | 
    <a href="https://github.com/raiyaninit" target="_blank">GitHub</a>
</div>
""", unsafe_allow_html=True)

