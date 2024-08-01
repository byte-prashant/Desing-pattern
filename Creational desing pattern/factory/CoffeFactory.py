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
    def get_coffe(self, size):
        pass

    def prepare_coffee(self, size):

        coffee = self.get_coffe(size)
        coffee.get_coffe()



class MediumEspressoMachine(CoffeMachine):

    def get_coffe(self, size):
        return MediumEspresso()


class LargeEspressoMachine(CoffeMachine):

    def get_coffe(self, size):
        return LargeEspresso()



coffee = LargeEspressoMachine()
coffee.prepare_coffee()



# Limitations

# in this way we will be creating all the factory classes for each and every combination
# total combination  = no of coffe types * 3( small, medium, large)


# to avoid this we can pass size parameter to the coffeFactory
class EspressoMachine(CoffeMachine):

    def get_coffe(self, size):

        if size=="medium":
            return MediumEspresso()
        elif size == "large":
            return LargeEspresso()
        else:
            return Espresso()
