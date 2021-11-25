import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.metrics import f1_score

df = pd.read_csv("cleaned.csv")

# Drop unnecessary features
df = df.drop(['anaemia', 'creatinine_phosphokinase', 'diabetes', 'high_blood_pressure', 'platelets', 'sex', 'smoking'], axis=1)

# Feature variable
X = df.drop('DEATH_EVENT', axis=1)

# Target Variable
y = df['DEATH_EVENT']

# 70% Training and 30% testing tests
X_train, X_test, y_train, y_test = train_test_split(X,
                                y,
                                test_size=0.3,
                                random_state=42)

# Instantiate the classifier
logreg = LogisticRegression()

# Fit the classifier
logreg.fit(X_train, y_train)

# Predict instances from the test set
y_pred = logreg.predict(X_test)

# Print the accuracy score of the model
print("Accuracy of logistic regression classifier using 70% training data: ", 
      logreg.score(X_test, y_test))

# Print the F1 score
print("F1 score for 70% training data", f1_score(y_test, y_pred))

# Print the confusion matrix of the model
print(confusion_matrix(y_test, y_pred))

# 80% Training and 20% testing tests
X_train, X_test, y_train, y_test = train_test_split(X,
                                y,
                                test_size=0.2,
                                random_state=42)

# Fit the classifier
logreg.fit(X_train, y_train)

# Predict instances from the test set
y_pred = logreg.predict(X_test)

# Print the accuracy score of the model
print("Accuracy of logistic regression classifier using 80% training data: ", 
      logreg.score(X_test, y_test))

# Print the F1 score
print("F1 score for 80% training data", f1_score(y_test, y_pred))

# Print the confusion matrix of the model
print(confusion_matrix(y_test, y_pred))

# 90% Training and 10% testing tests
X_train, X_test, y_train, y_test = train_test_split(X,
                                y,
                                test_size=0.1,
                                random_state=42)

# Fit the classifier
logreg.fit(X_train, y_train)

# Predict instances from the test set
y_pred = logreg.predict(X_test)

# Print the accuracy score of the model
print("Accuracy of logistic regression classifier using 90% training data: ", 
      logreg.score(X_test, y_test))

# Print the confusion matrix of the model
print(confusion_matrix(y_test, y_pred))

# Print the F1 score
print("F1 score for 90% training data", f1_score(y_test, y_pred))