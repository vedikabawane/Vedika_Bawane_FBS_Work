class Student:
    inName="FBS"
    def __init__(self,frn,name,bname):
        self.frn=frn
        self.name=name
        self.bname=bname
        # self.inName=inName

    def display(self):
        print(f"FRN={self.frn}\tName={self.name}\tbName={self.bname}\tinName={self.inName}")
    
s1=Student(10,"Vedika","july")
s3=Student(15,"Amisha","april")
s2=Student(11,"Kartik","june")
s1.display()
s2.display()
s3.display()
# print(s1.inName)  #by using object name   (This wrong way)
# print(s1.inName)
print(Student.inName)   #by using class name   (This right way)
Student.inName="FirstBitSolution"     #This is wrong way
s2.display()