from unittest import TestCase

from formatserializer.services.service_pickle.service import PickleService


class PickleServiceTestCase(TestCase):
    def setUp(self) -> None:
        self.service = PickleService

    def test__serialize_data__success(self):
        actual_result = self.service.serialize_data(123)

        self.assertEqual(actual_result, b'\x80\x04K{.')

    def test__serialize_data_with_type_error__success(self):
        actual_result = self.service.serialize_data((i for i in range(10)))

        self.assertIsNone(actual_result)

    def test__deserialize_data__success(self):
        actual_result = self.service.deserialize_data(b'\x80\x04K{.')

        self.assertEqual(actual_result, 123)
