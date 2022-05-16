"""Test the UnreliableCar object"""
from prac_08.unreliable_car import UnreliableCar


def main():
    """Start program"""
    test_car = UnreliableCar(name="UnreliableCar", fuel=100, reliability=90)
    # Test the drive(self, distance) method in UnreliableCar object
    print(test_car.drive(2))
    # Test the __str__(self) method in UnreliableCar object
    print(test_car)


if __name__ == '__main__':
    main()