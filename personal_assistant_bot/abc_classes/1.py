from abc import abstractclassmethod, ABCMeta


class MyBaseClass(metaclass=ABCMeta):
    @abstractclassmethod
    def foo(self):
        pass

    @abstractclassmethod
    def baz(self):
        pass

class Child(MyBaseClass):
    def foo(self):
        pass

    def baz(self):
        pass

c = Child()