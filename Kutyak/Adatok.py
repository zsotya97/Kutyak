import datetime
class KutyaNevek(object):
    def __init__(self, sor):
        split = sor.split(';')
        self.id =int(split[0])
        self.kutya_nev =split[1]

class KutyaFajtak(object):
    def __init__(self, sor):
        split = sor.split(';')
        self.id =int(split[0])
        self.nev =split[1]
        self.eredeti_nev =split[1]

class Kutyak(object):
    def __init__(self, sor):
        split = sor.split(';')
        self.id =int(split[0])
        self.fajta_id =int(split[1])
        self.nev_id =int(split[2])
        self.eletkor =int(split[3])
        self.ellenorzes =datetime.datetime.strptime(split[4], "%Y.%m.%d")


class Statisztika(object):
    def __init__(self,nev, szam):
        self.nev=nev
        self.szam=szam
     
    

    


