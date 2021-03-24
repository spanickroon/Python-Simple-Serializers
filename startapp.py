from formatserializer.serializers.serializer_factory.factory import ObjectSerializeFactory

import test_startapp


def main():
    factory = ObjectSerializeFactory()
    serialize_format = 'json'
    file_to_convert = 'test.json'
    file_from_convert = 'test.json'

    serialize = factory.create_serializer(serialize_format)

    print(serialize.dumps(test_startapp.MyClass))
    serialize.dump(test_startapp.my_func, file_to_convert)

    test_func = serialize.load(file_from_convert)

    print(test_func(10, 5))


if __name__ == '__main__':
    main()
