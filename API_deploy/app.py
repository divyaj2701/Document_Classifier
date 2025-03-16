import os
from flask import Flask, request, jsonify
from sensitivity_predictor import SensitivityPredictor

# Initialize the predictor
predictor = SensitivityPredictor('sensitivity_classifier.joblib')

# Function to predict sensitivity for a file
def predict_file(file_path):
    result = predictor.predict(file_path)
    return result

# Flask API
app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return '''
    <h1>Upload a File for Sensitivity Prediction</h1>
    <form method="POST" enctype="multipart/form-data" action="/predict">
        <input type="file" name="file">
        <input type="submit" value="Upload">
    </form>
    '''

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({"error": "No file provided"}), 400

    file = request.files['file']
    file_path = os.path.join("/tmp", file.filename)
    file.save(file_path)

    result = predict_file(file_path)
    os.remove(file_path)  # Clean up the uploaded file

    output = {
        "Classification": result['prediction'],
        "Confidence": result['confidence']
    }
    return jsonify(output)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
