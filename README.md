# 📧 Spam Email Detection using Machine Learning

A Machine Learning and Natural Language Processing (NLP) project that classifies email messages as **Spam** or **Not Spam (Ham)**. The project includes a trained machine learning model and an interactive Streamlit web application for real-time spam detection.

---

## 🚀 Live Demo

🔗 https://spam-email-detection-saurabh12.streamlit.app/

---

## 📌 Project Overview

Spam Email Detection is a text classification project that uses Natural Language Processing (NLP) and Machine Learning algorithms to identify whether an email message is spam or legitimate.

The project demonstrates the complete Machine Learning pipeline, including:

- Text preprocessing
- Data cleaning
- Feature extraction using TF-IDF
- Model training
- Performance evaluation
- Streamlit deployment

---

## ✨ Features

- 📧 Detect Spam and Legitimate Emails
- 🤖 Machine Learning-Based Classification
- 📝 Text Preprocessing with NLP
- ⚡ Real-Time Prediction
- 🌐 Interactive Streamlit Web App
- 💾 Saved Model using Joblib/Pickle
- 🚀 Ready for Streamlit Cloud Deployment

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- NLTK
- Streamlit
- Joblib / Pickle
- Matplotlib
- Seaborn

---

## 📂 Project Structure

```
Spam_Email_Detection/
│
├── spam_email_detection.py      # Streamlit Application
├── spam_model.pkl               # Trained ML Model
├── vectorizer.pkl               # TF-IDF Vectorizer
├── spam.csv                     # Dataset
├── requirements.txt
├── README.md
└── images/
    └── preview.png
```

---

## 📊 Dataset

The dataset contains email messages labeled as:

| Label | Description |
|-------|-------------|
| Ham | Legitimate Email |
| Spam | Unwanted Promotional or Fraudulent Email |

---

## ⚙️ Machine Learning Workflow

1. Data Collection
2. Data Cleaning
3. Text Preprocessing
4. Tokenization
5. Stopword Removal
6. Stemming/Lemmatization *(if applied)*
7. TF-IDF Vectorization
8. Model Training
9. Model Evaluation
10. Deployment using Streamlit

---

## ▶️ Installation

### Clone the Repository

```bash
git clone https://github.com/Saurabhgiri475/Spam_Email_Detection.git
```

### Navigate to the Project Folder

```bash
cd Spam_Email_Detection
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Streamlit App

```bash
streamlit run spam_email_detection.py
```

---

## 📈 Model Evaluation

The model is evaluated using:

- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix

---

## 💻 Example

**Input**

```
Congratulations! You have won a free iPhone.
Click the link below to claim your reward.
```

**Prediction**

```
🚨 Spam Email
```

---

**Input**

```
Hi Team,

Please find today's meeting agenda attached.
Regards,
Manager
```

**Prediction**

```
✅ Not Spam (Ham)
```

---

## 📷 Application Preview

Add screenshots after deployment.

Example:

```
images/home.png
images/prediction.png
```

---

## 📦 Requirements

```text
streamlit
pandas
numpy
scikit-learn
nltk
joblib
matplotlib
seaborn
```

---

## 🔮 Future Enhancements

- Deep Learning (LSTM/Bi-LSTM)
- BERT-based Spam Detection
- Explainable AI (SHAP/LIME)
- Email Subject Analysis
- Attachment Detection
- Phishing Detection
- REST API Integration
- Docker Deployment

---

## 👨‍💻 Author

**Saurabh Giri**

B.Tech Computer Science Engineering

GitHub:

https://github.com/Saurabhgiri475

LinkedIn:

https://www.linkedin.com/in/saurabh-giri-3aaa16300

---

## ⭐ Support

If you found this project useful, please give it a ⭐ on GitHub.

---

## 📄 License

This project is licensed under the MIT License.
