from flask import Flask, request, jsonify, g
from src.models.Incidents import Incidents as IncidentsModel
import os

app = Flask(__name__)

def main():
    app.run(host='0.0.0.0', debug=True)


@app.route('/incident', methods=['POST'])
def add_incident():
    endpoint_url = os.environ['DYNAMODB_URL']
    table_name = os.environ['TABLE_NAME']
    aws_region = os.environ['AWS_REGION']
    model = IncidentsModel(endpoint_url, table_name, aws_region)
    data = request.json
    resp = model.add_incident(data)
    return jsonify(resp)
