#!flask/bin/python
import json
from flask import Flask, Response
from helloworld.flaskrun import flaskrun
from flask import render_template
from flask_cdn import CDN

application = Flask(__name__)
application.config['CDN_DOMAIN'] = 'd1r1rtixv3o3sw.cloudfront.net'
application.config['CDN_DEBUG'] = True
application.config['CDN_HTTPS'] = True
CDN(application)

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
