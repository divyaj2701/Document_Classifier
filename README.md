## How To Run

1.  *Copy all 3 .py code-files to google Colab or Jupyter Notebook in a single notebook.*
2.  *Run *Dataset_Creation.py* and input number of files to create *file_metadata.csv*.*
3.  *Run *Model_Training.py* to create a model.*
4.  *Run *Sensitivity_Predictor.py* and input file path to check sensitivity and confidence score of file.*
5.  *Enter '*q*' if you want to end Predictions.*

## 📊 Model Training & Evaluation

1. *Dataset Preparation:*

   - Created sample file metadata (filename, size, extension, timestamps).
   - Labelled files as *Sensitive (Y) or Non-Sensitive (N)*.

2. *Feature Engineering:*

   - Extracted keywords ("PAN", "bank", etc.).
   - Considered file extensions (.pdf, .xlsx, .txt).
   - Used file size categories (small, medium, large).

3. *Model Training:*

   - Used *Random Forest Classifier* for initial implementation.
   - Tuned hyperparameters for better accuracy.

4. *Evaluation:*

   - Achieved *\~90% accuracy* on test data.
   - Outputs a *confidence score* with each prediction.
