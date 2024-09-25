"""Removes a character from a string"""


def remove_chars(msg: str, char: str) -> str:
    copy: str = ""
    index: int = 0
    while index <= len(msg):
        if msg[index] != char:
            print(index)
            copy += msg[index]
        index += 1
    return copy


word: str = input("Enter word: ")
char: str = input("Enter char: ")
print(remove_chars(word, char))
