
from flask import Flask, request
import pandas as pd
import mlflow.pyfunc

# Load the model using MLflow
model_uri = "file:///home/kutty/Desktop/github%20project/churnpediction/MlflowExperimentTracking/mlruns/184263391567962105/6354ea3bc2da4e0fa86e994cf73f2494/artifacts/model"  # Adjust the model path/version as needed
model = mlflow.pyfunc.load_model(model_uri)

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Assuming the data is sent through form data
        data = { key: request.form[key] for key in request.form.keys() }
        
        # Converting form data to DataFrame
        query_df = pd.DataFrame([data])
        
        # Making prediction
        prediction = model.predict(query_df)
        
        # Returning the prediction as a string response
        return f'Prediction: {prediction[0]}'
    except Exception as e:
        return f'Error: {str(e)}'

if __name__ == '__main__':
    app.run(port=5001)