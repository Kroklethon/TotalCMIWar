from ModulePersonne import Personne

class Info(Personne):
    def __init__(self,nom="Mark Zuckerberg",pv=110,pa=8,programmation=135):
        super(Info, self).__init__(nom=nom, pv=pv, pa=pa)
        self.programmation = programmation
    def information(self):
        return super().information() + "programmation =" + str(self.programmation)

if __name__ == "__main__":
    persos = []
    for i in range(10):
        if i%2 == 0:
            persos.append(Personne("Perso num " + str(i)))
        else:
            persos.append(Info("Info " + str(i), pv=12+i, programmation=120 + i+5))

    for p in persos:
        print(p.information())
