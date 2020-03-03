#!/usr/bin/env python
# coding: utf-8

# In[89]:


# =============================================================================
# Assignment: Final Project - Phase 1
# Filename: f1.py
# Description: Final Project
# Date: 04/14/2020
# Author: Tarini Dash
# =============================================================================

import pandas as pd
import math
import matplotlib.pyplot as plt


def main():
    fig, axs = plt.subplots(9,figsize=(15,100))
    count = 0
    col = ["Scn", "A2", "A3", "A4", "A5", "A6", "A7", "A8", "A9", "A10", "Class"]
    
    # read from file
    df = pd.read_csv('breast-cancer-wisconsin.data', na_values = '?', names = col)
    
    # drop columns
    df = df.drop(columns=['Scn', 'Class'])
    
    # replace missing value with mean
    df = df.fillna(df.mean()['A7'])
    

    for col_name in df.columns:
        print("Attribute",col_name," --------------------------")
        print("\t Mean \t\t\t:", round(df[col_name].mean(),1))
        print("\t Median \t\t:", round(df[col_name].median(),1))
        print("\t Variance \t\t:", round(df[col_name].var(),1))
        print("\t Standard Deviation \t:", round(df[col_name].std(),1), end="\n\n")
        axs[count].set_title("Histogram of attribute " + col_name)
        axs[count].set_xlabel("Value of attribute")
        axs[count].set_ylabel("Number of data points")
        axs[count].hist(df[col_name],bins=10, color="blue", edgecolor='black',linewidth=1.2, alpha=0.5) 
        count += 1
        
    fig.tight_layout()
    
    
#invoke main method
if __name__ == "__main__":
    main()


# In[ ]:




