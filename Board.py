import numpy as np
from matplotlib import pyplot as plt
import matplotlib.colors
import random as rand

class Board: 
    def __init__(self,dim,targetTerrain): #set default values for a board
        self.board = np.zeros((dim,dim), dtype= float)
        self.target = (rand.randint(0,dim-1),rand.randint(0,dim-1))
        self.dim = dim
        self.populateTerrain()
        self.newTarget(targetTerrain)



    def populateTerrain(self):
        terrain = [.1, .3, .7, .9]
        for i in range(self.dim):
            for j in range(self.dim):
                self.board[i,j] = rand.choices(terrain,weights = (.2, .3, .3, .2))[0]
                

    def newTarget(self,terrain):
        while True:
            x,y = (rand.randint(0,self.dim-1),rand.randint(0,self.dim-1))
            if self.board[x,y] == terrain:
                self.target = (x,y)
                break

    def printBoard(self):
        #print(self.board)
        plt.figure(figsize = (6,6))
        plt.pcolor(self.board,edgecolors = "black", cmap = 'Set3', linewidths = 1)
        for (j,i),label in np.ndenumerate(self.board): #consider using a mapping for label to mine/flag
            plt.text(i,j,label,ha='left',va='bottom')
        plt.tight_layout()
        plt.show() #block=False
        #plt.pause(.2)
        #plt.close()