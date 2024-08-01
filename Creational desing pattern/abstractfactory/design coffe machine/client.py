
from MediumEspresso import MediumEspresso
class coffeMaker:

    "The factory method"
    " we can create dictioanry of objects also instead of ifelse statements"

    @staticmethod
    def get_coffe(type,size):

        if type=="Espresso":
            if size == "medium":
                return MediumEspresso()



coffe = coffeMaker().get_coffe("Espresso","medium")
coffe.description()


