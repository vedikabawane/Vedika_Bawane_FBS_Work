# Write a program to prompt user to enter userid and password. If Id and  
# password is incorrect give him chance to re-enter the credentials. Let him try 3  
# times. After that program to terminate.


for i in range(1,4):
    user_id=input('Enter userid:')
    password=input('Enter password:')

    if(user_id=='vedika' and password=='123'):
        print('Login Successful')
        break
    else:
        print('Invalid userid or password')

else:
    print('Account blocked')

