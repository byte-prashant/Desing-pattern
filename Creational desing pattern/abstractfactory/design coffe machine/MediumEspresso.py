from interface_coffee import Coffe

class MediumEspresso(Coffe):

    def get_cost(self):
        return super().get_cost()+5

    def description(self):
        print("getting espresso")

    def get_coffe(self):
        print("getting medium espresso")