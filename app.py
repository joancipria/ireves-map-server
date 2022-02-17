# save this as app.py
from flask import Flask
from flask import request
from flask_cors import CORS, cross_origin
import json
import requests

from pop import *

from markupsafe import escape

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/isochrones', methods=['POST', 'GET'])
@cross_origin()
def isochrones():
    lat = request.args.get('lat')
    lng = request.args.get('lng')
    time = int(request.args.get('time'))
    """Cálcula la isócrona en la posición indicada y de la extensión de tiempo proporcionada

    Parameters:
    lng (float): Longitud de la posición
    lat (float): Latitud de la posición
    tiempoEnMinutos (int): Extensión de la isocrona en minutos

    Returns:
    string:Isocrona, en forma de GeoJson y formato string
    """
    body = {"locations":[[lng, lat]],"range":[time*60]}

    headers = {
        'Accept': 'application/json, application/geo+json, application/gpx+xml, img/png; charset=utf-8',
        'Authorization': '5b3ce3597851110001cf6248478bc3389a694195a33773d711ee4ebf', #Private
        'Content-Type': 'application/json; charset=utf-8'
    }
    call = requests.post('https://api.openrouteservice.org/v2/isochrones/driving-car', json=body, headers=headers)
    return call.json()

@app.route('/population', methods=['POST', 'GET'])
@cross_origin()
def population():
    polygon = request.args.get('polygon')
    population = calcPop(polygon)
    return population
