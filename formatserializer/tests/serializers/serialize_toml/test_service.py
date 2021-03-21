import toml

from unittest import TestCase, mock

from formatserializer.serializers.serializer_toml.serializer import TomlSerializer
from formatserializer.services.service_toml.service import TomlService
from formatserializer.testing.services.service_json.service import expected_dict_int


class TomlSerializerTestCase(TestCase):
    def setUp(self) -> None:
        self.serializer = TomlSerializer()

    @mock.patch.object(TomlService, 'write_to_toml_file')
    def test__dump__success(self, mock_service):
        mock_service.return_value = True

        self.serializer.dump('test', 'test')

    @mock.patch.object(TomlService, 'write_to_toml_file')
    def test__dump__with_type_error__success(self, mock_service):
        mock_service.side_effect = TypeError()

        self.serializer.dump('test', 'test')

    def test__dumps__success(self):
        actual_result = self.serializer.dumps(123)

        self.assertEqual(actual_result, toml.dumps(expected_dict_int))

    @mock.patch.object(TomlService, 'serialize_data')
    def test__dumps_with_type_error__success(self, mock_service):
        mock_service.side_effect = TypeError()

        actual_result = self.serializer.dumps('test')

        self.assertIsNone(actual_result)

    @mock.patch.object(TomlService, 'read_from_toml_file')
    def test__load__success(self, mock_service):
        mock_service.return_value = {'base64': expected_dict_int.get('base64')}

        actual_result = self.serializer.load('test')

        self.assertEqual(actual_result, 123)

    @mock.patch.object(TomlService, 'read_from_toml_file')
    def test__load__success_with_file_not_found_error__success(self, mock_service):
        mock_service.side_effect = FileNotFoundError()

        actual_result = self.serializer.load('test')

        self.assertIsNone(actual_result)

    @mock.patch.object(TomlService, 'read_from_toml_file')
    def test__load__success_with_type_error__success(self, mock_service):
        mock_service.side_effect = TypeError()

        actual_result = self.serializer.load('test')

        self.assertIsNone(actual_result)

    def test__loads__success(self):
        actual_result = self.serializer.loads(toml.dumps({'base64': expected_dict_int.get('base64')}))

        self.assertEqual(actual_result, 123)

    def test__loads_with_type_error__success(self):
        actual_result = self.serializer.loads({})

        self.assertIsNone(actual_result)
