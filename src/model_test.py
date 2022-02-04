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

    try:
        best_model = load("model/xgboost.pkl")
        logging.info(
            "SUCCESS|Testing test_train_model: Xgboost model is successfully loaded")
    except FileNotFoundError as err:
        logging.error(
            "Testing test_train_model: Loading xgboost model is failed")
