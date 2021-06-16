"""
@author: adhri
"""

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import re
import json
import warnings
warnings.filterwarnings("ignore")

df = pd.read_csv("worldPopulations.csv")
ind = df.loc[df['Country Name']=='India']

#remove Country Code, Indicator Name, and Indicator Code
ind.drop(["Country Name","Country Code", "Indicator Name", "Indicator Code"], axis=1, inplace=True)
ind = ind.T
#df.drop(["Country Code", "Indicator Name", "Indicator Code"], axis=1, inplace=True)

#remove rows with None values
ind.dropna(inplace = True)

#change column names
ind = ind.reset_index().rename(columns = {"index":"year", 107:"population"})

#model creation and prediction
x = df.iloc[:, 0].values.reshape(-1, 1)
y = df.iloc[:, 1].values.reshape(-1, 1)
model = LinearRegression().fit(x, y)
y_pred = model.predict([[2020]])
y_pred



def createModel(df):
    x = df.iloc[:, 0].values.reshape(-1, 1)
    y = df.iloc[:, 1].values.reshape(-1, 1)
    model = LinearRegression().fit(x, y)
    
    
def main():
    country = input("Which country would you like to know about?").lower()
    year = input("Which year do you want to predict the population of?").lower()
    
    
if __name__ == "__main__":
    main()