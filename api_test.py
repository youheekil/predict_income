"""
Tesing Heroku App test
"""

import requests

url_get = "https://income-prediction-ml-yh.herokuapp.com/"
url_post = "https://income-prediction-ml-yh.herokuapp.com/prediction_enum?age=45&workclass=Self-emp-inc&fnlgt=40&education=Prof-school&education_num=14&marital_status=Separated&occupation=Sales&relationship=Not-in-family&race=White&sex=Male&capital_gain=10000&capital_loss=1000&hours_per_week=45&native_country=United-States"

input = {
    "age": 30,
    "workclass": "State-gov",
    "fnlgt": 12,
    "education": "Bachelors",
    "education_num": 13,
    "marital_status": "Never-married",
    "occupation": "Adm-clerical",
    "relationship": "Not-in-family",
    "race": "White",
    "sex": "Male",
    "capital_gain": 1000,
    "capital_loss": 300,
    "hours_per_week": 60,
    "native_country": "United-States"
}


def try_get_api():
    response_get = requests.request("GET", url_get)
    print(f"status code for GET: {response_get.status_code}")
    print(response_get.json())


def try_post_api():
    response_post = requests.request("POST", url_post)
    print(f"status code for POST: {response_post.status_code}")
    print(response_post.json())


def input_api_test():
    r = requests.post('https://income-prediction-ml-yh.herokuapp.com/prediction', json=input)
    assert r.status_code == 200
    print("Response code: %s" % r.status_code)
    print("Response body: %s" % r.json())

if __name__ == '__main__':
    try_get_api()
    try_post_api()
    input_api_test()
    