# udacity_c3_cencus
ML pipeline to expose API on Heroku

## Repositories

* Set up `git` with `GitHub Actions`.
> git 
```shell
git init
ls -a
```
> github action 
> dvc
```shell
dvc init
ls -a # check the file 
# create a local remote 
# make the folder and tell it is your remote:
mkdir ../local_remote_dir
dvc remote add -d local_remote_dir # -d: default 
dvc remote list
# commit the changes to the .dvc/confi file to your version control 
head .dvc/config
# add two data (raw/census.csv, processed/processed_census.csv)
dvc add raw/census.csv
# add git .gitignore  raw/census.csv.dvc
dvc add processed/processed_census.csv
# git .gitignore processed/processed_census.csv.dvc
# git commit -m "commit of tracked of data"

# send data to the local remote with 
dvc push 

# retrieve the data, use dvc pull 
```
* install dvc 
```shell
pip install dvc
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
```bash
dvc remote add -d storage s3://mybucket/dvcstore
git add .dvc/config
git commit -m "Configure remote storage"
```

# Data
* Download census.csv and commit it to dvc.
```shell
dvc add ./data/raw/census.csv
git add .gitignore ./data/raw/census.csv
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

* Details of the model can be found in a model card (document/model_card_template.md)

# API Creation
*  Create a RESTful API using FastAPI this must implement:
    * GET on the root giving a welcome message.
    * POST that does model inference.
    * Type hinting must be used.
    * Use a Pydantic model to ingest the body from POST. This model should contain an example.
   	 * Hint: the data has names with hyphens and Python does not allow those as variable names. Do not modify the column names in the csv and instead use the functionality of FastAPI/Pydantic/etc to deal with this.
* Write 3 unit tests to test the API (one for the GET and two for POST, one that tests each prediction).

# API Deployment
* Create a free Heroku account (for the next steps you can either use the web GUI or download the Heroku CLI).
* Create a new app and have it deployed from your GitHub repository.
    * Enable automatic deployments that only deploy if your continuous integration passes.
    * Hint: think about how paths will differ in your local environment vs. on Heroku.
    * Hint: development in Python is fast! But how fast you can iterate slows down if you rely on your CI/CD to fail before fixing an issue. I like to run flake8 locally before I commit changes.
* Write a script that uses the requests module to do one POST on your live API.
