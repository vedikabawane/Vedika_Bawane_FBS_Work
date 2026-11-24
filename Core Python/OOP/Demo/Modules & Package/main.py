# from module1 import greet    # file yekhach folder mdhe asel tr
# greet('Vedu')


# #1. Direct import
# import MyPackage.module1
# import MyPackage.module2
# MyPackage.module1.greet('Vedika','Wellcome')
# MyPackage.module2.add(12,2)


# # 2.From packagename.modulename import memeber
# from MyPackage.module1 import greet
# greet('Vedu','Wellcome')


# # 3.from packagename.modulename import memeber
# from MyPackage.module2 import add,data
# add(12,3)
# print(data)

# # 3.from packagename.modulename import all
# from MyPackage.module2 import *
# add(12,3)
# print(data)


# # 4.Alice Name
# import MyPackage.module1 as m1
# m1.greet('Vedika','Wellcome')
# import MyPackage.module2 as m2
# m2.add(9,3)
# print(m2.data)