# Title of Project: Hill and Valley Prediction with Logistic Regression


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, classification_report

# Importing the data
data = pd.read_csv("hill_valley_dataset.csv")

# Exploratory Data Analysis
print(data.head())
print(data.info())
print(data.describe())

# Data Visualization
plt.scatter(data['attribute1'], data['attribute2'], c=data['class'], cmap='viridis')
plt.xlabel('Attribute 1')
plt.ylabel('Attribute 2')
plt.title('Hill and Valley Data Points')
plt.show()

# Data Preprocessing
X = data.drop('class', axis=1)
y = data['class']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Modeling
model = LogisticRegression()
model.fit(X_train, y_train)

# Model Evaluation
y_pred = model.predict(X_test)
confusion_matrix = confusion_matrix(y_test, y_pred)
classification_report = classification_report(y_test, y_pred)
accuracy = model.score(X_test, y_test)

print("Confusion Matrix:")
print(confusion_matrix)
print("Classification Report:")
print(classification_report)
print("Accuracy:", accuracy)

# Prediction
sample_data = [[0.5, 0.2]]  # Example input data point
prediction = model.predict(sample_data)

if prediction[0] == 1:
    print("The data point represents a hill.")
else:
    print("The data point represents a valley.")
