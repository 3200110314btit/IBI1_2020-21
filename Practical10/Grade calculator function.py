class Grade:
    def __init__(self,name,codeportfolio,posterpresentation,finalexam):
        self.__name = name
        self.__codeportfolio = codeportfolio
        self.__posterpresentation = posterpresentation
        self.__finalexam = finalexam
    def getname(self):
        return self.__name
    def getGrade(self):
        Grade = self.__codeportfolio*0.4+(self.__posterpresentation+self.__finalexam)*0.3
        return Grade
f=Grade('Fan Xiang',80,90,100)
#example
z=Grade(input('His name is:'),int(input('His code portfolio grade is:')),int(input('His poster presentation grade is:')),int(input('His final exam grade is:')))
print(f.getname(),'whose grade is',f.getGrade())
print(z.getname(),'whose grade is',z.getGrade())