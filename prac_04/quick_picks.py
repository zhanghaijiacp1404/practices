"""
Generate some lines (base on user input) of quick picks and then output each line
Rules for each line:
1-Each line (quick pick) should not contain any repeated number.
2-Each line of numbers should be displayed in sorted (ascending) order.
"""
from random import randint as ri
def main():
    """Main function body"""
    RANDOM_NUMBER_LOWER_BOUND = 1
    RANDOM_NUMBER_UPPER_BOUND = 45
    NUMBER_OF_QUICK_PICKS = int(input("How many quick picks? "))
    for i in range(NUMBER_OF_QUICK_PICKS):
        pass
        temp_list = []
        for j in range(6):
            TEMP_RANDOM_NUMBER = ri(RANDOM_NUMBER_LOWER_BOUND,RANDOM_NUMBER_UPPER_BOUND)
            while TEMP_RANDOM_NUMBER in temp_list:
                TEMP_RANDOM_NUMBER = ri(RANDOM_NUMBER_LOWER_BOUND,RANDOM_NUMBER_UPPER_BOUND)
            temp_list.append(TEMP_RANDOM_NUMBER)
        temp_list.sort()
        for number in temp_list:
            print(f"{number:>2} ",end='')
        print()
main()