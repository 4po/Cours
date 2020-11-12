import random
class Couleur :
    R : int
    V : int
    B : int

    image = "RVB"

    def __init__(self,rouge:int,vert:int,bleu:int):
        self.R,self.V,self.B = rouge,vert,bleu
    def __str__(self) :
        return "Rouge: " + str(self.R) + "\nVert: " + str(self.V) + "\nBleu: " + str(self.B) + "\n=============="
    @property
    def V(self):
        return self.__V
    @property
    def R(self):
        return self.__R
    @property
    def B(self):
        return self.__B
    @V.setter
    def V (self, composanteverte) :
        assert composanteverte >= 0 and composanteverte <= 255, "La valeur proposé pour le vert n'est pas correcte"
        self.__V = composanteverte
    @B.setter
    def B (self, composantebleu) :
        assert composantebleu  >= 0 and composantebleu <= 255, "La valeur proposé pour le bleu n'est pas correcte"
        self.__B = composantebleu
    @R.setter
    def R (self, composanterouge) :
        assert composanterouge  >= 0 and composanterouge <= 255, "La valeur proposé pour le rouge n'est pas correcte"
        self.__R = composanterouge

    def melange(self,e,melangeur) :
        self.R = int((self.R * (melangeur/100) + e.R * (1-melangeur/100)))
        self.V = int((self.V * (melangeur/100) + e.V * (1-melangeur/100)))
        self.B = int((self.B * (melangeur/100) + e.B * (1-melangeur/100)))

def color_random() :
    r = random.randint(0,255)
    v = random.randint(0,255)
    b = random.randint(0,255)
    sortie = Couleur(r, v, b)
    return sortie
UneCouleur = color_random()
DeuxCouleur = color_random()

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

    Endcolor = Couleur(int(x2),int(y2),int(z2))
    return Endcolor

print(DeuxCouleur)
print(UneCouleur)
UneCouleur.melange(DeuxCouleur,int(input("Par quelle % voulez vous mélangez les couleurs ? \n --> ")))
print(UneCouleur)
