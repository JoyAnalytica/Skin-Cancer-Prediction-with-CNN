# Skin-Cancer-Prediction-with-CNN

# 🔬 DermaAI — Skin Cancer Prediction with CNN

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/TensorFlow-CNN-orange?style=for-the-badge&logo=tensorflow&logoColor=white" />
  <img src="https://img.shields.io/badge/Streamlit-Web%20App-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" />
  <img src="https://img.shields.io/badge/Deep%20Learning-Image%20Classification-purple?style=for-the-badge" />
</p>

<p align="center">
  <b>AI-Powered Skin Lesion Classification System</b>
  <br/>
  An intelligent image classification project built using Convolutional Neural Networks (CNN).
</p>

<p align="center">
  <a href="YOUR_DEPLOYED_APP_URL">🚀 Live Demo</a> •
  <a href="https://github.com/JoyAnalytica/Skin-Cancer-Prediction-with-CNN">📂 GitHub Repository</a>
</p>

---

## 📌 Project Overview

**DermaAI** is a deep learning-based web application designed to classify skin lesion images into two categories: **Benign** and **Malignant**.

The project uses a Convolutional Neural Network (CNN) to analyze uploaded skin images and generate predictions with confidence scores.

The application provides a simple and interactive interface where users can upload an image and view the model's prediction instantly.

## ✨ Key Features

- 🧠 CNN-based skin lesion image classification.
- 📤 Upload skin images in JPG, JPEG, and PNG formats.
- 🔍 Automatic image preprocessing and normalization.
- 📊 Prediction results with confidence scores.
- 📈 Class probability visualization.
- 🎨 Modern and responsive Streamlit interface.
- ⚡ Real-time model inference.

## 🎯 Prediction Classes

| Class | Description |
|---|---|
| 🟢 Benign | Non-cancerous skin lesion |
| 🔴 Malignant | Cancerous skin lesion |

## 📊 Model Performance

The CNN model was evaluated using a separate test dataset.

| Evaluation Metric | Score |
|---|---:|
| Accuracy | 88.85% |
| Balanced Accuracy | 88.85% |

**Confusion Matrix**

| Actual / Predicted | Benign | Malignant |
|---|---:|---:|
| Benign | 852 | 148 |
| Malignant | 75 | 925 |

## 🛠️ Technology Stack

- **Programming:** Python
- **Deep Learning:** TensorFlow, Keras
- **Image Processing:** NumPy, Pillow
- **Web Framework:** Streamlit
- **Model:** Convolutional Neural Network (CNN)
- **Deployment:** Streamlit Cloud / Hosting Platform

## 🖥️ Application Workflow

1. Upload a skin lesion image.
2. The application preprocesses the image.
3. The CNN model analyzes image features.
4. The model predicts Benign or Malignant.
5. The application displays the prediction and confidence score.

## 📂 Project Structure

```text
Skin-Cancer-Prediction-with-CNN/
│
├── main.py
├── cnn_model.keras
├── requirements.txt
└── README.md
```

## ⚙️ Installation & Setup

**1. Clone the repository**

```bash
git clone https://github.com/JoyAnalytica/Skin-Cancer-Prediction-with-CNN.git
```

**2. Navigate to the project directory**

```bash
cd Skin-Cancer-Prediction-with-CNN
```

**3. Install dependencies**

```bash
pip install -r requirements.txt
```

**4. Run the Streamlit application**

```bash
streamlit run main.py
```

**5. Open in your browser**

```text
http://localhost:8501
```

## ⚠️ Medical Disclaimer

This project is developed for educational and research purposes only.

It is not a clinically validated medical diagnostic tool. Model predictions may contain errors and should never replace professional medical advice, diagnosis, or treatment.

Always consult a qualified dermatologist regarding skin health concerns.

## 👨‍💻 Author

**Joy Sarker**

Aspiring Data Analyst | Machine Learning & Deep Learning Enthusiast

- GitHub: [@JoyAnalytica](https://github.com/JoyAnalytica)

---

<p align="center">
  ⭐ If you find this project interesting, consider giving it a star!
  <br/>
  <b>Built with ❤️ using Python, TensorFlow & Streamlit</b>
</p>
