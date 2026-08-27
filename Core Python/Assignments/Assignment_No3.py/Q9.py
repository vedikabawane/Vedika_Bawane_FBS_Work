# Input 5 subject marks from user and display grade(eg.First class,Second class ..)

S1=int(input('Enter the subject1 marks:'))
S2=int(input('Enter the subject2 marks:'))
S3=int(input('Enter the subject3 marks:'))
S4=int(input('Enter the subject4 marks:'))
S5=int(input('Enter the subject5 marks:'))

Total=S1+S2+S3+S4+S5
percentage=Total*100/500

if(percentage>=75):
    print('Distinction class')
elif(percentage>=60):
    print('First class')
elif(percentage>=50):
    print('Second class')
elif(percentage>=35):
    print('Pass class')
else:
    print('Fail')