from typing import Dict
from json import dumps
from uuid import NAMESPACE_DNS, uuid3

class Incident:
    def transform(self, incident: Dict[str, str]) -> Dict[str, Dict[str, str]]:
        final_structure = {
            'incidents_uuid': {
                'S': self.__dict_to_uuid(incident)
            }
        }
        for key in incident:
            final_structure[key] = {
                'S': incident[key]
            }

        return final_structure

    def __dict_to_uuid(self, data):
        return str(uuid3(NAMESPACE_DNS, dumps(data, sort_keys=True)))
