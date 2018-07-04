#!flask/bin/python
import os
from flask import Flask
from flask import request
import pandas as pd
from sklearn import linear_model
import pickle

# creating and saving some model
reg_model = linear_model.LinearRegression()
reg_model.fit([[1.,1.,5.], [2.,2.,5.], [3.,3.,1.]], [0.,0.,1.])
pickle.dump(reg_model, open('some_model.pkl', 'wb'))

app = Flask(__name__)

@app.route('/isAlive')
def index():
    return "true"

@app.route('/prediction/api/v1.0/some_prediction', methods=['GET'])
def get_prediction():
    feature1 = float(request.args.get('f1'))
    feature2 = float(request.args.get('f2'))
    feature3 = float(request.args.get('f3'))
    loaded_model = pickle.load(open('some_model.pkl', 'rb'))
    prediction = loaded_model.predict([[feature1, feature2, feature3]])
    return str(prediction)

if __name__ == '__main__':
    if os.environ['ENVIRONMENT'] == 'production':
        app.run(port=80,host='0.0.0.0')
    if os.environ['ENVIRONMENT'] == 'local':
        app.run(port=5000,host='0.0.0.0')