from ModulePersonne import Personne
from random import*


class Info(Personne):
    def __init__(self, nom="Mark Zuckerberg", pv=110, pa=8, programmation=135):
        super(Info, self).__init__(nom=nom, pv=pv, pa=pa)
        self.programmation = programmation
        self.modeAttaque[3] = ["Azerty", self.azerty]
        self.modeAttaque[4] = ["Coup de clavier", self.coupdeclavier]

    def information(self):
        return super().information() + "programmation =" + str(self.programmation)

    def azerty(self, ennemi):  # virus informatique qui ne touche pas tt le temps#
        n = random()
        if super().peutattaquer(ennemi):
            if n <= (1/2):
                ennemi.blesse((1/2)*self.programmation)
                print("Good shot")
            elif (1/2) < n <= 0.75:
                ennemi.blesse(self.programmation)
                print("Amazing shot")
            else:
                print("Try again")

    def coupdeclavier(self, ennemi):
        if super().peutattaquer(ennemi):
            ennemi.blesse(self.PA+6)
            self.blesse(3)  # contrecoup (le clavier s'est cassé)#
            print("Aie ça fait mal")


if __name__ == "__main__":
    persos = []
    for i in range(10):
        if i % 2 == 0:
            persos.append(Personne("Perso num " + str(i)))
        else:
            persos.append(Info("Info " + str(i), pv=12 +
                               i, programmation=120 + i+5))

    for p in persos:
        print(p.information())
