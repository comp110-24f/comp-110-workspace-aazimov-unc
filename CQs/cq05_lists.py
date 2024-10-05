"""Mutating functions."""

__author__ = "730751385"


def manual_append(list: list[int], appended_num: int) -> None:
    list.append(appended_num)  # append number to end of list


def double(list: list[int]) -> None:
    # iterate each number in list & double each term
    idx: int = 0
    while idx < len(list):
        list[idx] *= 2
        idx += 1


list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1
double(list_2)

print(list_1)
print(list_2)
