from ModulePersonne import Personne

class Math(Personne):
    def __init__(self,nom="Gauss le boss",pv=90,pa=10,qi=150):
        super(Math, self).__init__(nom=nom, pv=pv, pa=pa)
        self.qi = qi
    def information(self):
        return super().information() + " le matheu qi=" + str(self.qi)


if __name__ == "__main__":
    persos = []
    for i in range(10):
        if i%2 == 0:
            persos.append(Personne("Perso num " + str(i)))
        else:
            persos.append(Math("Math num " + str(i), pv=12+i, qi=120 + i*10))

    for p in persos:
        print(p.information())
