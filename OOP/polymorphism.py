class Dog:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + " says WOOF!"


class Cat:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + " says MEOW!"


niko = Dog("Niko")
felix = Cat("Felix")

print(niko.speak())
print(felix.speak())

for pet_class in [niko, felix]:
    print(type(pet_class))
    print(pet_class.speak())


def pet_speak(pet):
    print(pet.speak())


pet_speak(niko)
pet_speak(felix)
