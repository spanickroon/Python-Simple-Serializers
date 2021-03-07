import json
import base64
import inspect
import pickle

from app.services.service_abstract_base.service import BaseService


class JsonService(BaseService):

    @classmethod
    def defining_type_object(cls, serialize_object):
        return super().defining_type_object(serialize_object)

    @classmethod
    def serialize_data_type_relative(cls, serialize_object):
        serialize_object_type = cls.defining_type_object(serialize_object)

        if serialize_object_type == 'class':
            return cls._json_serialize_class(serialize_object)
        elif serialize_object_type == 'function':
            return cls._json_serialize_function(serialize_object)
        else:
            return cls._json_serialize_object(serialize_object)

    @classmethod
    def _json_serialize_object(cls, serialize_object):
        return json.dumps(serialize_object, indent=4)

    @classmethod
    def _json_serialize_function(cls, serialize_object):
        list_type_args = [
            'args', 'varargs', 'varkw', 'defaults',
            'kwonlyargs', 'kwonlydefaults', 'annotations',
        ]

        json_template = {
            'object': repr(serialize_object),
            'type': 'function',
            'name': serialize_object.__name__,
            'args': {
                arg_name: args for (
                    arg_name, args
                ) in zip(
                    list_type_args,
                    inspect.getfullargspec(serialize_object)
                )
            },
            'code': inspect.getsource(serialize_object).split('\n'),
            'base64': base64.b64encode(pickle.dumps(serialize_object)).decode('ascii')
        }

        return json.dumps(json_template, indent=4)

    @classmethod
    def _json_serialize_class(cls, serialize_object):
        json_template = {
            'object': repr(serialize_object),
            'type': 'class',
            'name': serialize_object.__name__,
            'code': inspect.getsource(serialize_object).split('\n'),
            'dict_class': {k: str(v) for k, v in serialize_object.__dict__.items()},
            'base64': base64.b64encode(pickle.dumps(serialize_object)).decode('ascii')
        }

        return json.dumps(json_template, indent=4)
