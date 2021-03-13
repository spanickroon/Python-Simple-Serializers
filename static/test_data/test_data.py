class MyClass:

    def __init__(self, test, lol, kek):
        self.test = test
        self.lol = lol
        self.kek = kek

    @staticmethod
    def my_class_func(a, b, c):
        return sum((a, b, c)) - (a * b * c)

    def my_class_func_2(self):
        return self.lol + self.kek


def my_func(a, b):
    return (a * b) ** 2


my_list = [i for i in range(10)]

my_set = {i for i in range(5)}

my_dict = {i: i ** 2 for i in range(7)}

my_var = 'Hello'
