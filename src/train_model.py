# Script to train machine learning model.
# src/train_model.py
import pandas as pd
#from sklearn.model_selection import train_test_split
from sklearn.model_selection import train_test_split
from joblib import dump
from src.data import process_data
from src.model import train_model, slice_data, compute_model_metrics

def run_train_model():
    # Read the training data with folds 
    df = pd.read_csv("data/processed/processed_census.csv")

    train, test = train_test_split(df, test_size=0.20)

    cat_features = [
        "workclass",
        "education",
        "marital_status",
        "occupation",
        "relationship",
        "race",
        "sex",
        "native_country",
    ]

    X_train, y_train, encoder, lb = process_data(
        train, categorical_features=cat_features, label="salary", training=True
    )

    dump(encoder, "model/encoder.joblib")
    dump(lb, "model/lb.joblib")

    # Proces the test data with the process_data function.

    X_test, y_test, _, _ = process_data(test, categorical_features=cat_features, label="salary", encoder=encoder, lb=lb,
    training=False)

    # Train and save a model.
    _model = train_model(X_train = X_train, y_train = y_train)

    slice_data(data=test)

    preds = _model.predict(X_test)

    precision, recall, fbeta, accuracy = compute_model_metrics(y_test, preds)

    

    print(f"precision: {precision}, recall: {recall}, fbeta: {fbeta}, accuracy: {accuracy}")


