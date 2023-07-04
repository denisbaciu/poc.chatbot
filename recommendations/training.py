import pandas as pd
from sklearn.preprocessing import LabelEncoder, MinMaxScaler
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier, plot_importance
from sklearn.metrics import accuracy_score, classification_report
import joblib
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv('myFile0.csv')

# Encode categorical variables
le = LabelEncoder()
df['profession'] = le.fit_transform(df['profession'])

# Normalize numerical features
scaler = MinMaxScaler()
df[['annual_salary', 'months_ago_quoted']] = scaler.fit_transform(df[['annual_salary', 'months_ago_quoted']])

# Separate features and target
X = df.drop('needs_house_insurance', axis=1)
y = df['needs_house_insurance']

# Drop 'id'
X = X.drop('id', axis=1, errors='ignore')

# Split the dataset into training set and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=7)

# Define the model
model = XGBClassifier()

# Train the model
model.fit(X_train, y_train)

# Save the model to disk
joblib.dump(model, 'xgboost_model.pkl')
joblib.dump(le, 'label_encoder.pkl')
joblib.dump(scaler, 'scaler.pkl')

# Make predictions for test data
y_pred = model.predict(X_test)
predictions = [round(value) for value in y_pred]

# Evaluate predictions
accuracy = accuracy_score(y_test, predictions)
print("Accuracy: %.2f%%" % (accuracy * 100.0))
print(classification_report(y_test, predictions))

# Feature importance
plot_importance(model)
plt.show()
