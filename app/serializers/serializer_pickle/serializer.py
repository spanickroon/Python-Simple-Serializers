

from app.serializers.serializer_abstact_base.serializer import BaseSerializer

from app.services.service_pickle.service import PickleService


class PickleSerializer(BaseSerializer):
    def __init__(self):
        pass

    def dump(self, serialize_object, file_path):
        PickleService.write_to_pickle_file(PickleService.serialize_data(serialize_object), file_path)

    def dumps(self, serialize_object):
        return PickleService.serialize_data(serialize_object)

    def load(self, file_path):
        try:
            return PickleService.deserialize_data(PickleService.read_from_pickle_file(file_path))
        except FileNotFoundError as exc:
            return f'{exc.strerror} {exc.filename}'

    def loads(self, serialize_string):
        return PickleService.deserialize_data(serialize_string)