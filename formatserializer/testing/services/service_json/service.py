expected_dict_int = {
    'object': '123', 'type': 'int', 'serializable_by_default': True, 'name': None, 'value': 123,
    'dict_class': {}, 'args': {}, 'code': [], 'base64': 'gARLey4='
}

expected_dict_class = {
    'object': "<class 'formatserializer.testing.services.service_abstract_base.service.ExampleClass'>",
    'type': 'class',
    'serializable_by_default': False,
    'name': 'ExampleClass',
    'value': None,
    'dict_class': {
        '__module__': 'formatserializer.testing.services.service_abstract_base.service',
        '__init__': '<function ExampleClass.__init__ at 0x7faabd0c9670>',
        '__dict__': "<attribute '__dict__' of 'ExampleClass' objects>",
        '__weakref__': "<attribute '__weakref__' of 'ExampleClass' objects>",
        '__doc__': 'None'
    },
    'args': {
        'args': ['self'],
        'varargs': None,
        'varkw': None,
        'defaults': None,
        'kwonlyargs': [],
        'kwonlydefaults': None,
        'annotations': {}
    },
    'code': [
        'class ExampleClass:',
        '    def __init__(self):',
        '        pass', ''
    ],
    'base64': 'gASVVAAAAAAAAACMP2Zvcm1hdHNlcmlhbGl6ZXIudGVzdGluZy5zZXJ2aWNlcy5zZXJ2aWNlX2Fic3RyYWN0X2Jhc2Uuc2VydmljZZSMDEV4YW1wbGVDbGFzc5STlC4='
}

expected_dict_function = {
    'object': '<function example_function at 0x7faabd0aeb80>',
    'type': 'function',
    'serializable_by_default': False,
    'name': 'example_function',
    'value': None,
    'dict_class': {},
    'args': {
        'args': [],
        'varargs': None,
        'varkw': None,
        'defaults': None,
        'kwonlyargs': [],
        'kwonlydefaults': None,
        'annotations': {}},
    'code': [
        'def example_function():',
        '    pass', ''
    ],
    'base64': 'gASVWAAAAAAAAACMP2Zvcm1hdHNlcmlhbGl6ZXIudGVzdGluZy5zZXJ2aWNlcy5zZXJ2aWNlX2Fic3RyYWN0X2Jhc2Uuc2VydmljZZSMEGV4YW1wbGVfZnVuY3Rpb26Uk5Qu'
}
