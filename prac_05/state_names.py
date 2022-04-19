"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales",
                "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria",
                "TAS": "Tasmania"}
print(CODE_TO_NAME)

# Promote the user to enter the state code
state_code = input("Enter short state: ")
while state_code != "":
    if state_code in CODE_TO_NAME:
        print(state_code, "is", CODE_TO_NAME[state_code])
    else:
        print("Invalid short state")
    state_code = input("Enter short state: ")

# Display items in code to name dictionary
for key, value in CODE_TO_NAME.items():
    print(f"{key:<3} is {value}")