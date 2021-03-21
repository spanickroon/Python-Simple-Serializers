import toml

from formatserializer.services.service_abstract_base.service import BaseService
from formatserializer.services.service_json.service import JsonService


class TomlService(BaseService):

    @classmethod
    def defining_type_object(cls, serialize_object):
        return super().defining_type_object(serialize_object)

    @classmethod
    def serialize_data(cls, serialize_object):
        json_template = JsonService.serialize_data(serialize_object)
        return toml.dumps(json_template)

    @classmethod
    def deserialize_data(cls, json_object):
        return cls.getting_object_from_base64(json_object.get('base64'))

    @classmethod
    def write_to_yaml_file(cls, serialize_object, file_path):
        json_template = JsonService.serialize_data(serialize_object)
        with open(file_path, 'w+') as wf:
            toml.dump(json_template, wf)

    @classmethod
    def read_from_yaml_file(cls, file_path):
        with open(file_path, 'r') as rf:
            return toml.load(rf)
