def main():
    user_name = str(input("Please enter your name: "))
    with open("names.txt","w") as f:
        #f.truncate(0) #clear the data in the file before file write
        print(f"Your name is {user_name}",end='\n',file=f)
        f.close()

    with open("names.txt","r") as f:
        print(f.readline())
        f.close()

    with open("numbers.txt","r+") as f:
        sum = 0
        for i in range(2):
            sum += int(f.readline())
        print(f"The sum of first two lines numbers is: {sum}")
        f.close()

    with open("numbers.txt","r+") as f:
        for line in f:
            print(line,end='')
        f.close()
    pass
if __name__ == '__main__':
    main()