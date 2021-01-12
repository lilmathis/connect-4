"""
Fonctions de création et d'affichage de la grille:
grille_vide() / affiche ()
"""

def grille_vide(l,c): #définis une grille (liste bi-dimensionelle ) sur c par l de longeur
    g = [["." for j in range(c)] for i in range(l)] #on crée et remplis cette liste par des 0
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
        if g[5][c]==".":
            return True

def jouer(g,j,c): #place le jouer "j" dans la case libre (si une case est libre) dans la colonne "c" de la grille "g"
    n = 0
    while g[n][c] != ".": #pour chaque case de la colonne occupée par un pion on va incrimentée notre compteur de 1
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
    for c in range(7):
        if g[5][c] != ".": # on regarde si dans la ligne 5 (derniere ligne) un pion est présent
            n += 1 # si oui, on incrimente le compteur de 1
    if n == 7: # si le compteur atteint 6, toutes les cases sont remplies donc la partie est nulle
        print("Partie nulle, personne gagne :(")
        return True
    else:
        return False