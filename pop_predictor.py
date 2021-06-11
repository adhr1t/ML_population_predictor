# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 11:08:56 2021

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
df