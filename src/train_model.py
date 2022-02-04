# Script to train machine learning model.
# src/train_model.py
import pandas as pd
#from sklearn.model_selection import train_test_split
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn import metrics
import joblib


from rich.traceback import install
from sklearn.utils import compute_class_weight

from rich.traceback import install
install()

# Add the necessary imports for the starter code.
from data import process_data
import model

def train_model():
    # Read the training data with folds 
    df = pd.read_csv("data/clean_data.csv")

    train, test = train_test_split(df, test_size=0.20)

    cat_features = [
        "workclass",
        "education",
        "marital-status",
        "occupation",
        "relationship",
        "race",
        "sex",
        "native-country",
    ]

    X_train, y_train, _, _ = process_data(
        train, categorical_features=cat_features, label="salary", training=True
    )

    # Proces the test data with the process_data function.

    X_test, y_test, _, _ = process_data(test, categorical_features=cat_features, label="salary", training=False)

    # Train and save a model.
    _model = model.train_model(X_train = X_train, y_train = y_train)

    preds = _model.predict(X_test)

    precision, recall, fbeta = model.compute_model_metrics(y_test, preds)

    print(f"precision: {precision}, recall: {recall}, fbeta: {fbeta}")



if __name__ == '__main__':
    train_model()
