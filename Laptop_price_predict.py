# %%
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression

dataset=pd.read_csv(".\ML\laptop_info.csv")
# model=LinearRegression()
# x_start= detaset_merged.drop('Price',axis='columns')
# y_start=detaset_merged.Price
# # model.fit(x_start,y_start)
# # model.score(x_start,y_start)
# dataset.drop(['Company'],axis=1)

dataset['RAM']=dataset['RAM'].fillna(0)
dataset['Price']=dataset['Price'].fillna(0)
dataset['Company']=dataset['Company'].fillna(0)
# dataset.drop(20)
# print(dataset)
# First we need to create dummy variable columns to avoid complication while doing one hot encoding

dummies=pd.get_dummies(dataset.Company)
dataset = pd.concat([dataset,dummies],axis=1)
# print (dataset)
# There are other smart ways to replace value and I tried them all but it somehow didn't work on my device.

dataset['Acer']=dataset['Acer'].replace(True,1)
dataset['Acer']=dataset['Acer'].replace(False,0)
dataset['Asus']=dataset['Asus'].replace(False,0)
dataset['Asus']=dataset['Asus'].replace(True,1)
dataset['HP']=dataset['HP'].replace(False,0)
dataset['HP']=dataset['HP'].replace(True,1)
dataset['Dell']=dataset['Dell'].replace(False,0)
dataset['Dell']=dataset['Dell'].replace(True,1)
dataset['Lenovo']=dataset['Lenovo'].replace(False,0)
dataset['Lenovo']=dataset['Lenovo'].replace(True,1)
dataset['Apple']=dataset['Apple'].replace(False,0)
dataset['Apple']=dataset['Apple'].replace(True,1)
dataset['MSI']=dataset['MSI'].replace(False,0)
dataset['MSI']=dataset['MSI'].replace(True,1)
dataset['Microsoft']=dataset['Microsoft'].replace(True,1)
dataset['Microsoft']=dataset['Microsoft'].replace(False,0)
dataset['Samsung']=dataset['Samsung'].replace(True,1)
dataset['Samsung']=dataset['Samsung'].replace(False,0)
dataset['Toshiba']=dataset['Toshiba'].replace(False,0)
dataset['Toshiba']=dataset['Toshiba'].replace(True,1)
print(dataset)
x=dataset[['RAM','Acer','Asus','Toshiba','Microsoft','MSI','Samsung','Lenovo','Dell','HP','Apple']].values
y=dataset[['Price']].values
y=StandardScaler().fit_transform(y)
x=StandardScaler().fit_transform(x)
# Using linear regression for training the model 
model = LinearRegression()
model.fit(x,y)
pred_score=model.score(x,y)
print(f"\n This trained model's prediction score is {pred_score*100}%")


# %%
