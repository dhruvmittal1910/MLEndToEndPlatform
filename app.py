# flask application
import pickle
import os
from flask import Flask,request,app,jsonify,url_for,render_template
import numpy as np
import pandas as pd

app=Flask(__name__)
#load the model
regModel=pickle.load(open('regModel.pkl','rb'))
scaler=pickle.load(open('scaler.pkl','rb'))

@app.route('/')
def home():
# basically redirect to home.html
# create home.html file in templaates folder
    return render_template('home.html')

@app.route('/predict_api',methods=['POST'])
# when i hit predict_api, it will call predict_api function
def predict_api():
    data=request.json['data']
    # do standardization using pickle file
    #  we need to convert data into array as done in our notebook

    raw_values = [float(v) if v != "" else 0.0 for v in data.values()]
# list(data.values())
    new_data=scaler.transform(np.nan_to_num(np.array(raw_values).reshape(1,-1)))

    # now we can predict using our model
    output=regModel.predict(new_data)
    print("hello  " ,output[0])
    return jsonify(output[0])

@app.route('/predict',methods=['POST'])
def predict():
    # data=[float(x) for x in request.form.values()]
    data = [float(x) if x != "" else 0.0 for x in request.form.values()]
    print("data ",data)
    final_input=np.nan_to_num(scaler.transform((np.array(data).reshape(1,-1))))
    print("final inpiut s", final_input)
    output=regModel.predict(final_input)[0]
    print(output)
    return render_template('home.html',prediction_text='Predicted house price is {}'.format(output))

if __name__ == "__main__":
    app.run(debug=True)