<!-- Banner Image -->
<p align="center">
  <img src="gitbanner.jpg" alt="Project Banner" width="100%">
</p>

# EcoSortNet — Waste Classification Using CNN

EcoSortNet is an AI-powered waste classification system that uses a Convolutional Neural Network (CNN) to categorize waste images into **Organic** and **Recyclable** types. The project includes a Flask backend API, a Streamlit frontend, and a trained TensorFlow/Keras model for real-time image classification.

---

## 📌 Problem Statement

Global waste generation continues to rise every year. In countries like India, where millions of tons of waste are produced annually, **organic waste** (food scraps, garden material, paper) and **inorganic waste** (plastics, metals, glass) are often mixed together. This leads to:

- Rapidly filling landfills  
- Soil, water, and air pollution  
- Health hazards for humans and animals  
- Inefficient recycling processes  

Manual segregation remains common—slow, unsafe, and inconsistent.  
**EcoSortNet aims to automate waste classification** using a CNN-based model to support cleaner and more sustainable waste management.

---

## 🧠 Project Overview

EcoSortNet classifies waste images into:

- **Organic**  
- **Recyclable**

The system includes:

- A trained CNN model  
- A Flask backend for processing predictions  
- A Streamlit frontend UI  
- A clean, GitHub-inspired interface design  

---

## ✨ Features

### 🔹 AI Model
- Convolutional Neural Network (CNN)
- Trained using Kaggle’s Waste Classification dataset

### 🔹 Backend (Flask)
- REST API for waste prediction
- Accepts image uploads and returns JSON

### 🔹 Frontend (Streamlit)
- Minimalist UI with clean components
- Real-time image upload and classification
- Smooth animations and modern result panel

---

## 📁 Project Structure

```
EcoSortNet/
│
├── backend/
│   ├── app.py               # Flask API backend
│   └── uploads/             # Temporary uploaded images
│
├── frontend/
│   └── app.py               # Streamlit frontend
│
├── model/
│   └── waste_model.h5       # Trained CNN model
│
├── dataset/                 # Kaggle dataset folder
│
├── train_model.py           # Model training script
├── requirements.txt
└── README.md
```

---

## 📥 Dataset

**Kaggle Dataset:**  
Waste Classification Data  
https://www.kaggle.com/datasets/techsash/waste-classification-data

Place the dataset inside:

```
/dataset/
```

---

## 🧠 Train the Model

```
python train_model.py
```

---

## 🚀 Run the Backend (Flask)

```
cd backend
pip install flask tensorflow pillow numpy
python app.py
```

Backend runs at:

```
http://127.0.0.1:5000
```

---

## 💻 Run the Frontend (Streamlit)

```
cd frontend
pip install streamlit requests pillow
streamlit run app.py
```

Frontend runs at:

```
http://localhost:8501
```

---

## 🧪 How to Use

1. Start the Flask backend.  
2. Run the Streamlit frontend.  
3. Upload an image (JPG/JPEG/PNG).  
4. Click **Classify Waste**.  
5. The prediction (Organic or Recyclable) is displayed instantly.

Temporary images are stored in:

```
backend/uploads/
```

---

## 📚 Weekly Progress

### **Week 1 — Libraries, Data Import, and Setup**
- Imported libraries and frameworks  
- Built project folder structure  
- Explored dataset  
- Notebook: *Week1-Libraries-Importing-Data-Setup.ipynb*

### **Week 2 — Model Training, Evaluation, Predictions**
- Trained CNN model  
- Evaluated performance metrics  
- Generated confusion matrix  
- Notebooks:  
  - *Week2-Model-Training-Evaluation-Predictions.ipynb*  

### **Week 3 — Streamlit App & Deployment (4–7 Feb 2025)**
- Built Streamlit UI  
- Deployed model on Kaggle & GitHub  
- Finalized documentation  

---

## 📦 Dependencies

- Python 3.10+  
- Flask  
- TensorFlow / Keras  
- Streamlit  
- Pillow  
- NumPy  
- Requests  

---

## 📄 License

This project is licensed under the **MIT License**.

