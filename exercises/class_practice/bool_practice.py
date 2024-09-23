"""Bool Practice"""


def check_first_letter(word: str, letter: str) -> None:
    if word[0] == letter:
        print("match!")
    else:
        print("no match!")


if __name__ == "__main__":
    check_first_letter(
        word=str(input("Enter a word")), letter=str(input("Enter a letter"))
    )
    """Press Y to restart"""
    if input("Press Y to restart") == "Y" or "y":
        check_first_letter(
            word=str(input("Enter a word")), letter=str(input("Enter a letter"))
        )
    else:
        print("End!")
