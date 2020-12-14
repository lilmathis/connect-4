def grille_vide(l,c): #définis une grille ( liste bi-dimensionelle ) sur c par l de longeur
    g = [[0 for j in range(c)] for i in range(l)]
    g = ([i for i in g[::-1]]) #on inverse les listes (lignes)
    return g

def affiche(g): #affiche le tableau g ligne par ligne
    print(*g, sep='\n')
    print()

def coup_possible(c, g): #renvoie un booléen lorsque un élément dans c
    n=0
    for i in range(5):
        if g[i][c]==0:
            n += 1
    if n > 0:
        return True
    else:
        print("test")

def jouer(g,j,c): #place le jouer j dans la case libre (si une case est libre) dans la colonne c du tableau g
    if coup_possible(c, g):
        n = 5
        while g[n][c] != 0:
            n -= 1
        g[n][c] = j
        return partie_nulle(g)

def partie_nulle(g):
    l = 5
    for i in range(6):
        if g[l][i] == 0:
            return affiche(g)
        else:
            return True


## Déplacements ## -- Start

def horiz(g,j,l,c):
    n = 0
    for i in range(4):
        if l <= 5 and c <= 6:
            if g[l][c] == j:
                c += 1
                n += 1
    if n == 4:
        return True

def vert(g,j,l,c):
    n = 0
    for i in range(4):
        if l <= 5 and c <= 6:
            if g[l][c] == j:
                l -= 1
                n += 1
    if n == 4:
        return True

def diagonale_SE_NO(g,j,l,c):
    n = 0
    for i in range(4):
        if l <= 5 and c <= 6:
            if g[l][c] == j:
                l -= 1
                c -= 1
                n += 1
    if n == 4:
        return True

def diagonale_SO_NE(g,j,l,c):
    n = 0
    for i in range(4):
        if l <= 5 and c <= 6:
            if g[l][c] == j:
                l -= 1
                c += 1
                n += 1
    if n == 4:
        return True

## Déplacements ## -- End


def vict(g,j,l,c):
    if l <= 5 and c <= 6:
        if g[l][c] == j:
            if horiz(g,j,l,c) is True:
                print("gagner")
                return True
            elif vert(g,j,l,c) is True:
                print("gagner")
                return True
            elif diagonale_SE_NO(g,j,l,c) is True:
                print("gagner")
                return True
            elif diagonale_SO_NE(g,j,l,c) is True:
                print("gagner")
                return True

g = grille_vide(6,7)
jouer(g,1,3)
jouer(g,1,3)
jouer(g,1,3)
jouer(g,1,3)

vict(g,1,5,3)

# print(horiz(g,1,5,2))
# print(vert(g,1,5,2))
# print(diagonale_SE_NO(g,1,5,4))
# print(diagonale_SO_NE(g,1,5,2))

