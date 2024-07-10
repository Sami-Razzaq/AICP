import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from statsmodels.tsa.seasonal import seasonal_decompose

from pdb import set_trace
import warnings
warnings.filterwarnings('ignore')

# Part 1
data = pd.read_csv('Instagram-Reach.csv')

# print(data.isnull().sum())
# print(data.isna().sum())

data['Date'] = pd.to_datetime(data['Date'], utc=False)
data['Day'] = data['Date'].dt.day_name()
dataDay = data.groupby('Day')['Instagram reach'].sum()
# Setting order of days correct
ordered_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
dataDay = dataDay.reindex(ordered_days)
d30 = data[:30] # Gets first 30 days of data

# print(data.head())
# print(data.tail())
# print(data.describe())
# print(data.info())

# Part 2
# Line Plot
# data.plot(x='Date', y='Instagram reach', xlabel='Time', ylabel='Instagram Reach', title='Instagram Reach over Time')
# plt.grid(axis='y', linestyle='--', alpha=0.7)
# plt.tight_layout()

# Bar Plot
# data['Date'] = data['Date'].dt.date
# box = data.plot.bar(x='Date', xlabel='Time', ylabel='Instagram Reach', title='Instagram Reach over Time', rot='vertical')
# box.grid(axis='y', linestyle='--', alpha=0.7)
# box.get_xaxis().set_ticks([])
# plt.tight_layout()

# Box Plot
# data.plot.box(title='Instagram Reach over Time')
# plt.grid(axis='y', linestyle='--', alpha=0.7)
# plt.tight_layout()

# Mean Median Standard Deviation for Weekly Grouped Data
# print("Mean: ")
# print(data.groupby('Day').mean())
# print("\nMedian: ")
# print(data.groupby('Day').median())
# print("\nStandard Deviation: ")
# print(data.groupby('Day').std())

# Bar Plot per Week Day
# plt.figure()
# dataDay.plot.bar(xlabel='Days of the Week', ylabel='Instagram Reach', title='Instagram Reach for Each Day of the Week', edgecolor='Black', rot=45)
# plt.grid(axis='y', linestyle='--', alpha=0.7)
# plt.tight_layout()

# Part Three
# Trend and Seasonal Analysis
# Period = 30 shows the monthly change in trend
analysis = seasonal_decompose(data['Instagram reach'], model="multiplicative", period=30)
analysis.plot()

plt.show()