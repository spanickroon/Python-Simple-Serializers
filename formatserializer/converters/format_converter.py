import os

import json
import pickle
import toml
import yaml


class FormatConverter:
    def __init__(self, convert_format, file_from_covert, file_to_convert):
        self.convert_format = convert_format
        self.file_from_covert = file_from_covert
        self.file_to_convert = file_to_convert
        self.data = None

        self.read_file_info = {
            'json': self._read_json,
            'pickle': self._read_pickle,
            'toml': self._read_toml,
            'yaml': self._read_yaml
        }

        self.write_file_info = {
            'json': self._write_json,
            'pickle': self._write_pickle,
            'toml': self._write_toml,
            'yaml': self._write_yaml
        }

    def _read_json(self):
        with open(self.file_from_covert, 'r') as rf:
            return json.load(rf)

    def _read_pickle(self):
        with open(self.file_from_covert, 'rb') as rfb:
            return pickle.load(rfb)

    def _read_toml(self):
        with open(self.file_from_covert, 'r') as rf:
            return toml.load(rf)

    def _read_yaml(self):
        with open(self.file_from_covert, 'r') as rf:
            return yaml.load(rf, Loader=yaml.Loader)

    def _write_json(self):
        with open(self.file_to_convert, 'w+') as wf:
            json.dump(self.data, wf, indent=4)

    def _write_pickle(self):
        with open(self.file_to_convert, 'w+b') as wfb:
            pickle.dump(self.data, wfb)

    def _write_toml(self):
        with open(self.file_to_convert, 'w+') as wf:
            toml.dump(self.data, wf)

    def _write_yaml(self):
        with open(self.file_to_convert, 'w+') as wf:
            yaml.dump(self.data, wf)

    def _file_convert(self):
        _, file_extension = os.path.splitext(self.file_from_covert)
        file_extension = file_extension[1:]

        if file_extension == self.convert_format:
            return False

        self.data = self.read_file_info[file_extension]()

        self.write_file_info[self.convert_format]()

        return True

    def convert(self):
        try:
            return self._file_convert()
        except KeyError:
            print(f'Format converting not found or file from convert has has the wrong extension')
            return False
        except FileNotFoundError:
            print(f'File {self.file_from_covert} not found')
