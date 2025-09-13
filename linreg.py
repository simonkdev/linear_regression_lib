import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#%matplotlib inline

df = pd.read_csv('data/ex1data1.txt')
df.columns = ['Population', 'Profit']

ax = sns.scatterplot(data=df, x='Population', y='Profit')   
ax.set(xlabel='Population of City in 10,000s', ylabel='Profit in $10,000s', title='Scatter plot of training data')

