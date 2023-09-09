# -*- coding: utf-8 -*-
"""Untitled13.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1R3osfrvz-lcW-A6i-E49ddsucNX5O4o6
"""

pip install kaggle

from google.colab import files

uploaded = files.upload()

for fn in uploaded.keys():
  print('User uploaded file "{name}" with length {length} bytes'.format(
      name=fn, length=len(uploaded[fn])))

!mkdir -p /root/.kaggle
!mv kaggle.json /root/.kaggle/

!kaggle datasets download -d timoboz/tesla-stock-data-from-2010-to-2020

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from xgboost import XGBClassifier
from sklearn import metrics

import warnings
warnings.filterwarnings('ignore')

df = pd.read_csv('/content/tesla-stock-data-from-2010-to-2020.zip')
df.head()

df.shape

df.describe()

df.info()

plt.figure(figsize=(15,5))
plt.plot(df['Close'])
plt.title('TESLA STOCK PRICE', fontsize=15)
plt.ylabel('Price in dollars.')
plt.show()

df.head()

df[df['Close'] == df['Adj Close']].shape

df = df.drop(['Adj Close'], axis=1)

df.isnull().sum()

features = ['Open', 'High', 'Low', 'Close', 'Volume']

plt.subplots(figsize=(20,10))

for i, col in enumerate(features):
 plt.subplot(2,3,i+1)
 sb.distplot(df[col])
plt.show()

plt.subplots(figsize=(20,10))
for i, col in enumerate(features):
 plt.subplot(2,3,i+1)
 sb.boxplot(df[col])
plt.show()

plt.figure(figsize=(10, 10))

# As our concern is with the highly
# correlated features only so, we will visualize
# our heatmap as per that criteria only.
sb.heatmap(df.corr() > 0.9, annot=True, cbar=False)
plt.show()