import os
import pandas as pd
from datetime import datetime
import joblib

class SensitivityPredictor:
    def __init__(self, model_path):
        self.model = joblib.load(model_path)
        self.permission_map = {
            '600': 'Restricted', '400': 'Restricted',
            '644': 'Open', '755': 'Open', '777': 'Public'
        }
        self.department_map = {
            'fin_user1': 'Finance', 'fin_user2': 'Finance',
            'hr_admin': 'HR', 'hr_recruiter': 'HR',
            'sysadmin': 'IT', 'devops': 'IT'
        }
    
    def _map_owner(self, username):
        return self.department_map.get(username.split('_')[0], 'unknown')
    
    def _map_permissions(self, mode):
        return self.permission_map.get(mode[-3:], 'unknown')
    
    def extract_features(self, file_path):
        try:
            stat = os.stat(file_path)
            return {
                'extension': os.path.splitext(file_path)[1].lower(),
                'owner': self._map_owner(self._get_owner(file_path)),
                'permissions': self._map_permissions(oct(stat.st_mode)[-3:]),
                'size': stat.st_size / 1024,  # Convert to KB
                'days_since_creation': (datetime.now() - datetime.fromtimestamp(stat.st_ctime)).days,
                'days_since_modification': (datetime.now() - datetime.fromtimestamp(stat.st_mtime)).days,
                'has_sensitive_keyword': any(kw in os.path.basename(file_path).lower() for kw in SENSITIVE_KEYWORDS)
            }
        except Exception as e:
            print(f"Error processing {file_path}: {str(e)}")
            return None
    
    def predict(self, file_path, threshold=0.6):
        features = self.extract_features(file_path)
        if not features:
            return {"error": "Could not process file"}
            
        df = pd.DataFrame([features])
        proba = self.model.predict_proba(df)[0]
        
        return {
            "prediction": "Sensitive" if proba[1] > threshold else "Non-Sensitive",
            "confidence": f"{max(proba)*100:.1f}%",
            "features": features
        }
    
    def _get_owner(self, path):
        try:
            import pwd
            return pwd.getpwuid(os.stat(path).st_uid).pw_name
        except:
            return "unknown"

# Usage
if __name__ == "__main__":
    predictor = SensitivityPredictor('sensitivity_classifier.joblib')
    file_path = input("Enter file path: ")
    while(file_path != 'q'):
      result = predictor.predict(file_path)
    
      print("Prediction Result:")
      print(f"Classification: {result['prediction']}")
      print(f"Confidence: {result['confidence']}")
      # print("\nMetadata Analysis:")
      # for k, v in result['features'].items():
      #   print(f"{k.replace('_', ' ').title()}: {v}")
      print()
      file_path = input("Enter file path: ")
      
