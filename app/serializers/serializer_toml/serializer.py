import toml

from app.serializers.serializer_abstact_base.serializer import BaseSerializer
from app.services.service_toml.service import TomlService


class TomlSerializer(BaseSerializer):
    def __init__(self):
        pass

    def dump(self, serialize_object, file_path):
        try:
            TomlService.write_to_yaml_file(serialize_object, file_path)
        except TypeError:
            pass

    def dumps(self, serialize_object):
        try:
            return TomlService.serialize_data(serialize_object)
        except TypeError:
            return None

    def load(self, file_path):
        try:
            return TomlService.deserialize_data(TomlService.read_from_yaml_file(file_path))
        except FileNotFoundError:
            return None
        except TypeError:
            return None

    def loads(self, serialize_string):
        try:
            return TomlService.deserialize_data(toml.loads(serialize_string))
        except TypeError:
            return None
