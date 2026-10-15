def add(a,b):
    print(a+b)
add(10,20)

def add(a,b):
    print(a+b)
add('virat','rohit')

a=[10,20,30,40]
b=[30,40,60,80,90]
print(a+b)

class Time:
    def __init__(self, hr, min, sec):
        self.hr = hr
        self.min = min
        self.sec = sec
    def __str__(self):
        return f'{self.hr}:{self.min}:{self.sec}'
    def __add__(self, other):
        thr = self.hr + other.hr
        tmin = self.min + other.min
        tsec = self.sec + other.sec
        return Time(thr, tmin, tsec)
        # to = Time(thr, tmin, tsec)
        # return to

x = Time(1, 2, 3)
y = Time(3, 4, 5)
# add(Time[1, 2, 3], Time[3, 4, 5])
print(x+y)