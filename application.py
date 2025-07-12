from flask import Flask,request,jsonify,render_template
import pickle
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler


application=Flask(__name__)
app=application

## import ridge and scaler
ridge_model=pickle.load(open('models/ridge.pkl','rb'))
scaler_model=pickle.load(open('models/scaler.pkl','rb'))

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/predictdata',methods=['GET','POST'])
def 

if __name__=="__main__":
    app.run(host="0.0.0.0")
