import os
from injector import singleton
from src.models.Incidents import Incidents

def configure(binder):
    endpoint_url = os.environ['DYNAMODB_URL']
    table_name = os.environ['TABLE_NAME']
    binder.bind(Incidents, to=Incidents(endpoint_url, table_name), scope=singleton)
