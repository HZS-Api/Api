from flask import Blueprint, Flask, request, jsonify
from injector import inject
from src.models.Incidents import Incidents as IncidentsModel

incidents_blueprint = Blueprint('api', __name__)


@incidents_blueprint.route('/test', methods=['GET'])
def index():
    return jsonify([{'foo': 'bar'}])


@inject
@incidents_blueprint.route('/incident', methods=['POST'])
def add_incident(model: IncidentsModel):
    data = request.json
    resp = model.add_incident(data)
    return jsonify(resp)
