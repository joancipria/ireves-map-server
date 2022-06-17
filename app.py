# Flask imports
from flask import Flask
from flask import request
from flask_cors import CORS, cross_origin
import requests
from markupsafe import escape
import json

# Server imports
from population import calcPop
from static_models import *

# Create server
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

#-----------------
# --- API REST ---
#-----------------

"""
/health/openroute
Checks openroute service health
"""
@app.route('/health/openroute', methods=['POST', 'GET'])
@cross_origin()
def health():
    headers = {
        'Accept': 'application/json, application/geo+json, application/gpx+xml, img/png; charset=utf-8',
        'Content-Type': 'application/json; charset=utf-8'
    }
    call = requests.get('http://localhost:8080/ors/v2/health/', headers=headers)
    return call.json()

"""
/isochrones/:lat,:lng,:time
Returns an isochron in GeoJSON format from the given latitude (:lat), longitude (:lng) and time (:time).
"""
@app.route('/isochrones', methods=['POST', 'GET'])
@cross_origin()
def isochrones():
    lat = request.args.get('lat')
    lng = request.args.get('lng')
    time = int(request.args.get('time'))

    body = {"locations":[[lng, lat]],"range":[time*60]}

    headers = {
        'Accept': 'application/json, application/geo+json, application/gpx+xml, img/png; charset=utf-8',
        'Content-Type': 'application/json; charset=utf-8'
    }
    call = requests.post('http://localhost:8080/ors/v2/isochrones/driving-car', json=body, headers=headers)
    return call.json()

"""
/population/:polygon
Returns population of an area determined by a GeoJSON polygon (:polygon).
"""
@app.route('/population', methods=['POST', 'GET'])
@cross_origin()
def population():
    polygon = request.args.get('polygon')
    population = calcPop(polygon)
    return population

"""
/model/static/:version
Returns the specified (:version) static model in JSON formart
"""
@app.route('/model/static/', methods=['POST', 'GET'])
@cross_origin()
def staticModel():
    #modelVersion = request.args.get('version')
    return staticModelV1