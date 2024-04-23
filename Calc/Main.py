from Calc.GameState import GameState
from Calc.MCTSNode import MCTSNode

#initialize root node and find best move
def main(simNo, goal, initialRounds):
    initialState = GameState(initialRounds)
    root = MCTSNode(state=initialState, mode=goal)
    selectedNode = root.bestMove(simNo)

    #print best action and win rate if selectedNode exists
    if selectedNode and selectedNode.parent:
        action = selectedNode.parentMove
        winrate = selectedNode.winRate() * 100  #convert to percentage
        if goal == 0:
            print(f"Best action: {action}, with a {winrate:.2f}% chance of losing less lives than your opponent this round.")
        if goal == 1:
            print(f"Best action: {action}, with a {winrate:.2f}% chance of winning the match.")
    else:
        print("No valid actions could be determined.")
    
    return selectedNode

if __name__ == "__main__":
    result = main(100000, 0, [0, 1, 0, 1, 1, 0])