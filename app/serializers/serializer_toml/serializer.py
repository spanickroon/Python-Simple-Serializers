import toml

from app.serializers.serializer_abstact_base.serializer import BaseSerializer
from app.services.service_toml.service import TomlService


class TomlSerializer(BaseSerializer):
    def __init__(self):
        pass

    def dump(self, serialize_object, file_path):
        TomlService.write_to_yaml_file(serialize_object, file_path)

    def dumps(self, serialize_object):
        return TomlService.serialize_data(serialize_object)

    def load(self, file_path):
        try:
            return TomlService.deserialize_data(TomlService.read_from_yaml_file(file_path))
        except FileNotFoundError as exc:
            return f'{exc.strerror} {exc.filename}'

    def loads(self, serialize_string):
        return TomlService.deserialize_data(toml.loads(serialize_string))
