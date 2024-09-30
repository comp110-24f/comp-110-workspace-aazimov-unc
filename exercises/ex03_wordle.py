"""EX03 - Wordle - 6 turns to find the secret word"""

__author__ = "730751385"


def input_guess(secret_word_len: int) -> str:
    """Checks if length of word is same as the length of secret word"""
    checkLength: bool = True
    user_word: str = str(input(f"Enter a {secret_word_len} character word: "))
    while (
        checkLength
    ):  # if user inputs word not at length, ask for input again until correct length
        if secret_word_len != len(user_word):
            user_word = str(
                input((f"That wasn't {secret_word_len} chars! Try again: "))
            )
            return user_word
        else:  # return word with correct length
            checkLength = False
    return user_word


def contains_char(secret_word: str, char_guess: str) -> bool:
    """Searches if given string has a character"""
    assert len(char_guess) == 1
    found: bool = False  # determines if char_guess is found in secret word
    index: int = 0
    while len(secret_word) > index:  # Loops through each character in word_guess
        if char_guess == secret_word[index]:
            # if char matches to char_guess, char is "found"
            found = True
        index += 1
    return found


def emojified(guess: str, secret: str) -> str:
    """Outputs emojis based on presence of characters in secret vs. guess"""
    assert len(guess) == len(secret)  # Length of guess HAS to be same as secret
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    index: int = 0
    emojis: str = ""
    while len(secret) > index:
        # Whether a char in secret & guess are in same position
        if secret[index] == guess[index]:
            emojis += GREEN_BOX
        # Whether char is in secret but not in same position
        elif contains_char(secret_word=secret, char_guess=guess[index]):
            emojis += YELLOW_BOX
        else:
            # char is not found at all in secret
            emojis += WHITE_BOX
        index += 1
    return emojis


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""

    won: bool = False  # Determines if player wins game or not
    turns_taken: int = 1  # Number of turns player took
    TOTAL_TURNS: int = 6  # num of total turns allowed in-game

    while (turns_taken <= TOTAL_TURNS) and not (won):
        # Rinse & repeats each turn until turns maxed out
        print(f"=== Turn {turns_taken}/{TOTAL_TURNS} ===")

        # Get & check if player's guess within length range
        user_guess = str(input_guess(len(secret)))

        # Prints emojis based on where player guessed right
        print(emojified(user_guess, secret))

        # If player guesses secret word correctly, player won & game ends
        if secret == user_guess:
            print(f"You won in {turns_taken}/{TOTAL_TURNS} turns!")
            won = True
        else:  # Move on to next turn
            turns_taken += 1

    # If player guesses incorrectly after all turns, player loses & game ends
    if not won:
        print(f"X/{TOTAL_TURNS} - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")
