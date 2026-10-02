class Employee:
    def __init__(self):
        print("I am in Con of Employee",id(self))
    def display(self):
        print("I am from Display of Employee")

e1=Employee()
e2=Employee()
print(f"id e1={id(e1)}")
print(f"id e1={id(e2)}")