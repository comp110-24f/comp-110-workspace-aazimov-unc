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


three: Node = Node(3, None)
two: Node = Node(2, three)
one: Node = Node(1, two)
print(one)
print(last(one))
