from ModuleMath import Math
from random import*


class MathSoigneur(Math):
    def __init__(self, nom="Newton", pv=85, pa=8, pd=8):
        super(MathSoigneur, self).__init__(nom=nom, pv=pv, pa=pa)
        self.pd = pd
        self.modeAttaque[7] = ["Soins legers", self.soinslegers]
        self.modeAttaque[8] = ["Super Soins ", self.supersoins]

    def soinslegers(self, allie):
        if super().peutattaquer(allie):
            allie.PV = allie.PV+7

    def supersoins(self, allie):  # ne soigne que lui#
        if allie.PV <= 45:
            allie.PV = allie.PV+25

    def information(self):
        return super().information() + " <Soigneur>"
