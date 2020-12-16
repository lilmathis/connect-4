                                                            #####################################
#                                                                      Puissance 4 - NSI
#                                                               (Edgard.P, Jeremy.M, Mathis.R)
                                                            #####################################

"""
Fonctions de création et d'affichage de la grille:
grille_vide() / affiche ()
"""

def grille_vide(l,c): #définis une grille (liste bi-dimensionelle ) sur c par l de longeur
    g = [[0 for j in range(c)] for i in range(l)] #on crée et remplis cette liste par des 0
    return g

def affiche(g): #affiche le tableau (=grille) g ligne par ligne et inversement de celui-ci
    print()
    for l in range(6): #nombre de lignes
        for c in range(7): #nombre de colonnes
            print(g[5-l][c], end=" | ") #inversement des lignes avec le 5-l puis mise en forme
        print(" ")
    print()

"""
Fonctions rendant le jeux possible:
coup_possible() / jouer()
"""

def coup_possible(c, g): #Renvoie "True" si dans la 5 eme (et derniere) ligne de la colonne c il y a un 0 => on peuc jouer
        if g[5][c]==0:
            return True

def jouer(g,j,c): #place le jouer "j" dans la case libre (si une case est libre) dans la colonne "c" de la grille "g"
    n = 0
    while g[n][c] != 0: #pour chaque case de la colonne occupée par un pion on va incrimentée notre compteur de 1
        n += 1
    g[n][c] = j # on affecte le pion du joueur "j" dans la colonne "c" (chosit au préalable) et a la ligne n (premiere ligne disponisble)
    return affiche(g) #on affiche la grille

"""
Fonctions verifiant si 4 pions identique sont a cotés:
-horizontalement (vers la droite)
-verticalement (vers le haut)
-diagonale SE à NO
-diagonale SO à NE
"""

def horiz(g,j,l,c):
    n = 0
    for i in range(4):
        if l <= 5 and c <= 6: #On met une condition pour verifier qu'on aura pas de depacements d'index
            if g[l][c] == j: #On vérifie si la case choisit comporte bien un joueur j
                c += 1 # on passe a la colonne de droite
                n += 1 #on incrimente le compteur
    if n == 4:
        return True #si 4 pions du meme joueur sont a cotés on renvoie True

def vert(g,j,l,c):
    n = 0
    for i in range(4):
        if l <= 5 and c <= 6: #On met une condition pour verifier qu'on aura pas de depacements d'index
            if g[l][c] == j: #On vérifie si la case choisit comporte bien un joueur j
                l += 1 #on passe a la ligne du dessus
                n += 1 #on incrimente le compteur
    if n == 4: #si 4 pions du meme joueur sont a cotés on renvoie True
        return True

def diagonale_SE_NO(g,j,l,c):
    n = 0
    for i in range(4):
        if l <= 5 and c <= 6: #On met une condition pour verifier qu'on aura pas de depacements d'index
            if g[l][c] == j: #On vérifie si la case choisit comporte bien un joueur j
                l += 1 # on passe a la ligne du dessus
                c -= 1 # on passe a la colonne de gauche
                n += 1 #on incrimente le compteur
    if n == 4:
        return True #si 4 pions du meme joueur sont a cotés on renvoie True

def diagonale_SO_NE(g,j,l,c):
    n = 0
    for i in range(4):
        if l <= 5 and c <= 6: #On met une condition pour verifier qu'on aura pas de depacements d'index
            if g[l][c] == j: #On vérifie si la case choisit comporte bien un joueur j
                l += 1 # on passe a la ligne du dessus
                c += 1 # on passe a la colonne de droite
                n += 1 #on incrimente le compteur
    if n == 4:
        return True #si 4 pions du meme joueur sont a cotés on renvoie True

"""
Fonctions vérifiant la fin de la parite
vict() / partie_nulle()
"""

def vict(g,j,l,c):
    if l <= 5 and c <= 6: #On met une condition pour verifier qu'on aura pas de depacements d'index
        if g[l][c] == j: #On vérifie si la case choisit comporte bien un joueur j

            #on vérifie si 4 pions sont alignés dans une des 4 directions possible
            if horiz(g,j,l,c) is True:
                return True
            elif vert(g,j,l,c) is True:
                return True
            elif diagonale_SE_NO(g,j,l,c) is True:
                return True
            elif diagonale_SO_NE(g,j,l,c) is True:
                return True

def partie_nulle(g):
    n = 0
    for c in range(6):
        if g[5][c] != 0: # on regarde si dans la ligne 5 (derniere ligne) un pion est présent
            n += 1 # si oui, on incrimente le compteur de 1
    if n == 6: # si le compteur atteint 6, toutes les cases sont remplies donc la partie est nulle
        print("Partie nulle, personne gagne :(")
        return True
    else:
        return False

"""
Main du programme, on execute les fonctions
- on alterne entre le joueur 1 et le joueur 2 en entrant / sortant dans des boucles while True
- on entre a l'instruction "while True:" et on sort au "break"
- avant d'entrer dans une des boucles on vérifie que la partie n'est pas gagner par un joueur ou nulle
"""

g = grille_vide(6,7) # on définit notre grille sur du 6 (lignes) par 7 (colonnes)

# ésthétique
print("Bienvenue au jeu de Puissance 4 :")
print("Voici le tableau")
affiche(g)

hasWon = False # on initialise une variable a gagner a faux
# point de départ

# pour le joueur 1:
while not hasWon and not partie_nulle(g): # (pendant que) - on verifie que personne a gagner la partie et que la partie n'est pas nulle
    while True: # crée une "boucle" qui nous permet de ne pas avoir a arreter le programme si une erreur survient, mais de recommencer a un point donner
        try: # permet de gerer si une erreur survient (voir except)
            choix_j1 = int(input("Vous etes le 1er joueur, dans quelle colone voulez-vous jouer ? "))
            if coup_possible(choix_j1,g): #on verifie si il est possible de jouer dans la colonne désignée
                jouer(g, 1, choix_j1) #si oui, on joue
            else:
                print("Cette colonne est pleine, merci de jouer dans une autre colonne") #si non, on demande au joueur de saisir une autre colonne
                continue # on recommence au point donner (while True 1)

            # On vérifie si le joueur 1 a gagner
            for c in range(7):
                for l in range(6): # avec les deux for inrange() on vérifie pour chaque valeur du tableau si la condition est vérifier
                    if vict(g,1,l,c): # si la le jeu détecte que 4 pions du joueur 1 sont aligné quelque part sur la grille
                        print("Le joueur 1 a gagné bravo !")
                        hasWon = True # on met "a gagner" a vrai pour que le programme s'arrete
                        break # on sort de la boucle while True 1
            break # on sort de la boucle while True 1
        except: # si une erreur survient suite a une mauvaise valeur entrée
            print("Merci d'entrer une valeur entre 0 et 6 !")
            continue # on recommence au point donner (while True)

# pour le joueur 2:
    if hasWon == False: # on vérifie que personne n'as deja gagner la partie
        while True:# crée une "boucle" qui nous permet de ne pas avoir a arreter le programme si une erreur survient, mais de recommencer a un point donner
            try: # permet de gerer si une erreur survient (voir except)
                choix_j2 = int(input("Vous etes le 2nd joueur, dans quelle colone voulez-vous jouer ? "))
                if coup_possible(choix_j2,g): #on verifie si il est possible de jouer dans la colonne désignée
                    jouer(g, 2, choix_j2) #si oui, on joue
                else:
                    print("Cette colonne est pleine, merci de jouer dans une autre colonne") #si non, on demande au joueur de saisir une autre colonne
                    continue # on recommence au point donner (while True 2)

                # On vérifie si le joueur 2 a gagner
                for c in range(7):
                    for l in range(6): # avec les deux for inrange() on vérifie pour chaque valeur du tableau si la condition est vérifier
                        if vict(g,2,l,c):  # si la le jeu détecte que 4 pions du joueur 2 sont aligné quelque part sur la grille
                            print("Le joueur 2 a gagné bravo !")
                            hasWon = True # on met "a gagner" a vrai pour que le programme s'arrete
                            break # on sortde la boucle while True 2
                break # on sort de la boucle while True 2
            except: # si une erreur survient suite a une mauvaise valeur entrée
                print("Merci d'entrer une valeur entre 0 et 6 !")
                continue # on recommence au point donner (while True)
