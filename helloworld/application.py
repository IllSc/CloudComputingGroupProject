#!flask/bin/python
import json
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
if __name__ == '__main__':
    flaskrun(application)
