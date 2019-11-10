def gagnant(plateau):
    Nbr_Lignes = 4
    Nbr_Colonnes = 4
    ligne = 0
    Etat = True
    while ligne < Nbr_Lignes and Etat == True:
        colonne = 0
        while colonne < Nbr_Colonnes and Etat == True:
            if grille[ligne][colonne] == 2:
                a = 1
                while a < 3 and colonne < 4 and grille[ligne][colonne+a] == 2:
                    a += 1
                    if a == 3 and grille[ligne][colonne+a]== 2:
                        Etat = False
                        resultat = 2
                a = 1
                while a < 3 and ligne < 3 and grille[ligne+a][colonne] == 2:
                    a+=1
                    if a == 3 and grille[ligne+a][colonne]== 2:
                        resultat = 2
                        Etat = False
                a = 1
                while a < 3 and ligne < 3 and colonne <= 3 and grille[ligne + a][colonne+a] == 2 :
                    a += 1
                    if a == 3 and grille[ligne + a][colonne+a] == 2:
                        resultat = 2
                        Etat = False
                a = 1
                while a < 3 and ligne < 3 and colonne >= 3 and grille[ligne + a][colonne - a] == 2 :
                    a += 1
                    if a == 3 and grille[ligne + a][colonne - a] == 2:
                        resultat = 2
                        Etat = False
            elif grille[ligne][colonne] == 1:
                a = 1
                while a < 3 and colonne < 4 and grille[ligne][colonne + a] == 1 :
                    a += 1
                    if a == 3 and grille[ligne][colonne + a] == 1:
                        resultat = 1
                        Etat = False
                a = 1
                while a < 3 and ligne < 3 and grille[ligne + a][colonne] == 1 :
                    a += 1
                    if a == 3 and grille[ligne + a][colonne] == 1:
                        resultat = 1
                        Etat = False
                a = 1
                while a < 3 and ligne < 3 and colonne <= 3 and grille[ligne + a][colonne + a] == 1 :
                    a += 1
                    if a == 3 and grille[ligne + a][colonne + a] == 1:
                        resultat = 1
                        Etat = False
                a = 1
                while a < 3 and ligne < 3 and colonne >= 3 and grille[ligne + a][colonne - a] == 1 :
                    a += 1
                    if a == 3 and grille[ligne + a][colonne - a] == 1:
                        resultat = 1
                        Etat = False
            colonne += 1
        ligne += 1
    if Etat == False :
        return resultat
    else :
        return True

def affichage() :
    alias = {0 : '_', 1 : 1, 2 : 2}
    numeros = [4,3,2,1]
    a = 0
    for i in range(4,-1,-1) :
        for j in range(4) :
            print(alias(plateau[i][j]),end=' ')
            print(numeros[a])
            a = a+1
        print()
    print('  A B C D')

def selection() :
    if plateau[ligne][colonne] == 0 :
        res = True
    if plateau[ligne][colonne] != 0 :
        res = False
    return res

def boucle_jeu() :
    plateau = [[0,0,0,0],
               [0,0,0,0],
               [0,0,0,0],
               [0,0,0,0],]
    joueur1 = 1
    joueur2 = 2

plateau = [[0,0,0,0],
           [0,0,0,0],
           [0,0,0,0],
           [0,0,0,0],]
print(affichage())
