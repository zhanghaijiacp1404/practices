"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

from random import randint as ri
def main()->None:
    user_score = float(input("Enter score: "))
    print(generate_result(user_score))

    random_score = ri(0, 100)
    print(f"Random generated score is {random_score}")
    print(generate_result(random_score))
    print("End program")
def generate_result(user_score):
    if user_score >= 0 and user_score <= 100:
        if user_score >= 90 and user_score <=100:
            return "Excellent"
        elif user_score >= 50 and user_score < 90:
            return "pass"
        elif user_score >= 0 and user_score < 50:
            return "bad"
if __name__ == '__main__':
    main()