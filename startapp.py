#!.venv/bin/python3
from app.serializers.serializer_factory.factory import ObjectSerializeFactory
from app.args.arguments import SerializeArguments

from static.test_data import test_data


def main():
    factory = ObjectSerializeFactory()
    parser = SerializeArguments().setup_args()

    serialize_format, file_to_convert, file_from_convert = SerializeArguments.distribution_arguments(parser)
    file_to_convert, file_from_convert = (
        f'{file_to_convert}.{serialize_format}',
        f'{file_from_convert}.{serialize_format}'
    )

    serialize = factory.create_serializer(serialize_format)

    print(serialize.dumps(test_data.MyClass))
    serialize.dump(test_data.my_func, file_to_convert)

    test_func = serialize.load(file_from_convert)

    print(test_func(10, 5))


if __name__ == '__main__':
    main()
