from Car_Object import Car
from types import SimpleNamespace

import json
import random


def car_input():
    car_map = ["Ford", "Dodge", "BMW", "Honda", "Hyundai", "Lincoln", "Toyota"]
    year_map = [1999, "102 B.C.", 2002, 2003, 2020, 2021, 2022, 2023]

    # Map for our json strings
    json_string = []

    # Create 100 different car objects, convert them to a json str, then store into the list
    for x in range(0, 100):
        json_string.append(Car(random.choice(year_map), random.choice(car_map) + f" {(x + 1)}").to_json())

    # Loop through the json map, converting each one back to Car object
    for z in json_string:
        car = json.loads(z, object_hook=lambda d: SimpleNamespace(**d))
        print(car.year, car.name, car.UID)


def main():
    welcome_line = [
        "Python program #1",
        "Please enter an option",
        "   1. A list of 100 Cars",
        "   2. Control a Car",
        ""
    ]

    for x in welcome_line:
        print(x)

    option = input("Enter option: ")

    if option == "1":
        car_input()

    elif option == "2":
        new_car = Car(2022, "Lickem")
        while new_car.running:
            print("")
            print("Tell me what to do! [A]ccelerate, [B]rake, show [T]ime running, or [S]top the vehicle")
            action = input("Option: ").lower() # so we can ignore case

            if action not in "abts" or len(action) != 1:
                print("Incorrect option")
                continue

            if action == "a":
                new_car.accelerate()

            elif action == "b":
                new_car.brake()

            elif action == "t":
                new_car.show_timeRunning()

            elif action == "s":
                new_car.stop()

            new_car.run()
            new_car.say_state()

    else:
        print("Invalid Option")
        print("")
        main()


if __name__ == "__main__":
    main()
