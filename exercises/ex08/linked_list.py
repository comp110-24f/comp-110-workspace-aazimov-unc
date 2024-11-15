"""Exploring linked list utils in class."""

from __future__ import annotations


class Node:
    value: int
    next: Node | None

    def __init__(self, val: int, next: Node | None):
        self.value = val
        self.next = next

    def __str__(self) -> str:
        rest: str = ""
        if self.next is None:  # Base Case
            rest = "None"
        else:
            rest = str(self.next)
        return f"{self.value} -> {rest}"


def last(head: Node) -> int:
    if head.next is None:  # Base Case
        return head.value
    else:
        return last(head.next)


def value_at(head: Node | None, index: int) -> int:
    """returns value at index in a linked list."""
    index -= 1  # advances list
    if head is None:  # if no other Node or value on list
        raise IndexError("Index is out of bounds on the list.")
    elif index < 0:  # returns data at current node
        return head.value
    else:
        # recursive
        return value_at(head.next, index)


def max(head: Node | None) -> int:
    if head is None:
        raise ValueError("Cannot call max with None")

    if head.next is None:
        return head.value

    max_of_rest = max(head.next)

    return max(max_of_rest)


three: Node = Node(3, None)
two: Node = Node(2, three)
one: Node = Node(1, two)
# print(one)
# print(last(one))
print(max(Node(10, Node(20, Node(30, None)))))
