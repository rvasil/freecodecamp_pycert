class Parent1:
    def __init__(self):
        print('Parent1 init')
        self.__data = 'Parent1 data'

class Parent2:
    def __init__(self):
        print('Parent2 init')
        self.__data = 'Parent2 data'

class Child(Parent1, Parent2):
    def __init__(self):
        Parent1.__init__(self)
        Parent2.__init__(self)
        # super().__init__()
        self.__data = 'Child data'
        print(self.__data)

c = Child()

print(c.__dict__)
