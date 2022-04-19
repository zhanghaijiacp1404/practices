"""
Check whether the password meet the minimum length.
Print the password and changing every character to '*' in output
"""
def main():
    """Get user input, and iterate the user input string"""
    password = get_password(10)
    for i in password:
        print('*',end='')
    print()
def get_password(mininum_lendth):
    """Return user input password with legal length"""
    password = str(input("Enter password: "))
    while len(password) < mininum_lendth:
        password = str(input("Enter password: "))
    return password
main()