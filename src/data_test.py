# src/data_test

# HOT ENCODING 
# LOAD ENCODING, LIB ETC
import logging
import pandas as pd
from joblib import dump
from pytest import fixture
from src.data import get_cat_features, process_data

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
        logging.error("FAILED Testing importing processed data: The file wasn't found")
        raise err
    return df


def test_data(_processed_data):
    """Testing data module
    """
    try:
        X_train, y_train, encoder, lb = process_data(_processed_data, categorical_features=get_cat_features(), label = "salary", training=True, encoder=None, lb=None)

        assert len(X_train) == len(y_train)
        assert sum(len(X_train.columns), len(y_train.columns)) == len(_processed_data.columns)
        logging.info(
            "Testing processed_data SUCCESS: Data Processing is successed."
        )


        dump(encoder, "model/encoder.joblib")
        dump(lb, "model/lb.joblib")
        logging.info(
            "Testing processed_data SUCCESS: ENCODING is successfully completed and saved in right place"
        )


    except AttributeError as err:
        logging.error(
            "FAILED Testing processed_data: ENCODING is not successfully completed"
        )




