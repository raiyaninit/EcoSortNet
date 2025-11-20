♻️ EcoSortNet — Waste Classification Using CNN

EcoSortNet is an AI-powered waste classification system that uses a Convolutional Neural Network (CNN) to categorize waste images into Organic and Recyclable categories.
The project includes a Flask backend API, a Streamlit frontend, and a trained TensorFlow/Keras model that provides real-time image classification.

🌍 Problem Statement

Global waste generation continues to increase each year. In India, where millions of tons of waste are produced annually, organic waste (food scraps, garden waste, paper) and inorganic waste (plastics, metal, glass) are often mixed. This leads to:

Rapidly filling landfills

Soil, water, and air pollution

Health hazards for humans and animals

Inefficient recycling processes

Manual segregation is still widely used—slow, unsafe, and inconsistent.
EcoSortNet aims to automate waste segregation using a CNN-based classification model to support cleaner and more sustainable waste management.

🧠 Project Overview

EcoSortNet uses a TensorFlow/Keras CNN model trained on real-world waste images to classify them into:

Organic

Recyclable

The system provides:

Fast and accurate predictions

A user-friendly Streamlit interface

A robust Flask backend for image processing

A clean UI inspired by GitHub’s modern design style

✨ Features
AI Model

CNN-based waste classifier

Trained on Kaggle’s Waste Classification dataset

Backend (Flask)

REST API for predictions

Accepts image uploads and returns JSON results

Frontend (Streamlit)

Minimalistic GitHub-style theme

Smooth UI interactions and custom styling

Real-time image upload and classification

Clear and professional results panel

📁 Project Structure
EcoSortNet/
│
├── backend/
│   ├── app.py               # Flask API backend
│   └── uploads/             # Temp folder for uploaded images
│
├── frontend/
│   └── app.py               # Streamlit frontend
│
├── model/
│   └── waste_model.h5       # Trained CNN model
│
├── dataset/                 # Kaggle dataset goes here
│
├── train_model.py           # Model training script
├── requirements.txt
└── README.md

📥 Dataset

Kaggle Dataset:
Waste Classification Data
https://www.kaggle.com/datasets/techsash/waste-classification-data

Place the downloaded dataset folders inside:

/dataset/

🧠 Train the Model
python train_model.py

🚀 Run the Backend (Flask)
cd backend
pip install flask tensorflow pillow numpy
python app.py


Runs at:

http://127.0.0.1:5000

💻 Run the Frontend (Streamlit)
cd frontend
pip install streamlit requests pillow
streamlit run app.py


Access at:

http://localhost:8501

🧪 How to Use

Launch the Flask backend.

Start the Streamlit frontend.

Upload an image (JPG/JPEG/PNG).

Click Classify Waste.

The model predicts whether the waste is Organic or Recyclable.

Temporary images are stored in:

backend/uploads/

📚 Weekly Progress

Week 1: Libraries, Data Import, and Setup

Imported required libraries and frameworks

Set up folder structure and environment

Explored dataset

Notebook: Week1-Libraries-Importing-Data-Setup.ipynb

Week 2: Model Training, Evaluation, and Predictions

Trained CNN model

Evaluated accuracy & loss

Visualized confusion matrix

Notebooks:

Week2-Model-Training-Evaluation-Predictions.ipynb

Kaggle Notebook

Week 3: Streamlit App and Deployment

Developed Streamlit UI

Deployed model on Kaggle and GitHub

Completed documentation and README

📦 Dependencies

Python 3.10+

Flask

TensorFlow / Keras

Streamlit

Pillow

NumPy

Requests

📄 License

This project is licensed under the MIT License.