from hr import Hr
from developer import Devloper
class  Empmanage:
    empDetil={}
    def addEmp(self):
        emp=None
        eid=int(input("Enter the Id of Emp= "))
        if eid in Empmanage.empDetil:
            print("Employee with this id is Allredy Exist ")
        else:
            ename=input("enter the Name= ")
            sal=float(input("enter the Sal= "))
            print("1.HR \n2.Devloper")
            chio=int(input("enter the Choice= "))
            if chio==1:
                com=float(input("Enter the Com of Hr "))
                emp=Hr(eid,ename,sal,com)
            elif chio==2:
                bonus=float(input("Enter the Bonus of Dev  "))
                emp=Devloper(eid,ename,sal,bonus)
            else:
                print("Inavalid choice")
                return
            Empmanage.empDetil[eid]=emp
    def displayEmp(self):
        for i,j in Empmanage.empDetil.items():
            print(f"{i} :{j}")
    def updateEmp(self):
        eid = int(input('Enter the Id of Emp = '))
        if eid not in Empmanage.empDetil:
            print('Employee with this id is not exist')
        else:
            emp = Empmanage.empDetil[eid]
            ch = int(input('1. For Name  2. For Sal'))
            if ch == 1:
                name = input('Enter the Updated name of Emp')
                emp.setName(name)
            elif ch == 2:
                sal = float(input('Enter the number'))
                emp.setSal(sal)
            print('Emp Name updated Successfully............')
    def searchEmp(self):
        eid = int(input('Enter the Id of Emp = '))
        if eid in Empmanage.empDetil:
            print(f'Your Employee Details = {Empmanage.empDetil[eid]}')
        else:
            print('Employee not exists...........')
    def delEmp(self):
        eid = int(input('Enter the Id of Emp = '))
        if eid in Empmanage.empDetil:
            print(f'Employee with {eid} is Deleted Successfully.....')
            del Empmanage.empDetil[eid]
        else:
            print('Employee with this id is not found')