__author__ = "730751385"


def mimic(message: str) -> str:
    """Copies and returns message"""
    return message


def main() -> None:
    """Main function, prints out mimiced message once input given"""
    print(mimic(message=input("What is your message?")))
    return None


if __name__ == "__main__":
    """Calls the main function, mimics message given"""
    main()
