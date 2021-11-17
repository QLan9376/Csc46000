# -*- coding: utf-8 -*-
"""etl_heart_failure_clinical_records_dataset.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15HlNyRwCxvB_YYPl-QoOTLnvle0vY_QI
"""

import pandas as pd

url = 'https://raw.githubusercontent.com/QLan9376/Csc46000/main/raw_heart_failure_clinical_records_dataset.csv?token=AKRWZVXN2QER6ULZMLOFTLLBSSGIO'
df = pd.read_csv(url)

df.head()

df.drop(['time'],axis = 1)

df = df.astype({'age': 'int'})
print(df)