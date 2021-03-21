from unittest import TestCase
from parameterized import parameterized

from formatserializer.services.service_abstract_base.service import BaseService

from formatserializer.testing.services.service_abstract_base.service import (
    ExampleClass, example_function, expected_dict_args_function, expected_dict_args_class,
    expected_base64_string,
)


class BaseServiceTestCase(TestCase):
    def setUp(self) -> None:
        self.service = BaseService

    @parameterized.expand([
        ('list_object', [1, 2, 3], 'list'),
        ('string_object', '123', 'str'),
        ('class_object', ExampleClass, 'class'),
        ('function_object', example_function, 'function')
    ])
    def test__defining_type_object__success(self, _, object_serialize, expected_result):
        actual_result = self.service.defining_type_object(object_serialize)

        self.assertEqual(actual_result, expected_result)

    def test__getting_function_arguments__success(self):
        actual_result = self.service.getting_function_arguments(example_function)

        self.assertDictEqual(actual_result, expected_dict_args_function)

    def test__getting_function_arguments_with_type_error__success(self):
        actual_result = self.service.getting_function_arguments(0)

        self.assertDictEqual(actual_result, {})

    def test__getting_class_dict__success(self):
        actual_result = self.service.getting_class_dict(ExampleClass)

        self.assertEqual(actual_result.get('__module__'), expected_dict_args_class.get('__module__'))
        self.assertEqual(actual_result.get('__dict__'), expected_dict_args_class.get('__dict__'))
        self.assertEqual(actual_result.get('__weakref__'), expected_dict_args_class.get('__weakref__'))
        self.assertEqual(actual_result.get('__doc__'), expected_dict_args_class.get('__doc__'))

    def test__getting_class_dict_with_attribute_error__success(self):
        actual_result = self.service.getting_class_dict(0)

        self.assertDictEqual(actual_result, {})

    @parameterized.expand([
        ('class_object', ExampleClass, 'ExampleClass'),
        ('function_object', example_function, 'example_function')
    ])
    def test__getting_name_object__success(self, _, serialize_object, expected_result):
        actual_result = self.service.getting_name_object(serialize_object)

        self.assertEqual(actual_result, expected_result)

    def test__getting_name_object_with_attribute_error__success(self):
        actual_result = self.service.getting_name_object(0)

        self.assertIsNone(actual_result)

    @parameterized.expand([
        ('class_object', ExampleClass, ['class ExampleClass:', '    def __init__(self):', '        pass', '']),
        ('function_object', example_function, ['def example_function():', '    pass', ''])
    ])
    def test__getting_source_code__success(self,  _, serialize_object, expected_result):
        actual_result = self.service.getting_source_code(serialize_object)

        self.assertListEqual(actual_result, expected_result)

    def test__getting_source_code_with_type_error__success(self,):
        actual_result = self.service.getting_source_code(0)

        self.assertListEqual(actual_result, [])

    def test__getting_base64_pickle_object__success(self):
        actual_result = self.service.getting_base64_pickle_object(example_function)

        self.assertEqual(actual_result, expected_base64_string)

    def test__getting_base64_pickle_object_with_type_error__success(self):
        actual_result = self.service.getting_base64_pickle_object((i for i in range(10)))

        self.assertIsNone(actual_result)

    def test__getting_object_from_base64__success(self):
        actual_result = self.service.getting_object_from_base64(expected_base64_string)

        self.assertEqual(actual_result, example_function)

    def test__getting_object_from_base64_with_attribute_error__success(self):
        actual_result = self.service.getting_object_from_base64(0)

        self.assertIsNone(actual_result)
