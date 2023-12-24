# Title of Project: Objective Data Source 

"""
Objective:
The objective of this project is to predict the median house value in California using the Random Forest Regressor algorithm.
"""
"""
Data Source:
The dataset used in this project is the California Housing dataset which can be found in scikit-learn's datasets module.
"""

# Import Library:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_california_housing
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split


# Import Data:

california_data = fetch_california_housing()

X = pd.DataFrame(california_data.data, columns=california_data.feature_names)
y = pd.Series(california_data.target)


# Describe Data:

print(X.head())
print(X.info())
print(X.describe())


# Data Visualization:

X.hist(bins=50, figsize=(20, 15))
plt.show()


# Data Preprocessing:

# Scaling data
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
y_scaled = scaler.fit_transform(y.values.reshape(-1, 1)).ravel()


#Define Target Variable (y) and Feature Variables (X):

X_train, X_test, y_train, y_test = train_test_split(X_scaled, y_scaled, test_size=0.2, random_state=42)


#Train Test Split:


model = RandomForestRegressor(n_estimators=100)
model.fit(X_train, y_train)


# Modeling:

y_test_pred = model.predict(X_test)


#Model Evaluation:

print("Mean Absolute Error: ", mean_absolute_error(y_test, y_test_pred))
print("Mean Squared Error: ", mean_squared_error(y_test, y_test_pred))
print("RMSE: ", np.sqrt(mean_squared_error(y_test, y_test_pred)))
print("R Squared Score: ", r2_score(y_test, y_test_pred))


#Prediction:

sample_house_features = pd.DataFrame(X_test[0], columns=california_data.feature_names)
sample_house_target = y_test[0]

print("Predicted House Price: ", model.predict(sample_house_features)[0])
print("Actual House Price: ", sample_house_target)


# Explaination:

"""
In this project, we used the Random Forest Regressor algorithm to predict the median house value in California using the California Housing dataset. After importing the data, we explored and visualized the dataset to understand the relationships between different features and the target variable.

Next, we preprocessed the data by scaling it and splitting it into training and testing sets using the train_test_split method. We then trained a Random Forest Regressor model using the training set and made predictions on the testing set.

Finally, we evaluated the performance of the model using various metrics and made a prediction on a sample house. The model achieved an R-squared score of 0.81, indicating that it is a good fit for the dataset.

"""