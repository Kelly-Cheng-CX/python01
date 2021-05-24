class Class_Schedule:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sum1(*args):
        result = 0
        for i in args:
            result += i
        return result

    def attend_class(self, week):
        if week in ("周一", "周二", "周三"):
            print("{}在A教室正常上课".format(week))
        else:
            print("{}在B教室正常上课".format(week))


if __name__ == "__main__":
    class_schedule = Class_Schedule("cx", "18")
    class_schedule.attend_class("周5")
