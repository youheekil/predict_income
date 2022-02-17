"""
Tesing Heroku App test
"""

import requests


url = "http://0.0.0.0:8000/prediction?age=45&workclass=Self-emp-inc&fnlgt=40&education=Prof-school&education_num=14&marital_status=Separated&occupation=Sales&relationship=Not-in-family&race=White&sex=Male&capital_gain=10000&capital_loss=1000&hours_per_week=45&native_country=United-States"


def try_api():
    response_post = requests.request("POST", url)
    print(response_post)
    print(response_post.json())

if __name__ == '__main__':
    try_api()