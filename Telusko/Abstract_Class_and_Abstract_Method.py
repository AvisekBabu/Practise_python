from abc import ABC, abstractmethod


class Car(ABC):
    @abstractmethod
    def engine(self):
        pass


class UpdatedCar(Car):
    # same method required to use abstract method from a new class
    def engine(self):
        print("it's running")


class Test:
    def tyre(self, eng):
        print("MRF..")
        eng.engine()


# car = Car()  # Can't create object for a abstract class
car = UpdatedCar()  # Need to use UpdatedCar class for instantiate abstract method
car.engine()

test = Test()
test.tyre(car)  # We can pass reference object of other class, hence both classes method will be called

