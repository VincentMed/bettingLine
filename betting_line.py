# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 09:55:05 2022

@author: Vincent Medrano
"""

import pandas as pd
import matplotlib.pyplot as plt

dataSet = pd.read_csv('lineVSactual.csv')

dataSet.columns
betLine = dataSet["line"]
result = dataSet["actual"]

error = result - betLine

plt.hist(dataSet["line"], alpha = 0.5, label = "line", density = True)
plt.hist(dataSet["actual"], alpha = 0.5, label = "actual", density = True)
plt.legend()
plt.grid()
plt.show()