from unittest import TestCase
from formatserializer.serializers.serializer_factory.factory import ObjectSerializeFactory
from formatserializer.serializers.serializer_json.serializer import JsonSerializer
from formatserializer.serializers.serializer_pickle.serializer import PickleSerializer
from formatserializer.serializers.serializer_yaml.serializer import YamlSerializer
from formatserializer.serializers.serializer_toml.serializer import TomlSerializer


class ObjectSerializeFactoryTestCase(TestCase):
    def setUp(self) -> None:
        self.factory = ObjectSerializeFactory()

    def test__create_serializer__success(self):
        actual_factory_pickle = self.factory.create_serializer('pickle')
        actual_factory_json = self.factory.create_serializer('json')
        actual_factory_toml = self.factory.create_serializer('toml')
        actual_factory_yaml = self.factory.create_serializer('yaml')

        self.assertEqual(actual_factory_pickle.class_id, PickleSerializer.class_id)
        self.assertEqual(actual_factory_json.class_id, JsonSerializer.class_id)
        self.assertEqual(actual_factory_toml.class_id, TomlSerializer.class_id)
        self.assertEqual(actual_factory_yaml.class_id, YamlSerializer.class_id)

    def test__create_serializer__raise_exception(self):
        with self.assertRaises(ValueError):
            self.factory.create_serializer('test')
