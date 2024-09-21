class Animal:
    def sound(self):
        return "I an animal"

class Dog(Animal):
    def sound(self):
        return "Bark"

class Cat(Animal):
    def sound(self):
        return "Meow"

def make_animal_sound(animal):
    print(animal.sound())

dog = Dog()
cat = Cat()
animal = Animal()

make_animal_sound(animal)
make_animal_sound(dog)  
make_animal_sound(cat)  