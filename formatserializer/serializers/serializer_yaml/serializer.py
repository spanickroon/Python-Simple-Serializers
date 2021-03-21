import yaml
import uuid

from formatserializer.serializers.serializer_abstact_base.serializer import BaseSerializer
from formatserializer.services.service_yaml.service import YamlService


class YamlSerializer(BaseSerializer):
    class_id = uuid.uuid4()

    def __init__(self):
        pass

    def dump(self, serialize_object, file_path):
        try:
            YamlService.write_to_yaml_file(serialize_object, file_path)
        except TypeError:
            pass

    def dumps(self, serialize_object):
        try:
            return YamlService.serialize_data(serialize_object)
        except TypeError:
            return None

    def load(self, file_path):
        try:
            return YamlService.deserialize_data(YamlService.read_from_yaml_file(file_path))
        except FileNotFoundError:
            return None
        except TypeError:
            return None

    def loads(self, serialize_string):
        try:
            return YamlService.deserialize_data(yaml.load(serialize_string, Loader=yaml.Loader))
        except TypeError:
            return None
