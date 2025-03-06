import os
import pandas as pd
from datetime import datetime
import joblib

SENSITIVE_KEYWORDS = [
    # Financial Documents  
    "bank", "Bank_Statement", "loan", "credit", "debit", "salary", "salary_slip",  
    "transaction", "invoice", "billing", "payment", "account", "tax", "gst", "receipt",  
    "balance_sheet", "financial_report", "audit", "expense", "investment", "cheque", "ledger",  
    "payslip", "funds", "securities", "loan_document", "mortgage", "financial_statement",  

    # Identity Proofs  
    "aadhar", "aadhar_card", "aadhaar", "aadhaar_card", "pan", "pan_card", "passport", "voter_id",  
    "driving_license", "dl", "ssn", "social_security", "national_id", "identity_proof", "kyc",  
    "government_id", "citizenship", "residence_permit", "work_permit", "birth_certificate",  
    "visa", "id_card", "national_insurance", "itin", "sin", "personal_id",  

    # Legal Documents  
    "nda", "contract", "agreement", "legal", "lawsuit", "court", "license", "policy",  
    "confidential", "privileged", "disclosure", "terms_conditions", "compliance",  
    "non_disclosure", "intellectual_property", "patent", "litigation", "testimony", "copyright",  
    "trademark", "corporate_law", "privacy_policy", "terms_of_service", "arbitration",  
    
    # Medical Records  
    "medical", "patient", "health", "insurance", "prescription", "treatment", "hospital",  
    "diagnosis", "lab_report", "clinical", "medical_record", "doctor", "surgery",  
    "emergency", "pharmacy", "medication", "mental_health", "covid", "xray",  
    "scan", "blood_test", "radiology", "disease", "disability", "ehr", "emr", "hospital_bill",  

    # Corporate Data  
    "internal", "client", "project_details", "business", "strategy", "proprietary", "confidential",  
    "proposal", "presentation", "meeting_minutes", "organization", "roadmap", "budget",  
    "profit_loss", "shareholders", "board_meeting", "executive_summary", "sales_data",  
    "market_analysis", "financial_forecast", "investor_report", "sensitive_data", "pricing",  
    "supplier_contract", "partnership", "company_policy", "hr_policy", "employee_data",  

    # Variations & Naming Conventions  
    "aadharcard", "aadhaarcard", "panCard", "bankStatement", "salarySlip", "confidential_doc",  
    "medicalRecord", "financials", "auditReport", "investmentPortfolio", "loanAgreement",  
    "passportCopy", "nda_doc", "contractAgreement", "policy_doc", "balanceSheet", "billingInvoice",  
    "contract_doc", "legal_doc", "corporate_policy", "business_strategy", "tax_return",  
    "budget_plan", "investment_summary", "data_privacy", "cybersecurity", "payroll", "cibil_score",

    #Corporate
    "HR", "Admin", "CEO" 
]

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
      