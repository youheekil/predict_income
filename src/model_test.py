import logging 
from joblib import load
from src.model import train_model


FORMAT = "%(asctime)s | %(name)s - %(levelname)s - %(message)s"
LOG_FILEPATH = "logs/testing.log/"
logging.basicConfig(
    filename=LOG_FILEPATH,
    level=logging.INFO,
    filemode='w',
    format=FORMAT)


def test_train_model():
    """
    This function is to test if the model is successfully saved at the right location
    :return:
    """
    try:
        best_model = load("model/xgboost.pkl")
        logging.info(
            "SUCCESS|Testing test_train_model: Xgboost model is successfully loaded")
    except FileNotFoundError as err:
        logging.error(
            "Testing test_train_model: Loading xgboost model is failed")


def test_slice_data():
    """
    This function is to test slice_data function if it's successfully stroed the result in txt file.

    :return:
    """
    try:
        with open("notebook/slice_output.txt", 'r') as file:
            contents = file.readlines()
        logging.info(
                "SUCESS|Testing slice_data: slice output is successfully saved it"
        )
    except FileNotFoundError as err:
        logging.error(
                "Testing slice_data: Reading slice_output.txt file is failed. "
        )

