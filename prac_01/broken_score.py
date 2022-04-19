"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

# TODO: Fix this!

from typing import *
def main()->None:
    user_score = float(input("Enter score: "))
    if user_score >= 0 and user_score <= 100:
        if user_score >= 90 and user_score <=100:
            print("Excellent")
        elif user_score >= 50 and user_score < 90:
            print("pass")
        elif user_score >= 0 and user_score < 50:
            print("bad")
    print("End program")
if __name__ == '__main__':
    main()