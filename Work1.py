class Session:
    def __init__(self, semestr, numberOfTests, numberOfExams):
        self.__semestr = semestr
        self.__numberOfTests = numberOfTests
        self.__numberOfExams = numberOfExams
    
    def get_semestr (self):
        return self.__semestr

    def set_semestr (self, semestr):
        self.__semestr = semestr
    
    def get_numberOfTests(self):
        return self.__numberOfTests

    def set_numberOfTest(self, numberOfTests):
        self.__numberOfTests = numberOfTests

    def get_numberOfExams(self):
        return self.__numberOfExams

    def set_numberOfExams(self, numberOfExams):
        self.__numberOfExams = numberOfExams

Test = Session(2, 4, 2)
print(Session.get_semestr(Test))
print(Session.get_numberOfTests(Test))
print(Session.get_numberOfExams(Test))

Test2 = Session()
Session.set_semestr(Test2, 1)
Session.set_numberOfTest(Test2, 3)
Session.set_numberOfExams(Test2, 1)
print(Session.get_semestr(Test2))
print(Session.get_numberOfTests(Test2))
print(Session.get_numberOfExams(Test2))
