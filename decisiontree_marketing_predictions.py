# -*- coding: utf-8 -*-
"""DecisionTree_Marketing_Predictions.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1a0r_PQEX3m2aqxgCbzLNYQP-gUhFAH-E

# PRODIGY INFOTECH

# **Task-03: Decision Tree Classifier for Customer Purchase Prediction**

## Introduction:

In the dynamic landscape of marketing and customer engagement, predicting whether a customer will make a purchase is crucial for businesses to tailor their strategies effectively. This notebook presents the development of a decision tree classifier, leveraging demographic and behavioral data, to predict customer purchase behavior. The chosen dataset for this task is the Bank Marketing dataset from the UCI Machine Learning Repository.

## **Problem Statement**:

Understanding and predicting customer purchase behavior is a key challenge faced by businesses. By analyzing demographic information such as age, education, and marital status, along with behavioral data like previous marketing interactions and economic indicators, we aim to build a decision tree classifier capable of predicting whether a customer will purchase a product or service.

### Key Challenges:

1. **Data Complexity:** Demographic and behavioral data can be diverse and complex, requiring thorough preprocessing to extract meaningful insights.
2. **Model Interpretability:** Decision tree models offer interpretability, but tuning them for optimal predictive performance is essential.
3. **Business Impact:** Accurate predictions of customer purchase behavior can significantly impact marketing strategies and resource allocation.

## Objective:

The primary objective of this notebook is to guide through the process of developing a decision tree classifier for customer purchase prediction. We will explore the Bank Marketing dataset, preprocess the data, analyze key features, build the decision tree model, and evaluate its performance.

## Approach:

1. **Data Exploration and Understanding:** Explore the structure of the Bank Marketing dataset, identifying features and the target variable.
2. **Data Preprocessing:** Clean and preprocess the data to handle missing values, encode categorical variables, and prepare it for model training.
3. **Exploratory Data Analysis (EDA):** Analyze demographic and behavioral features to gain insights into the dataset.
4. **Model Building:** Develop a decision tree classifier using scikit-learn.
5. **Model Evaluation:** Assess the model's performance using metrics such as accuracy, precision, and recall.
6. **Visualize Decision Tree:** Optionally, visualize the decision tree for interpretability.

## Expectations:

By the end of this notebook, we should have a comprehensive understanding of building a decision tree classifier for customer purchase prediction. The insights gained can inform marketing strategies and contribute to better customer engagement.

Let's dive into the exciting world of data-driven customer purchase prediction!
"""

!pip install --upgrade seaborn

# import all library to requreted
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
from sklearn.tree import plot_tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import RandomizedSearchCV
from sklearn.metrics import confusion_matrix,classification_report,accuracy_score,precision_score,recall_score
import pickle

# loading the data from csv file to pandas dataframs
df= pd.read_csv('bank-full.csv')
df

df.sample(3)

# number of row and columns
df.shape

# gatting some information in DataFram
df.info()

# checking the number of mission value in each columns
df.isna().sum()

# gatting some statistical measures about the data
df.describe()

"""# Data Analysis"""

df.groupby('y').mean()

df['y'].value_counts()

# making a count plot for Y column
sns.set()
sns.countplot(x="y", data=df)
plt.show()

# checking no of parcentage yes and no
countyes=len(df[df.y=='yes'])
countno= len(df[df.y=='no'])
print(f'parcentage of yes---->',countyes/len(df.y)*100)
print(f'parcentage of no---->',countno/len(df.y)*100)

# Replacing categorical columns
df.replace({'y':{'no':0,'yes':1}},inplace=True)

sns.distplot(df['age'][df['y']==1])
sns.distplot(df['age'][df['y']==0])

# no of y Age base
plt.figure(figsize=(10,5))
sns.countplot(x='age', hue='y', data=df)
plt.show()

plt.scatter(x=df.age[df.y==1],y=df.duration[df.y==1],c='blue')
plt.scatter(x=df.age[df.y==0],y=df.duration[df.y==0],c='red')
plt.legend(['Have subscrive' , "Haven't subscrive"])
plt.xlabel('Age')
plt.ylabel('Duration')
plt.show()

# checking parcentage of people y in age
df.groupby(['age'])['y'].mean()

df['job'].value_counts()

# making a count plot for job column
plt.figure(figsize=(30,10))
sns.countplot(x="job", data=df)
plt.show()

# no of y job base
plt.figure(figsize=(30,10))
sns.countplot(x='job', hue='y', data=df)
plt.show()

plt.figure(figsize=(15,8))
plt.scatter(x=df.job[df.y==1],y=df.duration[df.y==1],c='blue')
plt.scatter(x=df.job[df.y==0],y=df.duration[df.y==0],c='red')
plt.legend(['Have subscrive' , "Haven't subscrive"])
plt.xlabel('job')
plt.ylabel('Duration')
plt.show()

# checking parcentage of people y in job
df.groupby(['job'])['y'].mean()

# making a count plot for marital column
plt.figure(figsize=(10, 5))
sns.countplot(x='marital', data=df)
plt.show()

# no of y marital base
plt.figure(figsize=(10, 5))  # Adjust the figure size as needed
sns.countplot(x='marital', hue='y', data=df)
plt.show()

# plt.figure(figsize=(15,8))
plt.scatter(x=df.marital[df.y==1],y=df.duration[df.y==1],c='blue')
plt.scatter(x=df.marital[df.y==0],y=df.duration[df.y==0],c='red')
plt.legend(['Have subscrive' , "Haven't subscrive"])
plt.xlabel('marital')
plt.ylabel('Duration')
plt.show()

# checking parcentage of people y in marital
df.groupby(['marital'])['y'].mean()

df['education'].value_counts()

# making a count plot for Y column
plt.figure(figsize=(10, 5))
sns.countplot(x='education', data=df)
plt.show()

# no of y education base
plt.figure(figsize=(10, 5))  # Adjust the figure size as needed
sns.countplot(x='education', hue='y', data=df)
plt.show()

plt.scatter(x=df.education[df.y==1],y=df.duration[df.y==1],c='blue')
plt.scatter(x=df.education[df.y==0],y=df.duration[df.y==0],c='red')
plt.legend(['Have subscrive' , "Haven't subscrive"])
plt.xlabel('education')
plt.ylabel('Duration')
plt.show()

# checking parcentage of people y in education
df.groupby(['education'])['y'].mean()

# making a count plot for housing column
plt.figure(figsize=(10, 5))  # Adjust the figure size as needed
sns.countplot(x='housing', data=df)
plt.show()

# no of y housing base
plt.figure(figsize=(10, 5))
sns.countplot(x='housing', hue='y', data=df)
plt.show()

plt.scatter(x=df.housing[df.y==1],y=df.duration[df.y==1],c='blue')
plt.scatter(x=df.housing[df.y==0],y=df.duration[df.y==0],c='red')
plt.legend(['Have subscrive' , "Haven't subscrive"])
plt.xlabel('housing')
plt.ylabel('Duration')
plt.show()

# checking parcentage of people y in housing
df.groupby(['housing'])['y'].mean()

df.columns

# making a count plot for loan column
plt.figure(figsize=(10, 5))
sns.countplot(x='loan', data=df)
plt.show()

# no of y loan base
plt.figure(figsize=(10, 5))
sns.countplot(x='loan', hue='y', data=df)
plt.show()

plt.scatter(x=df.loan[df.y==1],y=df.duration[df.y==1],c='blue')
plt.scatter(x=df.loan[df.y==0],y=df.duration[df.y==0],c='red')
plt.legend(['Have subscrive' , "Haven't subscrive"])
plt.xlabel('loan')
plt.ylabel('Duration')
plt.show()

# checking parcentage of people y in loan
df.groupby(['loan'])['y'].mean()

sns.pairplot(data=df)

# sns.pairplot(data=df,hue='y',vars=['age','job','marital','education','housing','loan','balance','duration'])

plt.figure(figsize=(10,10))
sns.heatmap(data=df.corr(),annot=True,cmap='viridis')

df.corr()

df.sample(4)

"""# Encoding"""

df.info()

# Encoding categorical columns
df['job'].value_counts()

# Encoding categorical columns
df['marital'].value_counts()

# Encoding categorical columns
df['education'].value_counts()

# Encoding categorical columns
df['default'].value_counts()

# Encoding categorical columns
df['housing'].value_counts()

# Encoding categorical columns
df['loan'].value_counts()

# Replacing all categorical columns
df.replace({'job':{ 'blue-collar' : 0,
                    'management'  : 1,
                   'technician'   : 2,
                    'admin.'      : 3,
                    'services'    : 4,
                    'retired'     : 5,
                    'self-employed':6,
                    'entrepreneur' :7,
                    'unemployed'   :8,
                    'housemaid'    :9,
                    'student'      :10,
                    'unknown'      :11, },
            'marital':{'married':0,'single':1,'divorced':2},
            'education':{'secondary':0,'tertiary':1,'primary':2,'unknown':3},
            'default':{'no':0,'yes':1},
            'housing':{'no':0,'yes':1},
            'loan':{'no':0,'yes':1}
                      },inplace=True)

# Drop columns
df.drop(columns=['contact','day','month','poutcome'],inplace=True)

df.sample(5)

"""# Pre-Modeling"""

x=df.drop(columns=['y'])
y=df.y

x.shape

y.shape

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=10)

"""# Using Logistic Regression"""

Lor=LogisticRegression()
Lor.fit(x_train,y_train)

Lor.score(x_test,y_test)

train_score = Lor.score(x_train,y_train)
print(train_score)

test_score = Lor.score(x_test,y_test)
print(test_score)

print(classification_report(y_test,Lor.predict(x_test)))

print(confusion_matrix(y_test,Lor.predict(x_test)))

"""# Using RandomForestClassifier"""

Rm = RandomForestClassifier()
Rm.fit(x_train,y_train)

Rm.score(x_test,y_test)

train_score = Rm.score(x_train,y_train)
print(train_score)

test_score = Rm.score(x_test,y_test)
print(test_score)

print(classification_report(y_test,Rm.predict(x_test)))

print(confusion_matrix(y_test,Rm.predict(x_test)))

"""# Using DecisionTreeClassifier"""

Dc = DecisionTreeClassifier()
Dc.fit(x_train,y_train)

y_pred = Dc.predict(x_test)
y_pred

# Testing Data Evaluation

y_pred = Dc.predict(x_test)

cm = confusion_matrix(y_test,y_pred)
print(f"Confusion Matrix =\n",cm)
print("*"*50)
ac = accuracy_score(y_test,y_pred)
print(f"Accuracy Score = {ac}")
print("*"*50)
cr = classification_report(y_test,y_pred)
print(f"Classification report= \n{cr}")

# Training Data Evaluation

y_pred = Dc.predict(x_train)

cm = confusion_matrix(y_train,y_pred)
print(f"Confusion Matrix =\n",cm)
print("*"*50)
ac = accuracy_score(y_train,y_pred)
print(f"Accuracy Score = {ac}")
print("*"*50)
cr = classification_report(y_train,y_pred)
print(f"Classification report= \n{cr}")

# bias - Variance Tradeoff

# bias >> low
# variance >> high

# Overfitting

"""# Randoimisezed search"""

DC= DecisionTreeClassifier(min_samples_split =  15,min_samples_leaf =  16,max_depth=3,criterion='gini')

DC.fit(x_train,y_train)

# Testing Data Evaluation

y_pred = DC.predict(x_test)

cm = confusion_matrix(y_test,y_pred)
print(f"Confusion Matrix =\n",cm)
print("*"*50)
ac = accuracy_score(y_test,y_pred)
print(f"Accuracy Score = {ac}")
print("*"*50)
cr = classification_report(y_test,y_pred)
print(f"Classification report= \n{cr}")

# Training Data Evaluation

y_pred = DC.predict(x_train)

cm = confusion_matrix(y_train,y_pred)
print(f"Confusion Matrix =\n",cm)
print("*"*50)
ac = accuracy_score(y_train,y_pred)
print(f"Accuracy Score = {ac}")
print("*"*50)
cr = classification_report(y_train,y_pred)
print(f"Classification report= \n{cr}")

# Bias >> low
# variance >> low

plt.figure(figsize=(100,50))
tree_fig = plot_tree(DC, feature_names=x.columns, filled=True, class_names=['yes','no'])
plt.savefig("decision_tree.png")

"""# Save Model File"""

with open('model.pkl','wb') as file:
    pickle.dump(DC,file)

"""# Read pickle file"""

pkl=pd.read_pickle('model.pkl')
pkl

