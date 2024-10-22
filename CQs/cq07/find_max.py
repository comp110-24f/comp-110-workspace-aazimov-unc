"""Find and Remove Max Element in List"""

__author__ = "730751385"


def find_and_remove_max(list_1: list[int]) -> int:
    # finds max number in list and removes it
    max: int = 0
    index: int = 0
    # return -1 when list is empty
    if len(list_1) == 0:
        return -1
    else:
        # first find the max element in list
        for num in list_1:
            if max == 0 or max < num:
                max = num
        # remove that max element from list
        while index < len(list_1):
            if max == list_1[index]:
                list_1.pop(index)
            else:
                index += 1
        return max
