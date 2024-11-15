"""File to define River class."""

__author__ = "730751385"

from exercises.ex07.fish import Fish
from exercises.ex07.bear import Bear


class River:
    """Defines River class w/ declaredattributes day, fish, & bears."""

    day: int
    fish: list[Fish]
    bears: list[Bear]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Removes or kills off bear or fish at certain age."""
        # created new list w/ Fish & Bear classes
        new_fish: list[Fish] = []
        new_bears: list[Bear] = []
        # appended all fish that are less than 3 years old
        for fish in self.fish:
            if fish.age <= 3:
                new_fish.append(fish)
        # appended all bears that are less than 5 years old
        for bear in self.bears:
            if bear.age <= 5:
                new_bears.append(bear)

        # set new lists as current self. lists
        self.bears = new_bears
        self.fish = new_fish
        return None

    def remove_fish(self, amount: int):
        """Removes fish by amount."""
        for _ in range(amount):
            self.fish.pop(0)
        return None

    def bears_eating(self):
        """Bear consumption of 3 fish per bear."""
        # for each bear in bears
        for bear in self.bears:
            # if there are more than 5 fishes
            if len(self.fish) >= 5:
                # num of fish to eat/take out
                num_eaten: int = 3
                self.remove_fish(num_eaten)
                bear.eat(num_eaten)
        return None

    def check_hunger(self):
        """Removes starving bears from population."""
        # checks if there are any starving bears
        surviving_bears: list[Bear] = []
        # adds surving bear w/ hunger_score >= 0:
        for bear in self.bears:
            if bear.hunger_score >= 0:
                surviving_bears.append(bear)
        # updates bears by ignoring starved bears
        self.bears = surviving_bears
        return None

    def repopulate_fish(self):
        """Fish repopulation for 4 offspring per fish pair."""
        # counts total fish
        total_fish: int = len(self.fish)
        # for each pair of fish, 4 offsprings produced
        fish_offspring: int = (total_fish // 2) * 4
        # creates fish_offspring amount of fish
        for _ in range(fish_offspring):
            self.fish.append(Fish())
        return None

    def repopulate_bears(self):
        """Bear repopulation for 1 offspring per bear pair."""
        # counts total bears
        total_bears: int = len(self.bears)
        # divides total bears by 2 to get offspring
        bear_offspring: int = total_bears // 2
        # creates a new bear for offspring
        for _ in range(bear_offspring):
            self.bears.append(Bear())
        return None

    def view_river(self):
        """Prints output."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
        return None

    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        """Repeats one river day 7 times."""
        for _ in range(7):
            self.one_river_day()
