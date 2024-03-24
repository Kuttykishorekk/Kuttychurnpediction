# README - E-Commerce Kutty's Churn Prediction with Explainable AI (SHAP)

This project focuses on the prediction of customer churn in an E-commerce setting using Machine Learning (Random Forest Classifier) and attempts to explain the model's predictions using SHAP (SHapley Additive exPlanations), a unified measure of feature importance that allocates the contribution of each feature to the prediction for each instance.

## Dataset

The dataset utilized in this project is related to customer behavior and attributes in an E-Commerce environment. The key features include:

- `CustomerID`: Unique identifier for each customer.
- `Churn`: Target variable indicating whether the customer has churned or not.
- `Tenure`: The duration a customer has been with the E-Commerce platform.
- `PreferredLoginDevice`: The device a customer prefers for logging in.
- `CityTier`: The tier of the city the customer resides in.
- Numerous other features like `WarehouseToHome`, `HourSpendOnApp`, `NumberOfDeviceRegistered`, `SatisfactionScore`, `NumberOfAddress`, etc.

## Model

A Random Forest Classifier is employed to predict the `Churn` variable. The model is trained on a portion of the data, with part of it held out as a test set to evaluate the model's performance.

## Model Explanation with SHAP

SHapley Additive exPlanations (SHAP) is a game theoretic approach to explain the output of any machine learning model. It assigns each feature an importance value for a particular prediction.

### SHAP Visualizations

After fitting the model and computing the SHAP values, several visualizations are generated to understand and explain the model's predictions:

1. **Summary Plot** \
   This plot provides an overview of feature importance, with features ranked by the sum of SHAP value magnitudes across all samples. Features pushing the prediction higher are shown in red, and those pushing the prediction lower are in blue.

2. **Force Plot (for a specific instance)** \
   Force plots help us understand the contribution of each feature to the prediction for a single instance. The base_value is the value that would be predicted if we did not know any features for the current output (the average output over the training dataset).

3. **Waterfall Plot (for a specific instance)** \
   Waterfall plot is another way of explaining individual predictions. The prediction starts from the baseline or expected value. Features pushing the prediction higher are shown in red, and those pushing the prediction lower are in blue.

4. **Beeswarm Plot** \
   A Beeswarm plot is a summary plot without overlapping points. This plot is designed to provide an overview of the impact of all features for all instances.

5. **Dependence Plot** \
   The dependence plot helps us understand the interaction between features.  It shows how the prediction's dependency on a single feature (for instance, 'CashbackAmount') changes with its value and interacts with other features.

Note: The model explanation process may face certain challenges due to compatibility issues between different versions of the SHAP package and certain machine learning models (for instance, RandomForestClassifier), which may lead to dimension discrepancies between the computed SHAP values and the dataset. These challenges are tackled in the given project by using suitable alternative methods and troubleshooting options.

**Remember**: Explainable AI aims to open the black box of complex models, enhancing transparency and helping stakeholders have a better understanding of the model's decisions. It aims to answer questions about what features are most important for predictions and how these features affect predictions. While this project provides specific insights into the given dataset, the general approach can be widely applied across projects and sectors to improve interpretability and trust in AI systems.