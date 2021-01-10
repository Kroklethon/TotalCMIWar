from ModuleInfo import Info
from random import*


class InfoSoutien(Info):
    def __init__(self, nom="Bill Gate", pv=115, pa=12, pd=7):
        super(InfoSoutien, self).__init__(nom=nom, pv=pv, pa=pa)
        self.pd = pd
        self.modeAttaque[17] = ["Ravitaillement", self.ravitaillement]
        self.modeAttaque[18] = ["Piratge", self.piratage]
    def ravitaillement(self, allie):
        if allie.PA <= 15:
            allie.PA = allie.PA+1
        #if allie.pd <= 10:
        #    allie.pd = allie.pd+1

    def piratage(self, ennemi):
        if ennemi.PA >= 1:
            ennemi.PA = ennemi.PA-1
        #if ennemi.pd >= 1:
        #    ennemi.pd = ennemi.pd-1

    def information(self):
        return super().information() + " <Soutien>"
