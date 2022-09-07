import uuid
import json


class Car:

    def __init__(self, year, name):
        self.name = name
        self.speed = 0
        self.year = year
        self.time_running = 0
        self.running = True
        self.UID = str(uuid.uuid4())

    def to_json(self):
        return json.dumps(self.__dict__)

    def accelerate(self):
        self.speed += 5

    def brake(self):
        if self.speed < 5:
            self.speed = 0
        else:
            self.speed -= 5

    def run(self):
        self.time_running += 1

    def say_state(self):
        if self.running:
            print(f"I'm currently going {self.speed} mph!")
        else:
            print("")
            print("Turning off this Car's engine.")
            print(f"Car was currently going {self.speed}mph!")
            print(f"This Car has been running for {self.time_running} ticks!")

    def stop(self):
        self.running = False

    def show_timeRunning(self):
        print(f"This Car has been running for {self.time_running} ticks!")
