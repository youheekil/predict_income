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

# API Creation with FastAPI

- GET on the root giving a welcome message.
- POST that does model inference.
     This model should contain an example.
- Write 3 unit tests to test the API (one for the GET and two for POST, one that tests each prediction).

# Deploying on Heroku API through CLI 

* Create Procfile 
Procfile is to give heroku command on what should be running (without extension)

* Create runtime.txt
runtime.txt is to specify which python version you are running. 

* shell 
```shell
> heroku
> heroku create
> heroku apps
> heroku create <app-name> --buildpack heroku/python 
> heroku buildpacks --app <app-name>
```

* git
```shell
> git status
> git add *
> git commit -m "heroku setup"
> git branch # check branch of git
> git push heroku main
```

* shell 
```shell
> heroku run bash --app income-prediction-ml-yh
# running heroku
> pwd # check current work directory
> ls
> exit # exit the heroku
```

# Final
You can check my API here: 

- click the link (https://income-prediction-ml-yh.herokuapp.com/docs)

- click `POST` -> `prediction` -> `Try it out`
- play with it !

OR 

- clone current github repository

- DATA CLEANING STEP
```shell
python main.py --action data_mining 
```

- PREDICTING STEP
```shell
python main.py --action predicting 
```

- ALL STEP 
```shell
python main.py --action all 
```
