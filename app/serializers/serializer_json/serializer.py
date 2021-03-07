from app.serializers.serializer_abstact_base.serializer import BaseSerializer

from app.services.service_json.service import JsonService


class JsonSerializer(BaseSerializer):
    def __init__(self):
        pass

    def dump(self, serialize_object, file_path):
        pass

    def dumps(self, serialize_object):
        return JsonService.serialize_data_type_relative(serialize_object)

    def load(self, file_path):
        pass

    def loads(self, serialize_string):
        pass
