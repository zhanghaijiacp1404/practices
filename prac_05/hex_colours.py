"""
Use a dictionary to represent ten colours' hexadecimal values.
User can see the corresponding hex values of their input colour
"""

COLOUR_TO_HEXADECIMAL = {"AliceBlue": "#f0f8ff", "AntiqueWhite": "#faebd7",
                         "AntiqueWhite1": "#ffefdb", "AntiqueWhite2": "#eedfcc",
                         "AntiqueWhite3": "#cdc0b0", "AntiqueWhite4": "#8b8378",
                         "aquamarine1": "#7fffd4", "aquamarine2": "#76eec6",
                         "aquamarine4": "#458b74", "azure1": "#f0ffff",
                         "azure2": "#e0eeee", "azure3": "#c1cdcd", "azure4": "#838b8b",
                         "beige": "#f5f5dc", "bisque1": "#ffe4c4"}


def main():
    """Start program"""
    colour_name = str(input("Enter the colour's name: "))
    while colour_name != "":
        print(f"The code for \"{colour_name}\" is: {COLOUR_TO_HEXADECIMAL.get(colour_name)}")
        colour_name = str(input("Enter the colour's name: "))


if __name__ == '__main__':
    main()
