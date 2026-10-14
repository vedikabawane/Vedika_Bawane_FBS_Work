class Emp:
    def __init__(self,id,name,sal):
        self._id=id
        self._name=name
        self._sal=sal
    def getId(self):
        return self._id
    def setId(self,nid):
        self._id=nid
    def __str__(self):
        return f'Id={self._id} Name={self._name} Sal={self._sal}'

class Hr(Emp):
    def __str__(self):
        print(self._id)
        return super().__str__()

e1=Emp(12,'vedika',123)
print(e1.getId())
e1.setId(18)
print(e1.getId())
print(e1)
