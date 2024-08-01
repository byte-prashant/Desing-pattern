# problem statement is to create different type of button for windows and linux
# bulid a system to generate logistic
from abc import ABC, abstractmethod


# creating products

class Transport(ABC):
    @abstractmethod
    def deliver(self, destination):
        pass


class Truck(Transport):

    def deliver(self, destination):
        print("delivered by truck")


class Ship(Transport):

    def deliver(self, destination):
        print('delivered via sea')


class Logistic(ABC):


    #factory method
    @abstractmethod
    def createTransport(self):
        pass

    def planDelivery(self, destination):
        transport = self.createTransport()
        transport.deliver(destination)
        return


class SeaLogistics(Logistic):

    def createTransport(self):
        return Ship()


class RoadLogistics(Logistic):

    def createTransport(self):
        return Truck()


logistics = SeaLogistics()
logistics.planDelivery("bangladesh")
