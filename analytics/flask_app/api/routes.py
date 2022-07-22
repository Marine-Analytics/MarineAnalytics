from flask import (
    Flask,
    jsonify,
    request,
    )
from . import api
import pandas as pd
from joblib import load
import numpy as np
from .utils import data_preprocessing

def lag_preprocess(df, name):
    
    # смещение
    for i in range(30, 0, -1):
        oxy_shift = df[f'{name}'].shift(periods=i)
        oxy_shift.name = f'{name} {i} shift'
        df[oxy_shift.name] = oxy_shift
    return df

@api.route('/stend_danger', methods=['POST'])
def stend_danger():
    data = request.json
    if data is None:
        data = request.form.to_dict()

    df = pd.DataFrame(data, index=[0])
    df = df.drop('date', axis=1)
    model = load('./models/vibro_model.joblib')
    vibro_predict = model.predict(df)
    model = load('./models/oxygen_model.joblib')
    oxygen_predict = model.predict(df)
    model = load('./models/temperature_model.joblib')
    tempreture_predict = model.predict(df)
    
    return jsonify({'vibro_predict': 1 if vibro_predict[0] == 1 else 0,
                    'oxygen_predict': 1 if oxygen_predict[0] == 1 else 0,
                    'temperature_predict': 1 if tempreture_predict[0] == 1 else 0})

@api.route('/stend_predict', methods=['POST'])
def stend_predict():
    data = request.json
    if data is None:
        data = request.form.to_dict()

    df = pd.DataFrame.from_dict(data)
    df = df.drop('date', axis=1)

    oxy = df.copy(deep=True)
    temp = df.copy(deep=True)
    vibro = df.copy(deep=True)

    oxy = lag_preprocess(oxy, name='oxygen')
    temp = lag_preprocess(temp, name='temperature')
    vibro = lag_preprocess(vibro, name='vibro')

    model = load('./models/predict_oxygen_model.joblib')
    oxy_predict = model.predict(np.asarray(oxy.drop('oxygen', axis=1).iloc[[-1]].values).astype(np.float32))
    model = load('./models/predict_temperature_model.joblib')
    temp_predict = model.predict(np.asarray(temp.drop('temperature', axis=1).iloc[[-1]].values).astype(np.float32))
    model = load('./models/predict_vibro_model.joblib')
    vibro_predict = model.predict(np.asarray(vibro.drop('vibro', axis=1).iloc[[-1]].values).astype(np.float32))
    
    return jsonify({
        'oxygen_predict': oxy_predict[-1],
        'temperature_predict': temp_predict[-1],
        'vibro_predict': vibro_predict[-1]})

@api.route('/vodnik_danger', methods=['POST'])
def vodnik_danger():
    data = request.json
    if data is None:
        data = request.form.to_dict()
    
    model = load('./models/mov_state_model.joblib')
    df = pd.DataFrame(data, index=[0])
    df = data_preprocessing(df)
    predict = model.predict(df)[: , 1]
    print(predict[0])

    return jsonify({'predict': predict[0]})


@api.route('/vodnik_predict', methods=['POST'])
def vodnik_predict():
    data = request.json
    if data is None:
        data = request.form.to_dict()
    
    data = pd.DataFrame.from_dict(data)
    
    values_speed = data.copy(deep=True)
    values_frequency = data.copy(deep=True)
    values_vibration = data.copy(deep=True)
    values_left_bak = data.copy(deep=True)
    values_right_bak = data.copy(deep=True)

    values_speed = lag_preprocess(values_speed, 'values_speed')
    values_frequency = lag_preprocess(values_frequency, 'values_frequency')
    values_vibration = lag_preprocess(values_vibration, 'values_vibration')
    values_left_bak = lag_preprocess(values_left_bak, 'values_left_bak')
    values_right_bak = lag_preprocess(values_right_bak, 'values_right_bak')

    model = load('./models/vodnik_predict_values_speed_model.joblib')
    speed_predict = model.predict(np.asarray(values_speed.drop('values_speed', axis=1).iloc[[-1]].values).astype(np.float32))

    model = load('./models/vodnik_predict_values_frequency_model.joblib')
    frequency_predict = model.predict(np.asarray(values_frequency.drop('values_frequency', axis=1).iloc[[-1]].values).astype(np.float32))

    model = load('./models/vodnik_predict_values_vibration_model.joblib')
    vibration_predict = model.predict(np.asarray(values_vibration.drop('values_vibration', axis=1).iloc[[-1]].values).astype(np.float32))

    model = load('./models/vodnik_predict_values_left_bak_model.joblib')
    left_bak_predict = model.predict(np.asarray(values_left_bak.drop('values_left_bak', axis=1).iloc[[-1]].values).astype(np.float32))

    model = load('./models/vodnik_predict_values_right_bak_model.joblib')
    right_bak_predict = model.predict(np.asarray(values_right_bak.drop('values_right_bak', axis=1).iloc[[-1]].values).astype(np.float32))

    return jsonify({
        'speed_predict': speed_predict[-1],
        'frequency_predict': frequency_predict[-1],
        'vibration_predict': vibration_predict[-1],
        'left_bak_predict': left_bak_predict[-1],
        'right_bak_predict': right_bak_predict[-1],
        })