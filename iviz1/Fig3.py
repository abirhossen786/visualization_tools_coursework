import numpy as np
import pandas as pd
import scipy.stats as st
pd.set_option('display.max_columns', None)

import math

import matplotlib.pyplot as plt
%matplotlib inline

import seaborn as sns
sns.set_style('whitegrid')

import missingno as msno

from sklearn.preprocessing import StandardScaler
from scipy import stats



import os
for dirname, _, filenames in os.walk('/vgsales.csv'):
    for filename in filenames:
        print(os.path.join(dirname, filename))
		
		
drop_row_index = data[data['Year'] > 2015].index
data = data.drop(drop_row_index)


data_platform = data.groupby(by=['Platform'])['Global_Sales'].sum()
data_platform = data_platform.reset_index()
data_platform = data_platform.sort_values(by=['Global_Sales'], ascending=False)
# data_platform

plt.figure(figsize=(15, 10))
ax = sns.barplot(x="Platform", y="Global_Sales", data=data_platform)
plt.xlabel('Video game platform', fontsize=22);
plt.ylabel('Global sales in millions', fontsize=22);
plt.xticks(rotation=90, fontsize=20)
plt.yticks(fontsize=20)
plt.title('Global sales of video game platforms', fontsize=25,weight="bold")
plt.savefig('foo.png', dpi=500)
		
