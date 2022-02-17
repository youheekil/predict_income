"""
Tesing Heroku App test
"""

import requests


response_get = requests.get('/')

url = "https://income-prediction-ml-yh.herokuapp.com/prediction?"\
        "age=32&"\
            "workclass=Private&"\
                "fnlgt=34&"\
                    "education=Some-college&education_num=45&"\
                        "marital_status=Married-civ-spouse&"\
                            "occupation=Exec-managerial&"\
                                "relationship=Husband&"\
                                    "race=White&"\
                                        "sex=Male&"\
                                            "capital_gain=10000&"\
                                                "capital_loss=12&"\
                                                    "hours_per_week=60&"\
                                                        "native_country=United-States"

response_post = requests.post(url)


print(response_get.status_code)
print(response_get.json())

print(response_post.status_code)
print(response_post.json())

