"""File to define Fish class."""

__author__ = "730751385"


class Fish:
    """Defines Fish class & declares age attribute."""

    age: int

    def __init__(self):
        """Initializes age of fish to 0."""
        self.age = 0
        return None

    def one_day(self):
        """Increases age of fish by 1 each day."""
        self.age += 1
        return None
