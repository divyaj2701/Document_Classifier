## CREATE VIRTUAL ENVIR0NMENT
python -m venv venv

## ACTIVATE VIRTUAL ENVIRONMENT
source venv/bin/activate

## INSTALL REQUIREMENTS
pip install requirements.txt

## IF ERROR OCCURS TRY UPGRADING
pip install --upgrade scikit-learn==1.6.1 

## RUN FROM TERMINAL
python Predictor.py test_file.pdf
## REPLACE test_file with actual file path
eg: python Predictor.py /home/user/Downloads/2025.pdf

## RUN API 
python Predictor.py api   
## OPEN - LINK FOR API
http://127.0.0.1:5000                                  

## DEACTIVATE THE VIRTUAL ENVIRONMENT
deactivate 
