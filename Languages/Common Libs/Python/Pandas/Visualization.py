#%%
%config ZMQInteractiveShell.ast_node_interactivity='all' 

#%%
# simple plot
# 1) select data to plot
# 2) df.plot
# %matplotlib inline # for jupyter notebook
import pandas as pd
# import matplotlib.pyplot as plt
# !pip list
df = pd.read_csv('Languages/Common Libs/Python/Pandas/water.csv')
df.info()
ax = df.plot()
df.head()

#%%
# assignment will stop showing object address
ax = df.plot(subplots=True, title="Water measurements off the Dutch coast")

#%%
ax = df['temp'].plot(title='Water temperature')

#%%
df['datetime'] = pd.to_datetime(df['datetime'])
df.info()
ax = df.plot(title="Water temperature", x="datetime", y="temp")

#%%
# histgram
df['temp'].plot.hist()

#%%
# box
df['temp'].plot.box()

#%%
#
df = pd.read_csv('Languages/Common Libs/Python/Pandas/nobel.csv')
df.head()
prizes_contries = df['Country'].value_counts()
prizes_contries
#%%
import os, inspect
# print(__file__)
# dir_path = os.path.dirname(os.path.realpath(__file__))
# os.chdir('/Users/leolin/Projects/Leo.Services.Algorithms')
# filename = inspect.getframeinfo(inspect.currentframe()).filename
# path = os.path.dirname(os.path.abspath(filename))
# currentFolder = os.getcwd()
# print(path)
#%%
# from inspect import currentframe, getframeinfo
# from pathlib import Path

# filename = getframeinfo(currentframe()).filename
# parent = Path(filename).resolve().parent
# print(parent)

#%%
# !pwd

#%%
