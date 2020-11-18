import numpy as np
import random as rand
import math

#cardinal = [(-1,0), (0,-1), (1,0), (0,1)]

def manhattanD(coords1,coords2):
    return abs(coords1[0]-coords2[0])+abs(coords1[1]-coords2[1])

def rule1(belief,maxBelief,board,currCell):
    cellList = []
    for i in range(belief.shape[0]):
        for k in range(belief.shape[0]):
            if belief[i,k] == maxBelief:
                cellList.append((i,k))

    return cellList

def rule2(belief,maxBelief,board,currCell):
    cellList = []
    for i in range(belief.shape[0]):
        for k in range(belief.shape[0]):
            if belief[i,k] * (1-board[i,k]) == maxBelief: #probability target is in cell | obs * probability of finding target in cell | target in cell
                cellList.append((i,k))
    
    return cellList

def rule3(belief,maxBelief,board,currCell):
    cellList = []
    for i in range(belief.shape[0]):
        for k in range(belief.shape[0]):
            if (-1 * manhattanD(currCell,(i,k))/(belief[i,k] * (1-board[i,k])) )== maxBelief: #only take maxBelief cells
                cellList.append((i,k))
    
    return cellList


def updateBelief(currCell, deltaBelief, maxBelief, ruleType, belief, board):
    """updates all neighbors and maxBelief will be max probability of containing target or finding target depending on ruleType

    Args:
        currCell ([type]): [description]
        deltaBelief ([type]): [description]
        maxBelief ([type]): [description]
        ruleType ([type]): [description]
        belief ([type]): [description]
        board ([type]): [description]
    """

    x,y = currCell
    for i in range(belief.shape[0]):
        for k in range(belief.shape[1]):
            if i == x and k == y: continue
            belief[i,k] += belief[i,k] *  deltaBelief / (1-belief[x,y])

            if ruleType == 1:
                maxBelief = max(maxBelief, belief[i,k]) 
            elif ruleType == 2:
                maxBelief = max(maxBelief, belief[i,k] * (1-board[i,k])) #the chance of finding it is belief*(1-failureRate)
            elif ruleType == 3:
                maxBelief = max(maxBelief, -(manhattanD(currCell,(i,k))/(belief[i,k] * (1-board[i,k])) )) # rule3 (manhattan distance from current location)/(probability of finding target in that cell)

    return maxBelief

    

def Agent1_2(board,ruleType,dist):
    belief = np.full((board.dim,board.dim),1/board.dim**2, dtype = float)
    moves = 0; totalDist = 0

    if ruleType == 1:
        rule = rule1
    else:
        rule = rule2
    
    currCell = (rand.randint(0,board.dim-1),rand.randint(0,board.dim-1))
    prevCell = currCell
    while True:
        moves+=1
        #print("moves: ",moves,"currCell: ",currCell)
        x,y = currCell
        if dist: totalDist += manhattanD(currCell,prevCell) #if we are counting movement as a move
        chance = rand.random()
       
        if currCell == board.target:
            print("moves: ",moves, "chance: ", chance)
          #  print(belief)
            m,k = board.target
            print("currCell: ",x,y,"chance: ", board.board[x,y],"target: ",m,k,"chance: ",board.board[m,k])
        if  chance >= board.board[x,y] and currCell == board.target:
            #print("current target belief :", belief[x,y])
            #print("currCell = ",currCell,'moves = ',moves, "totalDist = ",totalDist)
            return moves + totalDist

        else:
            tempBelief = belief[x,y] * board.board[x,y]
            deltaBelief = belief[x,y] - tempBelief 
            belief[x,y] = tempBelief
            
            maxBelief = 0 
            maxBelief = updateBelief(currCell, deltaBelief, maxBelief, ruleType, belief, board.board)
            cellList = rule(belief,maxBelief,board.board,currCell)
            
            prevCell = currCell
            if dist:
                minDist = board.dim**2
                for cell in cellList:
                    tempDist = manhattanD(cell,currCell)
                    if  tempDist < minDist:
                        currCell = cell
                        minDist = tempDist
            else:
                currCell = rand.choice(cellList)


def Agent1_2_3(board,ruleType,dist):
    belief = np.full((board.dim,board.dim),1/board.dim**2, dtype = float)
    moves = 0; totalDist = 0

    if ruleType == 1:
        rule = rule1
    elif ruleType == 2:
        rule = rule2
    elif ruleType == 3:
        rule = rule3
    else:
        rule = rule4
    
    currCell = (rand.randint(0,board.dim-1),rand.randint(0,board.dim-1))
    prevCell = currCell
    while True:
        moves+=1
        #print("moves: ",moves,"currCell: ",currCell)
        x,y = currCell
        if dist: totalDist += manhattanD(currCell,prevCell) #if we are counting movement as a move
        chance = rand.random()
       
        if currCell == board.target:
            print("moves: ",moves, "chance: ", chance)
          #  print(belief)
            m,k = board.target
            print("currCell: ",x,y,"chance: ", board.board[x,y],"target: ",m,k,"chance: ",board.board[m,k])
        if  chance >= board.board[x,y] and currCell == board.target:
            #print("current target belief :", belief[x,y])
            #print("currCell = ",currCell,'moves = ',moves, "totalDist = ",totalDist)
            return moves + totalDist

        else:
            tempBelief = belief[x,y] * board.board[x,y]
            deltaBelief = belief[x,y] - tempBelief 
            belief[x,y] = tempBelief
            
            maxBelief = -math.inf
            maxBelief = updateBelief(currCell, deltaBelief, maxBelief, ruleType, belief, board.board)
            cellList = rule(belief,maxBelief,board.board,currCell)
            
            prevCell = currCell
            if dist:
                minDist = board.dim**2
                for cell in cellList:
                    tempDist = manhattanD(cell,currCell)
                    if  tempDist < minDist:
                        currCell = cell
                        minDist = tempDist
            else:
                currCell = rand.choice(cellList)

                


            
                    


        

        
    
    
    
    



