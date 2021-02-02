from abc import ABC, abstractmethod


class FelineInterface(ABC):

    @abstractmethod
    def scratchy(self):
        raise NotImplementedError


class CanineInterface(ABC):

    @abstractmethod
    def swim(self):
        raise NotImplementedError


class Animal(ABC):
    def __init__(self, name, weight, height, age, legs, eye_color):
        self.name = name
        self.weight = weight
        self.height = height
        self.age = age
        self.legs = legs
        self.eye_color = eye_color

    @abstractmethod
    def voice(self):
        pass


class Pet(Animal):
    pass


class Cat(Pet, FelineInterface):
    def voice(self):
        print('Meeoow')

    def scratchy(self):
        print('Cat scratchy')


class Dog(Pet, CanineInterface):
    def voice(self):
        print('Wooooof')

    def swim(self):
        print('Dog swim')


class WildAnimal(Animal):
    pass


class Wolf(WildAnimal, CanineInterface):
    def voice(self):
        print('Wooooolf')

    def swim(self):
        print('Wolf swimming thru the river')


class Lion(WildAnimal, FelineInterface):
    def voice(self):
        print('Lion roar')

    def scratchy(self):
        print('Lion scratchy')
