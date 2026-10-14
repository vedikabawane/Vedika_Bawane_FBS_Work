class Emp:
    def __init__(self,id,name,sal):
        self.__id=id
        self.__name=name
        self.__sal=sal
    def getId(self):
        return self.__id
    def setId(self,nid):
        self.__id=nid
    def __str__(self):
        return f'Id={self.__id} Name={self.__name} Sal={self.__sal}'

class Hr(Emp):
    def __str__(self):
        print(self.__id)
        return super().__str__()

e1=Emp(12,'vedika',123)
print(e1.getId())
e1.setId(18)
print(e1.getId())
print(e1)
