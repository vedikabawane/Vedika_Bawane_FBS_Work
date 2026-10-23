# 1.Create a class Student with following
# a. data members:
# i. StudentId
# ii. Name
# iii. Age
# iv. Percentage
# b. Add the following methods:
# i. Parameterized constructor
# ii. Accept
# iii. Display
# iv. Method CalculateRank
# v. Override str Method

class Student:
    # Parameterized constructor
    def __init__(self, StudentId, Name, Age, Percentage):
        self.StudentId = StudentId
        self.Name = Name
        self.Age = Age
        self.Percentage = Percentage

    # Accept method to take input from user
    def Accept(self):
        self.StudentId = int(input("Enter Student ID: "))
        self.Name = input("Enter Student Name: ")
        self.Age = int(input("Enter Age: "))
        self.Percentage = float(input("Enter Percentage: "))

    # Display method
    def Display(self):
        print("Student ID     :", self.StudentId)
        print("Student Name   :", self.Name)
        print("Age           :", self.Age)
        print("Percentage    :", self.Percentage)

    # CalculateRank method
    def CalculateRank(self):
        if self.Percentage >= 75:
            return "Distinction"
        elif self.Percentage >= 60:
            return "First Class"
        elif self.Percentage >= 50:
            return "Second Class"
        elif self.Percentage >= 40:
            return "Pass"
        else:
            return "Fail"

    # Override __str__ method
    def __str__(self):
        return (
            f"Student ID: {self.StudentId}, "
            f"Name: {self.Name}, "
            f"Age: {self.Age}, "
            f"Percentage: {self.Percentage}, "
            f"Rank: {self.CalculateRank()}"
        )


# Using parameterized constructor
s1 = Student(101, "Amit", 18, 85)
print("Using constructor:")
s1.Display()
print("Rank:", s1.CalculateRank())
print(str(s1))

print()

# Using Accept method
s2 = Student(0, "", 0, 0)
s2.Accept()
print("\nUsing Accept method:")
s2.Display()
print("Rank:", s2.CalculateRank())
print(str(s2))