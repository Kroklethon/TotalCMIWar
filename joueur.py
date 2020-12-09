from ModuleGeosciences import Geosciences
from ModuleInfo import Info
from ModuleMath import Math

class joueur():
    def __init__(self):
        self.classe = []

    def selectClasse(self,type):
        if type == "info":
            self.classe = self.createClasse("info")
        if type == "maths":
            self.classe = self.createClasse("math")
        # if type == "geo":
        #     self.classe

    def getClasse(self):
        return self.classe

    def createClasse(self,type):
        print("createClasse")
        infos = ["Evan","Flo","RomRom","Théo"]
        maths = ["Aurélien","Simon","Julien","Léa"]
        if type == "info":
            print("info")
            for eleve in infos:
                self.classe.append(Info(nom=eleve))
        if type == "math":
            print("math")
            for eleve in maths:
                self.classe.append(Math(nom=eleve))
        

        