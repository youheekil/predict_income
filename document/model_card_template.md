# Model Card


## Model Details
Youhee used XGBoost model which is a decision-tree-based ensemble Machine Learning algorithm that uses a gradient boosting framework. We used GridSearchCV with XGBoost for best estimators. 

## Intended Use
This model was to predict the salary of a person based on a some attributes about it's financials.

## Training Data
80% of the ingested data. The original source of the data is https://archive.ics.uci.edu/ml/datasets/census+income. 

## Evaluation Data
20% of the ingested data. The original source of the data is https://archive.ics.uci.edu/ml/datasets/census+income. 
## Metrics
_Please include the metrics used and your model's performance on those metrics._
The model evaluationi metrics were accuracy, precision, recall, and F1.

* precision: 0.785828025477707
* recall: 0.6615281501340483
* fbeta: 0.7183406113537117
* accuracy: 0.8717056190949776

## Ethical Considerations

## Caveats and Recommendations
GridSearchCV with XGBoost took really long time, because XGBoost has many tuning parameters so an exhaustive grid search has an unreasonable number of combination. In the future, creating a function to tune reduced sets of parameters using grid search and use early stopping will be recommended. 
