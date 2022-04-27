from prac_06.guitar import Guitar


def main():
    print("My guitars!")
    guitar_list = []
    guitar_name = input("Name: ")
    while guitar_name != "":
        guitar_year = int(input("Year: "))
        guitar_cost = float(input("Cost: $"))
        temp_guitar_class = Guitar(guitar_name, guitar_year, guitar_cost)
        guitar_list.append(temp_guitar_class)
        print(f"{temp_guitar_class.name} ({temp_guitar_class.year}) : ${temp_guitar_class.cost:,.2f} added.")

        guitar_name = input("Name: ")

    print("These are my guitars: ")
    for index, item in enumerate(guitar_list, 1):
        vintage_string = ""
        if item.is_vintage():
            vintage_string = " (vintage)"
        print(f"Guitar {index}: {item.name: >20} ({item.year}), worth $ {item.cost: >10} {vintage_string}")
if __name__ == "__main__":
    main()