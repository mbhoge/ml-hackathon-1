#!/usr/bin/env python
# coding: utf-8

# In[3]:


def fill_missing_value(df):
    """
    This method will take a dataframe and calculate null count of each column and keep in a new dataframe.
    It will check each column, if the column contains null value then it will replace the null as below
    1. Replace null with Mode if the column is categorical
    2. Replace null with Mean if the column is numerical
    
    Note: verify null value count for each columns before and after invoking this method
    """
    null_df = df.isnull().sum()
    for col in df.columns:
        if null_df[col] > 0: # column contains null value
            if df[col].dtype == type(object): # categorical column data type is object
                mode_val = df[col].mode()[0]
                print('Mode fill ({}) -> Column: {}, Missing Count: {}'.format(mode_val, col, null_df[col]))
                df[col] = df[col].fillna(mode_val) # Mode fill for categorical column
            else:
                mean_val = df[col].mean()
                print('Mean fill ({}) -> Column: {}, Missing Count: {}'.format(mean_val, col, null_df[col]))
                df[col] = df[col].fillna(mean_val) # Mean fill for numerical column

