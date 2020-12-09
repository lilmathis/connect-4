def grille_vide(l,c):# définis une grille ( liste bi-dimensionelle ) sur c par l de longeur
    g = [[1 for j in range(c)] for i in range(l)]
    g[0][0] = 0
    g = ([i for i in g[::-1]])
    return g

def affiche(g):# affiche le tableau g ligne par ligne
    print(*g, sep='\n')

def coup_possible(c, g):#affiche le numero de la colonne si une colonne contient un zero
    for i in range(c):
        for k in range(6):
            if g[k][i] == 0:
                print(i)
                return True

# def jouer(g,j,c):


g = grille_vide(6,7)
print(coup_possible(7,g))
print(affiche(g))