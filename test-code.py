#!/usr/bin/env ipython
# Dependencies

import pandas as pd
from pandas import DataFrame
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler
import seaborn as sns
import matplotlib.pyplot as plt

train_data = pd.read_csv("if_down_train.csv", skiprows=1)
test_data = pd.read_csv("if_down_test.csv", skiprows=1)

print(train_data.head())
test_data.head()
x= np.array(train_data)
y = np.array(test_data)

kmeans = KMeans(n_clusters=2) # You want cluster the passenger records into 2: Survived or Not survived
kmeans.fit(x)
y_kmeans = kmeans.predict(x)
plt.scatter(x[:,0], x[:,1], c=y_kmeans, cmap='viridis')
centers = kmeans.cluster_centers_
plt.scatter(centers[:, 0], centers[:, 1], c='black', s=200, alpha=0.5)
plt.xlabel('Timestamp')
plt.ylabel('Value')
plt.show()


