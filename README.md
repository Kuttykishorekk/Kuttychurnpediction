Package Name: kuttychurn
Version: 0.1.0
Author: kishorekumar
Email: kishore.mourougane@epita.fr

# Kutty's Churn-Prediction
=======

## Project Overview
This project aims to predict customer churn for an E-Commerce platform. Using machine learning techniques, specifically Random Forest Classifier, we analyze customer behavior and other relevant features to identify patterns that indicate the likelihood of churn.

## Setup and Installation
Ensure you have Python installed on your system. This project is built using Python 3.8 or higher.

1. Clone the repository to your local machine.
2. Navigate into the project directory.
3. Install the required packages using the requirements.txt file provided in the project directory.

```bash
pip install -r requirements.txt
```

The Python version used is 3.9.17. Based on the analysis and model building steps performed in the project, the `requirements.txt` file should include the following packages:

```
numpy
pandas
scikit-learn
matplotlib
openpyxl
xlrd
```

## Data
The dataset, "E Commerce Dataset.xlsx", consists of various customer attributes and their interaction with the E-Commerce platform. Key features include CustomerID, Churn, Tenure, PreferredLoginDevice, CityTier, and many more.

## KuttyChurn Package

KuttyChurn is a Python package developed for predicting customer churn in E-commerce datasets. It encompasses a comprehensive workflow from data preparation to model evaluation and prediction, allowing users to efficiently process data, train machine learning models, and visualize important features influencing customer retention.

### Installation

Clone this repository to your local machine using:

```bash
git clone https://github.com/Kuttykishorekk/Kuttychurnprediction.git
```

Navigate to the project directory and install the package using pip:

```bash
cd KuttyChurn
pip install .
```
or

```bash
pip install kuttychurn
```

=======
### Components

- `data_preparation.py`: Script for loading and initially cleaning the raw E-commerce dataset.
- `feature_engineering.py`: Contains methods for feature extraction and preprocessing, ensuring data is suitable for model training.
- `model_training.py`: Facilitates the training of machine learning models using the preprocessed data, with a focus on Random Forest Classifier.
- `predict.py`: Provides functionality for making predictions on new data using the trained model.
- `visualization.py`: Offers several plotting functions to visualize the data distribution, model metrics, and feature importances.

### Usage

While it's recommended to explore individual scripts for granular control over the process, the package is designed to be used as follows:

1. Prepare your dataset using the `data_preparation` module.
2. Employ the `feature_engineering` module to process your dataset further.
3. Train your model with the `model_training` module.
4. Use the `predict` module for making predictions.
5. Visualize your model's performance using the `visualization` module.

## Running the Project

```python
# Pretend this is main.py
from KuttyChurn.data_preparation import load_data
from KuttyChurn.data_preparation import impute_missing_values
from KuttyChurn.feature_engineering import encode_categorical_variables
from KuttyChurn.data_preparation import split_data
from KuttyChurn.model_training import evaluate_model
from KuttyChurn.model_training import train_model

# Note: These function calls reference the structure described earlier,
# but we will simulate these steps directly here due to environmental constraints.

# Data Preparation
ecommerce_data_loaded = load_data('../data/raw/E Commerce Dataset.xlsx')
ecommerce_data_imputed = impute_missing_values(ecommerce_data_loaded)
ecommerce_data_encoded = encode_categorical_variables(ecommerce_data_imputed)
X_train, X_test, y_train, y_test = split_data(ecommerce_data_encoded, 'Churn')

# Feature Engineering
# (In this case, encoding was done during data preparation)

# Model Training
model = train_model(X_train, y_train)
accuracy, report = evaluate_model(model, X_test, y_test)

# Prediction
# (Not applicable for this demo; typically, you'd use make_predictions with new data)

print(f"Accuracy Score: {accuracy}")
print("Classification Report:")
print(report)
```

To run the project, execute the `main.py` script. This will perform data preparation, feature engineering, model training, and evaluation in sequence.

```bash
python main.py
```

### Contributing
Contributions to this project are welcome. Please ensure to follow best practices for code quality and consistency.

### LICENSE

For the MIT license, the contents would be as follows:

```license
MIT License

Copyright (c) 2024 Kishorekumar

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## Contribution

Contributions are welcome! Please read the contribution guidelines for more information.

## Authors

- Kishorekumar(kishorekumarmourougane@gmail.com)

Thank you for using Churn Predictor for your customer churn analysis needs!

