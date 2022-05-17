import abc
from abc import ABCMeta

from cocktail import Cocktail


class CocktailRepository(metaclass=ABCMeta):

    @abc.abstractmethod
    def create(self, cocktail: Cocktail):
        pass

    @abc.abstractmethod
    def create_all(self, cocktails: list[Cocktail]):
        pass

    @abc.abstractmethod
    def get(self, cocktail_id: int):
        pass

    @abc.abstractmethod
    def get_all(self):
        pass

    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'create') and callable(subclass.create) and
                hasattr(subclass, 'create_all') and callable(subclass.create_all) and
                hasattr(subclass, 'get') and callable(subclass.get) and
                hasattr(subclass, 'get_all') and callable(subclass.get_all)) or \
               NotImplemented
