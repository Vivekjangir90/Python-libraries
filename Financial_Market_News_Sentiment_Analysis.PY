# Title of Project: Financial Market News Sentiment Analysis


import pandas as pd
import numpy as np
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Importing the data
data = pd.read_csv("financial_news.csv")

# Exploratory Data Analysis
print(data.head())
print(data.info())
print(data.describe())

# Data Preprocessing
nltk.download('stopwords')
nltk.download('wordnet')

stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

def preprocess_text(text):
    text = re.sub('[^a-zA-Z]', ' ', text)
    text = text.lower()
    text = text.split()
    text = [lemmatizer.lemmatize(word) for word in text if not word in stop_words]
    text = ' '.join(text)
    return text

data['preprocessed_text'] = data['text'].apply(preprocess_text)

# Define Features and Target variable
X = data['preprocessed_text']
y = data['sentiment']

# Train Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Text Vectorization
vectorizer = CountVectorizer()
X_train = vectorizer.fit_transform(X_train)
X_test = vectorizer.transform(X_test)

# Modeling
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Model Evaluation
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
confusion_matrix = confusion_matrix(y_test, y_pred)
classification_report = classification_report(y_test, y_pred)

print("Accuracy:", accuracy)
print("Confusion Matrix:")
print(confusion_matrix)
print("Classification Report:")
print(classification_report)

# Prediction
sample_text = "Earnings of XYZ Corporation beat market expectations, leading to a surge in stock prices."
sample_text = preprocess_text(sample_text)
sample_text_vectorized = vectorizer.transform([sample_text])
prediction = model.predict(sample_text_vectorized)

print("Predicted Sentiment:", prediction[0])
