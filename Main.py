from Board import *
from Agent import *

#board1 = Board(50,.1)
#board1.printBoard()

#print(board1.board)
#x,y = board1.target
#print(x,y, board1.board[x,y])

#rule = 1; countDistanceAsMove = True
#print(Agent1_2(board1,rule,countDistanceAsMove))
#print(Agent1_2(board1,2,countDistanceAsMove))
#print(improvedAgent(board1,3,True))

terrains = [.1, .3, .7, .9]
terrFreqs= [.2, .3, .3, .2]
a1Moves = []; a2Moves = []; a3Moves = []; a4Moves = []
for terrain,freq in zip(terrains,terrFreqs):
    board1 = Board(50,terrain)
    temp1 = 0; temp2 = 0; temp3 = 0; temp4 = 0
    iter = int(50 * freq)
    for i in range(iter):
        board1.newTarget(terrain)
        moves1 = Agent1_2_3(board1,1,True); moves2 = Agent1_2_3(board1,2,True)
        moves3 = Agent1_2_3(board1,3,True); moves4 = improvedAgent(board1,3,True)
        temp1 += moves1; temp2 += moves2
        temp3 += moves3; temp4 += moves4

        print(terrain,"rule1:\t",moves1,"rule2:\t",moves2,"rule3:\t",moves3,"rule4\t",moves4)
    
    a1Moves.append(temp1/iter); a2Moves.append(temp2/iter); a3Moves.append(temp3/iter); a4Moves.append(temp4/iter)

print("Rule 1 moves for target on .1, .3, .7, .9 terrain: ", a1Moves)
print("Rule 2 moves for target on .1, .3, .7, .9 terrain: ", a2Moves)
print("Rule 3 moves for target on .1, .3, .7, .9 terrain: ", a3Moves)
print("Rule 4 moves for target on .1, .3, .7, .9 terrain: ", a4Moves)


plt.figure(figsize = (10,6))
plt.plot(terrains,a1Moves,label="Rule 1")
plt.plot(terrains,a2Moves,label = "Rule 2")
plt.plot(terrains,a3Moves,label = "Rule 3")
plt.plot(terrains,a4Moves,label = "Improved Agent")

plt.xticks(terrains)
plt.title("Average Moves vs Target Terrain Type" )
plt.xlabel("Target Terrain Type")
plt.ylabel("Average Number of Moves")
plt.legend()
plt.show()