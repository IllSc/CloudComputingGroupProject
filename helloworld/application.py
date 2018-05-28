#!flask/bin/python
import json
from flask import Flask, Response
from helloworld.flaskrun import flaskrun

application = Flask(__name__)

"""@application.route('/', methods=['GET'])
def get():
    return Response(json.dumps({'Output': 'Hello jayanthi'}), mimetype='application/json', status=200)

@application.route('/', methods=['POST'])
def post():
    return Response(json.dumps({'Output': 'Hello jayanthi'}), mimetype='application/json', status=200) """


@application.route('/')
def homepage():
	return """
		<h1>Hello world!</h1>

		<iframe src="https://search-cloud-computing-project-upc-uq5b7q3o57i5xaez54rlfluabu.eu-central-1.es.amazonaws.com/_plugin/kibana/app/kibana#/visualize/edit/3075e1e0-5fa3-11e8-b28b-e5ea3f49db77?embed=true&_g=()" height="600" width="800"></iframe>
		
		<iframe src="https://search-cloud-computing-project-upc-uq5b7q3o57i5xaez54rlfluabu.eu-central-1.es.amazonaws.com/_plugin/kibana/app/kibana#/visualize/edit/3075e1e0-5fa3-11e8-b28b-e5ea3f49db77?embed=true&_g=()" height="600" width="800"></iframe>
		<iframe src="https://search-cloud-computing-project-upc-uq5b7q3o57i5xaez54rlfluabu.eu-central-1.es.amazonaws.com/_plugin/kibana/app/kibana#/visualize/edit/9db1a9c0-5fac-11e8-b28b-e5ea3f49db77?embed=true&_g=()" height="600" width="800"></iframe>
		<iframe src="https://search-cloud-computing-project-upc-uq5b7q3o57i5xaez54rlfluabu.eu-central-1.es.amazonaws.com/_plugin/kibana/app/kibana#/visualize/edit/e62f3990-5fa4-11e8-b28b-e5ea3f49db77?embed=true&_g=()" height="600" width="800"></iframe>
		<iframe src="https://search-cloud-computing-project-upc-uq5b7q3o57i5xaez54rlfluabu.eu-central-1.es.amazonaws.com/_plugin/kibana/app/kibana#/visualize/edit/eabcf380-5fae-11e8-b28b-e5ea3f49db77?embed=true&_g=()" height="600" width="800"></iframe>
		<iframe src="https://search-cloud-computing-project-upc-uq5b7q3o57i5xaez54rlfluabu.eu-central-1.es.amazonaws.com/_plugin/kibana/app/kibana#/visualize/edit/82eb3cd0-5fa4-11e8-b28b-e5ea3f49db77?embed=true&_g=()" height="600" width="800"></iframe>
		"""
if __name__ == '__main__':
    flaskrun(application)
