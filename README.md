# 🔬 Skin Cancer Prediction with CNN

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/TensorFlow-CNN-orange?style=for-the-badge&logo=tensorflow&logoColor=white" />
  <img src="https://img.shields.io/badge/Streamlit-Deployed-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" />
  <img src="https://img.shields.io/badge/Deep%20Learning-Image%20Classification-purple?style=for-the-badge" />
</p>

<p align="center">
  <b>AI-Powered Skin Lesion Classification System</b>
  <br/>
  A deep learning application that classifies skin lesion images into Benign or Malignant using Convolutional Neural Networks (CNN).
</p>

<p align="center">
  <a href="https://skin-cancer-prediction-with-cnn-fc5wpmgvpef7a5npwaypz8.streamlit.app/">
    🚀 LIVE DEMO
  </a>
  &nbsp; | &nbsp;
  <a href="https://github.com/JoyAnalytica/Skin-Cancer-Prediction-with-CNN">
    📂 GitHub Repository
  </a>
</p>

---

## 📌 Project Overview

**DermaAI** is a deep learning-based web application designed to classify skin lesion images into two categories: **Benign** and **Malignant**.

Built using a Convolutional Neural Network (CNN), the application analyzes uploaded skin images and generates predictions with confidence scores through an interactive Streamlit interface.

## ✨ Key Features

- 🧠 CNN-based image classification
- 📤 Upload skin lesion images
- 🔍 Automatic image preprocessing
- 📊 Prediction with confidence scores
- 🎯 Benign and Malignant classification
- ⚡ Interactive Streamlit web application

## 🎯 Prediction Classes

| Class | Description |
|---|---|
| 🟢 Benign | Non-cancerous skin lesion |
| 🔴 Malignant | Cancerous skin lesion |

## 📊 Model Performance

Evaluated on a separate test dataset.

| Metric | Score |
|---|---:|
| Balanced Accuracy | 88.85% |

**Confusion Matrix**

| Actual / Predicted | Benign | Malignant |
|---|---:|---:|
| Benign | 852 | 148 |
| Malignant | 75 | 925 |

## 🛠️ Tech Stack

- Python
- TensorFlow & Keras
- Convolutional Neural Network (CNN)
- NumPy
- Pillow
- Streamlit

## 🔄 Application Workflow

1. Upload a skin lesion image.
2. Preprocess and normalize the image.
3. Extract image features using CNN.
4. Generate the prediction.
5. Display the predicted class and confidence score.

## 🚀 Live Application

<p align="center">
  <a href="https://skin-cancer-prediction-with-cnn-fc5wpmgvpef7a5npwaypz8.streamlit.app/">
    <img src="https://img.shields.io/badge/OPEN%20LIVE%20APP-Click%20Here-success?style=for-the-badge&logo=streamlit" />
  </a>
</p>

## ⚙️ Run Locally

**1. Clone the repository**

```bash
git clone https://github.com/JoyAnalytica/Skin-Cancer-Prediction-with-CNN.git
```

**2. Open project directory**

```bash
cd Skin-Cancer-Prediction-with-CNN
```

**3. Install dependencies**

```bash
pip install -r requirements.txt
```

**4. Run the application**

```bash
streamlit run main.py
```

## ⚠️ Medical Disclaimer

This project is developed for educational and research purposes only. It is not a clinically validated diagnostic tool and should not replace professional medical advice or diagnosis. Always consult a qualified dermatologist for medical concerns.

## 👨‍💻 Author

**Joy Sarker**

Aspiring Data Analyst | Machine Learning & Deep Learning Enthusiast

- GitHub: [@JoyAnalytica](https://github.com/JoyAnalytica)

---

<p align="center">
  ⭐ If you find this project useful, please consider giving it a star!
  <br
  ⭐ If you find this project interesting, consider giving it a star!
  <br/>
  <b>Built with ❤️ using Python, TensorFlow & Streamlit</b>
</p>
