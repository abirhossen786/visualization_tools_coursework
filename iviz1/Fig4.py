# Import essential tools/packages

import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

# Read in dataset
DATAPATH = '/vgsales.csv'
dataset = pd.read_csv(DATAPATH)

# Test dataset
dataset.head()

null_data_year = (271 / 16598) * 100
null_data_publisher = (58/ 16598) * 100

print(f'Percentage of "Year" null data: {null_data_year}%')
print(f'Percentage of "Publisher" null data: {null_data_publisher}%')

# Data dictionary creator
def operate_data_dictionary(features, descriptors, method="set", refpath=None):
  """ Operational function to work in creating or getting data dictionary. """
  if method == "set":
    # Produce dictionary-wrapped key-value associations of feature summaries
    data_dictionary = dict(zip(FEATURES, DESCRIPTORS))
    # Convert data dictionary to cleaner reference table
    reference = pd.DataFrame(data_dictionary, index=[0])
    # Save reference table for future access
    if refpath is not None and type(refpath) == str:
      reference.to_csv(refpath, index=False)
  if method == "get":
    # Get reference table from saved data dictionary
    if refpath is not None and type(refpath) == str:
      return pd.read_csv(refpath)
    else:
      raise TypeError("Saved file for data dictionary not found.")
	  
# Initialize plotting boundaries
plt.figure(figsize=(10, 8))

# Set parameters
needed_cols = ['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales']
# Generate heatmap
sns.heatmap(dataset[needed_cols].corr().round(4), annot=True, cmap='Blues', square=True)

# Set title for correlation matrix
plt.title("Sales Correlations", fontsize=25,weight="bold")
plt.xticks(fontsize=13)
plt.yticks(fontsize=13)
plt.savefig('corr.png', dpi=500)	  
