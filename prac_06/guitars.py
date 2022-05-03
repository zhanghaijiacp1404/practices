"""Guitar program"""
from prac_06.guitar import Guitar


def main():
    """Start program"""
    print("My guitars!")
    guitars = []
    guitar_name = input("Name: ")
    while guitar_name != "":
        guitar_year = int(input("Year: "))
        guitar_cost = float(input("Cost: $"))
        temp_guitar_class = Guitar(guitar_name, guitar_year, guitar_cost)
        guitars.append(temp_guitar_class)
        print(f"{temp_guitar_class} added.")
        guitar_name = input("Name: ")

    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    if guitars:
        guitars.sort()
        print("These are my guitars: ")
        for index, item in enumerate(guitars, 1):
            vintage_string = ""
            if item.is_vintage():
                vintage_string = " (vintage)"
            print(f"Guitar {index}: {item.name:>20} ({item.year}), worth $ {item.cost: >10,.2f} {vintage_string}")
    else:
        print("No guitars :( Quick, go and buy one!")


if __name__ == "__main__":
    main()