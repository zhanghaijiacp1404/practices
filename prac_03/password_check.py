def show_password(mininum_lendth):
    password = str(input("Enter password: "))
    while len(password) < mininum_lendth:
        password = str(input("Enter password: "))
    for i in password:
        print('*',end='')
    print('')
def main():
    show_password(10)
main()