from fastapi.testclient import TestClient

from app import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}


def test_prediction_high():
    r = client.post("http://0.0.0.0:8000/prediction?"\
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
                                                        "native_country=United-States")
    assert r.status_code == 200
    assert r.json() == {"Predicted Salary: ": " >50K"}


def test_prediction_low():
    r = client.post("http://0.0.0.0:8000/prediction?" \
    "age=32&"\
        "workclass=Private&"\
            "fnlgt=34&"\
                "education=Some-college&"\
                    "education_num=45&"\
                        "marital_status=Married-civ-spouse&"\
                            "occupation=Tech-support&"\
                                "relationship=Unmarried&"\
                                    "race=Amer-Indian-Eskimo&"\
                                        "sex=Male&capital_gain=1&"\
                                            "capital_loss=12&"\
                                                "hours_per_week=30&"\
                                                    "native_country=United-States")
    assert r.status_code == 200
    assert r.json() == {"Predicted Salary: ": " <=50K"}

def test_prediction_error():
    r = client.post("http://0.0.0.0:8000/prediction?" \
    "age=32&"\
        "workclass=Private&"\
            "fnlgt=34&"\
                "education=Some-college&"\
                    "education_num=45&"\
                        "marital_status=Married-civ-spouse&"\
                            "occupation=Tech-support&"\
                                "relationship=error&"\
                                    "race=Amer-Indian-Eskimo&"\
                                        "sex=Male&capital_gain=1&"\
                                            "capital_loss=12&"\
                                                "hours_per_week=30&"\
                                                    "native_country=United-States")
    assert r.status_code == 422



