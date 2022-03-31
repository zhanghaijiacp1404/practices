from typing import *
def main()->Any:
    print("Display all the odd numbers between 1 and 20 inclusive: ")
    for i in range(1, 21, 2):
        print(i, end=' ')
    print()

    print("count in 10s from 0 to 100: ")
    for i in range(0,101,10):
        print(i, end=' ')
    print()

    print("count down from 20 to 1 inclusive: ")
    for i in range(20,0,-1):
        print(i, end=' ')
    print()    
    
    print("print n stars: ")
    num_star  = int(input("Number of stars: "))
    for i in range(num_star):
        print('*', end='')
    print()

    print("print n lines of increasing stars: ")
    for i in range(num_star):
        for j in range(i + 1):
            print('*', end='')
        print('')
if __name__ == '__main__':
    main()