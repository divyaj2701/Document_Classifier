#!/bin/bash

FILE_PATH="test_file.pdf"  # Make sure this file exists
# eg : FILE_PATH = "/home/user/desktop/filename.pdf"
API_URL="https://document-classifier-hpge.onrender.com/predict"      

if [ ! -f "$FILE_PATH" ]; then
    echo "Error: File $FILE_PATH not found!"
    exit 1
fi

curl -X POST -F "file=@$FILE_PATH" "$API_URL"
