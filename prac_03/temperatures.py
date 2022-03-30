"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""

def main():
    MENU = """C - Convert Celsius to Fahrenheit
    F - Convert Fahrenheit to Celsius
    Q - Quit"""

    print(MENU)
    choice = input(">>> ").upper()

    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            print(f"Result: {celsius_to_fahrenheit(celsius):.2f}")
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit: "))
            print(f"Result: {fahrenheit_to_celsius(fahrenheit):.2f}")
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")
def celsius_to_fahrenheit(celsius):
    return float(celsius * 9.0 / 5 + 32)
def fahrenheit_to_celsius(fahrenheit):
    return float(5.0 / 9.0 * (fahrenheit - 32.0))
main()