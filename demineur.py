"""
Name : Demineur
Author : Eliott, Chakib
"""

"""
vide = 0
inconnu = .
mine = 1
drapeau = @
decouvert = int de mine autour
découvert = #
"""

"""
Libérer les cases proches avant de générer les mines
Afficher les mines proches
Bombe = Perdu
Signe drapeau
(Faire 3 difficulter)
Timeur
Quand il reste juste les mines gagner
"""

from random import randint

class Demineur:
    
    def __init__(self,coord:tuple):
        self.grille_mine = [
                            [0,0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0,0]
                            ] # Grille comportant toutes les mines
        self.grille_nb = [
                            [0,0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0,0]
                        ] # Grille comportant le nombre de mines à proximité
        self.grille_aff = [
                        ['.','.','.','.','.','.','.','.','.'],
                        ['.','.','.','.','.','.','.','.','.'],
                        ['.','.','.','.','.','.','.','.','.'],
                        ['.','.','.','.','.','.','.','.','.'],
                        ['.','.','.','.','.','.','.','.','.'],
                        ['.','.','.','.','.','.','.','.','.'],
                        ['.','.','.','.','.','.','.','.','.'],
                        ['.','.','.','.','.','.','.','.','.'],
                        ['.','.','.','.','.','.','.','.','.'],
                        ] # Grille d'affichage, celle que l'utilisateur voit
        self.coord = coord # Tuple
    
    def afficher(self):
        """
        Affiche la grille.
        
        PARAS :
            self
        """
        for ligne in self.grille_aff:
            for elt in ligne:
                print(elt, end='  ')
            print()
    
    def admin_afficher(self):
        """
        Affiche la grille des mines.

        PARAS :
            self
        """
        print("-"*25)
        print("Mode affichage administrateur")
        for ligne in self.grille_mine:
            for elt in ligne:
                print(elt, end='  ')
            print()
        print()
        for ligne in self.grille_nb:
            for elt in ligne:
                print(elt, end='  ')
            print()
        print("-"*25)

    def voisin(self,case:tuple):
        """
        Créer un dictionnaire des voisins (haut,bas,gauche,droite et les diagonales)
        d'une case en informant si ils contiennent une mineou non.
        
        PARAMS :
            self
            case : tuple (coordonnées de la case)
        RETURNS :
            voisin : dict (Dictionnaire des voisins et de si ils ont une mine ou non)
        """
        voisin = {}
        if case[0] != 0:
            voisin[(case[0]-1,case[1])] = self.grille_mine[case[0]-1][case[1]]#En haut
        if case[0] != len(self.grille_aff)-1:
            voisin[(case[0]+1,case[1])] = self.grille_mine[case[0]+1][case[1]]#En bas
        if case[1] != 0:
            voisin[(case[0],case[1]-1)] = self.grille_mine[case[0]][case[1]-1]#A gauche
        if case[1] != len(self.grille_aff)-1:
            voisin[(case[0],case[1]+1)] = self.grille_mine[case[0]][case[1]+1]#A droite
        if case[0] != len(self.grille_aff)-1 and case[1] != 0:
            voisin[(case[0]+1,case[1]-1)] = self.grille_mine[case[0]+1][case[1]-1]#Diagonale bas gauche
        if case[0] != len(self.grille_aff)-1 and case[1] != len(self.grille_aff)-1:
            voisin[(case[0]+1,case[1]+1)] = self.grille_mine[case[0]+1][case[1]+1]#Diagonale bas droite
        if case[0] != 0 and case[1] != 0:
            voisin[(case[0]-1,case[1]-1)] = self.grille_mine[case[0]-1][case[1]-1]#Diagonale haut gauche
        if case[0] != 0 and case[1] != len(self.grille_aff)-1:
            voisin[(case[0]-1,case[1]+1)] = self.grille_mine[case[0]-1][case[1]+1]#Diagonale haut droite
        return voisin
    
    def generation_mine(self,mines:int):
        """
        Génère la grille des mines.

        PARAMS :
            self
            mines : int (nombre de mines voulu)
        """
        assert mines < 81*0.15, "Pas plus de 15% des cases"
        assert mines>0, "Que des entiers positifs"
        cpt = 0
        while cpt < mines:
            ligne = randint(0,8)
            mine = randint(0,8)
            if self.grille_mine[ligne][mine] == 0 and self.grille_aff[ligne][mine] != '#':
                self.grille_mine[ligne][mine] = 1
                cpt += 1
    
    def count_mine(self):
        """
        Compte le nombre de mine à proximité de chaque case

        PARAMS :
            self
        """
        for i in range(len(self.grille_nb)):
            for j in range(len(self.grille_nb)):
                if self.grille_mine[i][j] == 0:
                    voisins = self.voisin((i,j))
                    self.grille_nb[i][j] = sum(voisins.values())
    
    def depart(self):
        """
        Découvre la base du jeu pour jouer.

        PARAMS :
            self
        RETURNS :
            grille (à partir de la fonction afficher)
        """
        self.count_mine()
        if self.grille_nb[self.coord[0]][self.coord[1]] == 0:
            self.grille_aff[self.coord[0]][self.coord[1]] = '#'
            voisin = self.voisin(self.coord)
            self.decouvrir(voisin)
        else:
            self.grille_aff[self.coord[0]][self.coord[1]] = self.grille_nb[self.coord[0]][self.coord[1]]
        return self.afficher()

    def decouvrir(self,voisin:dict):
        """
        Découvre les parties vides.

        PARAMS :
            self
            voisin : dict
        """
        for elt in voisin.keys():
            if self.grille_aff[elt[0]][elt[1]] == '.':
                if self.grille_nb[elt[0]][elt[1]] == 0:
                    self.grille_aff[elt[0]][elt[1]] = '#'
                    self.decouvrir(self.voisin(elt))
                else:
                    self.grille_aff[elt[0]][elt[1]] = self.grille_nb[elt[0]][elt[1]]

print("Bienvenue dans le Demineur !")
depart = input("Veuillez entrer les coordonnées du point de départ (x y) : ")
coord = (int(depart[0])-1,int(depart[2])-1)
j = Demineur(coord)
j.generation_mine(int(input("Combien de mine voulez vous ? (il faut au moins 1 mine et moins de 15% du plateau soit 81 cases) ")))
j.depart()
print()
j.admin_afficher()