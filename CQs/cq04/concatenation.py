"""Returns concatenation of two strings"""

__author__ = "730751385"

word1: str = "happy"
word2: str = "tuesday"


def concat(str1: str, str2: str) -> str:  # concatenates string1 & string2
    return str1 + str2


if __name__ == "__main__":
    print(concat(word1, word2))
