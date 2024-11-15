"""Exercise 06"""

__author__: str = "730751385"


def invert(normal_dict: dict[str, str]) -> dict[str, str]:
    # Inverts keys and values of given dictionary
    inverted_dict: dict[str, str] = {}
    seen_val: list[str] = []  # stores seen values
    for key in normal_dict:
        for val in seen_val:
            if val == normal_dict[key]:
                raise KeyError("Cannot have duplicate keys")

        # update current seen_val
        seen_val.append(normal_dict[key])
        # inverts key and value
        inverted_dict[normal_dict[key]] = key
    return inverted_dict


def favorite_color(fav_colors: dict[str, str]) -> str:
    # outputs most common color in dictionary
    # based on num of occurances in fav_count
    fav_count: dict[str, int] = {}
    max_count: int = 0
    common_color: str = ""
    # adds count of occurance for each color
    for people in fav_colors:
        color = fav_colors[people]
        if color in fav_count:
            fav_count[color] += 1
        else:
            fav_count[color] = 1
    # Finds the max num of color based on its count
    for favorites in fav_count:
        count = fav_count[favorites]
        if count > max_count:
            max_count = count
            common_color = str(favorites)

    return common_color


def count(list_items: list[str]) -> dict[str, int]:
    # counts num of occurances in a str list
    count_dict: dict[str, int] = {}
    for item in list_items:
        # if item is already in dict, add to count
        if item in count_dict:
            count_dict[item] += 1
        # else, establish single occurance
        else:
            count_dict[item] = 1
    return count_dict


def alphabetizer(words: list[str]) -> dict[str, list[str]]:
    # orders dictionary key as alphabet with  matched
    # list of words that start with  first letter
    alpa_dict: dict[str, list[str]] = {}
    first_letter: str = ""
    # iterates through each word & orders letter to
    # corrosponding empty list
    for word in words:
        first_letter = word[0].lower()
        # if letter not in key, add to dict
        if first_letter not in alpa_dict:
            alpa_dict[first_letter] = []
        # if it is, append word to list
        alpa_dict[first_letter].append(word)
    return alpa_dict


def update_attendance(attendance: dict[str, list[str]], day: str, name: str) -> None:
    # using bool, will find whether the key "day" is inside attendance
    # if so, append that list in values to current name
    found = False
    for key in attendance:
        if key == day:
            if name not in attendance[day]:
                attendance[day].append(name)
            found = True
    # if not, simple create new value for new name
    if not found:
        attendance[day] = [name]
