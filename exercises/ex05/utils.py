"""Utillity Functions - Excercise 05"""

__author__: str = "730751385"


def only_evens(user_list: list[int]) -> list[int]:
    # adds all even number from user list to even list
    even_list: list[int] = []
    for num in user_list:
        # checks if element is even
        if num % 2 == 0:
            even_list.append(num)
            print(num)
    return even_list


# gives s subset of list based on start & end index
def sub(given_list: list[int], start_idx: int, end_idx: int) -> list[int]:
    sub_list: list[int] = []
    # if start index is a negative, set index at beginning of list
    if start_idx < 0:
        start_idx = 0
    # if end index is greater than list, set index at end of list
    if end_idx > len(given_list):
        end_idx = len(given_list)
    # if given list is empty, start endex greater than length, end index at most 0
    # return the empty sub list
    if len(given_list) == 0 or start_idx >= len(given_list) or end_idx <= 0:
        return sub_list
    else:
        # add resulting elements bounded by start & end indices
        while start_idx < end_idx:
            sub_list.append(given_list[start_idx])
            start_idx += 1
        return sub_list


def add_at_index(input_list: list[int], elem_add: int, index_add: int) -> None:
    # raises Index error if index to be added negative, or greater than length
    if index_add < 0 or index_add > len(input_list):
        raise IndexError("Index is out of bounds for the input list")
    # add a temporary val at end of list
    input_list.append(0)
    # shifts elements to the right
    # from last index on input_list to index to add, working backwards
    for idx in range(len(input_list) - 1, index_add, -1):
        input_list[idx] = input_list[idx - 1]
    # new element is inserted at index
    input_list[index_add] = elem_add
