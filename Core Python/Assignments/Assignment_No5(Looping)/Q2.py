# Enter number of students from user. For those many students accept marks of 5  
# subject marks from user and calculate percentage. Display all percentage and  
# average percentage of students. 

n = int(input("Enter number of students: "))

total_percentage = 0

for i in range(1, n + 1):

    total_marks = 0

    print("Enter marks for Student", i)

    for j in range(1, 6):
        marks = int(input("Enter marks of subject: "))
        total_marks = total_marks + marks

    percentage = total_marks / 5

    print("Percentage of Student", i, "=", percentage)

    total_percentage = total_percentage + percentage

average = total_percentage / n

print("Average Percentage =", average)
