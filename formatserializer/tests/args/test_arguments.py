from unittest import TestCase, mock
from parameterized import parameterized

from argparse import Namespace

from formatserializer.args.arguments import SerializeArguments


class SerializeArgumentsTestCase(TestCase):
    def setUp(self) -> None:
        self.parser = SerializeArguments()
        self.parser_class = SerializeArguments
        self.parsing_config_file = self.parser_class.parsing_config_file

    def test__setup_args__success(self):
        expected_result = Namespace(
            config_file=None,
            file_from_convert='test',
            file_to_convert='test',
            store='json'
        )

        actual_result = self.parser.setup_args()

        self.assertEqual(actual_result, expected_result)

    def test__check_config_file__success(self):
        actual_result = self.parser_class.check_config_file(self.parser.setup_args())

        self.assertFalse(actual_result)

    @parameterized.expand([
        ("check_config_true", True, True),
        ("check_config_false", False, True),
        ("not_parser_object", True, False)
    ])
    def test__distribution_arguments__success(self, _, check_config, is_parser):
        self.parser_class.check_config_file = mock.MagicMock(return_value=check_config)
        self.parser_class.parsing_config_file = mock.MagicMock(return_value=('json', 'test', 'test'))

        parser = self.parser.setup_args() if is_parser else None
        actual_result = self.parser_class.distribution_arguments(parser)

        self.assertTupleEqual(actual_result, ('json', 'test', 'test'))
