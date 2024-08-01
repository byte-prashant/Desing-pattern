from abc import abstractmethod

class CoffeMachine:

    @abstractmethod
    def get_medium_coffe(self):
        pass

    @abstractmethod
    def get_large_coffe(self):
        pass

    @abstractmethod
    def get_small_coffe(self):
        pass