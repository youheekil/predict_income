# src/clean_data_test.py 

import pandas as pd
import logging
from joblib import load
import pytest

import src.config as config
from src.clean_data import clean_data, removing_NA, removing_special_case

FORMAT = "%(asctime)s | %(name)s - %(levelname)s - %(message)s"
LOG_FILEPATH = "logs/testing.log/"
logging.basicConfig(
    filename=LOG_FILEPATH,
    level=logging.INFO,
    filemode='w',
    format=FORMAT)


def test_clean_data():
    '''
    Testing all functions of clean_data module
    '''
    col = ['age', 'workclass', 'fnlgt', 'education', 'education_num',
        'marital_status', 'occupation', 'relationship', 'race', 'sex',
        'capital_gain', 'capital_loss', 'hours_per_week', 'native_country',
        'salary']

    df = clean_data()
    new_df = removing_special_case(data=df)
    na_removed_df = removing_NA(data=new_df)

    try:
        assert df.shape[0] > 0
        assert df.shape[1] > 0
    except AssertionError as err:
        logging.error(
            "Testing clean_data: The file doesn't appear to have rows and columns")
        raise err
    

    try:
        assert sum(df.columns == col) == 15
    except AssertionError as err:
        logging.error(
            "Testing clean_data: The file doesn't appear to have space removal on each column of the data set"
        )

    
    try:
        assert df['workclass'][10] == 'Private' 
    except AssertionError as err:
        logging.error(
            "Testing clean_data: The file doesn't appear to have space removal on each value of the data set"
        )

    
    try:
        assert df['workclass'][10] == 'Private' 
    except AssertionError as err:
        logging.error(
            "Testing clean_data: The file doesn't appear to have space removal on each value of the data set"
        )
    
    try:
        spc_cnt_columns = 0
        for key in new_df.keys():
            for val in new_df[key]:
                if val == "?":
                    spc_cnt_columns += 1

        assert spc_cnt_columns == 0 
    except AssertionError as err:
        logging.error(
            "Testing clean_data: The file doesn't appear to have special case (?) removal in the data set"
        )
    
    try:
        assert na_removed_df.isnull().sum().sum() == 0
    except AssertionError as err:
        logging.error(
            "Testing clean_data: The file doesn't appear to have NA in the data set"
        )


    try: 
        dataframe = pd.read_csv("data/processed/processed_census.csv")

        assert dataframe.shape[0] > 0
        assert dataframe.shape[1] > 0

    except FileNotFoundError as err:
        logging.error(
            "Testing clean data: The file is not saved properly in the right location"
        )



