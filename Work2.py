class Session:
    def __init__(self, semestr = 0, numberOfTests = 0, numberOfExams = 0):
        self.__semestr = semestr
        self.__numberOfTests = numberOfTests
        self.__numberOfExams = numberOfExams
    
    def get_semestr (self):
        return self.__semestr

    def set_semestr (self):
        value = int(input("Введите семестр: "))
        if value > 8 or value < 1:
            return print("Введено недопустимое значение")
        else:
            self.__semestr = value
    
    def get_numberOfTests(self):
        return self.__numberOfTests

    def set_numberOfTests(self):
        value = int(input("Введите количество сданных зачетов: "))
        if self.__semestr in (3, 7):
            if value > 3:
                return print("Введено недопустимое значение")
            else:
                self.__numberOfTests = value
        if self.__semestr in (5 ,6):
            if value > 4:
                return print("Введено недопустимое значение")
            else:
                self.__numberOfTests = value
        else:
            if value > 5:
                return print("Введено недопустимое значение")
            else:
                self.__numberOfTests = value

    def get_numberOfExams(self):
        return self.__numberOfExams

    def set_numberOfExams (self):
        value = int(input("Введите количество сданных экзаменов: "))
        if value > 4:
            return print("Введено недопустимое значение")
        else:
            self.__numberOfExams = value
    
    def passed(self):
        if self.__semestr in (3, 7):
            if self.__numberOfTests == 3 and self.__numberOfExams == 4:
                return print("Зачет")
            else:
                return print("Незачет")
        if self.__semestr in (5, 6):
            if self.__numberOfTests == 4 and self.__numberOfExams == 4:
                return print("Зачет")
            else:
                return print("Незачет")
        else:
            if self.__numberOfTests == 5 and self.__numberOfExams == 4:
                return print("Зачет")
            else:
                return print("Незачет")


Test = Session()
Session.set_semestr(Test)
Session.set_numberOfTests(Test)
Session.set_numberOfExams(Test)
print(Session.get_semestr(Test))
print(Session.get_numberOfTests(Test))
print(Session.get_numberOfExams(Test))
Session.passed(Test)

Test2 = Session()
Session.set_semestr(Test2)
Session.set_numberOfTests(Test2)
Session.set_numberOfExams(Test2)
print(Session.get_semestr(Test2))
print(Session.get_numberOfTests(Test2))
print(Session.get_numberOfExams(Test2))
Session.passed(Test2)