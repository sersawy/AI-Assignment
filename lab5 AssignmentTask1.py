# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 09:28:55 2021

@author: workstation
"""

import matplotlib.pyplot as plt
import pandas as pd

# 1.Read the dataset, convert it to DataFrame and display some from it.
dataset=pd.read_csv("Wuzzuf_Jobs.csv")
x=dataset.iloc[:,[0]].values

# 2.Display structure and summary of the data.
dataset.describe()

# 3.Clean the data (null, duplications).
dataset=dataset.dropna()
dataset.drop_duplicates(keep = "first", inplace = True)

# 4.Count the jobs for each company and display that in order (What are the most demanding companies for jobs?).
b=dataset['Company'].value_counts()
print(b)
print("the most demanding companies for jobs is: "+b.index[0])

# 5.Show step4 in a pie chart.
plt.pie(b,labels=b.index)
plt.show() 

# 6.Find out what are the most popular job titles
c=dataset['Title'].value_counts()

print("the most popular job is : "+c.index[0])

# 7.Show step 6 in bar chart.
xx = list(c.index)
yy = list(c.values)
plt.bar(xx, yy, color ='maroon',
		width = 0.4)
plt.xlabel("Job title")
plt.ylabel("the num of job title")
plt.title("he most popular job titles")
plt.show()

# 8.Find out the most popular areas?
d=dataset['Location'].value_counts()

print("the most popular areas is : "+d.index[0])

# 9.Show step8 in bar chart.
xxx = list(d.index)
yyy = list(d.values)
plt.bar(xxx, yyy, color ='maroon',
		width = 0.4)
plt.xlabel("location")
plt.ylabel("the num of location")
plt.title("the most popular areas")
plt.show()

# 10.Print skills one by one , their count, and order the output to find out the most important skills required.
e=dataset['Skills'].value_counts()
print(e)
print("the most important skills required"+e.index[0])





