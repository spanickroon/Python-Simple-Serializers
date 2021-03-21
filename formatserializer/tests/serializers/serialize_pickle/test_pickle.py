import pickle

from unittest import TestCase, mock

from formatserializer.serializers.serializer_pickle.serializer import PickleSerializer
from formatserializer.services.service_pickle.service import PickleService


class PickleSerializerTestCase(TestCase):
    def setUp(self) -> None:
        self.serializer = PickleSerializer()

    @mock.patch.object(PickleService, 'write_to_pickle_file')
    def test__dump__success(self, mock_service):
        mock_service.return_value = True

        self.serializer.dump('test', 'test')

    @mock.patch.object(PickleService, 'write_to_pickle_file')
    def test__dump__with_type_error__success(self, mock_service):
        mock_service.side_effect = TypeError()

        self.serializer.dump('test', 'test')

    def test__dumps__success(self):
        actual_result = self.serializer.dumps(123)

        self.assertEqual(actual_result, pickle.dumps(123))

    @mock.patch.object(PickleService, 'serialize_data')
    def test__dumps_with_type_error__success(self, mock_service):
        mock_service.side_effect = TypeError()

        actual_result = self.serializer.dumps('test')

        self.assertIsNone(actual_result)

    @mock.patch.object(PickleService, 'read_from_pickle_file')
    def test__load__success(self, mock_service):
        mock_service.return_value = b'\x80\x04K{.'

        actual_result = self.serializer.load('test')

        self.assertEqual(actual_result, 123)

    @mock.patch.object(PickleService, 'read_from_pickle_file')
    def test__load__success_with_file_not_found_error__success(self, mock_service):
        mock_service.side_effect = FileNotFoundError()

        actual_result = self.serializer.load('test')

        self.assertIsNone(actual_result)

    @mock.patch.object(PickleService, 'read_from_pickle_file')
    def test__load__success_with_type_error__success(self, mock_service):
        mock_service.side_effect = TypeError()

        actual_result = self.serializer.load('test')

        self.assertIsNone(actual_result)

    def test__loads__success(self):
        actual_result = self.serializer.loads(b'\x80\x04K{.')

        self.assertEqual(actual_result, 123)

    def test__loads_with_type_error__success(self):
        actual_result = self.serializer.loads({})

        self.assertIsNone(actual_result)
