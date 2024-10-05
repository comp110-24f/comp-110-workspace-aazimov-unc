"""EX04 - List utility Functions"""

__author__ = "730751385"


def all(input_list: list[int], same_int: int) -> bool:
    # Searches through list if given same_int is present in all elements of list
    index: int = 0
    count: int = 0
    all_num_match: bool = False
    # returns false when list is empty
    if len(input_list) == 0:
        all_num_match = False
    else:
        # Iterates each element & adds to counter when same_int = index of that list
        while index < len(input_list):
            assert input_list[index] > 0
            if input_list[index] == same_int:
                count += 1
            index += 1
        # If all the counted elements add up to whole length of list
        # then all the elements are same_int
        if count == len(input_list):
            all_num_match = True
    return all_num_match


def max(input: list[int]) -> int:
    index: int = 0
    max: int = 0
    # output error when list is empty
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    else:
        # iterate through each element & set element as max
        # if the current element at the index is larger than max value
        while index < len(input):
            if max == 0 or input[index] > max:
                max = input[index]
            index += 1
    return max


def is_equal(list_1: list[int], list_2: list[int]) -> bool:
    # initialize shared index, count, and whether all terms match
    index: int = 0
    count: int = 0
    all_match: bool = False
    # return false when both lists are NOT the same length
    if len(list_1) != len(list_2):
        all_match = False
    else:  # if same length, iterate each element
        while index < len(list_1):
            # decide if a element at index in list_1 is same in list_2
            if list_1[index] == list_2[index]:
                count += 1
            index += 1
        # count if all elements are same
        if count == len(list_1):
            all_match = True
    return all_match


def extend(list_1: list[int], list_2: list[int]) -> None:
    # extends list_1 by adding elements from list_2
    index: int = 0
    while index < len(list_2):
        # appends elements of list_2 into the end of list_1
        list_1.append(list_2[index])
        index += 1


a: list[int] = [-5, -2, -3, -1]
print(max(a))
