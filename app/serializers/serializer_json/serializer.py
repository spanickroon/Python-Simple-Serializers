import json

from app.serializers.serializer_abstact_base.serializer import BaseSerializer

from app.services.service_json.service import JsonService


class JsonSerializer(BaseSerializer):
    def __init__(self):
        pass

    def dump(self, serialize_object, file_path):
        JsonService.write_to_json_file(JsonService.serialize_data(serialize_object), file_path)

    def dumps(self, serialize_object):
        return json.dumps(JsonService.serialize_data(serialize_object), indent=4)

    def load(self, file_path):
        try:
            return JsonService.deserialize_data(JsonService.read_from_json_file(file_path))
        except FileNotFoundError as exc:
            return f'{exc.strerror} {exc.filename}'

    def loads(self, serialize_string):
        return JsonService.deserialize_data(json.loads(serialize_string))
