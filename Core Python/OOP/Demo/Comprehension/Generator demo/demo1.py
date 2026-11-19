# def genNo():
#     yield(10)

# d=genNo()
# print(next(d))     #get the value from generator



# def genNo():
#     yield(20)
#     print("stop1")
#     yield(40)
#     print("stop2")
#     yield(50)
#     print("stop3")

# d=genNo()
# print(next(d))
# print(next(d))
# print(next(d))
# print(next(d))



def genNo():
    for i in range(1,100,10):
        yield(i)
d=genNo()
print(next(d))
print(next(d))
print(next(d))
print(next(d))