#!flask/bin/python
import json
import requests
from flask import Flask, Response
from helloworld.flaskrun import flaskrun
from flask import render_template

application = Flask(__name__)
"""@application.route('/', methods=['GET'])
def get():
    return Response(json.dumps({'Output': 'Hello jayanthi'}), mimetype='application/json', status=200)

@application.route('/', methods=['POST'])
def post():
    return Response(json.dumps({'Output': 'Hello jayanthi'}), mimetype='application/json', status=200) """


@application.route('/')
def homepage():
	return render_template('template.html')
@application.route('/chord')
def chord():
    url = "https://yev0r4zzyf.execute-api.eu-central-1.amazonaws.com/CloudComputing/rail-data-dev-agg"

    
    response = requests.request("GET", url)
    matrices = json.loads(response.text)

    return render_template('chord.html',matrixData=matrices)
    
if __name__ == '__main__':
    flaskrun(application)
