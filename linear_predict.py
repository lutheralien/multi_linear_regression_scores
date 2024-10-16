import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import numpy as np
import os

def load_data():
    while True:
        file_path = input("Enter the path to your CSV file: ")
        if os.path.exists(file_path) and file_path.endswith('.csv'):
            try:
                df = pd.read_csv(file_path)
                print("File loaded successfully.")
                return df
            except Exception as e:
                print(f"Error reading the file: {str(e)}")
                print("Please make sure the file is a valid CSV and try again.")
        else:
            print("File not found or incorrect file name. Please ensure the file exists and has a .csv extension.")

def select_columns(df):
    print("\nAvailable columns:", df.columns.tolist())
    
    features = []
    while True:
        feature = input("Enter a feature column name (or press Enter if done): ").strip()
        if feature == "":
            break
        if feature in df.columns:
            features.append(feature)
        else:
            print(f"Column '{feature}' not found. Please try again.")
    
    while True:
        target = input("Enter the target column name: ").strip()
        if target in df.columns:
            return features, target
        else:
            print(f"Column '{target}' not found. Please try again.")

def predict_score(model, features, df):
    print("\nEnter details:")
    input_data = {}
    for feature in features:
        while True:
            try:
                value = float(input(f"{feature}: "))
                input_data[feature] = value
                break
            except ValueError:
                print("Please enter a numeric value.")

    input_df = pd.DataFrame([input_data])
    predicted_score = model.predict(input_df)[0]

    print(f"\nPredicted score: {predicted_score:.2f}")

    with open('predictions.txt', 'a') as f:
        f.write("=" * 50 + "\n")
        f.write("New Prediction\n")
        f.write("=" * 50 + "\n")
        f.write("Input:\n")
        for feature, value in input_data.items():
            f.write(f"  {feature}: {value}\n")
        f.write("-" * 30 + "\n")
        f.write(f"Predicted Score: {predicted_score:.2f}\n")
        f.write("=" * 50 + "\n\n")

    print("Prediction saved to predictions.txt")
def main():
    try:
        df = load_data()
        features, target = select_columns(df)

        if len(features) == 0:
            raise ValueError("No features selected. At least one feature is required.")

        X = df[features]
        y = df[target]

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        model = LinearRegression()
        model.fit(X_train, y_train)

        y_pred = model.predict(X_test)
        mse = mean_squared_error(y_test, y_pred)
        print(f"\nMean Squared Error: {mse:.2f}")

        for feature, coef in zip(features, model.coef_):
            print(f"{feature}: {coef:.2f}")

        while True:
            predict_score(model, features, df)
            another = input("\nPredict another score? (y/n): ").lower()
            if another != 'y':
                break

        print("\nThank you for using the Score Prediction program.")
    except ValueError as ve:
        print(f"Error: {str(ve)}")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")
        print(f"Error details: {type(e).__name__}: {str(e)}")
    finally:
        input("Press Enter to exit...")

if __name__ == "__main__":
    main()