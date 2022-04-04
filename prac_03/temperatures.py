"""
Temperature convertion.
User input:
- "C": convert celsius to fahrenheit
- "F": convert fahrenheit to celsius
"""

def main():
    MENU = """C - Convert Celsius to Fahrenheit
    F - Convert Fahrenheit to Celsius
    Q - Quit"""

    # Show operating menu
    print(MENU)
    choice = input(">>> ").upper()

    # handling user input
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
    """With known celsius, calculate and return fahrenheit"""
    return float(celsius * 9.0 / 5 + 32)
def fahrenheit_to_celsius(fahrenheit):
    """With known fahreneit, calculate and return celsius"""
    return float(5.0 / 9.0 * (fahrenheit - 32.0))
main()