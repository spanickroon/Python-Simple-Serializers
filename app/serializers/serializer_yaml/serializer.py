from app.serializers.serializer_abstact_base.serializer import BaseSerializer


class YamlSerializer(BaseSerializer):
    def __init__(self):
        pass

    def dump(self, serialize_object, file_path):
        pass

    def dumps(self, serialize_object):
        pass

    def load(self, file_path):
        pass

    def loads(self, serialize_string):
        pass
