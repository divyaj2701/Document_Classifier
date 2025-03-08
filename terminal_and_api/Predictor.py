import os
import sys
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
@app.route('/', methods=['GET', 'POST'])
def predict():
    if request.method == 'GET':
        # Display a simple HTML form for file upload
        return '''
        <h1>Upload a File for Sensitivity Prediction</h1>
        <form method="POST" enctype="multipart/form-data">
            <input type="file" name="file">
            <input type="submit" value="Upload">
        </form>
        '''
    elif request.method == 'POST':
        # Handle file upload and prediction
        if 'file' not in request.files:
            return jsonify({"error": "No file provided"}), 400

        file = request.files['file']
        file_path = os.path.join("/tmp", file.filename)
        file.save(file_path)

        result = predict_file(file_path)
        os.remove(file_path)  # Clean up the uploaded file
        output = {"Classfication": result['prediction'], "Confidence": result['confidence']} 
        return jsonify(output)

# app = Flask(__name__)

# @app.route('/predict', methods=['POST'])
# def predict():
#     if 'file' not in request.files:
#         return jsonify({"error": "No file provided"}), 400

#     file = request.files['file']
#     file_path = os.path.join("/tmp", file.filename)
#     file.save(file_path)

#     result = predict_file(file_path)
#     os.remove(file_path)  # Clean up the uploaded file
    
#     output = {"Classfication": result['prediction'], "Confidence": result['confidence']} 
#     # print(f"Classification: {result['prediction']}")
#     # print(f"Confidence: {result['confidence']}")
#     return jsonify(output)

# Terminal mode
def terminal_mode(file_path):
    result = predict_file(file_path)

    print("Prediction Result:")
    print(f"Classification: {result['prediction']}")
    print(f"Confidence: {result['confidence']}")
    # print("\nMetadata Analysis:")
    # for k, v in result['features'].items():
    #     print(f"{k.replace('_', ' ').title()}: {v}")

# Main function
def main():
    if len(sys.argv) > 1 and sys.argv[1] == 'api':
        # Run the Flask API
        print("Starting API server...")
        app.run(host='0.0.0.0', port=5000)
    else:
        # Run in terminal mode
        if len(sys.argv) != 2:
            print("Usage: python combined_app.py <file_path>")
            print("       python combined_app.py api (to start API server)")
            sys.exit(1)

        file_path = sys.argv[1]
        terminal_mode(file_path)

if __name__ == "__main__":
    main()
    
