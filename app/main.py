from app.serializers.serializer_factory.factory import ObjectSerializeFactory


class ClassTest:
    ggg = 15

    def __init__(self):
        self.test = 5

    def test3(self):
        pass


def test(a, b):
    return a * b


def main():
    factory = ObjectSerializeFactory()
    serializer = factory.create_serializer('json')

    print(serializer.dumps(test))
    print(serializer.dumps(ClassTest))


if __name__ == '__main__':
    main()
