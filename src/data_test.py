# src/data_test

# HOT ENCODING 
# LOAD ENCODING, LIB ETC
import logging
import pandas as pd
from pytest import fixture
from src.data import get_cat_features, split_data, process_data

FORMAT = "%(asctime)s | %(name)s - %(levelname)s - %(message)s"
LOG_FILEPATH = "logs/testing.log/"
logging.basicConfig(
    filename=LOG_FILEPATH,
    level=logging.INFO,
    filemode='w',
    format=FORMAT)

@fixture
def _processed_data():
    try:
        df = pd.read_csv("data/processed/processed_census.csv")
        logging.info("Testing importing processed data: SUCCESS")
    except FileNotFoundError as err:
        logging.error("Testing importing processed data: The file wasn't found")
        raise err
    return df


def test_data(_processed_data):
    """Testing data module
    """
    try:
        X_train, y_train, encoder, lb = process_data(_processed_data, categorical_features=get_cat_features(), label = "salary", training=True, encoder=None, lb=None)
        
        sum(X_train, 2)
    except AttributeError as err:
        logging.error(
            "Testing processed_data: ENCODING is not successfully completed"
        )
    

