from typing_extensions import Self


class Board:
    def __init__(self, taille):
        self.grille = []

        for i in range(taille):
            ligne = [0] * taille
            self.grille.append(ligne)




    def placerReine(self, x,y):
        grille = [i.copy() for i in self.grille]
        #menace verticale et horizontale
        for i in range(len(grille)):
        # if grille[i][y] != 2:
            grille[i][y] = 2
            #elif grille[x][i] != 2:
            grille[x][i] = 2

        #menace diagonale droite
        i = x
        j = y
        while i < len(grille) and j < len(grille):
            #if grille[i][j] != 2
            grille[i][j] = 2
            i+=1
            j+=1

        i = x
        j = y

        while i >= 0 and j >= 0:
            grille[i][j] = 2
            i-= 1
            j-= 1

        #menace diagonale gauche
        i = x
        j = y
        while i >= 0 and j < len(grille):
            grille[i][j] = 2
            i-=1
            j+=1
        i = x
        j = y

        while i < len(grille) and j >= 0:
            grille[i][j] = 2
            i+= 1
            j-= 1

        
        grille[x][y] = 1

        self.grille = grille

    def print_grille(self):
        ligne = "+"
        ligne += "---+" * (len(self.grille))
        for i in range(len(self.grille)):
            ligne2 = "| "
            print(ligne)
            for j in range(len(self.grille)):
                if self.grille[i][j] == 0:
                    ligne2 += "  | "
                elif self.grille[i][j] == 1:
                    ligne2 += "Q | "
                else:
                    ligne2 += "x | "
            print(ligne2)
        print(ligne)

    def delReine(self, x,y):
        #menace verticale et horizontale
        for i in range(len(self.grille)):
            self.grille[i][y] = 0
            self.grille[x][i] = 0

        #menace diagonale droite
        i = x
        j = y
        while i < len(self.grille) and j < len(self.grille):
            self.grille[i][j] = 0
            i+=1
            j+=1

        i = x
        j = y

        while i >= 0 and j >= 0:
            self.grille[i][j] = 0
            i-= 1
            j-= 1

        #menace diagonale gauche
        i = x
        j = y
        while i >= 0 and j < len(self.grille):
            self.grille[i][j] = 0
            i-=1
            j+=1
        i = x
        j = y

        while i < len(self.grille) and j >= 0:
            self.grille[i][j] = 0
            i+= 1
            j-= 1


        for i in range(len(self.grille)):
            for j in range(len(self.grille)):
                if self.grille[i][j] == 1:
                    self.placerReine(i, j, self.grille)

        # 5 = case INTERDITE
        self.grille[x][y] = 5

    def getGrille(self):
        res = [i.copy() for i in self.grille]
        return res


def trouve_une_solution(board, x, y, grilles=[]):
    if len(grilles) == 0:
        grilles.append(board.getGrille())


    if grilles[-1][y][x] == 2 and x != (len(grilles[-1])-1):
        return trouve_une_solution(grilles[-1], x+1, y)
    elif y < len(grilles[-1])-1 and x == len(grilles[-1])-1:
        grilles.pop()
        return trouve_une_solution(grilles[-1], 0, y-1)
    elif grilles[-1][y][x] == 0 and y < len(grilles[-1]):
        board.placerReine(y,x)
        y+=1
        x=0
        grilles.append(board.getGrille())
        return trouve_une_solution(grilles[-1], x, y)
    else:
        return board.getGrille()


g = Board(8)
trouve_une_solution(g, 0, 0)







"""def initGrille(h,l):
    grille = []

    for i in range(h):
        ligne = [0] * l
        grille.append(ligne)

    return grille"""