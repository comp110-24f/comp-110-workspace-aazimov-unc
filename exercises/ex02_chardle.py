"""EX02 - Chardle - A cute step toward Wordle."""

__author__ = "730751385"


def input_word() -> str:
    word = str(input("Enter a 5-character word: "))
    max_char: int = 5
    if (len(word) < max_char) or (len(word) > max_char):
        print("Error: Word must contain 5 characters.")
        exit()
    return word


def input_letter() -> str:
    char = str(input("Enter a single character: "))
    if len(char) != 1:
        print("Error: Character must be a single character.")
        exit()
    return char


def contains_char(word: str, letter: str) -> None:
    print("Searching for " + str(letter) + " in " + str(word))
    index: int = 0
    count: int = 0
    while len(word) > index:
        if letter == word[index]:
            print(str(letter) + " found in index " + str(index))
            count += 1
        index += 1
    if count <= 0:
        print("No instances of " + str(letter) + " found in " + str(word))
    else:
        print(str(count) + " instances of " + str(letter) + " found in " + str(word))


def main() -> None:
    contains_char(word=input_word(), letter=input_letter())


if __name__ == "__main__":
    main()
