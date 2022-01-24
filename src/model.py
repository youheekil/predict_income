#src/ml/model.py
"""
This script trains with XGBOOST model
"""

import os
from joblib import dump, load
import pandas as pd
from xgboost import XGBClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import fbeta_score, precision_score, recall_score
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier

import data
from data import get_cat_features, process_data

def train_model(X_train, y_train):
    """
    Trains a machine learning model and returns it.

    Inputs
    ------
    X_train : np.array
        Training data.
    y_train : np.array
        Labels.
    Returns
    -------
    model
        Trained machine learning model.
    """
    # initialize the model 
    rfc = RandomForestClassifier(random_state=42)

    PARAM_GRID = { 
        'n_estimators': [200, 500],
        'max_features': ['auto', 'sqrt', 'log2'],
        'max_depth' : [4,5,6,7,8],
        'criterion' :['gini', 'entropy']
    }


    grid_search = GridSearchCV(
        estimator=rfc,
        param_grid=PARAM_GRID,
        scoring = 'roc_auc',
        n_jobs = 1,
        cv = 5,
        verbose=True
    )
    # fit model on training data
    grid_search.fit(X_train, y_train)

    # best model trained by GridSearch.
    best_model = grid_search.best_estimator_
    
    return best_model 


def inference(model, X):
    """ Run model inferences and return the predictions.

    Inputs
    ------
    model : Random Forest model 
        Trained machine learning model.
    X : np.array
        Data used for prediction. (X_test)
    Returns
    -------
    preds : np.array
        Predictions from the model.
    """
    preds = model.predict(X)

    return preds


def compute_model_metrics(y, preds):
    """
    Validates the trained machine learning model using precision, recall, and F1.

    Inputs
    ------
    y : np.array
        Known labels, binarized.
    preds : np.array
        Predicted labels, binarized.
    Returns
    -------
    precision : float
    recall : float
    fbeta : float
    """
    fbeta = fbeta_score(y, preds, beta=1, zero_division=1)
    precision = precision_score(y, preds, zero_division=1)
    recall = recall_score(y, preds, zero_division=1)
    return precision, recall, fbeta


def slice_data(data):
    """ Function for calculating descriptive stats on slices of the Iris dataset."""
    
    enc = load("model/encoder.joblib")
    lb = load("model/lb.joblib")
    best_model = load("model/random_forest.pkl")

    # categories
    categorical_features = get_cat_features()
    for cat in categorical_features:
        for cls in data[cat].unique():
            df_temp = data[data[cat] == cls]
            X_test, y_test, _, _ = process_data(df_temp, categorical_features=get_cat_features(), label="salary", encoder=enc, lb=lb,
            training=False)

        pred = inference(model=best_model, X=X_test)
        
        precision, recall, fbeta = compute_model_metrics(y=y_test, preds=pred)

        with open("notebook/data_slicing_score.txt", "a") as f:
            f.write(f"{cat}[{cls}]\n")
            f.write(f"precision: {precision}\n")
            f.write(f"recall: {recall}\n")
            f.write(f"fbeta: {fbeta}\n")
            f.write("===================================\n")



if __name__ == '__main__':
    df = pd.read_csv("data/processed/processed_census.csv")
    train, test = train_test_split(df, test_size = 0.2)
    X_train, y_train, encoder, lb = data.process_data(
        train, categorical_features=data.get_cat_features(), label="salary", training=True
    )
    best_model = train_model(X_train, y_train)
    slice_data(data=test)

