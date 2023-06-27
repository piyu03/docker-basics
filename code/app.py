
import numpy as np
import pandas as pd
from flask import Flask, request, render_template
from sklearn import preprocessing
import pickle

app = Flask(__name__)
filename = '/data/rf.pkl'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
            # Get values through input bars
    LIMIT_BAL = request.form.get("LIMIT_BAL")
    AGE = request.form.get("AGE")
    SEX = request.form.get("SEX")
    EDUCATION = request.form.get("EDUCATION")
    PAY_1 = request.form.get("PAY_1")
    PAY_2 = request.form.get("PAY_2")
    PAY_3 = request.form.get("PAY_3")

    final_features = pd.DataFrame([[LIMIT_BAL, AGE,SEX,EDUCATION,PAY_1, PAY_2,PAY_3 ]], columns = ["LIMIT_BAL","AGE","SEX","EDUCATION","PAY_1","PAY_2","PAY_3"])
    loaded_model = pickle.load(open(filename, 'rb'))
    y_pred = loaded_model.predict(final_features)

    if y_pred == 1:
        text = "accepted"
    else:
        text = "rejected"

    return render_template('index.html', prediction_text='Your loan is {}'.format(text))


if __name__ == "__main__":
    #app.run(port = 80,debug=True, host = '0.0.0.0')
     app.run(debug=True)
