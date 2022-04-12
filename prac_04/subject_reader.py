"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"

def main():
    """Main function part"""
    data = get_data()
    print(data)
    display_data()
def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    data_list = []
    input_file = open(FILENAME)
    for line in input_file:
        print(line)  # See what a line looks like
        print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        print(parts)  # See what the parts look like (notice the integer is a string)
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        print(parts)  # See if that worked
        print("----------")
        data_list.append(parts)
    input_file.close()
    return data_list
def display_data():
    """Display the elements in the list return by above function by a proper formatting"""
    pass
    data_list = get_data()
    for sub_list in data_list:
        print(f"{sub_list[0]} is taught by {sub_list[1]:<12} and has {sub_list[2]:>3} students.")
main()