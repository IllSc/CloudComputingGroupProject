#!flask/bin/python
import json
import requests
from flask import Flask, Response
from helloworld.flaskrun import flaskrun
from flask import render_template,request, redirect, url_for
from elasticsearch import Elasticsearch, RequestsHttpConnection
import elasticsearch_dsl
from elasticsearch_dsl import Search



application = Flask(__name__)
origin = None
esendpoint = 'search-cloud-computing-project-upc-uq5b7q3o57i5xaez54rlfluabu.eu-central-1.es.amazonaws.com'
es = Elasticsearch(
            hosts=[{'host': esendpoint, 'port': 443}],
            use_ssl=True,
            verify_certs=True,
            connection_class=RequestsHttpConnection)

"""@application.route('/', methods=['GET'])
def get():
    return Response(json.dumps({'Output': 'Hello '}), mimetype='application/json', status=200)

@application.route('/', methods=['POST'])
def post():
    return Response(json.dumps({'Output': 'Hello '}), mimetype='application/json', status=200) """


@application.route('/')
def homepage():
	return render_template('template.html')

@application.route('/search', methods = ['GET','POST'])
def get_info():
    global origin
    origin = request.form['value']
    s = Search(using=es, index="train_departure").query("match", origin_name=origin)
    result = s.execute()
    return render_template('result.html', result= result, value = origin)

@application.route('/back', methods = ['GET','POST'])
def back():
    return redirect(url_for('homepage'))

@application.route('/chord')
def chord():
    url = "https://yev0r4zzyf.execute-api.eu-central-1.amazonaws.com/CloudComputing/rail-data-dev-agg"

    
    response = requests.request("GET", url)
    matrices = json.loads(response.text)
    print(response)
    return render_template('chord.html',matrixData=matrices)

if __name__ == '__main__':
    flaskrun(application)
