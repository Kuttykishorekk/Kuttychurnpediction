# Streamlit App Folder

This folder contains files for a Streamlit web application that serves a pre-trained machine learning model for prediction.

## Files

- `app.py`: The main Python script for the Streamlit web application. It includes a Flask server that serves the ML model and provides an interface for making predictions.
- `model.ipynb`: Jupyter Notebook containing code for training the ML model and saving it as a pickle file (`randomforest.pkl`).
- `randomforest.pkl`: Pre-trained Random Forest model saved as a pickle file.
- `requirements.txt`: Text file listing all Python dependencies required to run the Streamlit application.

## Usage

### Installation

Before running the Streamlit app, ensure you have all the required dependencies installed. You can install them using pip:

```bash
pip install -r requirements.txt
```

### Running the Streamlit App

To start the Streamlit app, run the following command:

```bash
streamlit run app.py
```

This will start a local server and open the Streamlit app in your default web browser.

### Interacting with the App

Once the Streamlit app is running, you can interact with it using the provided interface. It may include input fields, sliders, buttons, etc., depending on the design of the app.

### Making Predictions

Use the Streamlit app to make predictions using the pre-trained ML model (`randomforest.pkl`). Provide input data through the interface, and the app will display the predicted output.

### Model Training

If you want to retrain the ML model or modify the existing one, you can use the `model.ipynb` Jupyter Notebook. It contains code for loading data, training the model, and saving it as a pickle file.

## References

- [Streamlit Documentation](https://docs.streamlit.io/)
- [Scikit-learn Documentation](https://scikit-learn.org/stable/documentation.html)

## Contributors

- [kishorekumar](https://github.com/kuttykishorekk)