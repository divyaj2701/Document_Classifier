import requests

API_URL = "https://document-classifier-hpge.onrender.com/predict"
FILE_PATH = "test_file.pdf"
# eg : FILE_PATH = "/home/user/desktop/filename.pdf"

try:
    with open(FILE_PATH, "rb") as file:
        response = requests.post(API_URL, files={"file": file})
        print("Python Requests Response:")
        print(response.json())
except Exception as e:
    print("Python Requests Failed:", e)
