"""
try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")
"""
#TODO When will a ValueError occur?
# This can occur when numerator or denominator is not a number variable (ex. character, string, boolean values)

#TODO When will a ZeroDivisionError occur?
# This can occur when denominator is zero

#TODO Could you change the code to avoid the possibility of a ZeroDivisionError?
# New code
try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        denominator = int(input("Denominator shouldn't be zero, enter again: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")