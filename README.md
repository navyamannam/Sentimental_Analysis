🧠 Sentiment Analysis Using Machine Learning

A Machine Learning and NLP project that classifies text into Positive, Negative, or Neutral sentiment.

📌 Project Overview

This project performs Sentiment Analysis on the DailyDialog dataset using Natural Language Processing (NLP) and Machine Learning techniques.

The system classifies text into:

🟢 Positive | 🔴 Negative | ⚪ Neutral

Three machine learning models are implemented and compared:

Support Vector Machine (SVM)
Logistic Regression
Naive Bayes
🎯 Objectives
Perform text preprocessing and cleaning.
Convert text into numerical features using TF-IDF.
Train different Machine Learning models.
Compare model performance.
Predict sentiment for new text.
🔄 Project Workflow
Dataset
   ↓
Data Preprocessing
   ↓
TF-IDF Feature Extraction
   ↓
Train-Test Split
   ↓
Model Training
   ↓
Sentiment Prediction
   ↓
Model Evaluation
📂 Dataset

The project uses the DailyDialog dataset, which contains everyday human conversations.

The sentiment classes are:

Sentiment	Label
🔴 Negative	0
⚪ Neutral	1
🟢 Positive	2
🛠️ Technologies Used
Technology	Purpose
🐍 Python	Programming
🐼 Pandas	Data processing
🔢 NumPy	Numerical operations
🤖 Scikit-learn	Machine Learning
📊 Matplotlib	Visualization
📝 NLP	Text processing
📓 Jupyter Notebook	Model development
🧹 Text Preprocessing

The following preprocessing steps are performed:

Convert text to lowercase
Remove punctuation and special characters
Clean the text data
Convert text into numerical features using TF-IDF
TF-IDF

TF-IDF (Term Frequency-Inverse Document Frequency) is used to transform text into numerical feature vectors for machine learning.

🤖 Machine Learning Models
1. Support Vector Machine (SVM)

Used to classify text into the three sentiment categories.

2. Logistic Regression

Used as a linear classification model for sentiment prediction.

3. Naive Bayes

Used as a probabilistic classification model.

📊 Model Performance
🏆 Model	🎯 Accuracy
SVM	80.73%
Logistic Regression	80.63%
Naive Bayes	72.24%
🥇 Best Model: SVM

The SVM model achieved the highest accuracy of 80.73% among the three models.

📈 SVM Classification Report
Class	Precision	Recall	F1-Score
🔴 Negative	0.85	0.91	0.88
⚪ Neutral	0.72	0.71	0.71
🟢 Positive	0.77	0.61	0.68

Overall Accuracy: 80.73%

📁 Project Structure
Sentiment-Analysis/
│
├── 📄 DailyDialog.csv
├── 📓 NaiveBayes.ipynb
├── 📓 Logistic_Regression.ipynb
├── 📓 SVM.ipynb
├── 🖼️ Flow.png
├── 🖼️ Model Comparision.png
├── 📑 ML_Report.pdf
└── 📘 README.md
▶️ How to Run
Step 1: Clone the Repository
git clone https://github.com/navyamannam/Sentimental_Analysis.git
Step 2: Open the Project
cd Sentimental_Analysis
Step 3: Install Required Libraries
pip install pandas numpy scikit-learn matplotlib jupyter
Step 4: Run the Notebook

Open the project in VS Code or Jupyter Notebook and run:

SVM.ipynb
Logistic_Regression.ipynb
NaiveBayes.ipynb
📌 Results

The project successfully performs sentiment classification using Machine Learning.

SVM → 80.73% Accuracy 🏆

This shows that TF-IDF combined with traditional Machine Learning algorithms can effectively classify text sentiment.

🚀 Future Enhancements
Improve model accuracy using larger datasets.
Implement LSTM, BERT, and other Deep Learning models.
Improve detection of mixed and complex sentiments.
Deploy the model as a web application.
Add real-time sentiment prediction.
