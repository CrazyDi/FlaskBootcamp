class Sample():
    pass


x = Sample()

print(type(x))


class Dog:
    def __init__(self, breed):
        self.breed = breed


x = Dog('lab')

print(type(x))
print(x.breed)
