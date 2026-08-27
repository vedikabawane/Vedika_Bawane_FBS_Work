gender=input('Enter gender(M/F:)')
age=int(input('Enter the age:'))

if(gender== 'F'):
    if(age>=18):
        print('girl is eligible for marriage.')
    else:
        print('girl is not eligible for marriage.')    
else:
    if(age>=21):
        print('boy is eligible for marriage.')
    else:
        print('boy is not eligible for marriage.')


