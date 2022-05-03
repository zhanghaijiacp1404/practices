"""Programming language class"""


class ProgrammingLanguage:
    """Represent programming language's information"""
    def __init__(self, name, typing, reflection, year):
        """Constructor of a ProgrammingLanguage object"""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """Return a string representation of a ProgrammingLanguage object"""
        return f"{self.name}, {self.typing} Typing, Reflection = {self.reflection}, " \
               f"First appeared in {self.year}"

    def is_dynamic(self):
        """Returns whether a programming language is dynamically typed"""
        return self.typing == "Dynamic"
