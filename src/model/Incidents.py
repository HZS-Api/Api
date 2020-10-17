import boto3
from src.transformer.Incident import Incident as IncidentTransformer


class Incidents:
    __incident_transformer: IncidentTransformer
    __client: boto3
    __table_name: str

    def __init__(self, incident_transformer: IncidentTransformer, db_client: boto3, table_name: str):
        self.__incident_transformer = incident_transformer
        self.__client = db_client
        self.__table_name = table_name

    def add_incident(self, incident):
        resp = self.__client.put_item(
            TableName = self.__table_name,
            Item = self.__incident_transformer.transform(incident)
        )

        return resp
