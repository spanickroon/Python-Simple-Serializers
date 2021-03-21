class ExampleClass:
    def __init__(self):
        pass


def example_function():
    pass


expected_dict_args_function = {
    'args': [],
    'varargs': None,
    'varkw': None,
    'defaults': None,
    'kwonlyargs': [],
    'kwonlydefaults': None,
    'annotations': {}
}

expected_dict_args_class = {
    '__module__': 'formatserializer.testing.services.service_abstract_base.service',
    '__dict__': "<attribute '__dict__' of 'ExampleClass' objects>",
    '__weakref__': "<attribute '__weakref__' of 'ExampleClass' objects>",
    '__doc__': 'None'
}

expected_base64_string = ('gASVWAAAAAAAAACMP2Zvcm1hdHNlcmlhbGl6ZXIudGVzdGluZy5zZXJ2aWNl'
                          'cy5zZXJ2aWNlX2Fic3RyYWN0X2Jhc2Uuc2VydmljZZSMEGV4'
                          'YW1wbGVfZnVuY3Rpb26Uk5Qu'
)
