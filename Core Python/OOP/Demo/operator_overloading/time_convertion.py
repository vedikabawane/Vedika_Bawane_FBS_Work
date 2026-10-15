# def add(a,b):
#     print(a+b)
# add(10,20)

# def add(a,b):
#     print(a+b)
# add('virat','rohit')

# a=[10,20,30,40]
# b=[30,40,60,80,90]
# print(a+b)

class Time:
    def __init__(self,hr,min,sec):
        self.hr=hr
        self.min=min
        self.sec=sec
    def __str__(self):
        return f'{self.hr}:{self.min}:{self.sec}'
    def __add__(self,other):
        tsec=self.sec+other.sec
        emin=tsec//60
        tsec=tsec%60
        tmin=self.min+other.min+emin
        ehr=tmin//60
        tmin=tmin%60
        thr=self.hr+other.hr+ehr
        return Time(thr,tmin,tsec)


t1=Time(12,33,55)
t2=Time(8,30,56)
a1=t1+t2
print(a1)

    
