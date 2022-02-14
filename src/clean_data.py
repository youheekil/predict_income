# src/clean_data.py
"""
cleaning messy data

author : Youhee
data: Jan 2022
"""


# libraries
import numpy as np
import pandas as pd
from re import search

import src.config as config
from src.data import get_cat_features


def clean_data():
    """
    Cleaning data such as removing space in the columns and save it at data/processed folder

    Returns:
        clean_data: data without space
    """
    raw_data = pd.read_csv(config.RAW_DATA_FILE)
    spc = "-"
    # remove space in column 
    _columns = raw_data.columns
    replaced_columns = []
    for column in _columns:
        col = column.replace(" ", "")
        if search(spc, col):
            col = col.replace("-", "_")
        else: 
            pass
        replaced_columns.append(col)
    raw_data.columns = replaced_columns
    cleaned_data = raw_data.applymap(lambda x: x.strip() if isinstance(x, str) else x)
    return cleaned_data


def removing_special_case(data):
    """
    Replaced ? in data to NA

    Args:
        data: data removed spaces from `removing_spaces` function
    
    Returns:
        processed_data: data removed special string cases and saved the data under
            the data/processed folder
    """
    cols = get_cat_features()
    # data.applymap(lambda x: np.nan if x == '?' else x)
    data[cols] = data[cols].replace("?", np.NaN)
    return data


def removing_NA(data):
    """
    Removing NA in data

    Args:
        data ([type]): data removed spaces and replaced special string cases ("?") to NA

    Returns:
        data: data removed NA
    """
    data = data.dropna()
    data.to_csv(config.CLEAN_DATA_FILE, index = False, header = True)
    return data


def run_clean_data():
        df = clean_data()
        new_df = removing_special_case(data=df)
        _ = removing_NA(data=new_df)
