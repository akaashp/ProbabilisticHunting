from Board import *
from Agent import *

board1 = Board(50,.1)
#board1.printBoard()

#print(board1.board)
#x,y = board1.target
#print(x,y, board1.board[x,y])

#rule = 1; countDistanceAsMove = True
#print(Agent1_2(board1,rule,countDistanceAsMove))
#print(Agent1_2(board1,2,countDistanceAsMove))
print(Agent1_2_3(board1,3,True))

terrains = [.1, .3, .7, .9]
terrFreqs= [.2, .3, .3, .2]
a1Moves = []; a2Moves = []; a3Moves = []
for terrain,freq in zip(terrains,terrFreqs):
    board1 = Board(50,terrain)
    temp1 = 0; temp2 = 0; temp3 = 0
    #iter = 50 * freq
    for i in range(2): #in range(iter)
        board1.newTarget(terrain)
        moves1 = Agent1_2_3(board1,1,True); moves2 = Agent1_2_3(board1,2,True)
        moves3 = Agent1_2_3(board1,3,True)
        temp1 += moves1
        temp2 += moves2
        temp3 += moves3

        print(terrain,"rule1:\t",moves1,"rule2:\t",moves2,"rule3:\t",moves3)
    
    a1Moves.append(temp1/2); a2Moves.append(temp2/2); a3Moves.append(temp3/2)

print("Rule 1 moves for target on .1, .3, .7, .9 terrain: ", a1Moves)
print("Rule 2 moves for target on .1, .3, .7, .9 terrain: ", a2Moves)
print("Rule 3 moves for target on .1, .3, .7, .9 terrain: ", a3Moves)

plt.figure(figsize = (10,6))
plt.plot(terrains,a1Moves,label="Rule 1")
plt.plot(terrains,a2Moves,label = "Rule 2")
plt.plot(terrains,a3Moves,label = "Rule 3")
plt.xticks(terrains)
plt.title("Average Moves vs Target Terrain Type" )
plt.xlabel("Target Terrain Type")
plt.ylabel("Average Number of Moves")
plt.legend()
plt.show()