from prac_08.taxi import Taxi


def main():
    prius_1 = Taxi(name = "Prius 1", fuel=100.0)
    prius_1.drive(40)
    print(prius_1)
    print(f"Prius 1's fare is: ${prius_1.get_fare()}")

    prius_1.start_fare()
    prius_1.drive(100)
    print("")
    print(prius_1)
    print(f"Prius 1's fare is: ${prius_1.get_fare()}")


if __name__ == '__main__':
    main()