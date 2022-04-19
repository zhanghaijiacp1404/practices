"""
Simulate quick picks. Detailed data is based on user-defined like the
range of lower and upper bound
"""
from random import randint as ri

#Initialize some important global constants
LOWER_BOUND = 1
UPPER_BOUND = 45
NUMBER_OF_VALUES = 6
def main():
    number_of_quick_picks = int(input("How many quick picks? "))
    #Check the validation of user input
    while number_of_quick_picks < 0:
        number_of_quick_picks = int(input("Invalid value. Re-enter: "))
    #Generate and output quick picks
    for i in range(number_of_quick_picks):
        quick_pick_list = []
        for j in range(NUMBER_OF_VALUES):
            temp_random_number = ri(LOWER_BOUND, UPPER_BOUND)
            while temp_random_number in quick_pick_list:
                temp_random_number = ri(LOWER_BOUND, UPPER_BOUND)
            quick_pick_list.append(temp_random_number)
        quick_pick_list.sort()

        for number in quick_pick_list:
            print(f"{number:>2}", end=" ")
        print("")
if __name__ == '__main__':
#Call main function here
    main()