__author__ = "730751385"

"""Counts the # of occurances in a phrase"""


def num_instances(phrase: str, searchcar: str) -> None:
    searching: bool = True
    count: int = 0
    index: int = 0
    while searching:
        # While iterating, check if index reaches end of phrase
        if len(phrase) > index:
            # If letter at index matches to char, add to count
            if phrase[index] == searchcar:
                count += 1
            # Adds 1 to index each iteration
            index += 1
        else:
            # Once it reaches end of phrase, exit while loop
            searching = False
    print(str(count))
