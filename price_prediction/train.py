import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.model_selection import RandomizedSearchCV
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.preprocessing import LabelEncoder
import pickle

# Load and preprocess the data
df = pd.read_csv('myFile0.csv')

job_title_le = LabelEncoder()
car_use_le = LabelEncoder()
postcode_le = LabelEncoder()

df['job_title'] = job_title_le.fit_transform(df['job_title'])
df['car_use'] = car_use_le.fit_transform(df['car_use'])
df['postcode'] = postcode_le.fit_transform(df['postcode'])
df['previous_claims'] = df['previous_claims'].map({'yes': 1, 'no': 0})

# Define features and target variable
X = df[['job_title', 'car_use', 'total_miles', 'previous_claims', 'postcode', 'credit_score']]
y = df['cheapest_quote']

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Define parameter grid
param_grid = {
    'n_estimators': np.linspace(10, 200).astype(int),
    'max_depth': [None] + list(np.linspace(3, 20).astype(int)),
    'max_features': ['auto', 'sqrt', None] + list(np.arange(0.5, 1, 0.1)),
    'max_leaf_nodes': [None] + list(np.linspace(10, 50, 500).astype(int)),
    'min_samples_split': [2, 5, 10],
    'bootstrap': [True, False]
}

# Define model
estimator = RandomForestRegressor(random_state=42)

# Define search
rf_random = RandomizedSearchCV(estimator, param_grid, cv=5, n_jobs=-1)

# Fit model
rf_random.fit(X_train, y_train)

# Predict
y_pred = rf_random.predict(X_test)

# Print the best parameters
print("Best Parameters: ", rf_random.best_params_)

# Print the feature importance
importances = rf_random.best_estimator_.feature_importances_
for feature, importance in zip(X.columns, importances):
    print(f"Feature: {feature}, Importance: {importance}")

# Print model evaluation metrics
print("MAE: ", mean_absolute_error(y_test, y_pred))
print("MSE: ", mean_squared_error(y_test, y_pred))
print("RMSE: ", np.sqrt(mean_squared_error(y_test, y_pred)))
print("R^2 Score: ", r2_score(y_test, y_pred))

# Plot true vs predicted values
plt.scatter(y_test, y_pred)
plt.xlabel('True Values')
plt.ylabel('Predicted Values')
plt.title('True vs Predicted Values')
plt.show()

# Plot the histogram of residuals
sns.histplot(y_test - y_pred, bins=30)
plt.title('Histogram of Residuals')
plt.show()

# Save the model
pickle.dump(rf_random, open('model.pkl', 'wb'))
pickle.dump(job_title_le, open("job_title_le.pkl", "wb"))
pickle.dump(car_use_le, open("car_use_le.pkl", "wb"))
pickle.dump(postcode_le, open("postcode_le.pkl", "wb"))