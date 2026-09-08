📊 Sentiment Analysis — Comparative Study

A machine learning project that compares Naive Bayes, Logistic Regression, and Support Vector Machine (SVM) models for sentiment classification using the DailyDialog dataset.

The project performs text preprocessing, TF-IDF feature extraction, model training, evaluation, and sentiment prediction. A Streamlit application provides an interactive interface for the final model.

🌐 Live Demo

🚀 Try the deployed Streamlit application:

https://sentimentalanalysis-2e2iguxmqlkgehxkxe2p3b.streamlit.app/

📌 Project Overview

Sentiment analysis is the task of identifying the emotional tone of a piece of text.

This project compares three machine learning algorithms:

Multinomial Naive Bayes

Logistic Regression

Support Vector Machine (SVM)

The models classify text into three sentiment categories:

😊 Positive

😐 Neutral

😞 Negative

After comparing the models, SVM achieved the best overall performance in this project.

✨ Features

Text preprocessing and cleaning

Sentiment label mapping

TF-IDF based feature extraction

Training with multiple machine learning algorithms

Model comparison using accuracy

Evaluation using precision, recall, and F1-score

Data augmentation for the SVM model

Interactive sentiment prediction through Streamlit

Sample dataset included in the repository

📊 Model Performance

The models were evaluated on the DailyDialog dataset.

Model

Accuracy

🥇 Support Vector Machine (SVM)

80.73%

🥈 Logistic Regression

80.63%

🥉 Naive Bayes

72.24%

Best Model

The Support Vector Machine (SVM) model achieved the highest accuracy of approximately 80.73% and provided the best overall balance among the tested approaches.

🧠 Machine Learning Workflow

DailyDialog Dataset
        ↓
Data Cleaning
        ↓
Emotion → Sentiment Mapping
        ↓
Text Preprocessing
        ↓
TF-IDF Vectorization
        ↓
Train / Test Split
        ↓
Model Training
   ┌────┼───────────────┐
   ↓    ↓               ↓
Naive  Logistic         SVM
Bayes  Regression
   └────┼───────────────┘
        ↓
Model Evaluation
        ↓
Best Model Selection
        ↓
Sentiment Prediction
        ↓
Streamlit Web Application

📂 Project Structure

Sentimental_Analysis-main/
│
├── DailyDialog.csv
├── NaiveBayes.ipynb
├── Logistic_Regression.ipynb
├── SVM.ipynb
├── Comparision.png
├── Flowchart (1).png
├── ML_Report_merged.pdf
└── README.md

Files

File

Description

DailyDialog.csv

Dataset used for sentiment analysis

NaiveBayes.ipynb

Naive Bayes implementation

Logistic_Regression.ipynb

Logistic Regression implementation

SVM.ipynb

SVM implementation with data augmentation

Comparision.png

Model comparison visualization

Flowchart (1).png

Project workflow/flowchart

ML_Report_merged.pdf

Detailed project report

README.md

Project documentation

🛠️ Technologies Used

Programming Language

Python

Machine Learning

Scikit-learn

Naive Bayes

Logistic Regression

Support Vector Machine (SVM)

Data Processing

Pandas

NumPy

Regular Expressions

NLP / Feature Extraction

TF-IDF Vectorization

Text preprocessing

Sentiment label mapping

Visualization

Matplotlib

Deployment

Streamlit

Streamlit Community Cloud

Development Environment

Jupyter Notebook

Google Colab

Visual Studio Code

Git

GitHub

🚀 How to Run the Project

1. Clone the repository

git clone <YOUR_GITHUB_REPOSITORY_URL>
cd Sentimental_Analysis-main

Replace <YOUR_GITHUB_REPOSITORY_URL> with your GitHub repository URL.

2. Install the required Python libraries

pip install pandas numpy scikit-learn matplotlib

3. Run the notebooks

You can open the notebooks using Jupyter Notebook or Google Colab.

For example:

jupyter notebook

Then open:

SVM.ipynb

You can also run:

NaiveBayes.ipynb

Logistic_Regression.ipynb

4. Dataset

The notebooks use:

DailyDialog.csv

The notebooks are designed to work with the dataset included in this repository.

🔍 Sentiment Classification

The project maps the original emotion labels from the DailyDialog dataset into three broader sentiment categories:

Positive
Neutral
Negative

The text is then cleaned and converted into numerical features using TF-IDF (Term Frequency–Inverse Document Frequency).

These features are used to train the machine learning classifiers.

📈 Evaluation Metrics

The models are evaluated using:

Accuracy

Precision

Recall

F1-Score

Classification Report

These metrics help compare the models beyond accuracy alone.

🌐 Streamlit Deployment

The sentiment analysis application is deployed using Streamlit Community Cloud.

Live Application

https://sentimentalanalysis-2e2iguxmqlkgehxkxe2p3b.streamlit.app/

The deployed application provides an interactive way to enter text and obtain a predicted sentiment.

📸 Project Workflow

The repository also contains:

Flowchart (1).png — project workflow

Comparision.png — model performance comparison

These files provide a visual overview of the machine learning pipeline and model results.

🎯 Future Enhancements

Possible improvements include:

Use transformer-based models such as BERT

Improve handling of class imbalance

Add more NLP preprocessing techniques

Add confidence scores to predictions

Support multiple languages

Add sentiment visualization

Improve the Streamlit user interface

Deploy additional trained models for comparison

Add automated model retraining

👩‍💻 Author

Navya Mannam

GitHub:
https://github.com/navyamannam

📄 License

This project is created for educational and demonstration purposes.
    * When the first cell prompts you to upload a file, please upload the `DailyDialog.csv` file.
    * Run the cells in order to see the data preprocessing, model training, and evaluation.
