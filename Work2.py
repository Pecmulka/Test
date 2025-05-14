class Session:
    def __init__(self, semestr = 0, numberOfTests = 0, numberOfExams = 0): #Конструктор класса сессии
        self.__semestr = semestr
        self.__numberOfTests = numberOfTests
        self.__numberOfExams = numberOfExams
    
    def get_semestr (self): #Получение семестра
        return self.__semestr

    def set_semestr (self): #Изменение семестра
        value = int(input("Введите семестр: "))
        if value > 8 or value < 1: #Проверка на допустимость значения
            return print("Введено недопустимое значение")
        else:
            self.__semestr = value
    
    def get_numberOfTests(self): #Получение кол-во зачетов
        return self.__numberOfTests

    def set_numberOfTests(self): #Изменение кол-во зачетов
        value = int(input("Введите количество сданных зачетов: "))
        if self.__semestr in (3, 7): #Проверка на допустимость значения
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

    def get_numberOfExams(self): #Получение кол-во экзаменов
        return self.__numberOfExams

    def set_numberOfExams (self): #Изменение кол-во экзаменов
        value = int(input("Введите количество сданных экзаменов: "))
        if value > 4: #Проверка на допустимость значения
            return print("Введено недопустимое значение")
        else:
            self.__numberOfExams = value
    
    def passed(self): #Метод проверки, получил ли студент зачет, или нет.
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


Test = Session() #Создание пустого объекта Test класса Session
Session.set_semestr(Test) 
Session.set_numberOfTests(Test) #Присвоение значений объекту Test
Session.set_numberOfExams(Test)
print(Session.get_semestr(Test))
print(Session.get_numberOfTests(Test)) #Вывод значений объекта Test
print(Session.get_numberOfExams(Test))
Session.passed(Test) #Проверка зачета

Test2 = Session() #Создание пустого объекта Test2 класса Session
Session.set_semestr(Test2)
Session.set_numberOfTests(Test2) #Присвоение значений объекту Test2
Session.set_numberOfExams(Test2)
print(Session.get_semestr(Test2))
print(Session.get_numberOfTests(Test2)) #Вывод значений объекта Test2
print(Session.get_numberOfExams(Test2))
Session.passed(Test2) #Проверка зачета
