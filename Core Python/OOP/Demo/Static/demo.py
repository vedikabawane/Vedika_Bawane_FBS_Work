class Student:
    def __init__(self,frn,name,bname,inName):
        self.frn=frn
        self.name=name
        self.bname=bname
        self.inName=inName

    def display(self):
        print(f"FRN={self.frn}\tName={self.name}\tbName={self.bname}\tinName={self.inName}")
    
s1=Student(10,"Vedika","july","FBS")
s3=Student(15,"Amisha","april","FBS")
s2=Student(11,"Kartik","june","FBS")
s1.display()
s2.display()
s3.display()