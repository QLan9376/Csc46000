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
We created a correlation heatmap to see which features are significantly correlated with the target variable, death_event. These features are time, serum_creatinine, ejection_fraction, age, and serum_sodium. We looked at boxplots to undertsand the distribution of these features and density plots to understand the relationship between the features and death event. The `EDA_feature_selection` includes the excuetive summary of the analysis.

For the Logistic Regression Model, we've used 70%, 80% and 90% training set respectively to evaluate how the model performance changes with more training data. Based on our observations, as the number of training data increase, the model accuracy decreased. The F-1 score also decreased which indicates that the precision and recall were poor. In this case, it seems that more data is hurting the model.

### Challenges
This might be a current or future challenge which is choosing the right features for building the model. As of right now, we're not entirely sure that we've chosen the right features to make the prediction.

### Future Work
For the final analysis, we plan to use other supervised learning algorithm such as random forests and decision trees to determine which model will yield the best result. Also, we might test combinations of features to determine which features result in the highest score.

### Contributions

- Qing: Worked on the data cleaning to prepare for data analysis, feature selection and model building.
- Asma: Worked on the exploratory data analysis and selecting features for the modeling.
- Anthony: Worked on model building and evaluating the model.
