"""Test the UnreliableCar object"""
from prac_08.unreliable_car import UnreliableCar


def main():
    """Start program"""
    test_car = UnreliableCar(name="UnreliableCar", fuel=100, reliability=90)
    # Start driving this unreliable car
    print(test_car.drive(2))
    # Print the string representation of this unreliable car object
    print(test_car)


if __name__ == '__main__':
    main()