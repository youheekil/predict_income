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

from src.data import get_cat_features, process_data

def train_model(X_train, y_train):
    """
    Trains a machine learning model (xgboost) and returns it.

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
    # initialize the xgboost model 
    model = XGBClassifier(use_label_encoder=False, eval_metric='mlogloss')

    XGBClassifier(base_score=0.5, booster='gbtree', colsample_bylevel=1,
            colsample_bynode=1, colsample_bytree=1, eval_metric='mlogloss',
            gamma=0, gpu_id=-1, importance_type='gain',
            interaction_constraints='', learning_rate=0.300000012,
            max_delta_step=0, max_depth=6, min_child_weight=1,
            monotone_constraints='()', n_estimators=100, n_jobs=16,
            num_parallel_tree=1, objective='multi:softprob', random_state=0,
            reg_alpha=0, reg_lambda=1, scale_pos_weight=None, subsample=1,
            tree_method='exact', use_label_encoder=False,
            validate_parameters=1, verbosity=None)
    
    # fit model on training data
    model.fit(X_train, y_train)

    # best model trained by GridSearch.
    #best_model = grid_search.best_estimator_

    dump(model, "model/xgboost.pkl")
    return model



def xgb_accuracy(y, preds):

    """Run model (xgb) and return accuracy"""
    accuracy = accuracy_score(y, preds)
    return accuracy


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
    accuracy = accuracy_score(y, preds)
    return precision, recall, fbeta, accuracy


def slice_data(data):
    """ Function for evaluation metrics on slices of the dataset."""
    
    enc = load("model/encoder.joblib")
    lb = load("model/lb.joblib")
    xgboost_model = load("model/xgboost.pkl")
    
    # categories
    categorical_features = get_cat_features()
    for cat in categorical_features:
        for cls in data[cat].unique():
            df_temp = data[data[cat] == cls]
            X_test, y_test, _, _ = process_data(df_temp, categorical_features=get_cat_features(), label="salary", encoder=enc, lb=lb,
            training=False)

            pred = inference(model=xgboost_model, X=X_test)
            precision, recall, fbeta, accuracy = compute_model_metrics(y=y_test, preds=pred)
            
            with open("notebook/slice_output.txt", "a") as f:
                f.write(f"{cat}[{cls}]\n")
                f.write(f"precision: {precision}\n")
                f.write(f"recall: {recall}\n")
                f.write(f"fbeta: {fbeta}\n")
                f.write(f"accuracy: {accuracy}\n")
                f.write("===================================\n")
