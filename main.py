                                                            #####################################
#                                                                      Puissance 4 - NSI
#                                                               (Edgard.P, Jeremy.M, Mathis.R)
                                                            #####################################

import sys
sys.path.append('functions/')
import main_fn as m

"""
Main du programme, on execute les fonctions
- on alterne entre le joueur 1 et le joueur 2 en entrant / sortant dans des boucles while True
- on entre a l'instruction "while True:" et on sort au "break"
- avant d'entrer dans une des boucles on vérifie que la partie n'est pas gagner par un joueur ou nulle
"""

g = m.grille_vide(6,7) # on définit notre grille sur du 6 (lignes) par 7 (colonnes)

# ésthétique
print("Bienvenue au jeu de Puissance 4 :")
print("Voici le tableau")
m.affiche(g)

hasWon = False # on initialise une variable a gagner a faux
# point de départ

# pour le joueur 1:
while not hasWon and not m.partie_nulle(g): # (pendant que) - on verifie que personne a gagner la partie et que la partie n'est pas nulle
    while True: # crée une "boucle" qui nous permet de ne pas avoir a arreter le programme si une erreur survient, mais de recommencer a un point donner
        try: # permet de gerer si une erreur survient (voir except)
            choix_j1 = int(input("Vous etes le 1er joueur, dans quelle colone voulez-vous jouer ? ")) - 1
            if m.coup_possible(choix_j1,g): #on verifie si il est possible de jouer dans la colonne désignée
                m.jouer(g, "X", choix_j1) #si oui, on joue
            else:
                print("Cette colonne est pleine, merci de jouer dans une autre colonne") #si non, on demande au joueur de saisir une autre colonne
                continue # on recommence au point donner (while True 1)

            # On vérifie si le joueur 1 a gagner
            for c in range(7):
                for l in range(6): # avec les deux for inrange() on vérifie pour chaque valeur du tableau si la condition est vérifier
                    if m.vict(g,"X",l,c): # si la le jeu détecte que 4 pions du joueur 1 sont aligné quelque part sur la grille
                        print("Le joueur 1 a gagné bravo !")
                        hasWon = True # on met "a gagner" a vrai pour que le programme s'arrete
                        break # on sort de la boucle while True 1
            break # on sort de la boucle while True 1
        except: # si une erreur survient suite a une mauvaise valeur entrée
            print("Merci d'entrer une valeur entre 1 et 7 !")
            continue # on recommence au point donner (while True)

# pour le joueur 2:
    if hasWon == False: # on vérifie que personne n'as deja gagner la partie
        while True:# crée une "boucle" qui nous permet de ne pas avoir a arreter le programme si une erreur survient, mais de recommencer a un point donner
            try: # permet de gerer si une erreur survient (voir except)
                choix_j2 = int(input("Vous etes le 2nd joueur, dans quelle colone voulez-vous jouer ? ")) - 1
                if m.coup_possible(choix_j2,g): #on verifie si il est possible de jouer dans la colonne désignée
                    m.jouer(g, "O", choix_j2) #si oui, on joue
                else:
                    print("Cette colonne est pleine, merci de jouer dans une autre colonne") #si non, on demande au joueur de saisir une autre colonne
                    continue # on recommence au point donner (while True 2)

                # On vérifie si le joueur 2 a gagner
                for c in range(7):
                    for l in range(6): # avec les deux for inrange() on vérifie pour chaque valeur du tableau si la condition est vérifier
                        if m.vict(g,"O",l,c):  # si la le jeu détecte que 4 pions du joueur 2 sont aligné quelque part sur la grille
                            print("Le joueur 2 a gagné bravo !")
                            hasWon = True # on met "a gagner" a vrai pour que le programme s'arrete
                            break # on sortde la boucle while True 2
                break # on sort de la boucle while True 2
            except: # si une erreur survient suite a une mauvaise valeur entrée
                print("Merci d'entrer une valeur entre 1 et 7 !")
                continue # on recommence au point donner (while True)

