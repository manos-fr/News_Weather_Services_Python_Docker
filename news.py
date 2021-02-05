from flask import Flask, request
from flask_restful import Resource, Api, reqparse 
from json import dumps
from flask import jsonify
import json
import requests

app = Flask(__name__)
api = Api(app)

@app.route('/news')
def news():
    country_name = request.args.get('country')
    api_key = "70dcd1c6a0d24ebdb57ff071ff9b8ddc"
    base_url = "http://newsapi.org/v2/top-headlines?"
    complete_url = base_url + "country=" + country_name + "&apiKey=" + api_key
    response = requests.get(complete_url)
    return response.json()

if __name__ == '__main__':
     app.run(host="0.0.0.0",port='3003',threaded=True,debug=True)