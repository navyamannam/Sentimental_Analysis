📊 Sentiment Analysis using Machine Learning

A machine learning project for classifying conversational text into Positive, Negative, and Neutral sentiment categories using the DailyDialog dataset.

The project compares three traditional machine learning algorithms:

Multinomial Naive Bayes

Logistic Regression

Support Vector Machine (SVM)

A Streamlit web application is also provided for interactive sentiment prediction.

🚀 Live Demo

Try the deployed application here:

👉 Sentiment Analysis Web App

Replace the link above with your actual Streamlit deployment URL if it is different from your GitHub repository URL.

📌 Project Overview

Sentiment analysis is a Natural Language Processing (NLP) task that determines the emotional orientation of text.

In this project, conversational sentences from the DailyDialog dataset are converted into three sentiment classes:

Sentiment

Description

😊 Positive

Text expressing a positive or favorable attitude

😐 Neutral

Text expressing neither clearly positive nor negative sentiment

😞 Negative

Text expressing an unfavorable or negative attitude

The main objective is to compare multiple machine learning approaches and identify a model that performs effectively on conversational data.

🗂️ Dataset

The project uses the DailyDialog dataset, which contains multi-turn conversations representing everyday human communication.

The original emotion information is mapped into three broader sentiment categories:

Positive

Negative

Neutral

The dataset used in this project is available as:

DailyDialog.csv

🔄 Project Workflow

DailyDialog Dataset
        ↓
Data Cleaning
        ↓
Sentiment Label Mapping
        ↓
Text Preprocessing
        ↓
TF-IDF Feature Extraction
        ↓
Train / Test Split
        ↓
┌───────────────────────────────┐
│  Naive Bayes                  │
│  Logistic Regression          │
│  Support Vector Machine (SVM) │
└───────────────────────────────┘
        ↓
Model Evaluation
        ↓
Best Model Selection
        ↓
Streamlit Web Application
        ↓
Sentiment Prediction

The project workflow is also illustrated in Flow.png.

🧹 Data Preprocessing

The text data is processed before training the machine learning models.

The preprocessing pipeline includes:

Converting text to lowercase

Removing unnecessary punctuation and special characters

Cleaning the conversational text

Mapping the original emotion labels to sentiment categories

Converting text into numerical features using TF-IDF

🧮 Feature Extraction — TF-IDF

TF-IDF (Term Frequency–Inverse Document Frequency) is used to transform text into numerical feature vectors.

TF-IDF gives higher importance to words that are useful for distinguishing between documents while reducing the influence of very common words.

This representation is then supplied to the machine learning classifiers.

🤖 Machine Learning Models

1. Multinomial Naive Bayes

Naive Bayes is used as a baseline text-classification algorithm.

It is computationally efficient and commonly used for NLP classification tasks.

2. Logistic Regression

Logistic Regression is used as a strong linear classification model for the TF-IDF features.

It learns the relationship between words and the corresponding sentiment classes.

3. Support Vector Machine (SVM)

A linear SVM is used for high-dimensional text classification.

SVM was selected as the best-performing model in the comparative experiments.

📈 Model Performance

The comparative results from the project are:

Model

Accuracy

Weighted F1-Score

Naive Bayes

72.24%

69%

Logistic Regression

80.63%

80%

SVM

80.73%

80%

🏆 Best Model

Support Vector Machine (SVM) achieved the highest accuracy of approximately 80.73% among the tested models.

The model also showed improved performance for the positive and neutral classes after addressing the class imbalance through data augmentation.

📊 SVM Classification Report

Class

Precision

Recall

F1-Score

Negative

0.85

0.91

0.88

Neutral

0.72

0.71

0.71

Positive

0.77

0.61

0.68

Overall Accuracy: 80.73%

🖥️ Streamlit Application

The project includes an interactive Streamlit application where users can enter a sentence and obtain a sentiment prediction.

Example

Input:

I really enjoyed the movie.

Expected sentiment:

Positive

Another example:

Input:

I am not happy with the service.

Expected sentiment:

Negative

The Streamlit interface makes it possible to test the trained sentiment-analysis model without running the prediction code manually.

📁 Project Structure

Sentiment-Analysis-Project/
│
├── DailyDialog.csv
├── NaiveBayes.ipynb
├── Logistic_Regression.ipynb
├── SVM.ipynb
├── Flow.png
├── Model Comparision.png
├── ML_Report.pdf
├── app.py
├── requirements.txt
└── README.md

The exact files may vary depending on the final deployed version of the project.

⚙️ Installation

Clone the repository:

git clone https://github.com/YourUsername/Sentiment-Analysis-Project.git
cd Sentiment-Analysis-Project

Install the required Python packages:

pip install -r requirements.txt

If requirements.txt is not available, install the main dependencies:

pip install pandas numpy scikit-learn matplotlib streamlit

▶️ Run the Streamlit Application

Run:

streamlit run app.py

The application will open in your browser.

📓 Running the Notebooks

The project contains notebooks for the individual machine learning models:

NaiveBayes.ipynb
Logistic_Regression.ipynb
SVM.ipynb

They can be opened using:

Jupyter Notebook

JupyterLab

VS Code

Google Colab

🎯 Applications

This sentiment-analysis system can be used for:

Customer feedback analysis

Chat and conversation analysis

Social media sentiment monitoring

Market research

Customer-support analysis

Opinion mining

Conversational AI

🔮 Future Improvements

Possible future improvements include:

Using BERT or other Transformer models

Improving handling of negation such as "not bad"

Hyperparameter tuning

Better handling of class imbalance

Larger and more diverse datasets

Real-time sentiment monitoring

Improved probability/confidence calibration

Deployment with a production API

⚠️ Limitations

Traditional machine learning models based on TF-IDF primarily learn statistical relationships between words.

Therefore, they may have difficulty understanding:

Sarcasm

Context-dependent expressions

Negation

Mixed emotions

Very short sentences

Unseen vocabulary

For example, expressions such as "not bad" can sometimes be difficult for a traditional bag-of-words model because the model may give too much importance to individual words instead of understanding the complete phrase.

👨‍💻 Technologies Used

Python

Pandas

NumPy

Scikit-learn

Matplotlib

Jupyter Notebook

Streamlit

TF-IDF

Machine Learning

📚 Project Files

File

Description

DailyDialog.csv

Dataset

NaiveBayes.ipynb

Naive Bayes implementation

Logistic_Regression.ipynb

Logistic Regression implementation

SVM.ipynb

SVM implementation

Flow.png

Project workflow

Model Comparision.png

Model comparison visualization

ML_Report.pdf

Project report

app.py

Streamlit application

requirements.txt

Python dependencies

README.md

Project documentation

📜 License

This project is intended for educational and academic purposes.

⭐ Acknowledgement

The project uses the DailyDialog conversational dataset for experimentation with sentiment analysis and machine learning classification.

If you find this project useful, consider giving the repository a ⭐.
