class Student:
    stCount = 0
    def __init__(self, frn, name, bname):
        self.frn = frn
        self.name = name
        self.batch = bname
        Student.stCount += 1

    def display(self):
        print(f'FRN = {self.frn}\tName = {self.name}\tBatch = {self.batch}\tStudent Count = {Student.stCount}')

class PlacedStudent(Student):
    def __init__(self, frn, name, bname, cName):
        super().__init__(frn,name,bname)
        self.cName=cName
    def setCname(self,cName):
        self.cName=cName
    def getCname(self):
        return self.cName
    def display(self):
        print(f'CName={self.c}')
        super().display()

    # def display(self):
    #     print(f'FRN = {self.frn}\tName = {self.name}\tBatch = {self.bname}\tCompany Name = {self.cName}')

e1 = Student(11, 'Avani', 'Jul')
e2 = Student(12, 'Gauri', 'Aug')
e3 = Student(13, 'Sanvi', 'Sep')
e4 = PlacedStudent(14, 'Amisha', 'Aug', 'TCS')
e5 = PlacedStudent(15, 'Vedika', 'Aug', 'TCS')
print(Student.stCount)