"""Guitar class"""
CURRENT_YEAR = 2022


class Guitar:
    """Guitar class that contains all info regarding a guitar"""

    def __init__(self, name="", year=0, cost=0):
        """Constructor of a Guitar object"""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a string representation of a guitar"""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        """Get the age of a guitar based on the constant CURRENT_YEAR."""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Determine whether a guitar is vintage based on its age"""
        return self.get_age() >= 50

    def __lt__(self, other):
        """Return whether the guitar's year is less than another guitar"""
        return self.year < other.year