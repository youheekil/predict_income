# udacity_c3_cencus
ML pipeline to expose API on Heroku

## Repositories
```bash
ls
git init
dvc init
ls -a # check the file 
# create a local remote
# make the folder and tell DVC it is your remote:
mkdir ../local_remote_dir
dvc remote add -d local_remote_dir # -d: default
dvc remote list
# then commit the changes to the .dvc/config file to your version control 
head .dvc/config 
dvc add sample.csv
git add .gitignore sample.csv.dvc
git commit -m "Initial commit of tracked sample.csv"
# send data to the local remote with 
dvc push 
# retrieve the data, use dvc pull 

```
* Create a directory for the project and initialize git and dvc.
```bash
git init
dvc init
```
* As you work on the code, continually commit changes. Generated models you want to keep must be committed to dvc.
```bash
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
```bash
dvc add ./data/census.csv
git add .gitignore ./data/census.csv
```
* This data is messy, try to open it in pandas and see what you get.

* To clean it, use your favorite text editor to remove all spaces.

```python 
# remove all spaces
```
* Commit this modified data to dvc (we often want to keep the raw data untouched but then can keep updating the cooked version).

# Model
* Using the starter code, write a machine learning model that trains on the clean data and saves the model. Complete any function that has been started.
* Write unit tests for at least 3 functions in the model code.
* Write a function that outputs the performance of the model on slices of the data.
    * Suggestion: for simplicity, the function can just output the performance on slices of just the categorical features.
* Write a model card using the provided template.

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
