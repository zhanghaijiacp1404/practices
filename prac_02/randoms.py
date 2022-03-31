import random
from typing import Any

def main()->Any:
    pass
    print(dir(str))
    print(dir(random))

    print(random.randint(5, 20))  # line 1
    #helper code for checking whether the upper and lower boundary is inclusive or not
    '''
    for i in range(1000):
        random_number = random.randint(5,20)
        print(f"{5} and {20} are not inclusive") if (random_number > 20 or random_number < 5) else print(f"{random_number}")
    '''
    print(random.randrange(3, 10, 2))  # line 2, show be 3 or 5 or 7 or 9
    #helper code for checking whether the numbers are 3 or 5 or 7 or 9
    '''
    for i in range(1000):
        random_number = random.randrange(start=3, stop=10,step=2)
        if random_number == 4 or random_number == 6 or random_number == 8\
            or random_number == 10:
            print("The random numbers include 4 or 6 or 8 or 10")
            break
        else:
            continue
    '''
    print(random.uniform(2.5, 5.5))  # line 3
    #helper code for checking the upper and lower boundary
    '''
    for i in range(10000):
        random_number = random.uniform(2.5, 5.5)
        if not (random_number >= 2.5 or random_number <= 5.5):
            print(f"The number is not in the boundary [{2.5},{5.5}]")
            break
    '''
    #TODO What did you see on line 1?
    # a integer between 5 and 20 inclusive
    #TODO What was the smallest number you could have seen, what was the largest?
    # The smallest integer is 5, and the largest integer is 20

    #TODO What did you see on line 2?
    # a integer of 3 or 5 or 7 or 9
    #TODO What was the smallest number you could have seen, what was the largest?
    # The smallest integer is 3, the largest integer is 9
    #TODO Could line 2 have produced a 4?
    # Impossible to produce 4

    #TODO What did you see on line 3?
    # A floating point number between 2.5 and 5.5 inclusive
    #TODO What was the smallest number you could have seen, what was the largest?
    # The smallest floating point number is 2.5, the largest is 5.5

    #TODO Write code, not a comment, to produce a random number between 1 and 100 inclusive.
    random_number = random.randint(1,100)

if __name__ == '__main__':
    main()