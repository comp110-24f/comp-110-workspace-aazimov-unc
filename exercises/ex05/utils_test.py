import pytest
from exercises.ex05.utils import only_evens, sub, add_at_index

"""ONLY_EVENS"""


def test_only_evens_returns_expected_value() -> None:
    # only_evens should return a list that contains
    # only evens from test_list
    test_list: list[int] = [1, 2, 5, 6]
    assert only_evens(test_list) == [2, 6]


def test_only_evens_edge_case() -> None:
    # when numbers repeat in test list,
    # only_evens should return all even numbers
    test_list: list[int] = [6, 6, 6, 6]
    assert only_evens(test_list) == [6, 6, 6, 6]


def test_only_evens_non_mutable() -> None:
    # test list should not mutable, and instead
    # returns a new list with modified elements
    test_list: list[int] = [2, 6, 1, 3]
    assert only_evens(test_list) != test_list


"""SUB"""


def test_sub_returns_expected_value() -> None:
    # sub should return test list as subset,
    # between index 1 and 4, as [10, 12, 20]
    test_list: list[int] = [8, 10, 12, 20, 50]
    assert sub(test_list, 1, 4) == [10, 12, 20]


def test_sub_edge_case() -> None:
    # sub should return test list as subset
    # between index -1 and 1, where when negative start_idx,
    # sub should start at first of list
    test_list: list[int] = [1, 2, 4, 8]
    assert sub(test_list, -1, 1) == [1]


def test_sub_non_mutable() -> None:
    # sub should not mutate test list
    # and remain the same
    test_list: list[int] = [1, 3, 4, 6, 9, 8]
    assert sub(test_list, 1, 3) != test_list


"""ADD_TO_INDEX"""


def test_add_to_index_returns_expected_value() -> None:
    # When test_list has the number 2 added in the third index
    # test_list should add 2 and shift list
    test_list: list[int] = [1, 2, 3, 4]
    add_at_index(test_list, 5, 4)
    assert test_list == [1, 2, 3, 4, 5]


def test_add_to_index_edge_case() -> None:
    # When test_list has -1 added to first index,
    # test_list should have two -1 at first two indices
    test_list: list[int] = [-1, 1, 1, 1]
    add_at_index(test_list, -1, 0)
    assert test_list == [-1, -1, 1, 1, 1]


def test_add_to_index_mutable() -> None:
    # add_to_index should mutate test_list,
    # so that add_to_index(test_list) & test_list
    # are the same
    test_list: list[int] = [9, 9, 0, 1]
    add_at_index(test_list, 2, 3)
    assert test_list == [9, 9, 0, 2, 1]


def test_add_at_index_raises_indexerror():
    # Test that add_at_index raises an IndexError for an invalid index.
    with pytest.raises(IndexError):
        test_list: list[int] = [1, 2, 3, 4, 5, 6, 7, 8]
        add_at_index(test_list, 11, 10)
        # an IndexError is raised for the case when the
        # add_at_index is given an <index_to_insert_num>
        # that is greater than the length of our <list_object>
