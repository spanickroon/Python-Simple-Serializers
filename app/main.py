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

    """
    serializer = factory.create_serializer('json')

    test_func = serializer.dumps(test)
    print(test_func)
    print(serializer.dumps(ClassTest))
    print(serializer.dumps((i for i in range(10))))
    print(serializer.dumps([1, 2, 3, 4, 5]))
    print(serializer.dumps({1, 2, 3, 4, 5}))
    print(serializer.dumps(10))

    test_func_2 = serializer.loads(test_func)
    print(test_func_2(10, 20))

    serializer.dump(test, 'kek.json')

    test_func_3 = serializer.load('kek.json')
    print(test_func_3)
    print(test_func_3(50, 20))
    """

    serializer = factory.create_serializer('pickle')

    test_func = serializer.dumps(test)
    print(test_func)
    print(serializer.dumps(ClassTest))
    print(serializer.dumps((i for i in range(10))))
    print(serializer.dumps([1, 2, 3, 4, 5]))
    print(serializer.dumps({1, 2, 3, 4, 5}))
    print(serializer.dumps(10))

    test_func_2 = serializer.loads(test_func)
    print(test_func_2(10, 20))

    serializer.dump(test, 'kek.picdkldfgdfgdfgdfgdfgfdge')

    test_func_3 = serializer.load('kek.pickle')
    print(test_func_3)
    print(test_func_3(50, 20))

if __name__ == '__main__':
    main()
