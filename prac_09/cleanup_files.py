"""
CP1404/CP5632 Practical
Demos of various os module examples
"""
import shutil
import os


def main():
    """Demo os module functions."""
    print("Starting directory is: {}".format(os.getcwd()))

    # Change to desired directory
    os.chdir('Lyrics')

    # Print a list of all files in current directory
    print("Files in {}:\n{}\n".format(os.getcwd(), os.listdir('.')))

    for dir_name, dir_list, files in os.walk('.'):
        for filename in files:
            pass
            new_file_name = get_fixed_filename(filename)
            print(f"Renaming {filename} to {new_file_name}")
            full_file_name = os.path.join(dir_name, filename)
            new_file_name = os.path.join(dir_name, new_file_name)
            os.rename(full_file_name, new_file_name)


def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    new_name = filename.replace(" ", "_").replace(".TXT", ".txt")
    return new_name


main()
