# Q2. Create a derived class from Student as EnggStudent with:
# a. Data members:
# i. Branch
# ii. InternalMarks

# b. Add the following methods:
# i. Parameterized constructor
# ii. Accept
# iii. Display
# iv. Override Method CalculateRank
# v. Override str Method

class Student:
    def __init__(self, StudentId, Name, Age, Percentage):
        self.StudentId = StudentId
        self.Name = Name
        self.Age = Age
        self.Percentage = Percentage

    def Accept(self):
        self.StudentId = int(input("Enter Student ID: "))
        self.Name = input("Enter Name: ")
        self.Age = int(input("Enter Age: "))
        self.Percentage = float(input("Enter Percentage: "))

    def Display(self):
        print("Student ID   :", self.StudentId)
        print("Name        :", self.Name)
        print("Age         :", self.Age)
        print("Percentage  :", self.Percentage)

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

    def __str__(self):
        return (f"Student ID: {self.StudentId}, Name: {self.Name}, "
                f"Age: {self.Age}, Percentage: {self.Percentage}, "
                f"Rank: {self.CalculateRank()}")


class EnggStudent(Student):
    def __init__(self, StudentId, Name, Age, Percentage, Branch, InternalMarks):
        super().__init__(StudentId, Name, Age, Percentage)
        self.Branch = Branch
        self.InternalMarks = InternalMarks

    def Accept(self):
        super().Accept()
        self.Branch = input("Enter Branch: ")
        self.InternalMarks = float(input("Enter Internal Marks: "))

    def Display(self):
        super().Display()
        print("Branch        :", self.Branch)
        print("Internal Marks:", self.InternalMarks)

    def CalculateRank(self):
        if self.Percentage >= 75 and self.InternalMarks >= 70:
            return "Distinction"
        elif self.Percentage >= 60 and self.InternalMarks >= 60:
            return "First Class"
        elif self.Percentage >= 50 and self.InternalMarks >= 50:
            return "Second Class"
        elif self.Percentage >= 40 and self.InternalMarks >= 40:
            return "Pass"
        else:
            return "Fail"

    def __str__(self):
        return (f"Student ID: {self.StudentId}, Name: {self.Name}, "
                f"Age: {self.Age}, Percentage: {self.Percentage}, "
                f"Branch: {self.Branch}, Internal Marks: {self.InternalMarks}, "
                f"Rank: {self.CalculateRank()}")


# Using parameterized constructor
e1 = EnggStudent(101, "Rahul", 19, 82, "Computer Science", 88)
print("Using Parameterized Constructor:")
e1.Display()
print("Rank:", e1.CalculateRank())
print(str(e1))

print()

# Using Accept method
e2 = EnggStudent(0, "", 0, 0, "", 0)
e2.Accept()
print("\nUsing Accept Method:")
e2.Display()
print("Rank:", e2.CalculateRank())
print(str(e2))