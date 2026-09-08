# Sentiment Analysis: A Comparative Study 📈

This project compares three different machine learning models (Naive Bayes, Logistic Regression, and SVM) to determine the best approach for sentiment analysis on the DailyDialog dataset.

The **Support Vector Machine (SVM)**, combined with data augmentation, was identified as the optimal model, achieving **~81% accuracy**.

---

## 🚀 Project Overview

This repository contains three separate Jupyter Notebooks, each representing a different approach to the sentiment analysis task:

1.  **`NaiveBayes.ipynb`**: A baseline model using Multinomial Naive Bayes.
2.  **`Logistic_Regression.ipynb`**: A more robust model using Logistic Regression.
3.  **`SVM.ipynb`**: The optimal model, using a Linear Support Vector Machine with data augmentation to handle class imbalance.

### Key Steps in each Notebook:
* **Data Preprocessing**: Cleans the text (lowercase, punctuation removal) and maps nuanced emotion labels (like 'joy', 'sadness') to `positive`, `negative`, and `neutral`.
* **Feature Extraction**: Uses **TF-IDF (Term Frequency-Inverse Document Frequency)** to convert text sentences into numerical vectors.
* **Model Training**: Trains the respective classifier on the TF-IDF vectors.
* **Evaluation**: Assesses the model using Accuracy, Precision, Recall, and F1-Score.

---

## 📊 Results at a Glance

The SVM model provided the best balance of accuracy and performance, especially after its training data was augmented to help with class imbalance.

| Model | Overall Accuracy |
| :--- | :---: |
| **Support Vector Machine (SVM)** | **80.73%** |
| Logistic Regression | 80.63% |
| Naive Bayes | 72.24% |

---

## 🛠️ How to Run

You can run any of the notebooks in Google Colab or a local Jupyter environment.

1.  **Clone this repository:**
    ```sh
    git clone [https://github.com/YourUsername/YourRepoName.git](https://github.com/YourUsername/YourRepoName.git)
    ```

2.  **Install dependencies:**
    ```sh
    pip install pandas numpy scikit-learn matplotlib
    ```

3.  **Run a Notebook:**
    * Open `SVM.ipynb` (or any of the others) in Jupyter Notebook or Google Colab.
    * When the first cell prompts you to upload a file, please upload the `DailyDialog.csv` file.
    * Run the cells in order to see the data preprocessing, model training, and evaluation.
