class Time:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes

    def DisplayTime(self):
        if self.hours > 23:
            print("The input hours should be less than 24")
            return
        if self.minutes > 59:
            print("The input minutes should be less than 60")
            return
        if self.hours == 0:
            hour = 12
            suffix = "AM"
        elif self.hours < 12:
            hour = self.hours
            suffix = "AM"
        elif self.hours == 12:
            hour = 12
            suffix = "PM"
        else:
            hour = self.hours - 12
            suffix = "PM"
        print(f"The time is {hour}:{self.minutes:02d} {suffix}")

    def DisplayRatio(self):
        try:
            ratio = self.minutes / self.hours
        except ZeroDivisionError:
            print("Division by zero error")
            return
        print(f"The ratio of minutes to hours is {ratio:.2f}")


# Check for few sample inputs of hours and mins
hour_min_list = [(23, 45), (34, 50), (12, 34), (14, 67), (19, 20), (2, 15), (0, 10)]

for hour, minute in hour_min_list:
    time_obj = Time(hour, minute)
    time_obj.DisplayTime()
    time_obj.DisplayRatio()
    print("-" * 30)