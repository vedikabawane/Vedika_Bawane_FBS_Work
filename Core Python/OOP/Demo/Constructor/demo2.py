class Student:
    def __init__(self,roll_no1,name1,dept1):
        self.roll_no=roll_no1
        self.name=name1
        self.dept=dept1

    def getRoll_no(self):
        return self.roll_no
    def setRoll_no(self,newroll_no):
        self.roll_no=newroll_no

    def getName(self): 
        return self.name
    def setName(self,newname):
        self.name=newname

    def getDept(self):
        return self.dept
    def setDept(self,newdept):
        self.dept=newdept

    def display(self):
        print(f"Roll-no={self.roll_no}\tName={self.name}\tDept={self.dept}")

s1=Student(10,"Vedika","CSE")
s2=Student(11,"Kartik","IT")
print(s1.getName())
s1.display()
s2.display()
s2.setDept('CSE')
s2.display()