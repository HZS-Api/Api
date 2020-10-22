from dateutil.parser import parse
from typing import Dict
from json import dumps
from uuid import NAMESPACE_DNS, uuid3

class Incident:
    def transform(self, incident: Dict[str, str]) -> Dict[str, Dict[str, str]]:
        final_structure = {
            'incidents_uuid': {
                'S': self.__dict_to_uuid(incident)
            },
            'title': {
                'S': incident.get('department', False) or ''
            },
            'city': {
                'S': incident.get('city', False) or ''
            },
            'department': {
                'S': incident.get('department', False) or ''
            },
            'description': {
                'S': incident.get('description', False) or ''
            },
            'link': {
                'S': incident.get('link', False) or ''
            },
            'pub_date': {
                'S': self.__convert_datetime_format(incident['pub_date'])
            },
            'region': {
                'S': incident.get('region', False) or ''
            },
            'state': {
                'S': incident.get('state', False) or ''
            },
            'type': {
                'S': incident.get('type', False) or ''
            },
            'subtype': {
                'S': incident.get('subtype', False) or ''
            }
        }

        return final_structure

    def __dict_to_uuid(self, data: Dict[str, str]) -> str:
        return str(uuid3(NAMESPACE_DNS, dumps(data, sort_keys=True)))

    def __convert_datetime_format(self, timestamp: str) -> str:
        dt = parse(timestamp)
        return str(dt)
