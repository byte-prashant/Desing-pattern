from interfaceFactory import CoffeMachine
from MediumEspresso import MediumEspresso
from LargeEspresso import LargeEspresso
from Espresso_coffee import Espresso
from abc import abstractmethod


class EspressoMachine(CoffeMachine):

    @abstractmethod
    def get_medium_coffe(self):
        return MediumEspresso()

    @abstractmethod
    def get_large_coffe(self):
        return LargeEspresso()

    @abstractmethod
    def get_small_coffe(self):
        return Espresso()