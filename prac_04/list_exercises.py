"""
Operation of list class functions and other list operations
For example: min(), max(), or 'in'
"""
NUMBER_OF_VALUES = 5
def main():
    """Main function body"""
    numbers = []
    for i in range(NUMBER_OF_VALUES):
        temp_number = int(input("Number: "))
        numbers.append(temp_number)
    #Application of list class functions and index operation
    print(f"The first number is {numbers[0]}")
    print(f"The last number is {numbers[-1]}")
    print(f"The smallest number is {min(numbers)}")
    print(f"The largest number is {max(numbers)}")
    print(f"The average of the numbers is {sum(numbers) / len(numbers)}")

    #Application of 'in' operation regarding list
    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',
                 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer',
                 'bob']
    user_input_name = str(input("Enter username: "))
    print ("Access granted") if user_input_name in usernames else print("Access denied")
if __name__ == "__main__":
    main()