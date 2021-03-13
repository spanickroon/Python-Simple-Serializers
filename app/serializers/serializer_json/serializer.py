import json

from app.serializers.serializer_abstact_base.serializer import BaseSerializer

from app.services.service_json.service import JsonService


class JsonSerializer(BaseSerializer):
    def __init__(self):
        pass

    def dump(self, serialize_object, file_path):
        try:
            JsonService.write_to_json_file(JsonService.serialize_data(serialize_object), file_path)
        except TypeError:
            pass

    def dumps(self, serialize_object):
        try:
            return json.dumps(JsonService.serialize_data(serialize_object), indent=4)
        except TypeError:
            return None

    def load(self, file_path):
        try:
            return JsonService.deserialize_data(JsonService.read_from_json_file(file_path))
        except FileNotFoundError:
            return None
        except TypeError:
            return None

    def loads(self, serialize_string):
        try:
            return JsonService.deserialize_data(json.loads(serialize_string))
        except TypeError:
            return None
