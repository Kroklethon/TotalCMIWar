from ModuleMath import Math
from random import *


class MathAssaut(Math):
    def __init__(self, nom="Rieman", pv=95, pa=10, pd=10):
        super(MathAssaut, self).__init__(nom=nom, pv=pv, pa=pa)
        self.pd = pd
        self.modeAttaque[5] = ["Elimination confirmée", self.eliminationconfirmer]
        self.modeAttaque[6] = ["Echanger ", self.echanger]

    def eliminationconfirmer(self, ennemi):  # grosse frappe
        if super().peutattaquer(ennemi):
            n = random()
            if n < 0.75:
                ennemi.blesse(2*self.PA)
                print("Touché")
                if ennemi.PV == 0:
                    self.PV = self.PV+3  # Tuer c'est bon pour la santé
                    print("Elimination confirmé")

    def echanger(self, ennemi):  # echange de bons procédés
        if ennemi.PA >= 6:
            ennemi.PA = ennemi.PA-1
            self.PV = self.PV+5

    def information(self):
        return super().information() + " <Assaut>"
