import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score

st.set_page_config(
    page_title="Sentiment Analysis",
    page_icon="😊",
    layout="centered"
)

st.title("😊 Sentiment Analysis")
st.write("Enter a sentence and the model will predict its sentiment.")

@st.cache_resource
def train_model():
    df = pd.read_csv("DailyDialog.csv")

    df = df.dropna(subset=["text", "sentiment"])
    df["text"] = df["text"].astype(str)
    df["sentiment"] = df["sentiment"].astype(str)

    X = df["text"]
    y = df["sentiment"]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )

    model = Pipeline([
        ("tfidf", TfidfVectorizer(
            max_features=10000,
            stop_words="english"
        )),
        ("classifier", LogisticRegression(
            max_iter=1000
        ))
    ])

    model.fit(X_train, y_train)

    accuracy = accuracy_score(y_test, model.predict(X_test))

    return model, accuracy


with st.spinner("Training the model..."):
    model, accuracy = train_model()

st.success(f"Model accuracy: {accuracy * 100:.2f}%")

st.subheader("Enter text")

user_text = st.text_area(
    "Type your sentence here:",
    placeholder="Example: I am very happy today!"
)

if st.button("Predict Sentiment"):
    if user_text.strip():
        prediction = model.predict([user_text])[0]

        st.success(f"Predicted Sentiment: **{prediction}**")

        probabilities = model.predict_proba([user_text])[0]
        classes = model.classes_

        result = pd.DataFrame({
            "Sentiment": classes,
            "Probability": probabilities
        })

        result = result.sort_values(
            "Probability",
            ascending=False
        )

        st.subheader("Prediction probabilities")
        st.dataframe(result, use_container_width=True)

        st.bar_chart(
            result.set_index("Sentiment")["Probability"]
        )

    else:
        st.warning("Please enter some text.")