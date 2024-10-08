import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
dataset = pd.read_csv("naive.csv")
X = dataset.iloc[:, [0,1]].values
y = dataset.iloc[:, 2].values
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test =train_test_split(X,y,test_size= 0.25, random_state=0)
# importing standard scaler
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler() 
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.fit_transform(X_test)
from sklearn.naive_bayes import BernoulliNB
from sklearn.naive_bayes import GaussianNB
classifer1 = GaussianNB()
classifer1.fit(X_train, y_train)
y_pred1 = classifer1.predict(X_test)
from sklearn.metrics import accuracy_score
print(accuracy_score(y_test,y_pred1))
