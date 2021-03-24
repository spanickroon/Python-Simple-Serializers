import argparse
import json


class ConvertArguments:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description='Serialize args')

    def setup_args(self):
        self.parser.add_argument(
            '--config_file',
            type=str,
            help='Serialization config file',
        )

        self.parser.add_argument(
            '--convert_format',
            choices=['json', 'pickle', 'yaml', 'toml'],
            help='Data convert format json by default',
        )

        self.parser.add_argument(
            '--file_to_convert',
            type=str,
            help='The file where the serialization data will be sent',
        )

        self.parser.add_argument(
            '--file_from_convert',
            type=str,
            help='The file from which the data for serialization will be taken',
        )

        return self.parser.parse_args()

    @staticmethod
    def parsing_config_file(parser):
        if not parser.config_file:
            return

        try:
            with open(parser.config_file, 'r') as rf:
                config_dict = json.load(rf)

                parser.convert_format = config_dict['convert_format']
                parser.file_from_convert = config_dict['file_from_convert']
                parser.file_to_convert = config_dict['file_to_convert']

        except (FileNotFoundError, KeyError, json.decoder.JSONDecodeError):
            print("Invalid config file")
