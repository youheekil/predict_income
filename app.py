# from concurrent.futures import process
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Literal
import uvicorn
from enum import Enum
import pandas as pd 
from joblib import load
from src.data import process_data, get_cat_features
from src.model import inference

app = FastAPI(debug = True)


class Info(BaseModel):
    age: int = '42'
    workclass: Literal[
        'State-gov', 'Self-emp-not-inc', 'Private', 'Federal-gov',
        'Local-gov', 'Self-emp-inc', 'Without-pay'] = 'Private'
    fnlgt: int = 2334
    education: Literal[
        'Bachelors', 'HS-grad', '11th', 'Masters', '9th',
        'Some-college',
        'Assoc-acdm', '7th-8th', 'Doctorate', 'Assoc-voc', 'Prof-school',
        '5th-6th', '10th', 'Preschool', '12th', '1st-4th'] = 'Bachelors'
    education_num: int = 13
    marital_status: Literal[
        'Never-married', 'Married-civ-spouse', 'Divorced',
        'Married-spouse-absent', 'Separated', 'Married-AF-spouse',
        'Widowed'] = 'Never-married'
    occupation: Literal[
        'Adm-clerical', 'Exec-managerial', 'Handlers-cleaners',
        'Prof-specialty', 'Other-service', 'Sales', 'Transport-moving',
        'Farming-fishing', 'Machine-op-inspct', 'Tech-support',
        'Craft-repair', 'Protective-serv', 'Armed-Forces',
        'Priv-house-serv'] = 'Prof-specialty'
    relationship: Literal[
        'Not-in-family', 'Husband', 'Wife', 'Own-child',
        'Unmarried', 'Other-relative'] = 'Wife'
    race: Literal[
        'White', 'Black', 'Asian-Pac-Islander', 'Amer-Indian-Eskimo',
        'Other'] = 'Black'
    sex: Literal['Male', 'Female'] = 'Female'
    capital_gain: int = 2174
    capital_loss: int = 0
    hours_per_week: int = 60
    native_country: Literal[
        'United-States', 'Cuba', 'Jamaica', 'India', 'Mexico',
        'Puerto-Rico', 'Honduras', 'England', 'Canada', 'Germany', 'Iran',
        'Philippines', 'Poland', 'Columbia', 'Cambodia', 'Thailand',
        'Ecuador', 'Laos', 'Taiwan', 'Haiti', 'Portugal',
        'Dominican-Republic', 'El-Salvador', 'France', 'Guatemala',
        'Italy', 'China', 'South', 'Japan', 'Yugoslavia', 'Peru',
        'Outlying-US(Guam-USVI-etc)', 'Scotland', 'Trinadad&Tobago',
        'Greece', 'Nicaragua', 'Vietnam', 'Hong', 'Ireland', 'Hungary',
        'Holand-Netherlands'] = 'Cuba'
class Workclass(str, Enum):
    PRIVATE = "Private", 
    SELF_EMP_NOT_INC = "Self-emp-not-inc", 
    LOCAL_GOV = "Local-gov", 
    STATE_GOV = "State-gov", 
    SELF_EMP_INC = "Self-emp-inc", 
    FEDERAL_GOV = "Federal-gov", 
    WITHOUT_PAY = "Without-pay"

class Education(str, Enum):
    G_10TH = '10th',
    G_11TH = '11th',
    G_12TH = '12th',
    G_1ST_4TH = '1st-4th',
    G_5ST_6TH = '5th-6th',
    G_7TH_8TH = '7th-8th',
    G_9TH = '9th',
    ASSOC_ACAD = 'Assoc-acdm',
    ASSOC_VOC = 'Assoc-voc',
    BACHELORS = 'Bachelors',
    DOCTORATE = 'Doctorate',
    HIGHSCHOOL_GRAD = 'HS-grad',
    MASTERS = 'Masters',
    PRESCHOOL ='Preschool',
    PROFFESSIONAL_SCHOOL ='Prof-school',
    SOME_COLLEGE = 'Some-college'


class MaritalStatus(str, Enum):
    MARRIED_CIV_SPOUSE = 'Married-civ-spouse', 
    NEVER_MARRIED = 'Never-married', 
    DIVORCED = 'Divorced', 
    SEPARATED = 'Separated',
    WIDOWED ='Widowed', 
    MARRIED_SPOUSE_ABSENT = 'Married-spouse-absent', 
    MARRIED_AF_SPOUSE = 'Married-AF-spouse'


class Occupation(str, Enum):
    PROFESSOR_SPECIALITY = 'Prof-specialty',
    CRAFT_REPAIR = 'Craft-repair', 
    EXEC_MANAGERIAL = 'Exec-managerial',
    ADM_CLERICAL ='Adm-clerical',
    SALES ='Sales',
    OTHER_SERVICE = 'Other-service',
    MACHINE_OP_INSPECT ='Machine-op-inspct', 
    TRANSPORT_MOVING ='Transport-moving', 
    HANDLERS_CLEANERS = 'Handlers-cleaners', 
    FARMING_FISHING = 'Farming-fishing', 
    TECH_SUPPORT = 'Tech-support', 
    PROTECTIVE_SERV = 'Protective-serv', 
    PRIV_HOUSE_SERV ='Priv-house-serv', 
    ARMED_FORCES = 'Armed-Forces'


class Relationship(str, Enum):
    HUSBAND ='Husband', 
    NOT_IN_FAMILY = 'Not-in-family', 
    OWN_CHILD = 'Own-child', 
    UNMARRIED = 'Unmarried', 
    WIFE = 'Wife',
    OTHER_RELATIVE = 'Other-relative'

class Race(str, Enum):
    WHITE = 'White', 
    BLACK = 'Black', 
    ASIAN_PAC_ISLANDER ='Asian-Pac-Islander', 
    AMER_INDIAN_ESKIMO ='Amer-Indian-Eskimo', 
    OTHER = 'Other'


class Sex(str, Enum):
    MALE ='Male', 
    FEMALE = 'Female'


class Native_Country(str, Enum):
    UNITED_STATES = 'United-States',
    CUBA = 'Cuba', 
    JAMAICA = 'Jamaica', 
    INDIA = 'India', 
    MEXICO = 'Mexico',
    PUERTO_RICO = 'Puerto-Rico', 
    HONDURAS = 'Honduras', 
    ENGLAND = 'England', 
    CANADA = 'Canada', 
    GERMANY = 'Germany', 
    IRAN = 'Iran',
    PHILIPPINES = 'Philippines', 
    POLAND ='Poland', 
    COLUMBIA = 'Columbia', 
    CAMBODIA = 'Cambodia', 
    THAILAND = 'Thailand',
    ECUADOR = 'Ecuador',
    LAOS = 'Laos', 
    TAIWAN = 'Taiwan', 
    HAITI = 'Haiti', 
    PORTUGAL = 'Portugal',
    DOMINICAN_REPUBLIC = 'Dominican-Republic', 
    EL_SALVADOR = 'El-Salvador', 
    FRANCE = 'France', 
    GUATEMALA = 'Guatemala',
    ITALY = 'Italy', 
    CHINA = 'China', 
    SOUTH = 'South', 
    JAPAN = 'Japan', 
    YUGOSLAVIA = 'Yugoslavia', 
    PERU = 'Peru',
    OUTLYING_US = 'Outlying-US(Guam-USVI-etc)', 
    SCOTLAND = 'Scotland', 
    TRINADAD = 'Trinadad&Tobago',
    GREECE = 'Greece', 
    NICARAGUA = 'Nicaragua', 
    VIETNAM = 'Vietnam', 
    HONG = 'Hong', 
    IRELAND = 'Ireland', 
    HUNGARY = 'Hungary',
    HOLAND_NETHERLANDS = 'Holand-Netherlands'

_encoder = load("model/encoder.joblib.dvc")
_lb = load("model/lb.joblib.dvc")
_model = load("model/xgboost.pkl.dvc")


@app.get("/")
async def read_main():
    return {"msg": "Hello World"}


@app.post('/prediction')
async def predict_income(info: Info):
    data = {'age': [info.age], 
            'fnlgt':[info.fnlgt], 
            'workclass': [info.workclass], 
            'education': [info.education], 
            'education_num': [info.education_num], 
            'marital_status': [info.marital_status], 
            'occupation': [info.occupation], 
            'relationship': [info.relationship], 
            'race': [info.race], 
            'sex': [info.sex], 
            'capital_gain': [info.capital_gain], 'capital_loss': [info.capital_loss], 
            'hours_per_week': [info.hours_per_week], 
            'native_country': [info.native_country]}


    df_temp = pd.DataFrame.from_dict(data)

    X, _, _, _ = process_data(
                df_temp,
                categorical_features=get_cat_features(),
                encoder=_encoder, lb=_lb, training=False)
    pred = inference(_model, X)
    y = _lb.inverse_transform(pred)[0]
    
    return {"Predicted Salary: ": y}


@app.post('/prediction_enum')
async def create_prediction(
    age: int, 
    workclass: Workclass, 
    fnlgt: int,
    education: Education, 
    education_num: int, 
    marital_status: MaritalStatus, 
    occupation: Occupation, 
    relationship: Relationship, 
    race: Race, 
    sex: Sex, 
    capital_gain: int, 
    capital_loss: int, 
    hours_per_week: int, 
    native_country: Native_Country):
    data = {'age': [age], 
            'fnlgt':[fnlgt], 
            'workclass': [workclass], 
            'education': [education], 
            'education_num': [education_num], 
            'marital_status': [marital_status], 
            'occupation': [occupation], 
            'relationship': [relationship], 
            'race': [race], 
            'sex': [sex], 
            'capital_gain': [capital_gain], 'capital_loss':[capital_loss], 
            'hours_per_week': [hours_per_week], 
            'native_country': [native_country]}
    
    df_temp = pd.DataFrame.from_dict(data)
    X, _, _, _ = process_data(
                df_temp,
                categorical_features=get_cat_features(),
                encoder=_encoder, lb=_lb, training=False)
    pred = inference(_model, X)
    y = _lb.inverse_transform(pred)[0]
    
    return {"Predicted Salary: ": y}


if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
