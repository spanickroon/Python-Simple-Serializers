import inspect

from abc import ABC, abstractmethod


class BaseService(ABC):

    @classmethod
    @abstractmethod
    def defining_type_object(cls, serialize_object):
        if inspect.isclass(serialize_object):
            return 'class'
        else:
            return str(type(serialize_object)).split('\'')[1]
