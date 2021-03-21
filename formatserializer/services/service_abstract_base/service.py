import inspect
import base64
import pickle

from abc import ABC, abstractmethod


class BaseService(ABC):

    @classmethod
    @abstractmethod
    def defining_type_object(cls, serialize_object):
        if inspect.isclass(serialize_object):
            return 'class'
        else:
            return str(type(serialize_object)).split('\'')[1]

    @classmethod
    def getting_function_arguments(cls, serialize_function):
        list_type_args = [
            'args', 'varargs', 'varkw', 'defaults',
            'kwonlyargs', 'kwonlydefaults', 'annotations',
        ]
        try:
            return {
                arg_name: args for (
                    arg_name, args
                ) in zip(
                    list_type_args,
                    inspect.getfullargspec(serialize_function)
                )
            }
        except TypeError:
            return {}

    @classmethod
    def getting_class_dict(cls, serialize_class):
        try:
            return {k: str(v) for k, v in serialize_class.__dict__.items()}
        except AttributeError:
            return {}

    @classmethod
    def getting_name_object(cls, serialize_object):
        try:
            return serialize_object.__name__
        except AttributeError:
            return None

    @classmethod
    def getting_source_code(cls, serialize_object):
        try:
            return inspect.getsource(serialize_object).split('\n')
        except TypeError:
            return []

    @classmethod
    def getting_base64_pickle_object(cls, serialize_object):
        try:
            return base64.b64encode(pickle.dumps(serialize_object)).decode('ascii')
        except TypeError:
            return None

    @classmethod
    def getting_object_from_base64(cls, base64_object):
        try:
            return pickle.loads(base64.b64decode(base64_object.encode('ascii')))
        except AttributeError:
            return None
