# Event.py

class Event:

    def __init__(self, day, time, location):
        self.day = day
        self.time = tuple(time)
        self.location = location.upper()

    def __eq__(self, rhs):
        if (self.day == rhs.day) and (self.time == rhs.time) and (self.location == rhs.location):
            return True
        else:
            return False

    def __str__(self):
        return f"{self.day} {self.time[0]//100:0>2}:{self.time[0]%100:0>2} - {self.time[1]//100:0>2}:{self.time[1]%100:0>2}, {self.location}"

