import boto3

class Incidents:
    __client: boto3
    __table_name: str

    def __init__(self, db_client: boto3, table_name: str):
        self.__client = db_client
        self.__table_name = table_name

    def add_incident(self, incident):
        resp = self.__client.put_item(
            TableName=self.__table_name,
            Item={
                'incidents_uuid': {
                    'S': incident['name']
                }
            }
        )

        return resp
