"""A welcoming test program to start COMP110"""

__author__ = "01234567"

print("Welcome to COMP110!")
print("You are in for a fun adventure into programming!")
print("<3 the COMP110 Team!")


def view(my_list: list[str]):
    idx: int = 0
    while idx < len(my_list):
        print(my_list[idx])
        idx += 1


msg: list[str] = ["Hello", "World"]
view(msg)
