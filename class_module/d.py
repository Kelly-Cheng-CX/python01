class phone:
    name = "cx"

    def call(self):
        print("{}正在打电机".format(phone.name))

    def record(self):
        print("正在录音")


class SmartPhone(phone):
    def call(self, recode=False):
        super().call()
        if recode == True:
            self.record()


class Iphone(phone):
    def face_time(self):
        print("正在 facetime")

    def call(self, recode=False, face_time=False):
        super().call()
        if recode:
            self.record()
        if face_time:
            self.face_time()


# s = SmartPhone()
# i = Iphone()
# i.call(True, True)

# s.call(True)
class ExcelManual:
    def __init__(self, file):
        self.file = file

    def get_sheet(self, name):
        pass

    def read_sheet(self, row, column):
        pass

    def change_sheet(self, row, column,new_value):
        pass
