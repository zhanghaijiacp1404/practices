"""Testing for SilverServiceTaxi object"""
from prac_08.silver_service_taxi import SilverServiceTaxi


def main():
    """Start program"""
    Hummer = SilverServiceTaxi(name="Hummer", fuel=200, fanciness=2)
    # Start driving this taxi
    Hummer.drive(distance=18)
    # Print the current fare
    print(f"Current fare: ${Hummer.get_fare():.2f}")
    # Print the string representation of the Hummer object
    print(Hummer)


if __name__ == '__main__':
    main()