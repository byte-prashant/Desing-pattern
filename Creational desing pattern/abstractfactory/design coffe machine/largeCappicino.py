
from Cappuccino import Cappuccino

class LargeCappuccino(Cappuccino):

    def get_cost(self):
        return super().get_cost()+10

    def description(self):
        print("getting Cappuccino")

    def get_coffe(self):
        print("getting large Cappuccino")