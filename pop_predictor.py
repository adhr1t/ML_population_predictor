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

#add country names to list and create json file
def createCountryLists(df):
    df.rename(columns={'Country Name':'Country_Name'},inplace=True)
    #change all Country Names to lowercase
    df["Country_Name"] = df["Country_Name"].apply(lambda row: row.lower())
    lists = df['Country_Name'].unique().tolist()
    with open('country_list.json','w', encoding='utf-8') as f:
        json.dump(lists, f, ensure_ascii=False,indent=4)
    return lists, df
    
#create df for the desired country
def makeCountryDF(country, df):
    df = df.loc[df['Country_Name']==country]
    df.drop(["Country_Name","Country Code", "Indicator Name", "Indicator Code"], axis=1, inplace=True)
    df = df.T
    df.dropna(inplace = True)
    df = df.reset_index()
    return df

#train and create ML linear regression model
def createModel(df):
    x = df.iloc[:, 0].values.reshape(-1, 1)
    y = df.iloc[:, 1].values.reshape(-1, 1)
    model = LinearRegression().fit(x, y)
    return model
    
#determine population prediction
def prediction(model, year):
    return int(model.coef_ [0][0] * year + model.intercept_[0])
    
    
def main():
    while True:
        country = input("\nWhich country would you like to know about? Or type \"close\" if you would like to exit: ").lower()
        if country == "close":
            print("\nThanks for swinging by!")
            break
        year = int(input("Which year do you want to predict the population of? "))
        df = pd.read_csv("worldPopulations.csv")
        lists, df = createCountryLists(df)
        if country in lists:
            df = makeCountryDF(country, df)
            model = createModel(df)
            pred = prediction(model, year)
            print(f"\nThe predicted population of {country.capitalize()} in {year} will be {pred:,d}")        
        else:
            print("\nPlease check your spelling or see if the country exists in the JSON file.")
    
    
if __name__ == "__main__":
    main()