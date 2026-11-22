# Step1:Understand that function is the object of function class
# def demo1():
#     print("I am in demo")
# a=10
# print(type(a))
# print(type(demo1))       # demo1 function class ka object hai


# # Step2:We can store a function in variable
# x=demo1 
# x() 


# # Step3:We can pass function parameter to another function
# def hi():
#     print("I am in Hii")

# def demo(a):
#     print('I am in demo')
#     a()
# # demo()
# demo(hi)  # function ko argument ke roop me pass kar rahe hai


# Step4:We can return function from inside the function
# def outerFun():
#     print("I am in outer function")
#     def innerFun():
#         print("I am in inner function")
#     return innerFun
# res=outerFun()
# print(res)


# Step5:Closure(Closure is a special type of function which pass everything as to its neighboring function or another function)
def demo(a=10):
    def innerfunction():
        print(a)
    return innerfunction
res=demo()
# print(res)
res()




# def decore(x):
#     print("I am in decorator function")
#     def innerFun():
#         print("Logeer Added")
#         print("Time Started")
#         x()
#         print("Time Stoped")
#         print("Logeer Removed")
#     return innerFun

# def login():
#     print("I am in login function")

# res=decore(login)
# res()

# def decore(x):
#     print("I am in decorator function")
#     def innerFun():
#         print("\nLogeer Added")
#         print("Time Started")
#         x()
#         print("Time Stoped")
#         print("Logeer Removed")
#     return innerFun

# @decore
# def login():
#     print("I am in login function")

# @decore
# def logout():
#     print("I am in logout function")

# # res=decore(login)
# # res()
# # res=decore(logout)
# # res()
# login()
# logout()

# universal decorator
def decore(x):
    print("I am in decorator function")
    def innerFun(*a):
        print("\nLogeer Added")
        print("Time Started")
        x(*a)
        print("Time Stoped")
        print("Logeer Removed")
    return innerFun

@decore
def sum(a,b):
    print(f"Addition={a+b}")

@decore
def login():
    print("I am in login function")

@decore
def logout():
    print("I am in logout function")

# res=decore(login)
# res()
# res=decore(logout)
# res()
login()
logout()
sum(12,3)