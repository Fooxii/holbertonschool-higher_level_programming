#!/usr/bin/python3
"""
Docstring for python-abc.task_00_abv
"""
from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Docstring for Animal
    """
    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    """
    Docstring for Dog
    """
    def sound(self):
        return "Bark"


class Cat(Animal):
    """
    Docstring for Cat
    """
    def sound(self):
        return "Meow"
