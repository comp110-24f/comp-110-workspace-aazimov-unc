from find_max import find_and_remove_max


def test_find_and_remove_max_returns_expected_value() -> None:
    # when find_and_remove_max returns an expected value
    # for example, should return 9 as max value
    # if not, assert error
    list_1 = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    max_value = find_and_remove_max(list_1)
    assert max_value == 9, f"Expected 9, but got {max_value}"


def test_find_and_remove_max_mutates_input() -> None:
    # when mutating input list, the max value from list should be removed
    list_1 = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    find_and_remove_max(list_1)
    assert 9 not in list_1, "Max value was not removed from the list"
    assert len(list_1) == 10, f"Expected list length to be 10, but got {len(list_1)}"


def test_find_and_remove_max_edge_case() -> None:
    # edge case, list should be empty after everything removed
    list_1 = [7, 7, 7, 7]
    max_value = find_and_remove_max(list_1)
    assert max_value == 7, f"Expected 7, but got {max_value}"
    assert list_1 == [], "List should be empty after removing all max elements"
