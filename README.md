# Multi Linear Regression: Student Score Prediction

This project implements a multi linear regression model to predict student exam scores based on various features such as age, number of absences, and study time.

## Project Description

The script `student_score_prediction.py` uses a linear regression model to:

1. Load and preprocess student data
2. Train a model on the relationship between student features and exam scores
3. Evaluate the model's performance
4. Predict scores for new input (student features)

## Prerequisites

Before you begin, ensure you have met the following requirements:
* Python 3.7+
* Git (for cloning the repository)

## Installation

To set up the Multi Linear Regression project, follow these steps:

1. Clone the repository:
   ```
   git clone https://github.com/your-username/student-score-prediction.git
   cd student-score-prediction
   ```

2. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

To use the Student Score Prediction script:

1. Ensure you have a CSV file named `student-mat (2).csv` in the same directory as the script. This file should contain the following columns: 'age', 'absences', 'studytime', and 'G3' (final grade).

2. Run the script:
   ```
   python student_score_prediction.py
   ```

3. The script will output the Mean Squared Error of the model and the coefficients for each feature.

4. You will then be prompted to enter values for each feature:
   - Age
   - Number of absences
   - Study time (hours per week)

5. After entering the values, the script will output the predicted score for the student with the entered features.

6. The prediction, along with the input data, will be saved to a file named `student_score_predictions.txt`.

7. You will be asked if you want to predict another score. Enter 'y' to continue or any other key to exit.

Note: Make sure to enter numeric values when prompted. The script will convert your inputs to floating-point numbers.

## Sample Data

A sample `student-mat (2).csv` file is provided in the repository. This file contains data for students and can be used to train and test the model. In a real-world scenario, you might want to use a larger dataset for more accurate predictions.

## Contributing

To contribute to this Multi Linear Regression project, follow these steps:

1. Fork this repository.
2. Create a branch: `git checkout -b <branch_name>`.
3. Make your changes and commit them: `git commit -m '<commit_message>'`
4. Push to the original branch: `git push origin student-score-prediction/<location>`
5. Create the pull request.

Alternatively, see the GitHub documentation on [creating a pull request](https://help.github.com/articles/creating-a-pull-request/).

## Contact

If you want to contact the maintainer, you can reach them at `your-email@example.com`.
