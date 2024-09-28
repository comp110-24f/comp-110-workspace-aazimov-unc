"""Generate coordinates given x and y string values"""

__author__ = "730751385"


def get_coords(xs: str, ys: str) -> None:
    indexX: int = 0
    while len(xs) > indexX:  # Outer loop: Iterates over each char in xs string
        indexY: int = 0
        while len(ys) > indexY:  # Inner loop: Iterates over each char in ys string
            # Formatted as (xs, ys)
            print("(" + str(xs[indexX]) + "," + str(ys[indexY]) + ")")
            indexY += 1
        indexX += 1


if __name__ == "__main__":
    get_coords("hi", "bye")
