# app.py
from flask import Flask, request, jsonify

app = Flask(__name__)

keys = [
    {"id": 111, 'key': '513120'},
    {"id": 222, 'key': '7617930'},
    {"id": 333, 'key': '1010408'},
]

def _find_next_id():
    return max(key["id"] for key in keys) + 1

@app.get("/keys")
def get_keys():
    return jsonify(keys)

@app.get('/<int:number>/')
def get_key(number):
    for key in keys:
        if number==key['id']:
            return jsonify(key)
    return {"error": "data not found"}, 204

@app.post("/keys")
def add_keys():
    if request.is_json:
        key = request.get_json
        key["id"] = _find_next_id()
        keys.append(key)
        return key, 201
    return {"error": "Request must be JSON"}, 415
'''
env_name\Scripts\activate
deactivate
in env
set FLASK_APP=app.py
set FLASK_ENV=development
flask run
for get - curl url
for put - curl -X PUT -H "Content-Type: application/json" -d '{"key1":"value"}' "YOUR_URl"
use postman
'''