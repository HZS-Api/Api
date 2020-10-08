import os
from flask import Flask, request, jsonify
from src.models.Incidents import Incidents as IncidentsModel
from typing import Dict

services: Dict
app: Flask = Flask(__name__)


def main():
    app.run(host='0.0.0.0', debug=True)

@app.route('/incident', methods=['POST'])
def add_incident():
    endpoint_url = os.environ['DYNAMODB_URL']
    table_name = os.environ['TABLE_NAME']
    model = IncidentsModel(endpoint_url, table_name)
    data = request.json
    resp = model.add_incident(data)
    return jsonify(resp)
