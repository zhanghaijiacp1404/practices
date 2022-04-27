from prac_06.guitar import Guitar


def main():

    first_guitar = Guitar(name = "Gibson L-5 CES", year = 1922, cost = 16035.40)
    another_guitar = Guitar(name = "Another guitar", year = 2013, cost = 1206.15)

    print(f"{first_guitar.name} get_age() - Expected 100. Got {first_guitar.get_age()}")
    print(f"{another_guitar.name} get_age() - Expected 9. Got {another_guitar.get_age()}")

    print(f"{first_guitar.name} is_vintage() - Expected True. Got {first_guitar.is_vintage()}")
    print(f"{another_guitar.name} is_vintage() - Expected False. Got {another_guitar.is_vintage()}")


if __name__ == '__main__':
    main()