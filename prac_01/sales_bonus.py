"""
Program to calculate and display a user's bonus based on sales.  
If sales are under $1,000, the user gets a 10% bonus.  
If sales are $1,000 or over, the bonus is 15%.  
"""
from typing import *
def main()->None:
    user_sales = float(input("Please enter your sales: $"))
    while user_sales >= 0:
        if user_sales < 1000.0:
            user_bonus = user_sales * 0.1
        else:
            user_bonus = user_sales * 0.15
        print("Your bonus based on your sales of $" + str(user_sales) + " is: $" +str(user_bonus))
        print("")
        user_sales = float(input("Please enter your sales: $"))
    print("End program")
if __name__ == '__main__':
    main()