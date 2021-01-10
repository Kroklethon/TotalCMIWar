from ModuleInfo import Info
import random


class InfoSoigneur(Info):
    def __init__(self, nom="Jean Reno", pv=95, pa=8, pd=8):
        super(InfoSoigneur, self).__init__(nom=nom, pv=pv, pa=pa)
        self.pd = pd
        self.modeAttaque[15] = ["Cauterisation", self.cauterisation]
        self.modeAttaque[16] = ["Manipulation", self.manipulation]
    def cauterisation(self, allie):
        allie.PV = allie.PV+15

    def manipulation(self, ennemi):
        # l'ennemi se blesse de ses propres points d'attaques(utilecar le soigneur fait peu de dégats)
        ennemi.blesse(ennemi.PA)

    def information(self):
        return super().information() + " <Soigneur>"
