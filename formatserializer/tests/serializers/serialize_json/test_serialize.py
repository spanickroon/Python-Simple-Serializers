from unittest import TestCase
from parameterized import parameterized

from formatserializer.serializers.serializer_json.serializer import JsonSerializer


class JsonSerializerTestCase(TestCase):
    def setUp(self) -> None:
        self.serializer = JsonSerializer()
