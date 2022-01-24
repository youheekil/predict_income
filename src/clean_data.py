# src/clean_data.py
"""
cleaning messy data

author : Youhee
data: Jan 2022
"""


# libraries
import pandas as pd


import config


def clean_data():
    """ Cleaning data such as removing space in the columns and save it at data/processed folder

    Returns:
        processed_data: show 10 rows of the processed data. 
    """
    raw_data = pd.read_csv(config.RAW_DATA_FILE)
    
    # remove space in column 
    _columns = raw_data.columns
    replaced_columns = []

    for column in _columns:
        col = column.replace(" ", "")
        replaced_columns.append(col)
    
    clean_data = raw_data.dropna()
    clean_data.columns = replaced_columns

    clean_data.to_csv("data/processed/processed_census.csv", index = False, header = True)

    return clean_data.head(10)
