"""
CP1404/CP5632 Practical
Two functions:
1-Output statistics info regarding user input list
2-Check whether the user input name is in the list and generate different results
"""
def main():
    """Main function body"""
    number_statistics()
    security_checker()
def number_statistics():
    """Output statistics info regarding user input list"""
    MAX_LENGTH_OF_NUMBERS = 5
    numbers_list = []
    for i in range (0,MAX_LENGTH_OF_NUMBERS,1):
        temp_number = int(input("Number: "))
        numbers_list.append(temp_number)
    print(f"The first number is {numbers_list[0]}")
    print(f"The last number is {numbers_list[-1]}")
    print(f"The smallest number is {min(numbers_list)}")
    print(f"The largest number is {max(numbers_list)}")
    print(f"The average of the number is {sum(numbers_list) / len(numbers_list)}")
def security_checker():
    """Check whether the user input name is in the list. Finally output results"""
    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',
                 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer',
                 'bob']
    input_username = str(input("Username: "))
    print("Access granted") if input_username in usernames else print("Access denied")
main()