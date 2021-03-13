import json

from app.services.service_abstract_base.service import BaseService


class JsonService(BaseService):

    @classmethod
    def defining_type_object(cls, serialize_object):
        return super().defining_type_object(serialize_object)

    @classmethod
    def _check_serializable(cls, serialize_object):
        try:
            json.dumps(serialize_object)
            return True
        except TypeError:
            return False

    @classmethod
    def serialize_data(cls, serialize_object):
        serialize_object_type = cls.defining_type_object(serialize_object)
        serializable_by_default = cls._check_serializable(serialize_object)

        json_template = {
            'object': repr(serialize_object),
            'type': serialize_object_type,
            'serializable_by_default': serializable_by_default,
            'name': cls.getting_name_object(serialize_object),
            'value': serialize_object if serializable_by_default else None,
            'dict_class': cls.getting_class_dict(serialize_object),
            'args': cls.getting_function_arguments(serialize_object),
            'code': cls.getting_source_code(serialize_object),
            'base64': cls.getting_base64_pickle_object(serialize_object)
        }

        return json_template

    @classmethod
    def deserialize_data(cls, json_object):
        return cls.getting_object_from_base64(json_object.get('base64'))

    @classmethod
    def write_to_json_file(cls, serialize_object, file_path):
        with open(file_path, 'w+') as wf:
            json.dump(serialize_object, wf, indent=4)

    @classmethod
    def read_from_json_file(cls, file_path):
        with open(file_path, 'r') as rf:
            return json.load(rf)
