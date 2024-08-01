from abc import ABC, abstractmethod

class Coffe:

    @abstractmethod
    def get_cost(self):

        pass

    @abstractmethod
    def description(self):
        pass

    @abstractmethod
    def get_coffe(self):
        pass



class Espresso(Coffe):

    def get_cost(self):
        return 10

    def description(self):
        print("getting espresso")


    def get_coffe(self):
        print("getting espresso")


class MediumEspresso(Espresso):

    def get_cost(self):
        return super().get_cost()+5

    def description(self):
        print("getting espresso")

    def get_coffe(self):
        print("getting medium espresso")


class LargeEspresso(Espresso):

    def get_cost(self):
        return super().get_cost()+10

    def description(self):
        print("getting espresso")

    def get_coffe(self):
        print("getting large espresso")


class Cappuccino(Coffe):

    def get_cost(self):
        return 20

    def description(self):
        print("getting Cappuccino")

    def get_coffe(self):
        print("getting Cappuccino")


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



coffee = EspressoMachine().get_medium_coffe()
coffee.get_coffe()



###################################################################################



