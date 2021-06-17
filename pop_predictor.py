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

"""
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
x = ind.iloc[:, 0].values.reshape(-1, 1)
y = ind.iloc[:, 1].values.reshape(-1, 1)
model = LinearRegression().fit(x, y)
y_pred = model.predict([[2020]])
y_pred
"""

def createCountryLists(df):
    df.rename(columns={'Country Name':'Country_Name'},inplace=True)
    #change all Country Names to lowercase
    df["Country_Name"] = df["Country_Name"].apply(lambda row: row.lower())
    lists = df['Country_Name'].unique().tolist()
    with open('country_list.json','w', encoding='utf-8') as f:
        json.dump(lists, f, ensure_ascii=False,indent=4)
        
    return lists, df
    

def createModel(df):
    x = df.iloc[:, 0].values.reshape(-1, 1)
    y = df.iloc[:, 1].values.reshape(-1, 1)
    model = LinearRegression().fit(x, y)
    return model
    
    
def main():
    country = input("Which country would you like to know about? ").lower()
    year = int(input("Which year do you want to predict the population of? "))
    df = pd.read_csv("worldPopulations.csv")
    lists, df = createCountryLists(df)
    if country in lists:
        df
    
    
if __name__ == "__main__":
    main()