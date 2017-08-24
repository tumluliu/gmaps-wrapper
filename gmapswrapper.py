#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Wrapper service of Google Maps Directions API
"""

import os
import logging.config
import json
import requests
from settings import GMAPS_KEY
from flask import Flask, request
from flask_cors import CORS

LOGGING_CONF_FILE = 'logging.json'
DEFAULT_LOGGING_LVL = logging.INFO
path = LOGGING_CONF_FILE
value = os.getenv('LOG_CFG', None)
if value:
    path = value
if os.path.exists(path):
    with open(path, 'rt') as f:
        config = json.load(f)
    logging.config.dictConfig(config)
else:
    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)
CORS(app)
GOOGLE_MAPS_URL_TEMPLATE = "https://maps.googleapis.com/maps/api/directions/json"


@app.route("/")
def getGoogleMapsDirections():
    logger.debug(request.query_string)
    payload = {
        "origin": request.args.get("origin"),
        "destination": request.args.get("destination"),
        "mode": request.args.get("mode"),
        "key": request.args.get("key")
    }
    r = requests.get(GOOGLE_MAPS_URL_TEMPLATE, params=payload)
    return r.content


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
