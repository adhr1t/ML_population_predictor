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
ind.head()

#change column names
ind.reset_index().rename(columns = {"index":"year", 107:"population"})
ind.head()
