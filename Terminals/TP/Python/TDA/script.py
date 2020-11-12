class Couleur :
    R : int
    V : int
    B : int

    image = "RVB"

    def __init__(self,rouge:int,vert:int,bleu:int):
        self.R,self.V,self.B = rouge,vert,bleu
    def __str__(self) :
        return "Rouge:" + str(self.R) + " Vert:" + str(self.V) + " Bleu:" + str(self.B)
    @property
    def V(self):
        return self.__V
    def R(self):
        return self.__R
    def B(self):
        return self.__B
        
    def V (self, composanteverte) :
        assert composanteverte >= 0 and composanteverte <= 255, "La valeur proposé pour le vert n'est pas correcte"
        self.__V = composanteverte
UneCouleur = Couleur(255,0,0)
DeuxCouleur = Couleur(0,255,0)

def melanger(couleur1, couleur2, melangeur) :
    x = couleur1.R * (melangeur/100)
    x1 = couleur2.R * (melangeur/100)
    x2 = x + x1

    y = couleur1.V * (melangeur/100)
    y1 = couleur2.V * (melangeur/100)
    y2 = y + y1

    z = couleur1.B * (melangeur/100)
    z1 = couleur2.B * (melangeur/100)
    z2 = z + z1

    Endcolor = Couleur(x2,y2,z2)
    return Endcolor

print(UneCouleur.image)
print(UneCouleur)
print(melanger(UneCouleur,DeuxCouleur,60))
