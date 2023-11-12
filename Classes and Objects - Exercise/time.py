class Time:
    max_hours = 23
    max_minutes = 59
    max_seconds = 59

    def __init__(self, hours: int, minutes: int, seconds: int):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def time_validation(self, num1, num2) -> bool:
        return num2 >= num1

    def set_time(self, hours, minutes, seconds) -> None:
        if self.time_validation(seconds, Time.max_seconds):
            self.seconds = seconds
        else:
            self.seconds = 0
            minutes += 1

        if self.time_validation(minutes, Time.max_minutes):
            self.minutes = minutes
        else:
            self.minutes = 0
            hours += 1

        if self.time_validation(hours, Time.max_hours):
            self.hours = hours
        else:
            self.hours = 0

    def get_time(self) -> str:
        return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"

    def next_second(self) -> str:
        self.set_time(self.hours, self.minutes, self.seconds + 1)
        return self.get_time()



