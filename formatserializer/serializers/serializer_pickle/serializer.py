

from formatserializer.serializers.serializer_abstact_base.serializer import BaseSerializer

from formatserializer.services.service_pickle.service import PickleService


class PickleSerializer(BaseSerializer):
    def __init__(self):
        pass

    def dump(self, serialize_object, file_path):
        try:
            PickleService.write_to_pickle_file(PickleService.serialize_data(serialize_object), file_path)
        except TypeError:
            pass

    def dumps(self, serialize_object):
        try:
            return PickleService.serialize_data(serialize_object)
        except TypeError:
            return None

    def load(self, file_path):
        try:
            return PickleService.deserialize_data(PickleService.read_from_pickle_file(file_path))
        except FileNotFoundError:
            return None
        except TypeError:
            return None

    def loads(self, serialize_string):
        try:
            return PickleService.deserialize_data(serialize_string)
        except TypeError:
            return None
