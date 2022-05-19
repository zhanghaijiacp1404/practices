import os, shutil


def main():
    # Check and set working directory
    print(os.getcwd())
    os.chdir(os.getcwd() + "\\FilesToSort\\")
    print(os.getcwd())

    for file in os.listdir('.'):
        if os.path.isfile(file):
            file_type = os.path.splitext(file)[1].replace('.', '')
            category = input(f"What category would you like to sort {file_type} files into? ")
            if not os.path.isdir(category):
                os.mkdir(category)
            shutil.move(file, category + "\\")


if __name__ == '__main__':
    main()