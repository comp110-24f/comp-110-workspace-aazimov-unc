def get_weather_report() -> str:
    """D"""
    weather: str = input("What is the weather?")
    if (weather == "rainy") or (weather == "cold"):
        print("Bring a jacket!")
    elif weather == "hot":
        print("Keep cool out there!")
    else:
        print("I don't recognize this weather.")
    return weather


if __name__ == "__main__":
    get_weather_report()
