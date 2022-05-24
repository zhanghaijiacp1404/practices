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
    filename = list(filename)
    for index, char in enumerate(filename, 0):
        try:
            # change the pattern of such "AmericanBook" to "American_Book"
            if filename[index].islower() and filename[index+1].isupper():
                filename.insert(index + 1, '_')
        except IndexError:
            pass

    fixed_filename = ""
    for item in filename:
        fixed_filename += item
    return fixed_filename.title().replace(" ", "_").replace(".Txt", ".txt")


main()
