"""
Tesing Heroku App test
"""

import requests


url = "https://income-prediction-ml-yh.herokuapp.com/prediction?age=45&workclass=Self-emp-inc&fnlgt=40&education=Prof-school&education_num=14&marital_status=Separated&occupation=Sales&relationship=Not-in-family&race=White&sex=Male&capital_gain=10000&capital_loss=1000&hours_per_week=45&native_country=United-States"

response_post = requests.request("POST", url)


print(response_post)

