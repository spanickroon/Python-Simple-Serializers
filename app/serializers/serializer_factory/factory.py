class ObjectSerializeFactory:
    def __init__(self):
        self._serialize_creators = {
            'json': 1,
            'pickle': 1,
            'toml': 1,
            'yaml': 1,
        }

    def create_serializer(self, format_serialize: str):
        if format_serialize in self._serialize_creators:
            return self._serialize_creators[format_serialize]
        else:
            raise ValueError
