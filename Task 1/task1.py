import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

import warnings
warnings.filterwarnings('ignore')

# Part 1
data = pd.read_csv('Instagram-Reach.csv')

# print(data.isnull().sum())
# print(data.isna().sum())
# print(data.head())
data['Date'] = pd.to_datetime(data['Date'])
data['Date'] = data['Date'].dt.date # Removes the Time Portion
# print(data.head())
# print(data.tail())

# Part 2
# Line Plot
# data.plot(x='Date', y='Instagram reach', title='Instagram Reach over Time')

# Bar Plot for 30 Days
d30 = data[:30]
# d30.plot.bar(x='Date', title='Instagram Reach over Time - 30 Days')

# Box Plot
data.plot.box(title='Instagram Reach over Time')

plt.show()