"""Exploring linked list utils in class."""

from __future__ import annotations

__author__: str = "730751385"


class Node:
    """Node class with value and next as attributes."""

    value: int
    next: Node | None

    def __init__(self, val: int, next: Node | None):
        """Initializes attributes."""
        self.value = val
        self.next = next

    def __str__(self) -> str:
        """Magic method."""
        rest: str = ""
        if self.next is None:  # Base Case
            rest = "None"
        else:
            rest = str(self.next)
        return f"{self.value} -> {rest}"


def recursive_range(start: int, end: int) -> Node | None:
    """Create linked list with values from start to end."""
    # Edge case
    if start > end:
        raise ValueError("Start cannot be greater than end.")
    # Base case
    if start == end:
        return None
    # Recursive
    else:
        first: int = start
        rest: Node | None = recursive_range(start + 1, end)
        return Node(first, rest)


def last(head: Node) -> int:
    """Returns last value."""
    if head.next is None:  # Base Case
        return head.value
    else:
        return last(head.next)


def value_at(head: Node | None, index: int) -> int:
    """Returns value at index in a linked list."""
    index -= 1  # advances list
    if head is None:  # if no other Node or value on list
        raise IndexError("Index is out of bounds on the list.")
    elif index < 0:  # returns data at current node
        return head.value
    else:
        # recursive
        return value_at(head.next, index)


def max(head: Node | None) -> int:
    """Returns max value from linked list."""
    if head is None:  # Edge case
        raise ValueError("Cannot call max with None")
    if head.next is None:  # Base case
        return head.value

    rest = max(head.next)
    if head.value > rest:  # Recursive case, finds max in linked list
        return head.value
    else:
        return rest


def linkify(items: list[int]) -> Node | None:
    """Links elements togethor in a linked list."""
    if len(items) == 0:  # Base case when list is empty
        return None
    else:  # Recursive case:
        # create a Node with the first item and link it to the rest
        return Node(items[0], linkify(items[1:]))


def scale(head: Node | None, factor: int) -> Node | None:
    """Scales a linked list by a factor."""
    if head is None:  # Base case
        return None
    else:  # Recursive base:
        # multiplies current value by factor
        return Node(head.value * factor, scale(head.next, factor))
