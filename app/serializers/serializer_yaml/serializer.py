import yaml

from app.serializers.serializer_abstact_base.serializer import BaseSerializer
from app.services.service_yaml.service import YamlService


class YamlSerializer(BaseSerializer):
    def __init__(self):
        pass

    def dump(self, serialize_object, file_path):
        YamlService.write_to_yaml_file(serialize_object, file_path)

    def dumps(self, serialize_object):
        return YamlService.serialize_data(serialize_object)

    def load(self, file_path):
        try:
            return YamlService.deserialize_data(YamlService.read_from_yaml_file(file_path))
        except FileNotFoundError as exc:
            return f'{exc.strerror} {exc.filename}'

    def loads(self, serialize_string):
        return YamlService.deserialize_data(yaml.load(serialize_string, Loader=yaml.Loader))
