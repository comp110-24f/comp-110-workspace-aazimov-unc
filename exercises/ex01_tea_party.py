"""Tea Party Planning App"""

__author__: str = "730751385"


def main_planner(guests: int) -> None:
    """Calculate total cost of tea party"""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print(
        "Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )


def tea_bags(people: int) -> int:
    """How many bags of tea per person"""
    bags_of_tea: int = people * 2
    return bags_of_tea


def treats(people: int) -> int:
    """How many treats per cup of tea"""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """Computes total cost of teabags + treats"""
    return (tea_count * 0.50) + (treat_count * 0.75)


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
