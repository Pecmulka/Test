class Session:
    def __init__(self, semestr, numberOfTests, numberOfExams): #Конструктор объекта сессии
        self.__semestr = semestr 
        self.__numberOfTests = numberOfTests
        self.__numberOfExams = numberOfExams
    
    def get_semestr (self): #Получение семестра
        return self.__semestr

    def set_semestr (self, semestr): #Изменение семестра
        self.__semestr = semestr
    
    def get_numberOfTests(self): #Получение кол-во зачетов
        return self.__numberOfTests

    def set_numberOfTest(self, numberOfTests): #Изменение кол-во зачетов
        self.__numberOfTests = numberOfTests

    def get_numberOfExams(self): #Получение кол-во экзаменов
        return self.__numberOfExams

    def set_numberOfExams(self, numberOfExams): #Изменение кол-во экзаменов
        self.__numberOfExams = numberOfExams

Test = Session(2, 4, 2) #Создание объекта Test класса Session с переменными 2 семестр, 4 сданных зачетов и 2 сданных экзамена
print(Session.get_semestr(Test))
print(Session.get_numberOfTests(Test)) #Вывод информации
print(Session.get_numberOfExams(Test))

Test2 = Session() #Создание пустого объекта Test2 класса Session
Session.set_semestr(Test2, 1) #Задаём значение семестра
Session.set_numberOfTest(Test2, 3) #Задаём значение кол-во зачетов
Session.set_numberOfExams(Test2, 1) #Задаём значение кол-во экзаменов
print(Session.get_semestr(Test2))
print(Session.get_numberOfTests(Test2)) #Вывод информации
print(Session.get_numberOfExams(Test2))
