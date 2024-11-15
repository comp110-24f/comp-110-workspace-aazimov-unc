"""File to define Bear class."""

__author__ = "730751385"


class Bear:
    """Defines Bear class & declares age + hunger_score attributes."""

    age: int
    hunger_score: int

    def __init__(self):
        """Initializes bear age & hunger to 0."""
        self.age = 0
        self.hunger_score = 0
        return None

    def one_day(self):
        """Increases bear age & decreases hunger by 1."""
        self.age += 1
        self.hunger_score -= 1
        return None

    def eat(self, num_fish: int):
        """Bear relieves hunger from amount of fish eaten."""
        self.hunger_score += num_fish
        return None
