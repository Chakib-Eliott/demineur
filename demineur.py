"""
Name : Demineur
Author : Eliott, Chakib
"""

from random import randint

class Demineur:
    
    def __init__(self,coord:tuple,nb_mines:int):
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
        self.nb_mines = nb_mines # Int
        self.nb_drapeau = nb_mines # Int
        self.not_fini = True # Bool
    
    def afficher(self):
        """
        Affiche la grille.
        
        ARGS :
            self
        """
        for ligne in self.grille_aff:
            for elt in ligne:
                print(elt, end='  ')
            print()
    
    def admin_afficher(self):
        """
        Affiche la grille des mines.

        ARGS :
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
        
        ARGS :
            self
            case (tuple) : coordonnées de la case
        RETURNS :
            voisin (dict) : Dictionnaire des voisins et de si ils ont une mine ou non
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
    
    def generation_mine(self):
        """
        Génère la grille des mines.

        ARGS :
            self
        """
        assert self.nb_mines < 81*0.15, "Pas plus de 15% des cases"
        assert self.nb_mines>0, "Que des entiers positifs"
        cpt = 0
        while cpt < self.nb_mines:
            ligne = randint(0,8)
            mine = randint(0,8)
            if self.grille_mine[ligne][mine] == 0 and self.grille_aff[ligne][mine] != '#':
                self.grille_mine[ligne][mine] = 1
                cpt += 1
    
    def count_mine(self):
        """
        Compte le nombre de mine à proximité de chaque case

        ARGS :
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

        ARGS :
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

        ARGS :
            self
            voisin (dict)
        """
        for elt in voisin.keys():
            if self.grille_aff[elt[0]][elt[1]] == '.':
                if self.grille_nb[elt[0]][elt[1]] == 0:
                    self.grille_aff[elt[0]][elt[1]] = '#'
                    self.decouvrir(self.voisin(elt))
                else:
                    self.grille_aff[elt[0]][elt[1]] = self.grille_nb[elt[0]][elt[1]]
    
    def add_drapeau(self,coord:tuple):
        """
        Place un drapeau à l'endroit indiqué.

        ARGS :
            self
            coord (tuple) : coordonné du drapeau
        """
        assert self.grille_aff[coord[0]][coord[1]] != "#", "La case est déjà découverte !"
        assert self.grille_aff[coord[0]][coord[1]] not in [1,2,3,4,5,6,7,8], "La case est déjà découverte !"
        assert self.grille_aff[coord[0]][coord[1]] != "@", "La case a déjà un drapeau !"
        assert self.nb_drapeau > 0, "Vous n'avez plus de drapeau disponible !"
        self.grille_aff[coord[0]][coord[1]] = "@"
        self.nb_drapeau -= 1

    def remove_drapeau(self,coord:tuple):
        """
        Retire un drapeau à l'endroit indiqué.

        ARGS :
            self
            coord (tuple) : coordonné du drapeau
        """
        assert self.grille_aff[coord[0]][coord[1]] == "@", "La case n'est pas un drapeau !"
        self.grille_aff[coord[0]][coord[1]] = "."
        self.nb_drapeau += 1

    def jouer(self,coord:tuple):
        """
        Découvre ou non les cases du joueur.

        ARGS :
            self
            coord (tuple) : coordonné de l'action
        """
        if self.grille_mine[coord[0]][coord[1]] == 1:
            self.grille_aff[coord[0]][coord[1]] = "!"
            self.not_fini = False
        elif self.grille_nb[coord[0]][coord[1]] == 0:
            self.grille_aff[coord[0]][coord[1]] = '#'
            voisin = self.voisin(coord)
            self.decouvrir(voisin)
        else:
            self.grille_aff[coord[0]][coord[1]] = self.grille_nb[coord[0]][coord[1]]
        return self.afficher()
    
    def verif_gagne(self):
        """
        Vérifie si la partie est gagné.

        ARGS :
            self

        RETURN :
            gagne (bool) : Booléen de si le joueur a gagné
        """
        gagne = True
        for i in range(len(self.grille_aff)):
            for j in range(len(self.grille_aff)):
                if self.grille_mine[i][j] == 0 and self.grille_aff[i][j] == ".":
                    gagne = False
        if gagne:
            self.not_fini = False
        return gagne


print("Bienvenue dans le Demineur !")
depart = input("Veuillez entrer les coordonnées du point de départ (x y) : ")
coord = (int(depart[0])-1,int(depart[2])-1)
mines = int(input("Combien de mine voulez vous ? (il faut au moins 1 mine et moins de 15% du plateau soit 81 cases) "))
j = Demineur(coord,mines)
j.generation_mine()
j.depart()
while j.not_fini:
    action = input("Quelle case voulez-vous découvrir ? (d suivit des coordonnées pour mettre un drapeau) ")
    if action[0] == "d":
        if j.grille_aff[int(action[2])-1][int(action[4])-1] != "@":
            j.add_drapeau((int(action[2])-1,int(action[4])-1))
        else:
            j.remove_drapeau((int(action[2])-1,int(action[4])-1))             
        j.afficher()
    elif j.grille_aff[int(action[0])-1][int(action[2])-1] in [1,2,3,4,5,6,7,8,"#"]:
        print("La case est déjà découverte !")
    elif j.grille_aff[int(action[0])-1][int(action[2])-1] == "@":
        print("La case est déjà un drapeau !")
    else:
        j.jouer((int(action[0])-1,int(action[2])-1))
        gagne = j.verif_gagne()
if gagne:
    print("Vous avez gagnez !")
else:
    print("Vous avez perdu !")
# print()
# j.admin_afficher()