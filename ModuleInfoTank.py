from ModuleInfo import Info
from random import*


class InfoTank(Info):
    def __init__(self, nom="Jeff Bezos", pv=125, pa=15, pd=5):
        super(InfoTank, self).__init__(nom=nom, pv=pv, pa=pa)
        self.pd = pd
        self.modeAttaque[19] = ["Berserk", self.azerty]
        self.modeAttaque[20] = ["Boulet de canon", self.bouletdecanon]
    def berserk(self, ennemi):  # ne s'arrete pas tant que lui ou la cible n'est pas morte
        if super().peutattaquer(ennemi):
            if self.PV <= 30:
                while (self.en_vie == True) and (ennemi.en_vie == True):
                    ennemi.blesse(self.PA)
                    self.blesse(5)

    def bouletdecanon(self, ennemi):
        n = random()
        if n <= 0.15:
            ennemi.blesse(4*self.PA)

    def information(self):
        return super().information() + " <Tank>"
