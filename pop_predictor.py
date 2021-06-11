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

#remove Country Code, Indicator Name, and Indicator Code
df.drop(["Country Code", "Indicator Name", "Indicator Code"], axis=1, inplace=True)