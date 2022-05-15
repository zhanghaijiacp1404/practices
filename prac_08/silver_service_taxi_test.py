from prac_08.silver_service_taxi import SilverServiceTaxi


def main():
    Hummer = SilverServiceTaxi(name="Hummer", fuel=200, fanciness=2)
    Hummer.drive(distance=18)
    print(Hummer.get_fare())


if __name__ == '__main__':
    main()