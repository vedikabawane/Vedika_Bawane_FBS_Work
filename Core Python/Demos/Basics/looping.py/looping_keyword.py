#1.pass:Neglect expected indentation error
# for i in range(1,10):
#     pass


#2.break:For terminating the loop
# for i in range(1,10):
#     if(i==4):
#         break
#     print(i)


#3.continue:To stop perticular iteration
# for i in range(1,10):
#     if(i==4):
#         continue   
#     print(i)


#4.else:Will execute when loop executed succesfully
# for i in range(1,10):
#     if(i==4):
#         break   
#     print(i)
# else:
#     print('else block executed')   

for i in range(1,10):
    if(i==4):
        continue   
    print(i)
else:
    print('else block executed')