class Player:
    def __init__(self, name, jrno):
        self.name = name
        self.jrno = jrno
    def display(self):
            print(f'Name = {self.name}\tJr_no = {self.jrno}')
            
        
class CricketPlayer(Player):
    def __init__(self, name, jrno, runs):
        super().__init__(name, jrno)
        self.runs = runs

    def display(self):
            print(f'Runs = {self.runs}')
            super().display()
            
        
        # print(f'Name = {self.name}\tJr_no = {self.jrno}')



class KabbaddiPlayer(Player):
    def __init__(self, name, jrno, raidPoint):
        super().__init__(name, jrno)
        self.raidPoint = raidPoint
        
    def display(self):
        print(f'RaidPoint = {self.raidPoint}')
        super().display()
        
p1 = Player('Amisha', 3)
c1 = CricketPlayer('Gauri', 14, 999)
k1 = KabbaddiPlayer('Sanvi', 9, 11)
# p1.display()
c1.display()