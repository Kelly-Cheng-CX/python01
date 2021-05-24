from class_module.a import Class_Schedule


class Teacher_Information(Class_Schedule):

    def __init__(self, name, age, salary):
        Class_Schedule.__init__(self, name, age)
        self.salary = salary

    def talk(self, lesson):
        self.lesson = lesson
        print("{} talking {}".format(self.name,self.lesson))
        Class_Schedule.attend_class(self, self.lesson)


if __name__ == '__main__':
    TI = Teacher_Information("鹿晗", "31", "10000")
    TI.talk("Python")