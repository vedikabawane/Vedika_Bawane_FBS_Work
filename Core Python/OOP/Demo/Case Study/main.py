from emp_manage import Empmanage
class Main:
    @staticmethod
    def login():
        eid=input("Enter The USer Id= ")
        epass=input("Enter the password=  ")
        if eid=="admin" and epass=="1234":
            return True
        else :
            print("Inavalid Id Or PAssword")
    
    def view(self):
        em=Empmanage()
        while True:
            print("1. for Add Emp ")
            print("2. for Dispaly ")
            print("3.Update Emp")
            print("4.Search Emp")
            print("5.Delete Emp ")
            print("6 Exit.....")
            ch=int(input("Enter the Choice "))
            if ch==1:
                em.addEmp()
            elif ch==2:
                em.displayEmp()
            elif ch==3:
                em.updateEmp()
            elif ch==4:
                em.searchEmp()
            elif ch==5:
                em.delEmp()
            elif ch==6:
                print("Thank you GHari ja..")
                break
            else:
                print("Enter valid choice ")
m=Main()
if Main.login():
    m.view()