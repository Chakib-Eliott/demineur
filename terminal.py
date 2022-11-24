"""
Name : Demineur
Authors : Chakib & Eliott
"""

from demineur import Demineur

print("Bienvenue dans le Demineur !")
depart = input("Veuillez entrer les coordonnées du point de départ (x y) : ")
coord = (int(depart[0])-1,int(depart[2])-1)
mines = int(input("Combien de mine voulez vous ? (il faut au moins 1 mine et moins de 15% du plateau soit 81 cases) "))
j = Demineur(coord,mines)
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
print()
j.admin_afficher()