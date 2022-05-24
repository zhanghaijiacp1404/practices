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

    # A dictionary variable indicates: file suffix - file category
    file_category = {}

    for file in os.listdir('.'):
        # If system detect the directory, ignore it. Only focus on files
        if os.path.isdir(file):
            continue
        suffix = file.split('.')[-1]
        # Only handle the file if that file exists
        if suffix not in file_category:
            category = input(f"What category would you like to sort {suffix} files into? ")
            file_category[suffix] = category
            # Only create the user-defined directory when that directory doesn't exists. Avoid crashing
            try:
                os.mkdir(category)
            except FileExistsError:
                pass
            # Move the file to their belonging directories
        shutil.move(file, category + "\\")


if __name__ == '__main__':
    main()