import argparse
import json


class SerializeArguments:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description='Serialize args')

    def setup_args(self):
        self.parser.add_argument(
            '--config_file',
            type=str,
            help='Serialization config file',
        )

        self.parser.add_argument(
            '--serialize_format',
            dest='store',
            choices=['json', 'pickle', 'yaml', 'toml'],
            help='Data serialization format json by default',
            default='json',
        )

        self.parser.add_argument(
            '--file_to_convert',
            type=str,
            help='The file where the serialization data will be sent',
            default='test'
        )

        self.parser.add_argument(
            '--file_from_convert',
            type=str,
            help='The file from which the data for serialization will be taken',
            default='test'
        )

        return self.parser.parse_args()

    @classmethod
    def check_config_file(cls, parser):
        return parser.config_file is not None

    @classmethod
    def parsing_config_file(cls, parser):
        try:
            with open(parser.config_file, 'r') as rf:
                config_dict = json.load(rf)

                if len(config_dict) != 3 or \
                        not config_dict['serialize_format'] or \
                        not config_dict['file_to_convert'] or \
                        not config_dict['file_from_convert']:
                    raise KeyError

                return config_dict.values()
        except (FileNotFoundError, KeyError, json.decoder.JSONDecodeError):
            return None

    @classmethod
    def distribution_arguments(cls, parser):
        try:
            if cls.check_config_file(parser):
                return cls.parsing_config_file(parser)
            else:
                return parser.serialize_format, parser.file_to_convert, parser.file_from_convert
        except AttributeError:
            return 'json', 'test', 'test'
