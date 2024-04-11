Package Name: kuttychurn
Version: 0.1.0
Author: kishorekumar
Email: kishore.mourougane@epita.fr

# Kutty's Churn-Prediction
=======================================================================================

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

### Dataset:
You can download the dataset from the repo files or by clicking [Here](https://github.com/AnasKhaled18/E-Commerce-Customer-Churn-Analysis/tree/main/Dataset)

|Column| Description |
|---|-----------|
| CustomerID |Unique customer ID  |
| Churn | Churn Flag  |
| Tenure | Tenure of customer in organization |
| PreferredLoginDevice | Preferred login device of customer |
| CityTier | City tier  |
| WarehouseToHome |  Distance in between warehouse to home of customer|
| PreferredPaymentMode  | Preferred payment method of customer |
| Gender |  Gender of customer |
| HourSpendOnApp |  Number of hours spend on mobile application or website|
| NumberOfDeviceRegistered  |  Total number of deceives is registered on particular customer |
| PreferedOrderCat |  Preferred order category of customer in last month |
| SatisfactionScore |  Satisfactory score of customer on service |
| MaritalStatus |  Marital status of customer |
| NumberOfAddress |  Total number of added added on particular customer |
| Complain |  Any complaint has been raised in last month |
| OrderAmountHikeFromlastYear |  OrderAmountHikeFromlastYear |
| CouponUsed |  Total number of coupon has been used in last month |
| OrderCount |  Total number of orders has been places in last month |
| DaySinceLastOrder |  Day Since last order by customer |
| CashbackAmount |  Average cashback in last month |

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

========================================================================================
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

=====================================================================================

# Flask API Deployment on AWS EC2

This project demonstrates the implementation of a Flask API and its deployment to the cloud using Amazon Web Services (AWS) Elastic Compute Cloud (EC2) instances.

## Overview

The project consists of the following components:

1. **Flask API**: The main Python script for the Flask API is `app.py`. This script defines API endpoints and handles incoming HTTP requests.

2. **Deployment Script**: A deployment script (`deploy.sh`) is provided to automate the deployment process. It includes instructions for setting up the EC2 instance, transferring the Flask API files, and running the API server.

3. **Requirements**: The `requirements.txt` file lists all Python dependencies required to run the Flask API.

## Deployment Steps

Follow these steps to deploy the Flask API to an AWS EC2 instance:

1. **Launch EC2 Instance**: Log in to your AWS Management Console and launch a new EC2 instance. Make sure to choose an instance type suitable for your application's requirements.

2. **Security Group Configuration**: Configure security groups to allow inbound traffic on port 80 (HTTP) or any other port you intend to use for accessing the Flask API.

3. **SSH Access**: Connect to your EC2 instance using SSH. You can use a command similar to the following:
   
   ```bash
   ssh -i kutty.pem ec2-user@kutty-churn
   ```

4. **Clone Repository**: Clone your project repository onto the EC2 instance using Git or transfer the files manually.

5. **Install Dependencies**: Navigate to the project directory and install Python dependencies using pip:

   ```bash
   pip install -r requirements.txt
   ```

6. **Run Flask API**: Start the Flask API server by running the following command:

   ```bash
   python app.py
   ```

   Alternatively, you can use tools like `screen` or `tmux` to run the server in the background.

7. **Access API**: Once the Flask API is running, you can access it using the public IP address or domain name of your EC2 instance, along with the appropriate port (e.g., `http://kutty-churn:5001`).


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

