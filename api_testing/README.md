# Document Classifier API Testing

This repository contains multiple ways to test the Document Classifier API deployed on Render.

## API Endpoint:
https://document-classifier-hpge.onrender.com/predict
This API allows users to upload a document file for classification.

## Ensure your file exists at the specified path.

----------------------------------------------------------
### Using cURL (Shell Script)

Steps:
#### GIVE EXCECUTION PERMISSION
chmod +x test_curl.sh
#### EXECUTE
./test_curl.sh


----------------------------------------------------------
### Using Python (requests Library)

Steps:
#### Run the script: 
python test_python.py

----------------------------------------------------------
### Using JavaScript (fetch API in Node.js)

Steps:
#### INSTALL node-fetch
npm install node-fetch
#### RUN THE SCRIPT
node test_fetch.js

----------------------------------------------------------
#### Using HTML form

Steps:
#### Run the test_form.html file
#### choose and upload file from system

----------------------------------------------------------

