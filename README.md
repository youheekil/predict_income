# udacity_c3_cencus
ML pipeline to expose API on Heroku

## Repositories
> pip environment set up 
```shell 
git clone <github HTTPS filepath>
virtualenv venv
source venv/bin/activate

# Install all dependencies of this file.

pip install -r requirements.txt
```
> Set up git and dvc

* Install dvc 
```shell
pip install 'dvc[s3]'
```
* Create a directory for the project and initialize git and dvc.
```shell
git init
dvc init
ls -a # check the file 
```

* As you work on the code, continually commit changes. Generated models you want to keep must be committed to dvc.
```shell
mkdir ../local remote_dir
dvc remote add -d local_remote_dir
dvc remote list
```

* Connect your local git repo to GitHub.
* Setup GitHub Actions on your repo. You can use one of the pre-made GitHub Actions if at a minimum it runs pytest and flake8 on push and requires both to pass without error.

* Make sure you set up the GitHub Action to have the same version of Python as you used in development.
* Set up a remote repository for dvc.
mybucket name is youheekil
```bash
dvc remote add -d storage s3://youheekil/dvcstore
git add .dvc/config
git commit -m "Configure remote storage"
```

* send data to the local remote with 
```shell
dvc push
``` 
* retrieve the data
```shell
dvc pull 
```

# Data
* Download census.csv and commit it to dvc.
```shell
dvc add ./data/raw/census.csv
git add .gitignore ./data/raw/census.csv
dvc push
```
* Raw data is messy
  * Removed space in each column
  * Replaced '?' in data to NA
  * Dropped NA

```shell
python src/clean_data.py
```

* Commit this modified data to dvc. 
  * We kept the raw data untouched but then can keep updating the cooked version (processed).
```shell
dvc add ./data/processed/processed_census.csv
git add .gitignore ./data/processed/processed_census.csv
dvc push
```

# Model
* train machine learning model on data, save and load the model and any categorical encoders
model inference  determine the classification metrics.
```shell
python src/model.py
```
* Unit tests for 3 functions in the model code.
```shell
pytest src/model_test.py
```
```shell
dvc add ./model/xgboost.pkl
git add .gitignore ./model/xgboost.pkl
```
* Details of the model can be found in a model card (document/model_card_template.md)

# API Creation

- GET on the root giving a welcome message.
- POST that does model inference.
     This model should contain an example.
- Write 3 unit tests to test the API (one for the GET and two for POST, one that tests each prediction).

# API Deployment
* Create a free Heroku account (for the next steps you can either use the web GUI or download the Heroku CLI).
* Create a new app and have it deployed from your GitHub repository.
    * Enable automatic deployments that only deploy if your continuous integration passes.
    * Hint: think about how paths will differ in your local environment vs. on Heroku.
    * Hint: development in Python is fast! But how fast you can iterate slows down if you rely on your CI/CD to fail before fixing an issue. I like to run flake8 locally before I commit changes.
* Write a script that uses the requests module to do one POST on your live API.

# Deploying on Heroku through CLI 

```shell
> heroku
> heroku create
> heroku apps
> heroku create <app-name> --buildpack heroku/python 
> heroku buildpacks --app <app-name>

```


# confusion matrix
```python 
#importing confusion matrix
from sklearn.metrics import confusion_matrix

def plot_confusion_matrix(cm, classes, normalized=True, cmap='BuPu'):
    plt.figure(figsize=[10, 8])
    norm_cm = cm
    if normalized:
        norm_cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        sns.heatmap(norm_cm, annot=cm, fmt='g', xticklabels=classes, yticklabels=classes, cmap=cmap)


cm = confusion_matrix(y_test, predictions)
#call the confusion matrix function         
plot_confusion_matrix(cm, ['class1', 'class2', 'class3','class4'])
```

