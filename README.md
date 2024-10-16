# Universal Score Prediction App

## Description
The Universal Score Prediction App is a versatile machine learning tool that predicts scores or values based on user-selected features from any CSV dataset. Using linear regression, it offers a flexible approach to data analysis and prediction across various domains.

## Features
- CSV file compatibility: Works with any properly formatted CSV file
- User-defined variables: Allows selection of both input features and target variable
- Linear regression model: Utilizes scikit-learn's LinearRegression for predictions
- Interactive input: Enables real-time predictions with user-provided data
- Performance metrics: Displays Mean Squared Error and feature coefficients
- Prediction logging: Saves all predictions in a structured, easy-to-read format

## Requirements
- Python 3.7+
- Additional requirements are listed in the `requirements.txt` file

## Installation
1. Clone this repository or download the script.
2. Install required packages using the requirements file:
   ```
   pip install -r requirements.txt
   ```

## Usage
1. Run the script:
   ```
   python linear_predict.py
   ```
2. Follow the prompts:
   - Enter the path to your CSV file
   - Select feature columns for prediction
   - Choose the target column
   - Input values for predictions

## Building Executable
To create a standalone executable:
1. Ensure PyInstaller is installed: `pip install pyinstaller`
2. Run the following command:
   ```
   pyinstaller --onefile linear_predict.py
   ```
3. The executable will be found in the `dist` folder in the project root directory.

## CSV File Guidelines
- Use comma-separated values
- Include headers in the first row
- Ensure numerical data in columns used for prediction

## Output
- Console: Displays model performance and predictions
- File: Saves detailed prediction logs in 'predictions.txt'

## Prediction Log Format
```
==================================================
New Prediction
==================================================
Input:
  feature1: value1
  feature2: value2
  feature3: value3
------------------------------
Predicted Score: XX.XX
==================================================
```

## Troubleshooting
- Verify CSV file format and column names if loading fails
- Ensure selected columns contain numerical data
- Check console for specific error messages and guidance

## Limitations
- Assumes linear relationships between variables
- Limited to numerical data without preprocessing
- May not capture complex, non-linear patterns

## Future Enhancements
- Support for categorical variables
- Implementation of additional regression algorithms
- Data preprocessing options
- Visualization of results

## Contributing
Contributions are welcome! Please feel free to submit pull requests, create issues, or suggest improvements.

## Contact
For questions or support, please contact: eyandilutherking2003@gmail.com

## Acknowledgments
- Built with scikit-learn, pandas, and numpy
- Inspired by the need for flexible, user-friendly prediction tools