#!/usr/bin/env python
from abc import ABCMeta, abstractmethod

class Animal(metaclass=ABCMeta):
    def __init__(self, animal_type):
        self._type = animal_type

    @abstractmethod
    def make_noise(self):
        pass



class Insect(Animal):
    pass


i = Insect('scarab beetle')

print(i)
