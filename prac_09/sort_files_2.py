"""
Modified version for sort_files_1.py
Create directories (also the target for file moving)
based on user's classification.
"""
import os, shutil


def main():
    """Start program."""
    # Check and set working directory
    print(os.getcwd())
    # Set the correct working directory
    os.chdir(os.getcwd() + "\\FilesToSort\\")
    # Check the working directory again
    print(os.getcwd())

    for file in os.listdir('.'):
        # Only handle the file if that file exists
        if os.path.isfile(file):
            file_type = os.path.splitext(file)[1].replace('.', '')
            category = input(f"What category would you like to sort {file_type} files into? ")
            # Only create the user-defined directory when that directory doesn't exists. Avoid crashing
            try:
                os.mkdir(category)
            except FileExistsError:
                pass
            # Move the file to their belonging directories
            shutil.move(file, category + "\\")


if __name__ == '__main__':
    main()