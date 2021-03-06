"""
Determine score status base on score
"""

from random import randint as ri
def main()->None:
    """Interact with user based on generate_result() function"""
    user_score = float(input("Enter score: "))
    print(generate_result(user_score))

    #Code block for handling randomly generated "random_socre" variable
    random_score = ri(0, 100)
    print(f"Random generated score is {random_score}")
    print(generate_result(random_score))
    print("End program")
def generate_result(user_score):
    """Return different score status string for different range"""
    if user_score >= 0 and user_score <= 100:
        if user_score >= 90 and user_score <=100:
            return "Excellent"
        elif user_score >= 50 and user_score < 90:
            return "pass"
        elif user_score >= 0 and user_score < 50:
            return "bad"
if __name__ == '__main__':
    main()