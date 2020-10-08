import boto3
from src.ValueObject.Incident import Incident

class Incidents:
    __client: boto3
    __table_name: str

    def __init__(self, endpoint_url: str, table_name: str):
        self.__client = boto3.client('dynamodb', region_name='', aws_access_key_id='', aws_secret_access_key='', endpgoint_url=endpoint_url)
        self.__table_name = table_name

    def add_incident(self, incident):
        resp = self.__client.put_item(
            TableName=self.__table_name,
            Item={
                'incidents_uuid': {
                    "S": "kjn"
                }
            }
        )

        return resp
