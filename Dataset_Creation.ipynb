import os
import random
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Configuration
PATHS = [
    "/home/docs/", "/mnt/dev/", "C:\\Users\\", "/srv/records/", "/var/logs/", "/home/downloads/", 
    "/mnt/data/", "C:\\Program Files\\", "/srv/shared/", "/tmp/files/", "/home/user/Documents/", 
    "/mnt/backup/", "C:\\Users\\Public\\", "/var/tmp/", "/home/admin/logs/", "/mnt/secure/", 
    "/srv/storage/", "C:\\Windows\\Temp\\", "/var/spool/", "/home/common/", "/mnt/archive/", 
    "C:\\Users\\Default\\", "/etc/configs/", "/srv/logs/", "/var/backups/", "/home/shared/", 
    "/mnt/logs/", "C:\\Windows\\System32\\", "/tmp/storage/", "/srv/docs/", "/var/local/", 
    "/home/system/", "/mnt/mounts/", "C:\\Users\\Administrator\\", "/etc/logs/", "/srv/users/", 
    "/var/tmpdata/", "/home/backup/", "/mnt/files/", "C:\\Temp\\", "/srv/temp/", "/var/db/", 
    "/home/data/", "/mnt/devices/", "C:\\Users\\Guest\\", "/srv/backup/", "/var/lib/", 
    "/home/local/", "/mnt/storage/", "C:\\Users\\Desktop\\", "/srv/configs/", "/var/run/", 
    "/home/media/", "/mnt/projects/", "C:\\Users\\Documents\\", "/srv/system/", "/var/tmp_storage/"
]

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

NON_SENSITIVE_KEYWORDS = [
    # General Documents
    "notes", "lecture", "assignment", "homework", "project_plan", "task_list", "meeting_agenda", 
    "schedule", "calendar", "worksheet", "tutorial", "reference", "guide", "instructions", "checklist", 
    "minutes", "summary", "report", "presentation", "handbook", "newsletter", "brochure", "flyer", 
    "poster", "announcement", "memo", "proposal", "research", "whitepaper", "article", "blog", 
    "press_release", "news", "bulletin", "journal", "review", "case_study", "survey", "questionnaire", 
    
    # Public Information
    "public_notice", "government_notice", "circular", "press_announcement", "legal_notice", "policy_brief", 
    "open_data", "transparency_report", "census_data", "statistics", "weather_report", "market_report", 
    "trade_analysis", "industry_insights", "public_speech", "conference_paper", "open_access", 

    # Educational Documents
    "course_material", "syllabus", "curriculum", "class_notes", "school_report", "university_brochure", 
    "education_policy", "exam_papers", "sample_questions", "study_guide", "revision_notes", "teacher_guide", 
    "student_handbook", "scholarship_info", "research_paper", 

    # Technical and IT Documents
    "user_manual", "installation_guide", "configuration", "technical_doc", "api_documentation", 
    "troubleshooting_guide", "faq", "release_notes", "software_update", "patch_notes", "product_specs", 
    "system_requirements", "technical_report", "design_doc", "coding_guidelines", "development_notes", 
    "product_catalog", "feature_list", "wireframe", "prototype", "architecture_diagram", "network_plan", 

    # Business and Corporate Documents
    "invoice_template", "budget_plan", "marketing_plan", "branding_guide", "product_launch", 
    "corporate_strategy", "sales_forecast", "revenue_report", "expense_summary", "workflow_document", 
    "operation_manual", "team_meeting", "status_update", "business_roadmap", "partnership_agreement", 

    # Creative and Media Content
    "script", "storyboard", "podcast_notes", "song_lyrics", "music_sheet", "artwork", "animation", 
    "illustration", "photo_collection", "design_mockup", "video_script", "documentary_script", 
    "book_draft", "novel_outline", "manuscript", "poetry", "fanfiction", "comic_strip", "sketchbook", 

    # Travel and Events
    "itinerary", "flight_details", "hotel_booking", "trip_plan", "packing_list", "restaurant_review", 
    "travel_blog", "road_trip", "tourist_guide", "visa_guide", "city_map", "local_attractions", 
    "event_schedule", "concert_tickets", "festival_info", "conference_agenda", "movie_list", 
    "book_club", "sports_schedule", "game_rules", 

    # Lifestyle and Personal Documents
    "recipe", "cooking_tips", "fitness_plan", "diet_chart", "grocery_list", "home_maintenance", 
    "garden_tips", "pet_care", "budget_tracker", "financial_planner", "expense_sheet", "task_manager", 
    "time_tracker", "journal_entry", "diary", "self_improvement", "meditation_notes", "goal_setting", 
    "motivational_quotes", "daily_log", "bucket_list", 

    # Miscellaneous Variations
    "draft_project_plan", "updated_notes", "final_presentation", "backup_report", "sample_worksheet", 
    "new_task_list", "old_summary", "copy_meeting_agenda", "v1_memo", "v2_blog", "report_overview", 
    "info_handbook", "updated_case_study", "checklist_data", "public_notice_log", "survey_record", 
    "journal_entry_details", "meeting_notes_file", "release_notes_info", "research_paper_log", 
    "statistics_report_data", "course_material_info", "development_notes_file", "architecture_diagram_details", 
    "software_update_log", "financial_planner_report", "budget_plan_info", "partnership_agreement_file", 
    "event_schedule_details", "travel_blog_overview", "trip_plan_file", "visa_guide_record", "daily_log_info", 
    "motivational_quotes_record", "meditation_notes_file", "grocery_list_details", "home_maintenance_log", 
    "self_improvement_doc", "draft_budget_plan", "updated_coding_guidelines", "final_journal_entry", 
    "backup_lecture_notes", "sample_diary", "new_travel_blog", "old_study_guide", "copy_script", "v1_poetry", 
    "v2_comic_strip", "task_list_file", "article_overview", "business_roadmap_log", "invoice_template_data", 
    "marketing_plan_record", "patch_notes_doc", "troubleshooting_guide_file", "technical_doc_report", 
    "product_specs_overview", "schedule_log", "case_study_details", "industry_insights_record", 
    "reference_data", "workflow_document_log", "lecture_notes_file", "university_brochure_data", 
    "transparency_report_overview", "legal_notice_details", "updated_policy_brief", "sample_transparency_report", 
    "budget_tracker_file", "travel_blog_notes", "final_conference_agenda", "updated_movie_list", "book_club_info", 
    "sports_schedule_report", "game_rules_file", "script_record", "storyboard_overview", "daily_log_entry", 
    "self_improvement_notes", "backup_technical_doc", "sample_configuration", "new_software_update", 
    "old_release_notes", "copy_patch_notes", "v1_api_documentation", "v2_troubleshooting_guide", 
    "expense_summary_log", "corporate_strategy_file", "revenue_report_details", "festival_info_record", 
    "visa_guide_log", "concert_tickets_data"
]

EXTENSIONS = [".pdf", ".docx", ".xlsx", ".txt", ".pptx", ".csv"]
OWNERS = ["Finance", "HR", "IT", "Marketing", "Operations"]
PERMISSIONS = ["Restricted", "Confidential", "Public", "Internal"]

# Generate random file size using log-normal distribution
def random_size():
    return int(np.random.lognormal(mean=6, sigma=1.2))  # 1KB-500MB

# Generate random dates with temporal patterns
def random_date(is_sensitive):
    start_date = datetime.now() - timedelta(days=5 * 365)
    random_days = random.randint(0, 5 * 365)
    creation_date = start_date + timedelta(days=random_days)
    
    # Sensitive files are modified more recently
    if is_sensitive:
        modified_date = creation_date + timedelta(days=random.randint(0, 7))
    else:
        modified_date = creation_date + timedelta(days=random.randint(0, 365))
    
    return creation_date.strftime("%Y-%m-%d"), modified_date.strftime("%Y-%m-%d")

# Calculate sensitivity score
def calculate_sensitivity_score(row):
    weights = {"Keyword": 50, "Permissions": 5, "Owner": 15, "Extension": 20, "Size": 5, "Date": 5}
    score = 0
    score += weights["Keyword"] * row["has_sensitive_keyword"]
    score += weights["Permissions"] * (row["permissions"] == "Restricted")
    score += weights["Owner"] * (row["owner"] in ["Finance", "HR"])
    score += weights["Extension"] * (row["extension"] in [".pdf", ".docx"])
    score += weights["Size"] * (row["size"] > 1000)
    score += weights["Date"] * ((pd.to_datetime('today') - pd.to_datetime(row["created"])).days < 180)
    
    return 1 if score >= random.uniform(45, 60) else 0

# Generate synthetic metadata
def generate_metadata(num_files):
    data = []
    for _ in range(num_files):
        is_sensitive = random.choice([True, False])
        keyword = random.choice(SENSITIVE_KEYWORDS if is_sensitive else NON_SENSITIVE_KEYWORDS)
        path = random.choice(PATHS)
        ext = random.choice(EXTENSIONS)
        owner = random.choice(OWNERS)
        permissions = random.choice(PERMISSIONS)
        size = random_size()
        creation_date, modified_date = random_date(is_sensitive)
        
        record = {
            "filename": f"{path}{keyword}{ext}",
            "extension": ext,
            "owner": owner,
            "permissions": permissions,
            "size": size,
            "created": creation_date,
            "modified": modified_date,
            "has_sensitive_keyword": is_sensitive,
            "label": 0  # Will be updated based on score
        }
        data.append(record)
    
    df = pd.DataFrame(data)
    df['label'] = df.apply(calculate_sensitivity_score, axis=1)
    
    flip_indices = random.sample(range(len(df)), int(0.05 * len(df)))
    df.loc[flip_indices, "label"] = 1 - df.loc[flip_indices, "label"]
    
    return df

if __name__ == "__main__":
    num_files = int(input("Enter number of files to generate: "))
    df = generate_metadata(num_files)
    df.to_csv("file_metadata.csv", index=False)
    print(f"Generated dataset with {len(df)} records")

    # print("\nSample Data:")
    # print(df.head())

    print("\nTotal Sensitive Files:", df["label"].sum())
    print("Total Non-Sensitive Files:", len(df) - df["label"].sum())
