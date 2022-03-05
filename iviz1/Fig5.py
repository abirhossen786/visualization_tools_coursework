import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
%matplotlib inline

data = pd.read_csv('../input/videogamesales/vgsales.csv')

data.isnull().sum() # To check Null Values

data.dropna(inplace = True) # To drop null values
# Preprocessing our Data for some Useful Insights 
data_decade = data[data.Year > 2010] 


plt.figure(dpi=125)
sns.regplot(x=data['NA_Sales'],y=data['Global_Sales'])
plt.xlabel('North America Sales', fontsize = 15)
plt.ylabel('Global Sales', fontsize = 15)
plt.title('North America Sales and Global Sales', fontsize = 15)
plt.xticks(fontsize=14)
plt.yticks(fontsize=15)
plt.savefig("n.png",dpi=500)
plt.show()

plt.figure(dpi=125)
sns.regplot(x=data['EU_Sales'],y=data['Global_Sales'])
plt.xlabel('Europe Sales', fontsize = 15)
plt.ylabel('Global Sales', fontsize = 15)
plt.title('Europe Sales and Global Sales', fontsize = 15)
plt.xticks(fontsize=14)
plt.yticks(fontsize=15)
plt.savefig("e.png",dpi=500)
plt.show()