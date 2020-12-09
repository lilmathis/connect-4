def grille_vide(l,c): #définis une grille ( liste bi-dimensionelle ) sur c par l de longeur
    g = [[0 for j in range(c)] for i in range(l)]
    g = ([i for i in g[::-1]]) #on inverse les listes (lignes)
    return g

def affiche(g): #affiche le tableau g ligne par ligne
    print(*g, sep='\n')

def coup_possible(c, g): #renvoie un booléen lorsque un élément dans c
    if g[len(g)-1][c]==0:
        return True

def jouer(g,j,c): #place le jouer j dans la case libre (si une case est libre) dans la colonne c du tableau g
    n=0
    if coup_possible(c, g):
        while g[n][c] == 0 and n < 5: #
            n+=1
        g[n][c] = j
        return affiche(g)


g = grille_vide(6,7)
print(jouer(g,1,2))