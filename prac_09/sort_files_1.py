import os
import shutil


def main():
    print(os.getcwd())
    # Set path
    os.chdir(os.getcwd() + "\\FilesToSort\\")

    files = []
    for filename in os.listdir("."):
        files.append(filename)
    print(files)

    # Create sub directories base on the files' type
    # And move files to there belonging type directory
    for filename in files:
        if os.path.isfile(filename):
            file_type = os.path.splitext(filename)[1].replace(".", "")
            if not os.path.isdir(file_type):
                os.mkdir(file_type)
            shutil.move(filename, file_type + '\\')


if __name__ == '__main__':
    main()