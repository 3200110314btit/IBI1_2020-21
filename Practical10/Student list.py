class Student:
    #make a class
    def __init__(self,fir,last,major):
        self.__fir = fir
        self.__last = last
        self.__major = major
    
    def getfir(self):
        return self.__fir
    def getlast(self):
        return self.__last
    def getmajor(self):
        return self.__major
f=Student('Fan','Xiang','BMS')
z=Student(input('its first name is:'),input('its last name is:'),input('its major is:'))
#make an example
print(f.getfir(),f.getlast(),'whose major is',f.getmajor())
print(z.getfir(),z.getlast(),'whose major is',z.getmajor())
