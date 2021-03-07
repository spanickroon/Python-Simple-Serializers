from app.serializers.serializer_json.serializer import JsonSerializer
from app.serializers.serializer_pickle.serializer import PickleSerializer
from app.serializers.serializer_toml.serializer import TomlSerializer
from app.serializers.serializer_yaml.serializer import YamlSerializer


class ObjectSerializeFactory:
    def __init__(self):
        self._serialize_creators = {
            'json': JsonSerializer(),
            'pickle': PickleSerializer(),
            'toml': TomlSerializer(),
            'yaml': YamlSerializer(),
        }

    def create_serializer(self, format_serialize: str):
        if format_serialize in self._serialize_creators:
            return self._serialize_creators[format_serialize]
        else:
            raise ValueError(f'{format_serialize} argument not found')
