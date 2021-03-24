import json

from unittest import TestCase, mock
from argparse import Namespace

from formatserializer.args.arguments import ConvertArguments


class SerializeArgumentsTestCase(TestCase):
    def setUp(self) -> None:
        self.parser = ConvertArguments()
        self.parser_class = ConvertArguments
        self.parsing_config_file = self.parser_class.parsing_config_file

    def test__setup_args__success(self):
        expected_result = Namespace(
            config_file=None,
            convert_format=None,
            file_from_convert=None,
            file_to_convert=None,
        )

        actual_result = self.parser.setup_args()

        self.assertEqual(actual_result, expected_result)

    def test__parsing_config_file_with_not_file__success(self):
        parser = self.parser.setup_args()
        self.parser_class.parsing_config_file(parser)

        expected_result = Namespace(
            config_file=None,
            convert_format=None,
            file_from_convert=None,
            file_to_convert=None,
        )

        self.assertEqual(parser, expected_result)

    @mock.patch('builtins.open', mock.mock_open(read_data=json.dumps({
      'convert_format': 'toml',
      'file_to_convert': 'test.toml',
      'file_from_convert': 'test.json'
    })))
    def test__parsing_config_file__success(self):
        parser = self.parser.setup_args()
        parser.config_file = 'test_config.json'

        self.parser_class.parsing_config_file(parser)

        expected_result = Namespace(
            config_file='test_config.json',
            convert_format='toml',
            file_from_convert='test.json',
            file_to_convert='test.toml',
        )

        self.assertEqual(parser, expected_result)
