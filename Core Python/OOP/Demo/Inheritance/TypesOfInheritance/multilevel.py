class Emp:
    def __init__(self):
        print("Employee con")

class Scalcemanager(Emp):
    def __init__(self):
        super().__init__()
        print("I am in ScalceManager cont")

class AreaSM(Scalcemanager):
    def __init__(self):
        super().__init__()
        print("Area Scalce Manager")
a=AreaSM()