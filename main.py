class Student:
    def __init__(self, name, startmoney=300, defrate=9):
        self.startmoney = startmoney
        self.defrate = defrate
        self.skoka_let = 10
        self.logs = [f'{name} started']
        self.name = name

    def rost(self):
        self.skoka_let+=1

    def magazin(self, vesh, cena):
        self.logs.append(f'купив {vesh} за {cena}')
        if cena < self.startmoney:
            self.startmoney-= cena
            self.logs.append(f'купив {vesh} за {cena}')
        else:
            self.logs.append(f'не купив {vesh} за {cena} (бiмж)')

    def live(self):
        self.skoka_let += 1
        self.logs.append(f'{self.name} {self.skoka_let}')
        if self.skoka_let > 50:
            self.magazin = exit
            self.rost = exit
            self.live = exit


s = Student('alex')
while True:
    try:    
        print(s.logs)
        s.rost()
        print(s.logs)
        s.magazin('гераен', 123123)
        print(s.logs)
        s.magazin('марозива', 49)
        print(s.logs)
        s.live()
        print(s.logs)
    except:
        break