from abc import ABC, abstractmethod
from app.services.service_abstract_base.service import BaseService


class BaseSerializer(ABC):

    @abstractmethod
    def dump(self, serialize_object, file_path):
        pass

    @abstractmethod
    def dumps(self, serialize_object):
        pass

    @abstractmethod
    def load(self, file_path):
        pass

    @abstractmethod
    def loads(self, serialize_string):
        pass
