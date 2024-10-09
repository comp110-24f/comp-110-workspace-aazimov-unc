"""Summing the elements of a list using different loops"""

__author__ = "730751385"


def w_sum(vals: list[float]) -> float:
    # returns sum of elements in the vals list
    sum: float = 0.0
    index: int = 0
    # iterate each elem & add to sum
    while index < len(vals):
        sum += vals[index]
        index += 1
    return sum  # return as float


def f_sum(vals: list[float]) -> float:
    # using for-loop to iterate each element in vals
    # then adding each val to sum as float
    sum: float = 0.0
    for val in vals:
        sum += val
    return sum


def f_range_sum(vals: list[float]) -> float:
    # using for-loop w/ range function to
    # iterate each elem in vals list as val
    sum: float = 0.0
    for val in range(0, len(vals)):
        sum += vals[val]
    return sum
