from concurrent.futures import process
from fastapi import FastAPI, status
import uvicorn

from pydantic import BaseModel
from enum import Enum

import pandas as pd 
import numpy as np

from joblib import load

from src.data import process_data, get_cat_features
from src.model import inference

app = FastAPI(debug = True)


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
        United_States = 'United-States',
        Cuba = 'Cuba', 
        Jamaica = 'Jamaica', 
        India = 'India', 
        Mexico = 'Mexico',
        Puerto_Rico = 'Puerto-Rico', 
        Honduras = 'Honduras', 
        England = 'England', 
        Canada = 'Canada', 
        Germany = 'Germany', 
        Iran = 'Iran',
        Philippines = 'Philippines', 
        Poland ='Poland', 
        Columbia = 'Columbia', 
        Cambodia = 'Cambodia', 
        Thailand = 'Thailand',
        Ecuador = 'Ecuador',
        Laos = 'Laos', 
        Taiwan = 'Taiwan', 
        Haiti = 'Haiti', 
        Portugal = 'Portugal',
        Dominican_Republic = 'Dominican-Republic', 
        El_Salvador = 'El-Salvador', 
        France = 'France', 
        Guatemala = 'Guatemala',
        Italy = 'Italy', 
        China = 'China', 
        South = 'South', 
        Japan = 'Japan', 
        Yugoslavia = 'Yugoslavia', 
        Peru = 'Peru',
        Outlying_US = 'Outlying-US(Guam-USVI-etc)', 
        Scotland = 'Scotland', 
        Trinadad = 'Trinadad&Tobago',
        Greece = 'Greece', 
        Nicaragua = 'Nicaragua', 
        Vietnam = 'Vietnam', 
        Hong = 'Hong', 
        Ireland = 'Ireland', 
        Hungary = 'Hungary',
        Holand_Netherlands = 'Holand-Netherlands'

_encoder = load("model/encoder.joblib")
_lb = load("model/lb.joblib")
_model = load("model/xgboost.pkl")


@app.get("/")
async def root():
    return "Hello World"


@app.post('/prediction' )
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
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)