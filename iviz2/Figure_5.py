# math opeations
# import math
# produce random numbers
# import random
# to load json files
import json
# datetime oprations
from datetime import timedelta
# to get web contents
from urllib.request import urlopen

# for numerical analyiss
import numpy as np
# to store and process data in dataframe
import pandas as pd
# basic visualization package
import matplotlib.pyplot as plt
# advanced ploting
import seaborn as sns

# interactive visualization
import plotly.express as px
import plotly.graph_objs as go
# import plotly.figure_factory as ff
from plotly.subplots import make_subplots
# for offline ploting
from plotly.offline import plot, iplot, init_notebook_mode
init_notebook_mode(connected=True)
# converter
# from pandas.plotting import register_matplotlib_converters
# register_matplotlib_converters()   

# hide warnings
import warnings
warnings.filterwarnings('ignore')

# to USA states details
# import us

# color pallette
cnf, dth, rec, act = '#393e46', '#ff2e63', '#21bf73', '#fe9801' 

# seaborn plot style
# sns.set_style('darkgrid')

# Full data
# =========

full_table = pd.read_csv('../input/corona-virus-report/covid_19_clean_complete.csv')
full_table.head()
#full_table.shape

# Grouped by day, country
# =======================

full_grouped = pd.read_csv('../input/corona-virus-report/full_grouped.csv')
full_grouped['Date'] = pd.to_datetime(full_grouped['Date'])
# full_grouped.head()


# Day wise
# ========

day_wise = pd.read_csv('../input/corona-virus-report/day_wise.csv')
day_wise['Date'] = pd.to_datetime(day_wise['Date'])
# day_wise.head()

# Country wise
# ============

country_wise = pd.read_csv('../input/corona-virus-report/country_wise_latest.csv')
country_wise = country_wise.replace('', np.nan).fillna(0)
# country_wise.head()

# Worldometer data
# ================

worldometer_data = pd.read_csv('../input/corona-virus-report/worldometer_data.csv')
worldometer_data = worldometer_data.replace('', np.nan).fillna(0)
# worldometer_data.head()

temp = day_wise[['Date','Deaths', 'Recovered', 'Active']].tail(1)
temp = temp.melt(id_vars="Date", value_vars=['Active', 'Deaths', 'Recovered'])
fig = px.treemap(temp, path=["variable"], values="value", height=225, 
                 color_discrete_sequence=[act, rec, dth])
fig.data[0].textinfo = 'label+text+value'
fig.show()

def plot_daywise_line(col, hue):
    fig = px.line(day_wise, x="Date", y=col, width=700, color_discrete_sequence=[hue])
    fig.update_layout(title=col, xaxis_title="", yaxis_title="")
    fig.show()

temp = full_grouped.groupby('Date')['Recovered', 'Deaths', 'Active'].sum().reset_index()
temp = temp.melt(id_vars="Date", value_vars=['Recovered', 'Deaths', 'Active'],
                 var_name='Case', value_name='Count')
temp.head()

fig = px.area(temp, x="Date", y="Count", color='Case', height=600, width=700,
             title='Cases over time', color_discrete_sequence = [rec, dth, act])
fig.update_layout(xaxis_rangeslider_visible=True)
fig.show()    