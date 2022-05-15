"""UnreliableCar class"""
from prac_08.car import Car
from random import randint as ri


class UnreliableCar(Car):
    """An UnreliableCar object"""

    def __init__(self, name, fuel, reliability=0):
        """Initialize an UnreliableCar instance"""
        super().__init__(name, fuel)
        # A float variable between 0 and 100 inclusive
        self.reliability = reliability

    def drive(self, distance):
        """
        Drive this UnreliableCar and return the distance if the car's reliability is larger than a random integer
        Otherwise return 0
        """
        if self.reliability > ri(0, 100):
            return super().drive(distance)
        else:
            return 0
