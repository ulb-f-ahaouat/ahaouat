"""NOM :
NUM MATRICULE :
SECTION :"""

import os






def afficher(plateau) :
    os.system('cls')
    alias = {0 : '_', 1 : 'X', 2 : 'O'}
    numeros = [4,3,2,1]
    a = 0
    for i in range(3,-1,-1) :
        print(numeros[i],end=' ')
        for j in range(4) :
            print(alias[plateau[i][j]],end=' ')
        print()
    print('  A B C D')

def selection(ligne,colonne) :
    if plateau[ligne][colonne] == 0 :
        res = True
    if plateau[ligne][colonne] != 0 :
        res = False
    return res

def def_joueur(joueur_cours) :
    if joueur_cours % 2 == 0 :
        res = 2
    if joueur_cours % 2 != 0 :
        res = 1
    return res
joueur_cours = 1

def gagnant(plateau):
    possibilite1 = def_joueur(joueur_cours) == plateau[0][0] == plateau[1][0] == plateau[2][0] == plateau[3][0]
    possibilite2 = def_joueur(joueur_cours) == plateau[0][0] == plateau[1][1] == plateau[2][2] == plateau[3][3]
    possibilite3 = def_joueur(joueur_cours) == plateau[0][0] == plateau[0][1] == plateau[0][2] == plateau[0][3]
    possibilite4 = def_joueur(joueur_cours) == plateau[1][0] == plateau[1][1] == plateau[1][2] == plateau[1][3]
    possibilite5 = def_joueur(joueur_cours) == plateau[2][0] == plateau[2][1] == plateau[2][2] == plateau[2][3]
    possibilite6 = def_joueur(joueur_cours) == plateau[3][0] == plateau[3][1] == plateau[3][2] == plateau[3][3]
    possibilite7 = def_joueur(joueur_cours) == plateau[0][1] == plateau[1][1] == plateau[2][1] == plateau[3][1]
    possibilite8 = def_joueur(joueur_cours) == plateau[0][2] == plateau[1][2] == plateau[2][2] == plateau[3][2]
    possibilite9 = def_joueur(joueur_cours) == plateau[0][3] == plateau[1][3] == plateau[2][3] == plateau[3][3]
    possibilite10 = def_joueur(joueur_cours) == plateau[0][3] == plateau[1][2] == plateau[2][1] == plateau[3][0]
    res = possibilite1 or possibilite2 or possibilite3 or possibilite4 or possibilite5 or possibilite6 or possibilite7 or possibilite8 or possibilite9 or possibilite10
    return res


def boucle_jeu() :
    plateau = [[0,0,0,0],
               [0,0,0,0],
               [0,0,0,0],
               [0,0,0,0]]
    joueur_cours = 1
    liste_lettres = ['A','B','C','D']
    liste_chiffres = [1,2,3,4]
    lettres = {'A' : 0, 'B' : 1, 'C' : 2, 'D': 3}
    chiffres = {1 : 0, 2 : 1, 3 : 2, 4 : 3}
    while gagnant(plateau) != True :
        status = False
        entree = input('Entrez la case à jouer :')
        derniere_case = 'indefinie'
        while status == True :
            afficher(plateau)
            entree = input('Entrez la case à jouer :')
            a = ord(entree[0]) - ord('A')
            b = ord(entree[1]) - ord('1')
            if (entree[0] in liste_lettres) and (entree[1] in liste_chiffres) :
                    if selection(entree[1],entree[0]) == True :
                        if plateau[a][b] != def_joueur(joueur_cours) :
                            status = True
            elif (entree[0] not in liste_lettres) or (entree[1] not in liste_chiffres):
                print('commande invalide')
                status = False
            elif selection(entree[1], entree[0]) == False:
                if plateau[a][b] == def_joueur(joueur_cours):
                    print('cette case est déjà de votre couleur')
            elif entree == derniere_case:
                print('ce coup vient d’être joué')
                status = False
        a = ord(entree[0]) - ord('A')
        b = ord(entree[1]) - ord('1')
        plateau[a][b] = def_joueur(joueur_cours)
        afficher(plateau)
        derniere_case = entree
        joueur_cours = joueur_cours+1



    res = print('joueur',def_joueur(joueur_cours+1),'gagnant')
    return res








if __name__ == '__main__' :
    boucle_jeu()