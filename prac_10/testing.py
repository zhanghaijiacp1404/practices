"""
CP1404/CP5632 Practical
Testing demo using assert and doctest
"""

import doctest
from prac_06.car import Car


def repeat_string(s, n):
    """Repeat string s, n times, with spaces in between."""
    return " ".join(n * [s])


def is_long_word(word, length=5):
    """
    Determine if the word is as long or longer than the length passed in
    >>> is_long_word("not")
    False
    >>> is_long_word("supercalifrag")
    True
    >>> is_long_word("Python", 6)
    True
    """
    return len(word) >= length


def run_tests():
    """Run the tests on the functions."""
    # assert test with no message - used to see if the function works properly
    assert repeat_string("Python", 1) == "Python"
    # the test below should fail
    assert repeat_string("hi", 2) == "hi hi"

    # assert test with custom message,
    # used to see if Car's init method sets the odometer correctly
    # this should pass (no output)
    test_car = Car()
    assert test_car.odometer == 0, "Car does not set odometer correctly"

    # Assert statements that showing if the Car object sets the fuel correctly
    test_car = Car(fuel=10)
    assert test_car.fuel == 10
    test_car = Car()
    assert test_car.fuel == 0


def phase_to_sentence(phase):
    """
    Change a phase args to a formal sentence
    Capitalize the initial character, add an end stop if it doesn't have
    >>> phase_to_sentence("hello")
    'Hello.'
    >>> phase_to_sentence("It is an ex parrot.")
    'It is an ex parrot.'
    """
    if phase[-1] != '.':
        phase += '.'
    return phase.capitalize()


run_tests()
doctest.testmod()
