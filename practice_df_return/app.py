# app.py
from flask import Flask, request, jsonify
import numpy as np
import pandas as pd
app = Flask(__name__)

df=pd.read_csv("C:\\Users\\u27d09\\store_things\\dataset\\supermarket_sales - Sheet1.csv")
temp=list()

@app.get("/row/top_5")
def get_num():
    df_new=df[:5]
    return jsonify(df_new.to_dict(orient="records"))

@app.get('/row/<int:number>/<int:number1>')
def get_num1(number,number1):
    df_new=df[number:number1]
    return jsonify(df_new.to_dict(orient="records"))

@app.get('/row/<int:number>/')
def get_num2(number):
    df_new=df[:number]
    return jsonify(df_new.to_dict(orient="records"))

@app.post("/df_n")
def num3():
    if request.is_json:
        data = request.get_json(silent=True)
        temp.append(data)
        return 'done',201
    return {"error": "Request must be JSON"}, 415

@app.get("/df_n/done")
def num4():
    df_new1 = pd.DataFrame(temp,columns=["Branch","City","Customer type","Date","Gender",
             "Invoice ID","Payment","Product line","Quantity","Rating","Tax 5%","Time",
             "Total","Unit price","cogs","gross income","gross margin percentage"])
    df_new1.to_csv('file1.csv')
    return 'file saved'

@app.get("/df_n/view")
def num5():
    df_n_1=pd.read_csv("C:\\Users\\u27d09\\store_things\\flask_api_practice\\practice_df_return\\file1.csv")
    return jsonify(df_n_1.to_dict(orient="records"))
    
'''flask 
env_name\Scripts\activate
deactivate
in env
set FLASK_APP=app.py
set FLASK_ENV=development
flask run
for get - curl url
for put - curl -X PUT -H "Content-Type: application/json" -d '{"key1":"value"}' "YOUR_URl"
use postman
#using query string
@app.route('/data')
def data():
    # here we want to get the value of user (i.e. ?user=some-value)
    user = request.args.get('user')
'''