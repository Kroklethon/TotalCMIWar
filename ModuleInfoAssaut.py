from ModuleInfo import Info
import random


class InfoAssaut(Info):
    def __init__(self, nom="Snowden", pv=105, pa=10, pd=10):
        super(InfoAssaut, self).__init__(nom=nom, pv=pv, pa=pa)
        self.pd = pd
        self.modeAttaque[13] = ["Autodestruction", self.autodestruction]
        self.modeAttaque[14] = ["Jeu du dé", self.jeudude]
    def autodestruction(self, ennemi):
        if self.PV <= 40:
            ennemi.blesse(self.PV)
            self.blesse(self.PV)

    def jeudude(self, ennemi):
        n = random.randint(1, 6)  # nombre aléatoire entre 1 et 6#
        if n >= 3:
            ennemi.blesse(self.PA+2*n)

    def information(self):
        return super().information() + " <Assaut>"
