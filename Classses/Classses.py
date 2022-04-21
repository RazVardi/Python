class Cat:
    __age = None  # need space for comment hashtag=#
    __name = ""   # need space before the name of var and after the value
    __color = ""  # "__" before var name=private

    def __init__(self, age, name, color):  # this is constructor need 1 line empty before it,
        self.__age = age  # need space after the ",".
        self.__name = name
        self.__color = color

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_color(self):
        return self.__color

    def set_color(self, color):
        self.__color = color


class App:

    @staticmethod
    def main():
        cat1 = Cat("snoopi", "black", 2)
        cat2 = Cat("snoopi", "black", 3)
        print("hello world")
        print_obj(cat1, cat2)


def print_obj(cat1, cat2):
    print(cat1.get_name(), cat1.get_color(), cat1.get_age())
    print(cat2.get_name(), cat2.get_color(), cat2.get_age())


App.main()
