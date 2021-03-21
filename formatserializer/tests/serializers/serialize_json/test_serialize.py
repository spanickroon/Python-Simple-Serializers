import json

from unittest import TestCase, mock

from formatserializer.serializers.serializer_json.serializer import JsonSerializer
from formatserializer.services.service_json.service import JsonService
from formatserializer.testing.services.service_json.service import expected_dict_int


class JsonSerializerTestCase(TestCase):
    def setUp(self) -> None:
        self.serializer = JsonSerializer()

    @mock.patch.object(JsonService, 'write_to_json_file')
    def test__dump__success(self, mock_service):
        mock_service.return_value = True

        self.serializer.dump('test', 'test')

    @mock.patch.object(JsonService, 'write_to_json_file')
    def test__dump__with_type_error__success(self, mock_service):
        mock_service.side_effect = TypeError()

        self.serializer.dump('test', 'test')

    @mock.patch.object(JsonService, 'serialize_data')
    def test__dumps__success(self, mock_service):
        mock_service.return_value = {'test': 'test'}

        actual_result = self.serializer.dumps('test')

        self.assertEqual(actual_result, json.dumps({'test': 'test'}, indent=4))

    @mock.patch.object(JsonService, 'serialize_data')
    def test__dumps_with_type_error__success(self, mock_service):
        mock_service.side_effect = TypeError()

        actual_result = self.serializer.dumps('test')

        self.assertIsNone(actual_result)

    @mock.patch.object(JsonService, 'read_from_json_file')
    def test__load__success(self, mock_service):
        mock_service.return_value = {'base64': expected_dict_int.get('base64')}

        actual_result = self.serializer.load('test')

        self.assertEqual(actual_result, 123)

    @mock.patch.object(JsonService, 'read_from_json_file')
    def test__load__success_with_file_not_found_error__success(self, mock_service):
        mock_service.side_effect = FileNotFoundError()

        actual_result = self.serializer.load('test')

        self.assertIsNone(actual_result)

    @mock.patch.object(JsonService, 'read_from_json_file')
    def test__load__success_with_type_error__success(self, mock_service):
        mock_service.side_effect = TypeError()

        actual_result = self.serializer.load('test')

        self.assertIsNone(actual_result)

    def test__loads__success(self):
        actual_result = self.serializer.loads(json.dumps({'base64': expected_dict_int.get('base64')}))

        self.assertEqual(actual_result, 123)

    def test__loads_with_type_error__success(self):
        actual_result = self.serializer.loads({})

        self.assertIsNone(actual_result)
