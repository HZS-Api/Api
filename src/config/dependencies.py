import os
import boto3
from injector import singleton
from src.models.Incidents import Incidents

def configure(binder):
    endpoint_url = os.environ['DYNAMODB_URL']
    table_name = os.environ['TABLE_NAME']
    db_client = get_db_client(endpoint_url)
    binder.bind(Incidents, to=Incidents(db_client, table_name), scope=singleton)

def get_db_client(endpoint_url: str):
    if not endpoint_url :
        return boto3.client('dynamodb')
    else:
        return boto3.client('dynamodb', region_name='', aws_access_key_id='', aws_secret_access_key='', endpoint_url=endpoint_url)
