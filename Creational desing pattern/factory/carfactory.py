import abc
from inspect import getmembers, isclass, isabstract

class Cars(abc.ABC):
    @abc.abstractmethod
    def start(self):
        pass

    @abc.abstractmethod
    def stop(self):
        pass



class Ford(Cars):
  def start(self):

      print("ford engine is now running")

  def stop(self):
    print("Ford engine shutting down")


class Tata(Cars):
    def start(self):
        print("tata engine is now running")

    def stop(self):
        print("tata engine shutting down")

class GenericCar(Cars):
  def __init__(self, car_name):
    self.name = car_name

  def start(self):
    print(f"{self.name} engine starting!")

  def stop(self):
    print(f"{self.name} engine stopping!")



class CarFactory():
  cars = {}

  def __init__(self):
    self.load_cars()

  def load_cars(self):
      """

      :return:
         we can dynamically add factories, see dynmicloggerfactory

       """

      self.cars.update({"ford":Ford})
      self.cars.update({"tata":Tata})

  def create_instance(self, car_name):
    if car_name in self.cars:
      return self.cars[car_name]()
    else:
      return GenericCar(car_name)



factory = CarFactory()

for car_name in ['Ford', 'Ferrari', 'Tesla']:
  car = factory.create_instance(car_name)
  car.start()
  car.stop()