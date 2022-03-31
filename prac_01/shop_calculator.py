from typing import *
def main()->None:
    number_items = None
    total_price = 0.0
    number_items = int(input("Number of items: "))
    while number_items < 0:
        print("Invalid number of items!")
        number_items = int(input("Number of items: "))
    for i in range(number_items):
        temp_item_price = float(input("Price of item: "))
        total_price += temp_item_price
    if total_price > 100:
        total_price *= 0.9
    print("Total price for 3 items is ${:.2f}".format(total_price))
if __name__ == '__main__':
    main()