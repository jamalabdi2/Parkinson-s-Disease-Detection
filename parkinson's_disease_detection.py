# -*- coding: utf-8 -*-
"""Parkinson's Disease Detection.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1c7BGwGTvK04Z6at6qS5GUXou8FyV7N4M

#**Parkinson's Disease Detection.**

**Parkinson’s disease** is a progressive disorder of the central nervous system affecting movement and inducing tremors and stiffness.

It has 5 stages to it and affects more than 1 million individuals every year in The world.
This is chronic and has no cure yet. It is a neurodegenerative disorder affecting dopamine-producing neurons in the brain.

**Importing The necessary Libraries**
"""

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, plot_confusion_matrix, classification_report, roc_auc_score, plot_roc_curve
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split

import warnings
warnings.filterwarnings('ignore')
sns.set()

"""**Reading data**"""

!pip install opendatasets

import opendatasets
dataset_url = 'https://www.kaggle.com/datasets/thecansin/parkinsons-data-set?datasetId=409297&sortBy=voteCount'
opendatasets.download(dataset_url)

data_path = '/content/parkinsons-data-set/parkinsons.data'
df = pd.read_csv(data_path)
df.head()

# shape of the dataset
df.shape
# 195 ----> rows
# 24 -----> columns

# information about the data
df.info()

# dataframe columns
df.columns

# last five rows
df.tail()

# data types in the dataset
df.dtypes

"""**Target Column**

**1 ---> Has Parkinson's disease (147 in the dataset)**

**0 ---> Healthy (48 in the dataset)** 
"""

df.status.value_counts()

df.status.value_counts().plot(kind = 'bar')
plt.title('Distribution of Target variable')
plt.show()

df.status.value_counts().plot(kind = 'pie',autopct = '%.f%%')
plt.title('Distribution of Target variable')
plt.show()

# null values
df.isnull().sum().max()

"""**Exploratory data analysis**"""

df = df.drop('name',axis=1)

def plots(plot_kind,dataframe):
  plot_kind = plot_kind.lower()
  plot_func ={
      'violin':sns.violinplot,
      'box':sns.boxplot,
      'histogram':sns.histplot,
      'kde':sns.kdeplot
  }

  figure = plt.figure(figsize=(25,16))
  for index,column in enumerate(dataframe.columns):
    axis = figure.add_subplot(5,5,index+1)

    if plot_kind in ['violin','box']:
      plot_func[plot_kind](y=df[column],ax=axis)
      plt.title(f'{plot_kind} plot for {column}')
    else:
       plot_func[plot_kind](df[column],ax=axis)
       plt.title(f'{plot_kind} plot for {column}')

  plt.tight_layout()
  plt.show()

# violin plot
plots('violin',df)

# boxplot
plots('box',df)

# histogram plot
plots('histogram',df)

# kde plot
plots('kde',df)

# satistics about the dataframe
df.describe()

"""**Seperating features and target**"""

features = df.drop('status',axis=1)
target = df['status']

"""**Train Test Split**"""

train_data,test_data,train_labels,test_labels = train_test_split(features,target,stratify=target,test_size=0.2,random_state=2)

"""**MinMax Scalling between**"""

scaler = MinMaxScaler()
scaler.fit(train_data)
train_data = scaler.transform(train_data)
test_data = scaler.transform(test_data)

"""**Modeling**
**Base model LogisticRegression**
"""

log_model = LogisticRegression()
log_model.fit(train_data,train_labels)
log_prediction = log_model.predict(test_data)
log_accuracy = accuracy_score(log_prediction,test_labels)
answer = round(log_accuracy*100,2)
print(f'Accuracy on Logistic Regression is:{answer}')

# confusion matrix
log_confusion = confusion_matrix(log_prediction,test_labels)
log_confusion

# heatmap
sns.heatmap(log_confusion,annot=True)
plt.show()

"""**Different Models**"""

models = [LogisticRegression(max_iter=1000),SVC(kernel='linear'),KNeighborsClassifier(),RandomForestClassifier(),XGBClassifier()]
model_results = []
def best_model(model_list):
  for model in model_list:
    model.fit(train_data,train_labels)
    prediction = model.predict(test_data)
    accuracy = accuracy_score(prediction,test_labels)
    formated_answer = round(accuracy*100,2)
    model_results.append({
        'model Name':str(model),
        'Model Accuracy Score':formated_answer
    })
  return pd.DataFrame(model_results).sort_values(by='Model Accuracy Score',ascending=False)
best_model(models)

"""**Model Result comparison**

	                    **Model Accuracy Score**
                         
RandomForestClassifier() ----->	    97.44

XGBClassifier()	  ----->                    97.44

KNeighborsClassifier()	----->              94.87

SVC(kernel='linear')	  ----->              89.74

LogisticRegression(max_iter=1000)	----->    84.62

"""

