#!flask/bin/python
from flask import Flask
from flask import request
import pandas as pd

# creating and saving some model
reg_model = linear_model.LinearRegression()
reg_model.fit([[1,1,5], [2,2,5], [3,3,1]], [0,0,1])
pickle.dump(reg_model, open('./model/some_model.pkl', 'wb'))

app = Flask(__name__)

@app.route('/isAlive')
def index():
    return "true"

@app.route('/prediction/api/v1.0/getFromBody', methods=['POST'])
def get_prediction():
    body = request.get_json()
    loaded_model = pickle.load('./model/some_model.pkl', 'rb')

    messages = pd.DataFrame(body)
    modelFromRepo = modelRepository.load('./model/')    
    # make sure all emotions exist
    for k in ['sentiment', 'fear', 'anger', 'disgust', 'joy', 'sadness']:
        if k not in messages.columns:
            messages[k] = float('NaN')
        messages[k] = messages[k].astype('float64')
    session = messagesToSession.transform(messages, ['sessionId', 'isCustomer'])
    # fill none values with mean
    session = session.fillna(modelFromRepo['mean'])
    # normalize 
    session_normalized = (session - modelFromRepo['mean']) / (modelFromRepo['max'] - modelFromRepo['min'])
    prediction = modelFromRepo['model'].predict_proba(session_normalized[modelFromRepo['features']])[:,1][0]
    return str(prediction)

if __name__ == '__main__':
    app.run(port=5000,host='0.0.0.0')
