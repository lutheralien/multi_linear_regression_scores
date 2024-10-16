import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import numpy as np

# Read the CSV file
df = pd.read_csv('student-mat.csv', sep=',')

# Select relevant features
features = ['age', 'absences', 'studytime']
target = 'G3'  # Final grade

X = df[features]
y = df[target]

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Calculate the mean squared error
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse:.2f}")

# Print the coefficients
for feature, coef in zip(features, model.coef_):
    print(f"{feature}: {coef:.2f}")

# Function to get user input and make predictions
def predict_score():
    print("\nEnter student details:")
    age = float(input("Age: "))
    absences = float(input("Number of absences: "))
    study_time = float(input("Study time (hours per week): "))

    # Make prediction
    input_data = pd.DataFrame([[age, absences, study_time]], columns=features)
    predicted_score = model.predict(input_data)[0]

    print(f"\nPredicted score: {predicted_score:.2f}")

    # Save prediction to file
    with open('student_score_predictions.txt', 'a') as f:
        f.write(f"Age: {age}, Absences: {absences}, Study Time: {study_time}\n")
        f.write(f"Predicted Score: {predicted_score:.2f}\n\n")

    print("Prediction saved to student_score_predictions.txt")

# Run the prediction function
predict_score()

# Allow multiple predictions
while True:
    another = input("\nPredict another score? (y/n): ").lower()
    if another != 'y':
        break
    predict_score()