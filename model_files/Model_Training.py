import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from xgboost import XGBClassifier
from sklearn.metrics import classification_report, precision_recall_curve
import joblib
# import shap

def train_model():
    df = pd.read_csv("file_metadata.csv", parse_dates=['created', 'modified'])
    
    # Feature engineering
    df['days_since_creation'] = (pd.to_datetime('today') - df['created']).dt.days
    df['days_since_modification'] = (pd.to_datetime('today') - df['modified']).dt.days
    
    features = df[[
        'extension', 'owner', 'permissions', 'size',
        'days_since_creation', 'days_since_modification',
        'has_sensitive_keyword'
    ]]
    target = df['label']

    # Preprocessing
    preprocessor = ColumnTransformer([
        ('cat', OneHotEncoder(handle_unknown='infrequent_if_exist'), ['extension', 'owner', 'permissions']),
        ('num', StandardScaler(), ['size', 'days_since_creation', 'days_since_modification']),
        ('bool', 'passthrough', ['has_sensitive_keyword'])
    ])

    # Model pipeline
    model = Pipeline([
        ('preprocessor', preprocessor),
        ('classifier', XGBClassifier(
            n_estimators=150,
            max_depth=4,
            learning_rate=0.05,
            subsample=0.8,
            colsample_bytree=0.8,
            random_state=42
        ))
    ])

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(
        features, target, test_size=0.25, random_state=42, stratify=target
    )

    # Train model
    model.fit(X_train, y_train)

    # Evaluate model
    y_pred = model.predict(X_test)
    print("Model Evaluation:")
    print(classification_report(y_test, y_pred))

    # Save model
    joblib.dump(model, 'sensitivity_classifier.joblib')
    print("\nModel trained and saved successfully")

if __name__ == "__main__":
    train_model()
