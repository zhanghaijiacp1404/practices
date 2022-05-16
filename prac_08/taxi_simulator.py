from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"


def display_taxis(taxis):
    for index, taxi in enumerate(taxis, 0):
        print(f"{index} - {taxi}")


def main():
    taxis = [Taxi(name="Prius", fuel=100),
             SilverServiceTaxi(name="Limo", fuel=100, fanciness=2),
             SilverServiceTaxi(name="Hummer", fuel=200, fanciness=4)]
    bill_to_date = 0
    temp_taxi = None
    print("Let's drive!")
    print(MENU)
    user_choice = input(">>> ").lower()
    while user_choice != 'q':
        if user_choice == 'c':
            print("Taxis available")
            display_taxis(taxis)
            taxi_choice = int(input("Choose taxi: "))
            try:
                temp_taxi = taxis[taxi_choice]
            except IndexError:
                print("Invalid taxi choice")
        elif user_choice == 'd':
            if not temp_taxi:
                print("You need to choose a taxi before you can drive")
            else:
                temp_taxi.start_fare()
                distance_drive = float(input("Drive how far? "))
                temp_taxi.drive(distance=distance_drive)
                print(f"Your {temp_taxi.name} trip cost you ${temp_taxi.get_fare():.2f}")
                bill_to_date += temp_taxi.get_fare()
        else:
            print("Invalid option")
        print(f"Bill to date: ${bill_to_date:.2f}")
        print(MENU)
        user_choice = input(">>> ").lower()
    print(f"Total trip cost: ${bill_to_date:.2f}")
    print("Taxis are now:")
    display_taxis(taxis)


if __name__ == '__main__':
    main()