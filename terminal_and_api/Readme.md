python -m venv venv
source venv/bin/activate
pip install flask pandas xgboost scikit-learn

pip install --upgrade scikit-learn==1.6.1                       - TRY UPGRADING IF AN ERROR OCCURS 
python Predictor.py /home/divya27/Downloads/HKDRF_2025.pdf      - TO RUN IN TERMINAL
python Predictor.py api                                         - TO RUN THROUGH API
http://127.0.0.1:5000/predict                                   - LINK FOR API (ADD /predict IN END)


deactivate - TO DEACTIVATE VIRTUAL ENVIORNMENT
<!-- curl -X POST -F "file=@/home/divya27/Downloads/HKDRF_2025.pdf" http://127.0.0.1:5000/predict -->