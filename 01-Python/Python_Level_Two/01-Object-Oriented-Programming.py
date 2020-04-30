class Dog:

    species = 'mammal'

    def __init__(self, breed, name):
        self.breed = breed
        self.name = name


sam = Dog('lab', 'Frankie')
new_dog = Dog('Golden', 'Cindy')

print(type(sam))
print(sam.breed)
print(new_dog.breed)


class Circle:

    pi = 3.14

    def __init__(self, radius=1):
        self.radius = radius

    def area(self):
        return self.radius * self.radius * self.pi

    def circumfrence(self):
        return 2 * self.pi * self.radius


mycircle = Circle(10)
print(mycircle.radius)
print(mycircle.area())
print(mycircle.circumfrence())