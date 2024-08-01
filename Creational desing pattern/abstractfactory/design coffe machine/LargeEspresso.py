from interface_coffee import Coffe
from Espresso_coffee import Espresso
class LargeEspresso(Espresso):

    def get_cost(self):
        return super().get_cost()+5

    def description(self):
        print("getting espresso")

    def get_coffe(self):
        print("getting medium espresso")