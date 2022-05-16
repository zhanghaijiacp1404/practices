"""UnreliableCar class"""
from prac_08.car import Car
from random import randint as ri


class UnreliableCar(Car):
    """An UnreliableCar object"""

    def __init__(self, name, fuel, reliability):
        """Initialize an UnreliableCar instance"""
        super().__init__(name, fuel)
        # A float variable between 0 and 100 inclusive
        self.reliability = float(reliability)

    def drive(self, distance):
        """
        Drive this UnreliableCar and return the distance if a random integer is less than reliability
        Otherwise return 0
        """
        if ri(0, 100) < self.reliability:
            return super().drive(distance)
        else:
            return 0
