import pickle
import json
import numpy as np
from sklearn.metrics import accuracy_score

_data_columns=None
_scaler=None
_model=None

def get_predicted_result(location,mintemp,maxtemp,rainfall,evaporation,sunshine,windgustdir,windgustspeed,winddir9am,winddir3pm,windspeed9am,windspeed3pm,humidity9am,humidity3pm,pressure9am,pressure3pm,cloud9am,cloud3pm,temp9am,temp3pm,raintoday,month,day,year):
    input=np.zeros(len(_data_columns['data_columns']))
    input[0]=location
    input[1]=mintemp
    input[2]=maxtemp
    input[3]=rainfall
    input[4]=evaporation
    input[5]=sunshine
    input[6]=windgustdir
    input[7]=windgustspeed
    input[8]=winddir9am
    input[9]=winddir3pm
    input[10]=windspeed9am
    input[11]=windspeed3pm
    input[12]=humidity9am
    input[13]=humidity3pm
    input[14]=pressure9am
    input[15]=pressure3pm
    input[16]=cloud9am
    input[17]=cloud3pm
    input[18]=temp9am
    input[19]=temp3pm
    input[20]=raintoday
    input[21]=month
    input[22]=day
    input[23]=year

    return _model.predict(_scaler.transform([input]))[0]

def load_artifacts():
    global _data_columns
    global _model
    global _scaler
    print('Loading Artifacts...')

    with open('./columns.json','r') as f:
        _data_columns=json.load(f)

    with open('./scaler.pickle','rb') as f:
        _scaler=pickle.load(f)    
        
    with open('./model.pickle','rb') as f:
        _model=pickle.load(f)


    print('Artifacts...Loaded')


def column_names():
    return(_data_columns)


load_artifacts()
print(len(_data_columns['data_columns']))
result=get_predicted_result(49,18.6,28.6,1.5,3.8,9.8,15.0,46.0,15.0,14.0,4.0,9.0,100.0,56.0,1020.00,1015.80 ,8.0,5.0,19.8,26.9,1,4,20,2017)
if result==1:
    print('It will rain Tomorrow.')
else:
    print('It will not rain Tomorrow.')
        
