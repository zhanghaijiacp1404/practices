def get_password(mininum_lendth):
    password = str(input("Enter password: "))
    while len(password) < mininum_lendth:
        password = str(input("Enter password: "))
    return password
def main():
    password = get_password(10)
    for i in password:
        print('*',end='')
    print()
main()