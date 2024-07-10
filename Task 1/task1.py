import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

from pdb import set_trace
import warnings
warnings.filterwarnings('ignore')

# Part 1
data = pd.read_csv('Instagram-Reach.csv')

# print(data.isnull().sum())
# print(data.isna().sum())
# print(data.head())
data['Date'] = pd.to_datetime(data['Date'])
data['Day'] = data['Date'].dt.day_name()
dataDay = data.groupby('Day')

# print(data.head())
# print(data.tail())

# Part 2
# Line Plot
# data.plot(x='Date', y='Instagram reach', title='Instagram Reach over Time')

# Bar Plot for 30 Days
d30 = data[:30]
# d30.plot.bar(x='Date', title='Instagram Reach over Time - 30 Days')

# Box Plot
# data.plot.box(title='Instagram Reach over Time')

# Mean Median Standard Deviation for Weekly Grouped Data
# print("Mean: ")
# print(data.groupby('Day').mean())
# print("\nMedian: ")
# print(data.groupby('Day').median())
# print("\nStandard Deviation: ")
# print(data.groupby('Day').std())

# Bar Plot per Week Day
# dataDay.plot.bar(x='Day', y='Instagram reach', title='Instagram Reach over Time')

# Bar Plot per Weekday combined for 30 days
# sns.catplot(
#     x="Date",       # x variable name
#     y="Instagram reach",       # y variable name
#     hue="Day",  # group variable name
#     data=d30,     # dataframe to plot
#     kind="bar",
# )

plt.show()