# #1.direct import
# import demo     
# demo.add(12,4)  #using function
# print(demo.a)   #using variable
# demo.sub(12,4)  #using function

# # 2.from module name import member
# from demo import sub
# from demo import add
# from demo import a
# sub(12,9)
# add(2,3)
# print(a)


# # 3.from module name import members
# from demo import add,sub ,a
# add(2,3)
# print(a)

# # 4.from module name import all
# from demo import *
# add(2,3)

# 5.Alice name
import demo as d
print(d.a)