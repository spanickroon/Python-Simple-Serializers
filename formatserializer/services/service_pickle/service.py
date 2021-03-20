import pickle

from formatserializer.services.service_abstract_base.service import BaseService


class PickleService(BaseService):

    @classmethod
    def defining_type_object(cls, serialize_object):
        return super().defining_type_object(serialize_object)

    @classmethod
    def serialize_data(cls, serialize_object):
        try:
            return pickle.dumps(serialize_object)
        except TypeError:
            return None

    @classmethod
    def deserialize_data(cls, pickle_object):
        return pickle.loads(pickle_object)

    @classmethod
    def write_to_pickle_file(cls, serialize_object, file_path):
        with open(file_path, 'w+b') as wf:
            pickle.dump(serialize_object, wf)

    @classmethod
    def read_from_pickle_file(cls, file_path):
        with open(file_path, 'rb') as rf:
            return pickle.load(rf)
