# CSc 46000: Health Failure Prediction

### Group Members
- Anthony Yang
- Asma Sadia
- Qing Lan

### Repository Structure

- `data`
  - `raw_heart_failure_clinical_records_dataset.csv`: Raw data from the heart_failure_clinical_records_dataset.csv
  - `cleaned.csv`: Cleaned and combined dataset used for modeling
  
- `code`
  - `etl_heart_failure_clinical_records_dataset.py`: Cleans raw_heart_failure_clinical_records_dataset.csv
  - `EDA_feature_selection.ipynb`: Exploratory data analysis on the selected features for modeling
  - `build_model.py`: Builds a Logistic Regression model using the cleaned data

### Exploratory Analysis
We created a correlation heatmap to see which features are significantly correlated with the target variable, death_event. These features are time, serum_creatinine, ejection_fraction, age, and serum_creatinine. We looked at boxplots to undertsand the distribution of these features and density plots to understand the relationship between the features and death event. The `EDA_feature_selection` includes the excuetive summary of the analysis.

### Challenges
Describe any challenges you've encountered so far. Let me know if there's anything you need help with!

### Future Work
Describe what work you are planning to complete for the final analysis.

### Contributions

- Qing: Worked on the data cleaning to prepare for data analysis, feature selection and model building.
- Asma: Worked on the exploratory data analysis and selecting features for the modeling.
- Anthony: Worked on model building and evaluating the model.
