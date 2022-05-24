"""
A file sorting demo to classify the types of
different files based on their suffix like:
.doc .docx .txt .png .jpg .xls and so on.
Also, based on the files' suffix, create
directories and move the files to their belong
directory.
"""
import os
import shutil


def main():
    """Start program."""
    # Check working directory
    print(os.getcwd())
    # Set path
    os.chdir(os.getcwd() + "\\FilesToSort\\")

    files = []
    for file in os.listdir("."):
        files.append(file)
    print(files)

    # Create sub directories base on the files' type
    # And move files to there belonging type directory
    for file in files:
        # Only handling the file if that file exists
        if os.path.isfile(file):
            suffix = os.path.splitext(file)[1].replace(".", "")
            # Only create the directory when that directory doesn't exists. Avoid crashing
            try:
                os.mkdir(suffix)
            except FileExistsError:
                pass
            # Move the file to their belonging directory
            shutil.move(file, suffix + '\\')


if __name__ == '__main__':
    main()