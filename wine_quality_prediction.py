# -*- coding: utf-8 -*-
"""Wine_Quality_Prediction.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1m09ca01YVBPst4Xz7D1dLXqZRuQ_T-H-
"""

import pandas as pd

from google.colab import files
upload=files.upload()

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
import sklearn.datasets as datasets
import sklearn.metrics as metrics
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

data=pd.read_csv("/content/winequality-red.csv")

data.head()

data.info()

data.shape

data.isnull().sum()

data.describe()

#no of values for each quality::
sns.catplot(x='quality',data=data,kind='count')

plot=plt.figure(figsize=(5,5))
sns.barplot(x='quality',y='alcohol',data=data)
plt.show()

plot=plt.figure(figsize=(5,5))
sns.barplot(x='quality',y='volatile acidity',data=data)
plt.show()

plot=plt.figure(figsize=(5,5))
sns.barplot(x='quality',y='citric acid',data=data)
plt.show()

#relation between all the columns with the quality column:
corr=data.corr()
#heatmap is used to understand the correlation between columns.

plt.figure(figsize=(10,10))
sns.heatmap(corr,cbar=True,square=True,fmt='.1f',annot=True,annot_kws={'size':8},cmap='Blues')

x=data.drop('quality',axis=1)
print(x)

Y=data['quality'].apply(lambda y_value:1 if y_value>=7 else 0)
print(Y)

#train-test-split
x_train,x_test,y_train,y_test=train_test_split(x,Y,test_size=0.2,random_state=2)

print(Y.shape,y_train.shape,y_test.shape)

#Train the model
model=RandomForestClassifier()

model.fit(x_train,y_train)

x_test_prediction=model.predict(x_test)
test_data_accuracy=accuracy_score(x_test_prediction,y_test)
print('Accuracy:',test_data_accuracy)

input_data=(8.5,0.28,0.56,1.8,0.092,35.0,103.0,0.9969,3.3,0.75,10.5)
input_numpy=np.asarray(input_data)
input_reshape=input_numpy.reshape(1,-1)
prediction=model.predict(input_reshape)
print(prediction)
if(prediction[0]==0):
  print("Bad Quality Wine")
else:
  print("Good Quality Wine")