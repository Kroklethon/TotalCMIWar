from ModuleGeosciences import Geosciences
from ModuleInfo import Info
from ModuleInfoAssaut import InfoAssaut
from ModuleInfoSoigneur import InfoSoigneur
from ModuleInfoSoutien import InfoSoutien
from ModuleInfoTank import InfoTank
from ModuleMath import Math
from ModuleMathAssaut import MathAssaut
from ModuleMathSoigneur import MathSoigneur
from ModuleMathSoutien import MathSoutien
from ModuleMathTank import MathTank


class joueur():
    def __init__(self):
        self.classe = []
        self.type = ""
        self.nb_perso_morts = 0

    def selectClasse(self, type):
        self.type = type
        if type == "info":
            self.classe = self.createClasse("info")
        if type == "maths":
            self.classe = self.createClasse("math")
        # if type == "bio":
        #     self.classe= self.createClasse("bio")

    def getClasse(self):
        return self.classe

    def getType(self):
        return self.type

    def createClasse(self, type):
        self.type = type
        print("createClasse")
        infos = ["Evan", "Flo", "RomRom", "Théo"]
        maths = ["Aurélien", "Simon", "Julien", "Léa"]
        # bio=["Robert","Mauricette","Ginette","Dudule"]
        if type == "info":
            print("info")
            self.classe.append(InfoAssaut(nom=infos[0]))
            self.classe.append(InfoSoigneur(nom=infos[1]))
            self.classe.append(InfoSoutien(nom=infos[2]))
            self.classe.append(InfoTank(nom=infos[3]))
            """
            for eleve in infos:
                self.classe.append(Info(nom=eleve))
            """
        if type == "math":
            print("math")
            self.classe.append(MathAssaut(nom=maths[0]))
            self.classe.append(MathSoigneur(nom=maths[1]))
            self.classe.append(MathSoutien(nom=maths[2]))
            self.classe.append(MathTank(nom=maths[3]))

            """
            for eleve in maths:
                self.classe.append(MathAssaut(nom=eleve))
            """
        # if type =="bio":
        # print("bio")
        # for eleve in maths:
        # self.classe.append(Geosciences(nom=eleve))
