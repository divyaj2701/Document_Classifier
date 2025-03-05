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
