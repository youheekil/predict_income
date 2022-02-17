"""
Tesing Heroku App test
"""

import requests

url_get = "https://income-prediction-ml-yh.herokuapp.com/"
url_post = "https://income-prediction-ml-yh.herokuapp.com/prediction?age=45&workclass=Self-emp-inc&fnlgt=40&education=Prof-school&education_num=14&marital_status=Separated&occupation=Sales&relationship=Not-in-family&race=White&sex=Male&capital_gain=10000&capital_loss=1000&hours_per_week=45&native_country=United-States"


def try_get_api():
    response_get = requests.request("GET", url_get)
    print(f"status code for GET: {response_get.status_code}")
    print(response_get.json())


def try_post_api():
    response_post = requests.request("POST", url_post)
    print(f"status code for POST: {response_post.status_code}")
    print(response_post.json())


if __name__ == '__main__':
    try_get_api()
    try_post_api()